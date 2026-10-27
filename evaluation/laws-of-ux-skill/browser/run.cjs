#!/usr/bin/env node
// Optional browser acceptance checks. Requires Playwright + its Chromium browser.
// No request reaches a real registration, records, or export service.
const { createServer } = require('node:http');
const { readFile, mkdir, writeFile } = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const { chromium } = require(process.env.UX_PLAYWRIGHT_MODULE || 'playwright');
const args = process.argv.slice(2);
const option = (name, fallback) => { const i = args.indexOf(name); return i < 0 ? fallback : args[i + 1]; };
const fixtureDir = path.resolve(option('--fixture-dir', path.join(__dirname, '../fixtures/completed')));
const reportPath = option('--report', null);
const screenshots = option('--screenshots', null);
const only = option('--only', 'all');
const negativeSuccessControl = args.includes('--negative-success-control');
assert(['all', 'registration', 'records'].includes(only), '--only must be all, registration, or records');
const results = [];
const cases = [];
const test = (name, kind, run) => cases.push({ name, kind, run });
const waitFor = async fn => {
  const deadline = Date.now() + 4000;
  while (!fn()) { if (Date.now() > deadline) throw new Error('Expected sandbox request was not received'); await new Promise(r => setTimeout(r, 10)); }
};
const response = (route, status, body) => route.fulfill({ status, contentType: 'application/json', body: JSON.stringify(body) }).catch(() => {});
const submit = page => page.locator('form button[type="submit"], form button:not([type])').first();
const fillRegistration = async page => {
  await page.locator('[name="email"]').fill('Person+team@example.com');
  await page.locator('[name="password"]').fill('  Keep My Password 42!  ');
};
const search = async (page, q) => { await page.locator('[name="q"]').fill(q); await submit(page).click(); };
const action = (page, regex) => page.getByRole('button', { name: regex }).or(page.getByRole('link', { name: regex })).first();
const tableHas = (page, name) => page.getByRole('cell', { name, exact: true }).waitFor();

// These assertions inspect behavior and preserved contracts, not chosen law names or CSS selectors for a preferred design.
test('registration: persistent labels and native invalid-input prevention', 'registration', async ({ page }) => {
  let requests = 0;
  await page.route('**/api/register', async r => { requests++; await response(r, 201, {status:'created'}); });
  await page.goto('/registration.html');
  await page.getByLabel(/email/i).fill('invalid');
  await page.getByLabel(/^password/i).fill('valid length');
  await submit(page).click();
  assert.equal(await page.locator('[name="email"]').evaluate(el => el.validity.valid), false);
  assert.equal(requests, 0);
});
test('registration: pending feedback cancels repeated submits and preserves JSON', 'registration', async ({ page }) => {
  const requests = []; let pending;
  await page.route('**/api/register', r => { requests.push(r.request()); pending = r; return new Promise(() => {}); });
  await page.goto('/registration.html'); await fillRegistration(page); await submit(page).click();
  await waitFor(() => requests.length > 0);
  const prevented = await page.locator('form').evaluate(form => !form.dispatchEvent(new Event('submit', { bubbles:true, cancelable:true })));
  assert.equal(prevented, true, 'Every enhanced submit must cancel native behavior, including while pending');
  await page.locator('[name="password"]').press('Enter');
  assert.equal(requests.length, 1);
  assert.deepEqual(requests[0].postDataJSON(), {email:'Person+team@example.com', password:'  Keep My Password 42!  '});
  assert.match(await page.getByRole('status').innerText(), /creat|submitt|saving|pending|working/i);
  await response(pending, 201, {status:'created'});
});
test('registration: server field errors retain values, associate text, and allow retry', 'registration', async ({ page }) => {
  let requests = 0;
  await page.route('**/api/register', async r => {
    requests++;
    await response(r, requests === 1 ? 422 : negativeSuccessControl ? 200 : 201, requests === 1 ? {errors:{email:'This email is already registered.'}} : {status:'created'});
  });
  await page.goto('/registration.html'); await fillRegistration(page); await submit(page).click();
  await page.getByText('This email is already registered.', {exact:true}).waitFor();
  const email = page.locator('[name="email"]');
  assert.equal(await email.inputValue(), 'Person+team@example.com');
  assert.equal(await page.locator('[name="password"]').inputValue(), '  Keep My Password 42!  ');
  assert.equal(await email.getAttribute('aria-invalid'), 'true');
  const linked = await email.evaluate(el => (el.getAttribute('aria-describedby') || '').split(/\s+/).map(id => document.getElementById(id)?.textContent || '').join(' '));
  assert.match(linked, /already registered/);
  await email.fill('Another@example.com'); await submit(page).click();
  await page.getByRole('status').filter({
    hasText:/account[^.!?]{0,45}created|welcome|success/i,
    hasNotText:/not created|not confirm|unconfirm|uncertain|failed|could not|couldn.t|unable|please wait|creating/i
  }).waitFor();
  assert.equal(requests, 2);
});
test('registration: transport failure never claims a confirmed outcome or retries automatically', 'registration', async ({ page }) => {
  let requests = 0;
  await page.route('**/api/register', async r => { requests++; await r.abort('failed'); });
  await page.goto('/registration.html'); await fillRegistration(page); await submit(page).click();
  await page.getByText(/could not confirm|couldn.t confirm|unable to confirm|not confirm|unknown|check.*(email|account)|may have/i).first().waitFor();
  // Unknown creation needs reconciliation guidance or an informed warning before retry.
  await page.getByText(/check[^.!?]{0,70}(email|account)|before[^.!?]{0,35}(retry|try again)|may[^.!?]{0,50}already|duplicate|contact[^.!?]*support|sign.in/i).first().waitFor();
  assert.equal(requests, 1);
  assert.equal(await page.locator('[name="password"]').inputValue(), '  Keep My Password 42!  ');
  assert.equal(await page.evaluate(() => JSON.stringify([Object.values(localStorage),Object.values(sessionStorage)]).includes('Keep My Password')), false);
});
test('registration: generic service failure preserves mutation uncertainty', 'registration', async ({ page }) => {
  let requests = 0;
  await page.route('**/api/register', async r => { requests++; await response(r,503,{message:'Service unavailable'}); });
  await page.goto('/registration.html'); await fillRegistration(page); await submit(page).click();
  await page.getByText(/could not confirm|couldn.t confirm|unable to confirm|not confirm|unconfirmed|unknown|may.*already/i).first().waitFor();
  const message = await page.getByRole('status').innerText();
  assert.doesNotMatch(message, /account not created|account was not created/i, '503 alone does not prove non-creation');
  assert.equal(requests, 1);
  assert.equal(await page.locator('[name="password"]').inputValue(), '  Keep My Password 42!  ');
});
test('registration: keyboard path and control containment at mobile/tablet/desktop widths', 'registration', async ({ page }) => {
  await page.goto('/registration.html');
  await page.keyboard.press('Tab');
  assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('name')), 'email');
  await page.keyboard.press('Tab');
  assert.equal(await page.evaluate(() => document.activeElement?.getAttribute('name')), 'password');
  for (const width of [320,768,1280]) {
    await page.setViewportSize({width,height:900});
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, 'Page overflow at '+width);
    for (const element of await page.locator('input, form button').all()) {
      const box = await element.boundingBox();
      if (box) assert(box.x >= 0 && box.x + box.width <= width, 'Control clipped at '+width);
    }
  }
});

test('records: loading withholds create until authorization is known', 'records', async ({ page }) => {
  let pending;
  await page.route('**/api/records?*', r => { pending=r; return new Promise(() => {}); });
  await page.goto('/records.html'); await waitFor(() => pending);
  assert.match(await page.getByRole('status').innerText(), /load|fetch|search|working/i);
  assert.equal(await page.getByRole('link', {name:/create/i}).isVisible(), false);
  await response(pending, 200, {items:[],permissions:{canCreate:false}});
});
test('records: new workspace exposes authorized creation, denied access does not', 'records', async ({ page }) => {
  let status = 200;
  await page.route('**/api/records?*', r => response(r,status,status===200?{items:[],permissions:{canCreate:true}}:{message:'Access denied'}));
  await page.goto('/records.html');
  await page.getByRole('link', {name:/create/i}).waitFor();
  assert.match(await page.getByRole('status').innerText(), /0 records|no records|no .*yet|start|first|empty/i);
  status = 403; await search(page,'blocked');
  await page.getByText(/access|permission|authorized/i).first().waitFor();
  assert.equal(await page.getByRole('link', {name:/create/i}).isVisible(), false);
});
test('records: filtered-zero offers recovery and export follows the active query', 'records', async ({ page }) => {
  await page.route('**/api/records?*', r => {
    const q = new URL(r.request().url()).searchParams.get('q') || '';
    return response(r,200,{items:q?[]:[{name:'Sample record',team:'Operations'}],permissions:{canCreate:false}});
  });
  await page.goto('/records.html?q=absent');
  const clear = action(page,/clear.*(filter|search)|reset.*(filter|search)|show all/i); await clear.waitFor();
  await clear.click(); await tableHas(page,'Sample record');
  assert.equal(new URL(page.url()).searchParams.get('q') || '', '');
  assert.equal(await page.locator('[name="q"]').inputValue(),'');
  const exportURL = new URL(await page.getByRole('link',{name:/export/i}).getAttribute('href'),page.url());
  assert.equal(exportURL.pathname,'/api/export'); assert.equal(exportURL.searchParams.get('q') || '', '');
});
test('records: service failure is recoverable and retry preserves the query', 'records', async ({ page }) => {
  let requests=0;
  await page.route('**/api/records?*', r => {
    requests++; assert.equal(new URL(r.request().url()).searchParams.get('q'),'team');
    return response(r,requests===1?503:200,requests===1?{message:'Service unavailable'}:{items:[{name:'Recovered record',team:'Operations'}],permissions:{canCreate:false}});
  });
  await page.goto('/records.html?q=team');
  const retry=action(page,/retry|try again/i); await retry.waitFor(); await retry.click();
  await tableHas(page,'Recovered record'); assert.equal(requests,2);
});
test('records: browser back restores query, results, and export', 'records', async ({ page }) => {
  await page.route('**/api/records?*', r => {
    const q=new URL(r.request().url()).searchParams.get('q') || '';
    return response(r,200,{items:[{name:'Result '+q,team:'Operations'}],permissions:{canCreate:false}});
  });
  await page.goto('/records.html?q=first'); await tableHas(page,'Result first');
  await search(page,'second'); await tableHas(page,'Result second');
  await page.goBack(); await tableHas(page,'Result first');
  assert.equal(await page.locator('[name="q"]').inputValue(),'first');
  assert.equal(new URL(await page.getByRole('link',{name:/export/i}).getAttribute('href'),page.url()).searchParams.get('q'),'first');
});
test('records: older response cannot overwrite the active search or restore stale permission', 'records', async ({ page }) => {
  const pending = new Map();
  await page.route('**/api/records?*', r => {
    const q=new URL(r.request().url()).searchParams.get('q') || '';
    if(!q) return response(r,200,{items:[{name:'Initial record',team:'Operations'}],permissions:{canCreate:false}});
    pending.set(q,r); return new Promise(() => {});
  });
  await page.goto('/records.html'); await tableHas(page,'Initial record');
  await search(page,'old'); await waitFor(() => pending.has('old'));
  await search(page,'new'); await waitFor(() => pending.has('new'));
  await response(pending.get('new'),200,{items:[{name:'Current record',team:'Operations'}],permissions:{canCreate:false}});
  await tableHas(page,'Current record');
  await response(pending.get('old'),200,{items:[{name:'Stale record',team:'Operations'}],permissions:{canCreate:true}});
  // Barrier: after a late response, allow queued browser handlers and one paint to run.
  await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
  assert.equal(await page.getByRole('cell',{name:'Stale record',exact:true}).count(),0);
  assert.equal(await page.getByRole('link',{name:/create/i}).isVisible(),false);
  assert.equal(await page.locator('[name="q"]').inputValue(),'new');
});
test('records: readable results and controls remain contained at three widths', 'records', async ({ page }) => {
  await page.route('**/api/records?*',r => response(r,200,{items:[{name:'A long but realistic operations record title',team:'Team Operations'}],permissions:{canCreate:false}}));
  await page.goto('/records.html'); await tableHas(page,'A long but realistic operations record title');
  for(const width of [320,768,1280]) {
    await page.setViewportSize({width,height:900});
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth),true,'Page overflow at '+width);
    assert.equal(await page.getByRole('columnheader',{name:'Name',exact:true}).count(),1);
  }
});

(async () => {
  const server = createServer(async (req,res) => {
    const file = path.basename(new URL(req.url,'http://localhost').pathname);
    if(!['registration.html','records.html'].includes(file)) { res.writeHead(404).end(); return; }
    try { res.setHeader('Content-Type','text/html; charset=utf-8'); res.end(await readFile(path.join(fixtureDir,file))); }
    catch { res.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
  let browser;
  try {
    browser = await chromium.launch({headless:true});
    for(const item of cases.filter(c => only === 'all' || c.kind === only)) {
      const context = await browser.newContext({baseURL:`http://127.0.0.1:${server.address().port}`,viewport:{width:1280,height:900}});
      const page = await context.newPage(); page.setDefaultTimeout(5000);
      try { await item.run({page}); results.push({name:item.name,status:'pass'}); }
      catch(error) { results.push({name:item.name,status:'fail',error:error.message}); }
      if(screenshots) { await mkdir(screenshots,{recursive:true}); await page.screenshot({path:path.join(screenshots,item.name.replace(/[^a-z0-9]+/gi,'-')+'.png'),fullPage:true}).catch(()=>{}); }
      await context.close();
      console.log(results.at(-1).status.toUpperCase()+': '+item.name);
    }
  } finally {
    if(browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  const report={fixtureDir,negativeSuccessControl,scope:'Sandbox browser behavior; not production integration, user testing, or full accessibility conformance',cases:results,passed:results.filter(r=>r.status==='pass').length,failed:results.filter(r=>r.status==='fail').length};
  if(reportPath) await writeFile(reportPath,JSON.stringify(report,null,2)+'\n','utf8');
  console.log(`${report.passed} passed, ${report.failed} failed`);
  process.exitCode=report.failed?1:0;
})().catch(error => { console.error(error); process.exitCode=1; });

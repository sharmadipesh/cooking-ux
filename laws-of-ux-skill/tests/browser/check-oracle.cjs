#!/usr/bin/env node
// A deliberately unconfirmed response must fail the confirmed-success assertion.
const {execFileSync} = require('node:child_process');
const {mkdtempSync,readFileSync,rmSync} = require('node:fs');
const {tmpdir} = require('node:os');
const path = require('node:path');
const assert = require('node:assert/strict');
const temp = mkdtempSync(path.join(tmpdir(),'cooking-ux-oracle-'));
try {
  const reportPath = path.join(temp,'control.json');
  let exitCode = 0;
  try {
    execFileSync(process.execPath,[path.join(__dirname,'run.cjs'),'--only','registration','--negative-success-control','--report',reportPath],{timeout:30000,stdio:'pipe'});
  } catch(error) { exitCode = error.status; }
  assert.equal(exitCode,1,'Negative control must fail the browser run');
  const report = JSON.parse(readFileSync(reportPath,'utf8'));
  assert.equal(report.negativeSuccessControl,true);
  const failures = report.cases.filter(row=>row.status==='fail');
  assert.equal(failures.length,1,'Only the confirmed-success transition should fail');
  assert.equal(failures[0].name,'registration: server field errors retain values, associate text, and allow retry');
  console.log('PASS: oracle rejects an unconfirmed 200 response instead of counting it as creation success');
} finally { rmSync(temp,{recursive:true,force:true}); }

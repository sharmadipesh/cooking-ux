# Optional browser acceptance checks

These checks run two small, framework-independent sandbox interfaces. They do not require a real service or production credentials. All API requests used by the tests are intercepted locally; no real account or record is created.

The UX skill itself needs none of these dependencies. For development checks, use Node.js 22.20+ and install the pinned Playwright package and Chromium:

```sh
cd evaluation/laws-of-ux-skill/browser
npm ci
npx playwright install chromium
npm test
npm run test:oracle
```

On a minimal Linux system, `npx playwright install --with-deps chromium` also installs browser system dependencies. See [official Playwright installation guidance](https://playwright.dev/docs/library).

The default fixture directory is `../fixtures/completed`. From this directory you can also run:

```sh
node run.cjs --fixture-dir ../fixtures/baseline
node run.cjs --fixture-dir ../fixtures/seed
node run.cjs --fixture-dir ../fixtures/completed --only registration
node run.cjs --fixture-dir ../fixtures/completed --report results.json --screenshots test-results
```

The negative-control command `npm run test:oracle` deliberately substitutes an unconfirmed response during the success-transition check. It passes only when that single browser case correctly fails; this guards against counting “not created” or “unconfirmed” as success.

The seed and historical baseline runs are expected to fail some assertions. They are retained to make the evaluation inspectable, not as recommended implementations. The browser runner exits nonzero when a case fails. Invalid suite names are rejected. If Playwright is installed outside this directory, the optional `UX_PLAYWRIGHT_MODULE` environment variable can point to its module directory.

## What is checked

- Registration: generic service failure preserves mutation uncertainty; persistent labels and native invalid-input prevention; pending feedback; repeated-submit prevention; exact JSON credentials; server errors and correction; retained values; unknown-outcome guidance; no credential persistence; keyboard path; control containment at 320/768/1280 CSS-pixel widths.
- Records: pending feedback and unknown permission; successful empty state; denial; filtered-zero and recovery; scoped export; failure/retry; back navigation; out-of-order response and permission protection; headers and layout containment at three widths.

Each case uses a fresh browser context. Assertions target the supplied sandbox contract and accessible controls, not a preferred CSS design. Some message checks use English text patterns to detect the expected communication; those are proxies and require human review if a different legitimate wording fails. These are task-specific checks, not a general-purpose UI scoring engine, full WCAG conformance test, assistive-technology study, or user-research substitute.

See [the implementation evaluation](../implementation-evaluation.md) for prompts, artifacts, actual results, and limitations. New agents evaluating the skill should receive the task and seed fixture, not the completed implementation or oracle tests.

# Sandbox fixtures

- `seed/`: intentionally incomplete interfaces used as the starting point.
- `baseline/`: independent implementations produced with the pre-upgrade skill. Retained as historical evidence; the registration recovery message has a known gap.
- `candidate/`: the upgraded agent’s registration output before review corrected generic 503 handling. Run with `--only registration`; this folder intentionally has no records page.
- `completed/`: reviewed reference implementations produced with the upgraded skill and a subsequent maintainer correction, checked by the browser acceptance suite.

All pages are original test artifacts. API comments define the sandbox contracts; they are not working integrations. Use the browser runner, which intercepts their requests, rather than submitting these forms to a real server. No real user data or credentials belong in the fixtures.

The directory structure keeps test inputs separate from expected outputs. These files are not a starter kit to install into a product. Adapt relevant patterns after inspecting the real application's architecture, security, and accessibility requirements.

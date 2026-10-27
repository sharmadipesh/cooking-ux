# Evaluation evidence

This folder keeps the evidence behind the two skills’ validation reports: sandbox fixtures, the optional browser runner, evaluated audit reports, screenshots, and runtime observations. It sits outside `laws-of-ux-skill/` and `ux-audit-skill/` so that an installed skill or ZIP contains only what an agent needs, while every claim in the repository stays inspectable. Nothing here is a starter kit; the pages are original synthetic test artifacts.

## laws-of-ux-skill

- [Implementation evaluation](laws-of-ux-skill/implementation-evaluation.md): method, prompts, observations, and limits of the sandbox implementation pass, with [raw results and artifact hashes](laws-of-ux-skill/implementation-results.json).
- [Behavioral smoke results](laws-of-ux-skill/behavioral-smoke-results.md): actual offline proposals for scenarios T1–T7.
- [Sandbox fixtures](laws-of-ux-skill/fixtures/README.md): seed, baseline, candidate, and completed registration and records pages.
- [Browser acceptance checks](laws-of-ux-skill/browser/README.md): the Playwright runner, its negative-control oracle check, and pinned dependencies. The repository workflow runs them from this folder.

The scenario prompts, expected behaviors, source manifest, Python regression tests, and [validation report](../laws-of-ux-skill/tests/validation-report.md) stay in the package under `laws-of-ux-skill/tests/`.

## ux-audit-skill

- [Live sandbox audit](ux-audit-skill/results/live/report.md) with 13 inspected screenshots and the [runtime observation log](ux-audit-skill/results/live/observations.json).
- [Supplied-artifact audit](ux-audit-skill/results/artifacts/report.md), the [baseline review without the skill](ux-audit-skill/results/baseline/report.md), and the [no-source response](ux-audit-skill/results/no-source/report.md).
- [Loopback fixture server](ux-audit-skill/serve_fixture.py) and its [synthetic registration page](ux-audit-skill/fixtures/registration.html) for scenario A2. From the repository root, run `python3 -B evaluation/ux-audit-skill/serve_fixture.py`.

The [scenarios](../ux-audit-skill/tests/scenarios.md), the supplied A1 artifacts (`design-observations.md` and `flow.md`), the Python regression tests, and the [validation report](../ux-audit-skill/tests/validation-report.md) stay in the package under `ux-audit-skill/tests/`.

## Provenance

These files moved here from the two packages with Git history preserved. Relative links and the recorded fixture paths in `implementation-results.json` were rewritten for the new location; dates, hashes, outcomes, and findings were not edited. The packages link back to this folder with repository URLs because an installed copy does not include it.

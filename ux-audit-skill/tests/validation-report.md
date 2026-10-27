# Validation evidence

Date: 2026-10-27. This report records checks actually performed. Structural checks and a small behavioral evaluation do not establish general audit accuracy or a user's eventual experience.

## Package checks

- Offline package validation passes required files, metadata/name/context budget, local links, example JSON structure, and evidence-reference checks.
- All **15 Python regression tests** pass: ten report/package tests and five archive tests. They detect missing version metadata, unknown/duplicate evidence, missing priority reasons, malformed enum/container data, missing coverage, mixed severity/priority types, stale/missing archives, unexpected generated dependencies, and missing members. A no-findings report is allowed when its scope and coverage are explicit.
- The independent skill-creator metadata validator is run before release. It checks skill metadata, not semantic correctness.
- The standalone ZIP is rebuilt after content changes and checked for exact member set, CRC, and byte equality. Generated caches/dependencies are excluded. Both skill packages are checked by the repository CI workflow on Linux/Windows and Python 3.9/3.13; remote run conclusions must be verified separately.

## Behavioral evaluation

Each new-skill case ran in a fresh independent agent context with the skill and relevant sources. Agents could use the core/references/template but were told not to read examples, oracle tests, baseline reports, or other agent output. They did not edit source files. Reports were inspected against tests/scenarios.md. These are manual report-quality assessments, not numerical UX scores.

| Case | Actual work and evidence | Assessment / limit |
|---|---|---|
| A1 — supplied design observations and written flow | [Actual report](results/artifacts/report.md) cites D01–D05, F01–F04, and supplied node/frame names; calculates 2.81:1 from supplied colors; provides coverage and six findings with separate severity/priority/confidence, recommendations and checks | Relevant reporting/evidence gates pass. No live Figma or screenshot inspection was claimed; this tests supplied-artifact reasoning, not authenticated Figma integration |
| A2 — live local page | [Actual report](results/live/report.md), 13 captured/inspected screenshots, and [runtime observations](results/live/observations.json). A real Chromium browser traversed local validation, synthetic 422 rejection, keyboard correction/retry and 1440/768/390/320 CSS-pixel layouts | Live inspection and report gates pass. Reproduced erased input values, missing status semantics, and narrow reflow; six prioritized findings. No production backend, real account, screen-reader or user study was tested |
| A3 — source unavailable | [Actual response](results/no-source/report.md) reports the missing source, leaves dimensions unassessed, assigns no invented findings/priorities, and requests reviewable exports/context | Evidence-honesty gate passes; no completed product audit. This was a simulated no-source request, not a live permission test |

A baseline without the custom skill also [produced a useful artifact review](results/baseline/report.md), accurately distinguishing supplied descriptions from runtime risks. Its prompt asked for concise actionable prioritization and did not prescribe the new full schema. It did not use the new separate severity/confidence and coverage conventions. This is not a controlled measurement of causal improvement, and no fabricated baseline failure is claimed.

A4 written-flow-only, A5 live production payment boundary, and A6 conflicting dated sources remain documented scenarios; they were not independently executed in this release. No authenticated Figma file was supplied. The acquisition branch is documented using actual available read/screenshot capability concepts and official Figma integration documentation, but end-to-end connector access is unverified.

## Evidence provenance and limits

Sources and fixtures are original synthetic inputs, not copied third-party designs. The live server is loopback-only and always rejects synthetic submissions without creating accounts or storing payloads. Captures/observations belong to that local run and retain its original date, URL, state, and viewport. Artifact-report paths were normalized when archived; substantive findings were not edited.

Severity and predicted user impact remain expert judgments. No conversion/abandonment figures, full accessibility conformance, production defects, or general model performance are established. Report validation checks structure and traceability, not whether a cited observation is true or a recommendation is correct. Prototype traversal, Figma file permissions, assistive technology, and actual production journeys need their own appropriate access and evidence.

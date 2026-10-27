# Implementation evaluation

Date: 2026-10-27. This evaluation adds actual frontend implementation and browser evidence to the earlier proposal-only pass.

## Method

Two original single-file interfaces were created with explicit sandbox API contracts: a registration form and a searchable records table. Each task ran in a fresh isolated agent context, first with the skill from commit `4a4cb89`, then with the upgraded skill. Each candidate started from the same respective seed. Candidates could read the relevant skill and fixture, implement code, and run their own checks, but were instructed not to read the acceptance runner, other candidates, or answer artifacts. They were not given the suspected recovery flaw or an intended solution. Candidates did not browse.

A separate browser runner then exercised the resulting HTML. Independent review added a generic 503 case, tightened an ambiguous success assertion, and corrected the final registration reference. The pre-review upgraded registration artifact is retained under `candidate/`; final results include this maintainer correction rather than implying an untouched agent benchmark. Requests were intercepted on a loopback server; no account or record was created. The local run used Node 22.22.2, Playwright 1.62.1, and Chromium 151.0.7922.34 on macOS arm64. See [raw results and artifact hashes](implementation-results.json). The seven [HTML artifacts](fixtures/README.md) retain the inputs and candidate outputs. The baseline skill remains available in Git history.

## Task prompts

Registration:

> Improve registration.html for new small-team coordinators. Make the form understandable and accessible, handle submission/validation/feedback/recovery properly, and preserve the endpoint, JSON payload, native form behavior where appropriate, design tokens, and existing security boundaries. Implement actual changes in that HTML file. Do not add dependencies. The comments define the sandbox API contract. No real backend is available. Write a brief report with selected principles, actual checks, and limitations.

Records:

> Improve records.html for operations users finding team records. Make its data states understandable, actions relevant, navigation predictable, and behavior accessible/responsive. Preserve filtering, URL/deep-link behavior, export semantics, routes, permissions, and design tokens. Implement actual changes in that HTML file. Do not add dependencies. The comments define the sandbox API contract. No real backend is available. Write a brief report with selected principles, actual checks, and limitations.

Both were supplied with the applicable skill path and an isolated working directory, with the same offline and evidence-access restrictions.

## Observations

| Artifact stage | Registration checks | Records checks | Meaning |
|---|---|---|---|
| Intentionally incomplete seeds | 1/6 pass | 1/7 pass | Acceptance checks detect missing behavior; 11 fail |
| Pre-upgrade skill implementations | 4/6 pass | 7/7 pass | Most behavior worked; transport recovery guidance and generic 503 handling were incomplete |
| Upgraded agent output before review | 5/6 pass | 7/7 pass | Transport recovery improved; generic 503 handling still needed correction |
| Reviewed final references | 6/6 pass | 7/7 pass | All 13 targeted acceptance checks pass |

These are counts of task-specific assertions, not numerical usability scores.

The baseline registration implementation honestly said it could not confirm creation, retained entries, and avoided automatic retry. It then invited another submission after checking the connection, without telling users how to reconcile the uncertain creation or warning that it might already have completed. The upgrade moves unknown-outcome handling into the main instructions and frontend workflow, supported by a concrete form playbook. The upgraded agent implementation shows that warning and asks for acknowledgement before retry, without inventing a status API or sign-in route. Review then found that its generic 503 branch still claimed non-creation without a non-commit guarantee. A new case reproduced that failure; the final reference treats generic 503 as unconfirmed. The playbook and workflow now make that distinction explicit.

The success-transition assertion originally matched words also present in failure messages. It now requires an unambiguous positive outcome and excludes rejection/uncertainty text. A deliberate unconfirmed-response control proves that this browser case fails when it should.

The baseline records implementation already passed all seven checks. No measured improvement is claimed for it. The upgraded implementation retained those behaviors: permission-aware actions, distinct data states, URL/history/export contracts, current-scope response protection, and layout containment.

The main skill also now routes by requested deliverable, exposes a small evidence → mechanism → change → check decision process, and provides a component-specific playbook. Those additions are practical guidance; the two-task evaluation does not establish every proposed benefit.

## Reproduce and extend

Follow [browser setup](browser/README.md). Run completed fixtures for the passing reference suite. Run the historical baseline or seeds to inspect expected failures. The runner creates a new context per check and reports nonzero on failure.

For a new skill evaluation, provide only a fresh seed copy, the task, and the target skill. Keep the oracle and completed files unavailable to the candidate. Inspect actual code, screenshots/interactions, and result evidence. Preserve legitimate alternative implementations; English message patterns are proxies, and a different valid wording should receive human review rather than an automatic semantic judgment.

## Limits

This was one candidate implementation per task/version, not repeated randomized trials. It cannot establish general causal improvement, behavior across all models, production acceptance, or usability outcomes. It covers registration and empty/data-state tasks, plus some refactor invariants; the other original scenarios remain documented behavioral tasks. All API responses were mocked. Screen readers, real touch devices, password managers, other engines, full conformance, and representative user comprehension were not tested by the independent runner. Three-width containment and a simple keyboard path are narrower claims than complete responsive or accessibility validation.

Candidate self-reported additional checks are not counted in the independent 13-check result. The two final desktop screenshots from the independent run were visually inspected; this is visual review, not evidence of user comprehension.

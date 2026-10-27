# Expected behaviors and evaluation procedure

For each scenario, run a fresh agent context with SKILL.md and file access to this package. For offline evaluation disable browsing, but permit relevant local reads. Save the prompt, accessible fixtures, actual response/artifacts, files consulted when observable, model/client version, commands/results, and limitations. Compare a baseline without this package when useful; never fabricate a baseline failure.

Assess each applicable criterion as Pass / Fail / Not assessed, with concrete evidence rather than a numerical UX score. Relevant-principle lists below are examples, not mandatory named-law quotas. A different defensible selection can pass. A complete implementation task requires an implemented artifact and relevant verification when fixtures/tools allow it. A proposal alone does not pass implementation.

Cross-scenario gates: selective loading; actionable decisions; accurate names/sources; explicit trade-offs; honest evidence/verification; accessibility and state coverage; preserved task scope; usable without web access. Do not require runtime browsing simply to repeat bundled facts.

## T1: SaaS landing page

- **Expected behavior:** Inspect routes/tokens; establish audience/task assumptions; create clear content hierarchy and responsive action paths; distinguish functional from placeholder integrations.
- **Relevant principles:** Jakob’s Law; Proximity; Von Restorff Effect.
- **Poor response signs:** Dump all laws; fake testimonials; replace the stack; confuse visual emphasis with proven conversion.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T2: Cluttered analytics dashboard

- **Expected behavior:** Identify competing scope controls; group by task and retain visible date/filter context; preserve exports and saved filters; define regression checks and validate relevant widths.
- **Relevant principles:** Cognitive Load; Chunking; Working Memory.
- **Poor response signs:** Delete required metrics; invent usage counts; force everything behind menus; call a screenshot a keyboard test.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T3: Accessible registration form

- **Expected behavior:** Add persistent labels, textual associated errors, retained values, safe pending/retry states and logical focus; inspect backend contract; test rejection and keyboard paths.
- **Relevant principles:** Working Memory; Postel’s Law; Doherty Threshold; supplementary WCAG.
- **Poor response signs:** Claim Fitts mandates 44px; weaken server validation; silently change passwords; claim WCAG compliance from a checklist.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T4: Confusing navigation

- **Expected behavior:** Separate observed label/visual issues from unverified runtime behavior; retain destinations, improve terminology and navigation semantics; propose task-based validation.
- **Relevant principles:** Mental Model; Jakob’s Law; Hick’s Law.
- **Poor response signs:** Insist on seven items; claim unsaved data loss was observed without access; rename every route without migration.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T5: Empty state and calls to action

- **Expected behavior:** Inspect existing state signals; distinguish causes; offer create, clear filters, retry, or access guidance appropriately; preserve permissions; test branches.
- **Relevant principles:** Mental Model; Paradox of the Active User; Doherty Threshold.
- **Poor response signs:** Show create to unauthorized users; represent failure as no data; reset all settings when clearing a filter.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T6: Preserve behavior during refactor

- **Expected behavior:** Inspect current components/contracts; choose scoped changes and existing primitives; retain state and navigation behavior; run relevant regression checks and report actual results.
- **Relevant principles:** Jakob’s Law; Law of Similarity; Working Memory.
- **Poor response signs:** Rewrite state management; install a new UI library without need; drop URL state; claim tests passed without executing them.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## T7: Conflicting principles and misleading progress

- **Expected behavior:** Challenge the unsupported numeric claim and fabricated progress; preserve expert access; propose meaningful grouping and honest task-derived progress; identify missing evidence and a validation method.
- **Relevant principles:** Miller’s Law; Hick’s Law; Jakob’s Law; Flow; Goal-Gradient Effect.
- **Poor response signs:** Obey false premise; manufacture completion; cite nonexistent experiments; claim laws guarantee outcomes.
- **Evidence to retain:** Actual decisions/artifact, selected references, relevant acceptance checks and results, and clearly disclosed unknowns.

## Executable implementation subset

The repository’s [browser checks](https://github.com/sharmadipesh/cooking-ux/blob/main/evaluation/laws-of-ux-skill/browser/README.md) exercise registration (T3) and records/empty states (T5), including some contract-preservation behavior relevant to T6. See the [recorded evaluation](https://github.com/sharmadipesh/cooking-ux/blob/main/evaluation/laws-of-ux-skill/implementation-evaluation.md); both live in `evaluation/laws-of-ux-skill/`, outside this package. This does not turn the other proposal scenarios into completed implementation tests. Use fresh seed copies and do not provide the completed artifacts or test answers to a candidate agent.

For unknown mutation outcomes, require uncertainty plus existing reconciliation or an informed retry warning; do not accept a confident failure claim or an invented verification endpoint. For async reads, test late success, error, and permission changes against the active scope as relevant. Inspect actual rendered messages and code when an English-pattern assertion might reject a legitimate alternative.

## Completion rule

Mark a scenario passed only after inspecting its actual output against the criteria. A structural validator does not run these tasks or grade semantic accuracy. Report unrun cases and limits of proposal-only tests. If a test fails, retain the failure, make a narrow supported correction, then rerun it and relevant neighboring cases.

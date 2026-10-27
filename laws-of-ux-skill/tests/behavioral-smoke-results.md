# Independent offline behavioral pass

Context: delegated agent, 2026-10-27. Model/client version not exposed to agent. No browsing, no app repository or screenshots supplied, no implementation requested for this pass. Read local skill and references with exec_command; commands completed successfully. The scenario text is the only product evidence. Responses below are actual proposals, not completed implementations. T7 was answered first after loading references. T1–T6 share this evaluation context, rather than fresh isolated contexts as the package procedure recommends; evaluator awareness can bias assessment.

## T7 actual response

Miller’s Law does not establish seven as the ideal navigation count: its memory findings do not impose a menu limit. Keep all 12 expert destinations accessible. Prototype task-based groups with clearer labels while preserving routes and direct access to important expert actions; compare this with the current navigation before adding nesting. Grouping can reduce scanning effort but extra levels can slow familiar tasks ([Miller and Hick](../references/cognitive-load-and-decision-making.md)).

Do not ship fabricated 80% progress. Define meaningful required onboarding steps and calculate completed required steps / total required steps from authoritative saved state. Show “2 of 3 required steps complete,” list remaining work, distinguish optional steps, and support resumption. Failed or skipped required steps cannot count as complete. This applies Goal-Gradient without misleading people ([reference](../references/interaction-and-feedback.md#goal-gradient-effect)).

Without research, this is a hypothesis. Before release, run representative expert tasks against both navigation versions, measuring success, errors, backtracking and completion time. Check every route, keyboard/focus behavior, and narrow layouts. Test progress after failure, refresh and resumption; measure useful activation alongside completion. No outcomes or runtime checks have been verified.

## T1 actual response

Assume small-team coordinators want to understand the scheduling product and start a trial. Before editing, inspect app instructions, routes, tokens, existing components and the trial entry point. Reuse that system for a responsive page: familiar navigation; headline “Make team scheduling simpler”; brief audience/value explanation; one prominent “Start a trial” action; then real feature details and relevant practical questions. Only promise supported capabilities. Connect the CTA to a verified existing trial flow; if none exists, explicitly label a prototype and do not imply signup works. Do not invent customers, testimonials or conversion evidence.

Jakob supports familiar patterns; Proximity groups each benefit with its explanation; Von Restorff supports one primary action, without proving higher conversion ([perception reference](../references/visual-hierarchy-and-perception.md)). Trade-off: concise content must leave enough detail for evaluation. Acceptance: visitors can explain the product and locate trial entry; verify actual destination, keyboard focus, contrast, and mobile/tablet/desktop layouts. With no app fixture supplied, this remains an unimplemented proposal.

## T2 actual response

First map what each date selector controls and whether their ranges are intentionally independent; do not silently merge different reporting scopes. Keep all 18 metrics, exports and saved filters. Propose task-labeled metric sections, consistent units and comparison labels, with restrained emphasis within each section. Keep the applicable date range and active-filter summary beside results. Consolidate duplicate date controls only if they truly share state; otherwise label each scope explicitly. Keep export and saved-filter actions discoverable in the report toolbar.

Chunking and Working Memory support grouping and visible context ([reference](../references/cognitive-load-and-decision-making.md)); grouping may add scrolling, so compare task completion before hiding details. With no analytics, no metric is proven more important. Acceptance: all metrics remain reachable; saved filters, URL state, date scopes and exported results retain existing semantics; verify loading/error cases, keyboard order and relevant widths. These are proposed checks, none run.

## T3 actual response

Inspect the current form, submit handler and endpoint/payload contract first. Add persistent associated labels and plain requirements; retain red borders only as supplemental cues. Associate textual errors with fields, mark invalid state, provide a focusable error summary after rejection, and preserve entered values in component state through failed requests without adding persistent credential storage. Preserve raw credential values and server validation. During a pending request, guard submission, communicate “Submitting,” and prevent duplicate requests; on failure restore retry with retained edits and clear outcome text. Never report success before the server confirms it.

Working Memory supports retained input and Doherty supports immediate honest feedback ([references](../references/interaction-and-feedback.md)); accessibility requirements are separate ([checklist](../references/usability-review-checklist.md)). Focus changes should assist recovery without disrupting typing. Acceptance: unchanged endpoint and payload; keyboard-only completion; server field errors, timeout/retry, slow response and rapid repeated submissions; readable errors at zoom/narrow widths. No fixture was provided, so no code or accessibility compliance was verified.

## T4 actual response

The prompt reports jargon and a control that leaves without saving, but the screenshots and route definitions themselves have not been supplied here. Those artifacts could support label/layout and destination findings; they would not establish actual unsaved-data behavior. Retain all 12 destinations and route paths. Propose domain-language labels, task-based groups, visible current location and real links for destinations. Give departure and save actions distinct accurate names; inspect runtime save semantics before choosing a draft-preservation or unsaved-change recovery design.

Mental Model and Jakob favor predictable labels and behavior; Hick suggests organizing choices, not a seven-item limit ([psychology](../references/psychology-and-mental-models.md), [cognition](../references/cognitive-load-and-decision-making.md)). Grouping trades shorter scanning for possible extra navigation. Validate representative expert findability tasks, every deep link, browser back, unsaved edits, and keyboard/mobile navigation. These are hypotheses and planned checks; severity cannot be confidently assigned without inspecting evidence.

## T5 actual response

Inspect the table's request, authorization and filter state signals before editing. Render explicit branches rather than inferring all causes from an empty array: loading → “Loading records” with appropriate status; API failure → “Couldn’t load records” and Retry; denied → “You don’t have access” with the existing access-help route; successful filtered zero → “No records match these filters” and Clear filters; successful unfiltered zero → “No records yet” and Create only when authorized. Preserve table context and show old data as stale, if supported, during refresh. Retry should preserve filters; Clear filters should reset only relevant filter state, not unrelated settings. Use the existing authorization rules and never expose a create action to a user lacking permission.

Mental Model supports truthful cause-specific messages and Doherty supports timely status ([references](../references/interaction-and-feedback.md)). More branches increase implementation complexity but prevent misleading recovery actions. Acceptance: exercise each branch and transitions between them, including permission changes, successful empty responses, rejection/retry and keyboard access to CTAs; announce meaningful status without stealing focus. All are proposal-only checks.

## T6 actual response

Before editing, inspect the filter component, existing accessible primitives, query parsing/serialization, saved-filter handling, export inputs, API payloads and current tests. Make a narrow refactor: extract repeated presentation where useful, use semantic labels/fieldsets and native controls, keep existing state ownership and handlers, and provide logical keyboard order and visible focus. Preserve query names, defaults, deep-link hydration, browser back/forward, saved-filter semantics, export output and payload shapes. Use existing dialog/popover primitives if present; verify their keyboard and focus behavior rather than adding a new library.

Similarity supports consistent controls; Working Memory supports retained selections ([perception](../references/visual-hierarchy-and-perception.md), [cognition](../references/cognitive-load-and-decision-making.md)). Smaller extraction improves readability while limiting behavioral risk. Acceptance: compare existing and refactored URL round trips, saved-filter application, exports and network payloads; run relevant existing tests plus keyboard and narrow-layout checks. No repository fixture was supplied, so nothing has been refactored or tested.

## Assessment against expected behaviors

| Case | Proposal checks | Implementation/runtime checks | Overall scenario |
|---|---|---|---|
| T1 | Pass: inspect-first plan, audience, hierarchy, system reuse, honest integration, responsive acceptance | Not assessed: no fixture/artifact; routes and tokens not inspected | Not passed as implementation |
| T2 | Pass: scope mapping, retained 18 metrics/export/saved filters, visible context, explicit trade-off and checks | Not assessed: no actual dashboard or widths exercised | Proposal passes; implemented outcome not assessed |
| T3 | Pass: labels, associated text errors, retained values, pending guard, focus/retry and contract checks | Not assessed: backend contract, keyboard and rejection paths untested | Not passed as implementation |
| T4 | Pass: carefully separates reported from observed evidence, keeps routes/destinations, improves semantics, task validation | Not assessed: screenshots/routes unavailable; runtime save behavior untested | Proposal passes; audit findings unverified |
| T5 | Pass: signal inspection, five causes, permission-gated CTAs, limited filter reset, state tests | Not assessed: branches and permissions not executed | Proposal passes; implementation not assessed |
| T6 | Pass: scoped refactor plan, primitives, explicit preserved contracts and regressions | Not assessed: no code refactored or tests run | Not passed as implementation |
| T7 | Pass: rejects numeric premise and deception, protects expert access, proposes real progress and research | Not assessed: routing/progress implementation and user outcomes | Pass for requested proposal only |

Cross-scenario: offline usability Pass; actionable decisions Pass; selective reference categories Pass (four topic files cover different scenarios, no 30-law response dump); explicit trade-offs Pass; evidence honesty Pass; proposed accessibility/state coverage Pass. Actual accessibility, responsive behavior, contract preservation and runtime success Not assessed. Names and definitions agree with inspected bundled entries; external source accuracy Not assessed offline.

## Defects and limitations found

- No definite inaccurate definition found in the consulted entries. Miller, Fitts, Goal-Gradient and Doherty include appropriate scope cautions. Statements remain summaries rather than exhaustive scientific definitions.
- Evaluator output originally contained a malformed local link. Links in this archived evidence were normalized to package-relative paths; response decisions were not changed.
- Package evaluation requires fresh contexts for each scenario. This delegated batch does not meet that isolation requirement; treat it as a behavioral smoke pass, not seven isolated benchmark runs.
- No implementation fixtures means the pass cannot demonstrate that the skill produces functioning frontend changes. The package explicitly recognizes this limitation; a proposal must not be counted as completed implementation.
- Expected-behaviors.md is broad on cross-scenario accessibility/state coverage; assessment must remain relevant to each request, not require all checklist rows for a proposal.

## Files consulted

All paths relative to the package root:

- SKILL.md
- tests/test-prompts.md
- tests/expected-behaviors.md
- references/cognitive-load-and-decision-making.md
- references/interaction-and-feedback.md
- references/psychology-and-mental-models.md
- references/visual-hierarchy-and-perception.md
- references/usability-review-checklist.md
- workflows/frontend-implementation.md
- workflows/design-from-scratch.md

No package files edited. Only a temporary evidence file was written; its contents are archived here with portable links.

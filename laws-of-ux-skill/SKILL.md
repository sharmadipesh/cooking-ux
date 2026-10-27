---
name: laws-of-ux-skill
description: Apply relevant UX principles when designing pages, reviewing interfaces, improving user flows, or implementing frontend usability changes. Use for UI hierarchy, navigation, forms, feedback, cognitive load, and evidence-informed design trade-offs.
---
# Laws of UX in practice

Turn interface problems into concrete, testable design and code decisions. Match the deliverable to the request: implement for build/change tasks, report findings for audits, and answer advice questions directly. Work offline from the bundled references; browsing is optional for updates or new questions. This independent skill draws on Jon Yablonski’s Laws of UX, not an official endorsement or a substitute for user research.

## Understand → Analyze → Select principles → Apply → Validate → Explain

1. **Understand.** Identify the audience, main task, desired outcome, context of use, constraints, and requested deliverable. Ask only questions that block a meaningful decision; otherwise state assumptions and proceed. In a repository, inspect the affected route, design system, components, data contracts, and existing tests before editing. Preserve a short task contract: what must improve and which behaviors/contracts must stay intact.
2. **Analyze.** Trace the journey from entry to completion, including failure and recovery. For an audit, inspect real screens and interactions when possible. Record what was observed, where, and with what device/state. Label deductions from code or screenshots and untested user-behavior predictions. Do not claim keyboard, responsive, or runtime validation from a static image.
3. **Select principles.** Match the actual failure mechanism using the table below; start with one to three principles and add others only for a distinct need. Consult [the complete inventory](references/ux-laws-index.md) to locate an unfamiliar concept. Read the selected entries, especially their limitations. Never dump all 30 laws or invent a named law. If a principle does not explain a concrete cause or change, omit it.
4. **Apply.** Connect each principle to a specific change: “Because users must remember the date range, keep it visible beside the results (Working Memory).” Prefer working improvements over theory. Preserve functioning behavior, routes, API contracts, permissions, and existing conventions unless a justified change is in scope. Choose a solution that balances task success, accessibility, user control, engineering effort, and domain risk.
5. **Validate.** Set an observable acceptance condition before changing the UI. Exercise the main task, failure/retry, keyboard/focus, mobile/tablet/desktop layout, and affected regression paths as relevant. Check [the review checklist](references/usability-review-checklist.md). Report which checks actually ran and what remains uncertain. Laws suggest hypotheses; they do not prove usability or accessibility compliance.
6. **Explain.** Briefly state the change, user benefit, selected principle, trade-off, and validation result. Link the bundled entry or its original source for significant decisions. Separate observations from hypotheses and do not invent measurements or numerical usability scores.

## Select by mechanism

| Interface symptom | Start with | Read |
|---|---|---|
| Weak grouping, unclear hierarchy, competing highlights | Proximity, Similarity, Von Restorff | [Perception](references/visual-hierarchy-and-perception.md) |
| Too much to compare, remember, or interpret | Choice Overload, Working Memory, Cognitive Load | [Cognition](references/cognitive-load-and-decision-making.md) |
| Small controls, silent delays, interruptions, difficult setup | Fitts, Doherty, Flow, Active User | [Interaction](references/interaction-and-feedback.md) |
| Surprising behavior, unfamiliar labels, misleading conclusions | Mental Model, Jakob, Cognitive Bias | [Psychology](references/psychology-and-mental-models.md) |
| Need complexity reduction without losing capability | Tesler, Occam, Hick | [Cognition](references/cognitive-load-and-decision-making.md) |
| Unclear completion or abandoned drafts | Goal-Gradient, Zeigarnik, Peak-End | [Interaction](references/interaction-and-feedback.md) and [Psychology](references/psychology-and-mental-models.md) |

## Apply to the component and verify the decision

Read only the relevant section of [the component playbook](references/component-playbook.md) for forms, search/tables, navigation, onboarding, dialogs, and responsive hierarchy. It covers concrete states, contract preservation, and acceptance checks. For async interfaces, protect current results and permissions from older responses; “empty” requires successful data, not an exception.

For limited evidence, competing principles, or unclear success criteria, use [decision and validation guidance](references/decision-and-validation.md). Keep a short evidence → mechanism → change → check chain; a principle's name does not prove an outcome. Validate implementation and distinguish sandbox checks from production or user evidence.

## Choose the workflow

- New product/page: [design from scratch](workflows/design-from-scratch.md).
- Evaluate an interface: [UI audit](workflows/ui-audit.md).
- Improve a scoped flow/component: [improve existing UI](workflows/improve-existing-ui.md).
- Implement/refactor code: [frontend implementation](workflows/frontend-implementation.md).
- Need concrete output patterns: [decision examples](examples/good-and-bad-design-decisions.md), [audit example](examples/ui-review-example.md), [code example](examples/implementation-example.md).
- Need article concepts or accessibility distinctions: [related concepts](references/related-concepts.md).
- Need provenance, verification scope, or supplementary standards: [source links](references/source-links.md).

## Prioritize and report

Use task impact, severity, reach/frequency, evidence confidence, and implementation effort. Fix blockers and irreversible harm first, then substantial recurring friction, then smaller clarity and cosmetic issues. Accessibility exclusion can outrank a more frequent cosmetic problem. Priority labels:

- **Critical:** core task blocked, serious harm, or irreversible loss; no viable workaround.
- **High:** major task disruption or exclusion with a costly workaround.
- **Medium:** recurring confusion or effort with a reasonable workaround.
- **Low:** minor friction or polish with limited task impact.

For each audit issue provide: **problem and evidence/location; user impact; relevant principle; recommendation; priority with reason; implementation suggestion; assumptions/limitations.** State whether it is observed or a hypothesis. Do not claim an audit finding without evidence or pretend an illustrative example was inspected.

## Guard against misuse

- These concepts include empirical effects, models, and design heuristics with different scope. They are not universal prescriptions. Seven is not a navigation limit, 80/20 is not a measured distribution, and 400 ms is not a universal performance guarantee.
- When principles conflict, state the competing needs, compare viable options, choose for the audience/task, and specify a validation method. Do not simplify away essential information or hide expert tools just to reduce visible choices.
- Distinguish known rejection from unknown mutation outcome after timeout, abort, or connection failure. Use existing reconciliation or informed retry guidance; do not invent status endpoints or automatically retry non-idempotent work. Use honest progress and outcome messages. Do not fabricate completion, scarcity, success, or urgency. A source recommendation is not automatically suitable for the user’s goals.
- Accessibility is a separate requirement: use semantic HTML, labeled controls, keyboard support, visible focus, readable content, non-color cues, responsive layout, and appropriate error recovery. Fitts’s Law does not specify WCAG target dimensions. Reuse accessible primitives before inventing custom widgets.
- Prefer small, reversible changes within the requested scope. Do not change architecture or install dependencies solely to demonstrate a law. Report untested assumptions and remaining limitations.

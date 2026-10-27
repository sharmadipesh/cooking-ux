# Make decisions that can be checked

This is package-authored practice for applying the referenced concepts. Read it when a task is ambiguous, principles compete, evidence is limited, or an audit needs a defensible recommendation.

## Establish a small task contract

Identify the intended deliverable, audience/task, scope, and invariants before changing anything. For code, invariants include the relevant routes, request/response shape, state ownership, permissions, existing component conventions, and working interactions. For design, identify required content, brand constraints, devices, and the user's next meaningful action. Do not turn missing optional research into a reason to stop all useful work.

Separate evidence:

| Evidence | How to use it |
|---|---|
| Direct observation | Record route/state/device and reproduction or screenshot |
| Supplied requirement/report | Attribute it to the user or source; do not claim personal reproduction |
| Code inference | Cite the affected behavior and note runtime limits |
| User-behavior hypothesis | State what might happen and how to test it |

A screenshot can show unclear grouping; it cannot prove that people abandon a task. A mock API can test handling of a response; it cannot establish production integration.

## Select by cause, not by vocabulary

1. State the task obstacle in plain words: “Reviewers have to remember a period that is no longer visible.”
2. Identify the likely mechanism: memory demand, motor effort, ambiguous meaning, comparison effort, unfamiliar behavior, or missing feedback.
3. Choose the few principles that explain it. If a named law adds no explanatory value, leave it out.
4. Compare the smallest useful options against the task contract. A more attractive screen and fewer visible controls are not independent proof of improvement.
5. Define the intended result and an observable check before implementation.

Keep an internal decision note when useful:

> Evidence/problem → constraint → principle/mechanism → concrete change → acceptance check → trade-off.

Example: “The supplied screenshot separates labels from values. Keep each pair together (Proximity), preserving the comparison order. Check grouping and reading order at narrow widths. This may add height; user comprehension remains a hypothesis.”

## Resolve conflicts

| Competing needs | Resolve using | Example check |
|---|---|---|
| Fewer initial choices vs expert access | Experience level, task frequency/urgency, findability | Compare direct versus grouped commands on realistic tasks |
| Minimal appearance vs necessary detail | Comprehension, error cost, discoverability | Can users understand fees/constraints before committing? |
| Larger targets vs data density | Actual activation effort, device, adjacent actions | Pointer/touch and keyboard use with real row content |
| Faster feedback vs trustworthy outcomes | Immediate honest acknowledgement; authoritative completion | Pending never masquerades as saved/paid/created |
| Automation vs user control | Consequence of wrong defaults and correction effort | Explain and recover from a mistaken prefill or selection |

Do not settle a conflict by counting laws or claiming one always outranks another. Use accessibility, task safety, explicit requirements, context, and evidence. When evidence is insufficient, choose a reversible option and name what would change the decision.

## Match validation to the claim

- **Content/layout:** inspect real text, hierarchy, contrast, widths, zoom, and long/localized content.
- **Interaction:** operate the controls; inspect names, focus, keyboard paths, state transitions, and recovery.
- **Data contracts:** check request payloads, authoritative response handling, permissions, URL state, and relevant regressions.
- **Async behavior:** test pending, rejection, transport uncertainty, duplicate actions, stale/out-of-order results, and retry semantics when relevant.
- **User outcomes:** use representative task attempts or actual research; automated assertions cannot establish comprehension, confidence, conversion, or satisfaction.

Prefer checks that could fail if the intended improvement is absent. Reading your own new code, matching a recommended phrase, or listing applicable laws is not behavioral validation. Reuse existing test tools; do not add a framework solely for an easy change.

## Deliver the requested work

- **Build/improve/refactor:** produce the artifact or code, identify significant decisions briefly, and state checks run, results, and limitations. A plan alone does not complete an implementation request when editing is available.
- **Audit:** give prioritized issues with evidence, impact, selected principle, improvement, implementation direction, and uncertainty. Do not change code when only review was requested.
- **Design/prototype:** show the design and its states, explain material trade-offs, and distinguish a runnable prototype from a working production integration.
- **Advice-only:** answer the question directly; do not impose a full audit or universal checklist.

Do not perform unrelated publication, deployment, installation, or architectural changes because a UX principle suggests them. Preserve the user's scope and authorization. Report what is actually prepared, implemented, simulated, tested, or untested in ordinary language.

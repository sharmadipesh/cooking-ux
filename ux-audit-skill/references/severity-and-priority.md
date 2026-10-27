# Severity, priority, and confidence

These are package-specific reporting conventions, not a universal industry scale or an overall UX score. Consider impact, frequency, and persistence where there is evidence; never invent them.

## Severity: consequence if the issue occurs

| Level | Meaning |
|---|---|
| Critical | The core task is blocked, users face serious harm or irreversible loss, or a user group is excluded with no practical workaround |
| Major | Significant task disruption, likely serious error, or substantial recurring friction; workaround is costly or difficult |
| Moderate | Recoverable confusion or extra effort; a reasonable workaround exists |
| Minor | Limited task impact, low-cost inconsistency, or polish |

Explain the affected task/users and recoverability. Unknown frequency does not erase a reproducible severe barrier. Cosmetic preference is not Critical. A screenshot may support a severe design risk without establishing a severe production failure; label that distinction.

## Priority: what to do and when

| Level | Default action |
|---|---|
| P0 | Address or contain immediate serious risk before the affected release/use; investigate urgently if a high-consequence uncertainty needs verification |
| P1 | Next meaningful improvement cycle: a well-supported, high-impact problem or important dependency |
| P2 | Planned improvement or targeted validation with meaningful but less urgent benefit |
| P3 | Opportunistic polish or lower-value exploration |

State the reason, considering severity, evidence confidence, known reach, dependencies, and effort when available. Do not multiply invented numbers into a ranking. Priority need not mechanically mirror severity: a severe hypothesis may first need investigation, while a modest shared-component fix may have evidenced broad reach. Distinguish “investigate” from “implement” when uncertainty changes the action. Do not present a time/effort estimate as measured without input from the team or code.

## Confidence: strength of support

- **High:** directly reproducible or measured in the relevant source/state, with important assumptions resolved.
- **Medium:** the symptom is observed or explicitly supplied, but the mechanism or user consequence needs validation.
- **Low:** sparse, indirect, or conflicting evidence; present as a hypothesis/candidate issue and propose a check.

Confidence is not certainty about every predicted user outcome. State which part is measured and which part is inferred. A supplied screenshot is valid supplied evidence, not an auditor's live observation. Access gaps are coverage limits, not Low-confidence invented findings.

## Order the work

Lead with task blockers, consequential mistakes/exclusion, and recoverability. Then address recurring navigation/comprehension/interaction friction, followed by lower-impact consistency and polish. Identify dependencies and existing strengths worth preserving. Group a shared root cause and list occurrences instead of producing duplicate tickets. Team owners can be suggested as roles; do not assign work to real people or invent deadlines.

# Design decision examples

These are invented scenarios, not empirical results or audits of named products.

| Situation | Better decision and principle | Poor decision | Acceptance check / trade-off |
|---|---|---|---|
| SaaS landing page has five competing actions | Emphasize the trial entry and offer a secondary demo link (Von Restorff) | Make every action a bright primary button | Visitors can explain the offer and locate the intended action; keep alternatives visible |
| Analyst needs 12 report views | Task-based groups with search/favorites (Chunking, Jakob) | Delete five views because Miller requires seven | Existing report URLs still work; test expert findability |
| Registration has formatting errors | Explain requirements and tolerate harmless phone spacing (Postel) | Silently change credentials or ambiguous dates | Errors remain associated with fields; raw input is retained |
| Dashboard is overloaded | Group by decisions and keep units/date ranges visible (Cognitive Load, Proximity) | Hide required metrics without consulting task needs | Representative review task remains possible without memorizing hidden context |
| New workspace has no content | Explain why it is empty and offer “Create project” plus an optional sample (Active User) | Display only a decorative illustration | Creation is keyboard accessible; permission denial uses different copy |
| Booking ends | Show confirmed reference and next steps (Peak-End) | Say “Success” before the backend confirms | Failed and unknown outcomes remain distinguishable |
| Goal-Gradient versus honesty | Compute completion from real required steps | Pretend a task is nearly complete | Skips/failures do not increase progress |

## Competing principles: choice reduction versus expert efficiency

Hick’s Law suggests reducing unfamiliar choice effort; Jakob’s Law and Flow support familiar fast access for practiced users. A 12-command expert toolbar may be better than three commands hiding nine in submenus. Keep frequent commands visible, group them by task, and offer optional customization only if justified. Evaluate realistic expert and novice tasks separately using task success, errors, and completion time. No universal item count resolves the conflict.

## Explanation pattern

“Kept the active date range beside results so reviewers do not have to remember it while interpreting charts (Working Memory). This adds a small amount of visible text but preserves context. Confirmed that changing the range updates both label and results; usability with the target audience remains untested.”

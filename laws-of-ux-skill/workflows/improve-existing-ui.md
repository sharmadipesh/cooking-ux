# Improve existing UI

1. Inspect the real route and existing implementation, design tokens, component variants, state management, and backend contracts. Record the behavior that must remain available.
2. Identify the task friction and establish a baseline from available evidence: errors, task attempts, field relationships, or missing state feedback. Do not invent analytics.
3. Select principles and compare the smallest viable options. Example: group related analytics by decision (Chunking) before hiding specialist metrics (Hick versus expert access). Document why the chosen change fits the audience.
4. Set acceptance conditions for both improvement and preservation. Example: active filters remain visible, reload/back restores state, existing export parameters remain identical.
5. Make scoped changes using existing components. Keep error recovery and permissions intact. For broader shared changes, inspect affected consumers or prefer a local variant.
6. Validate the task, keyboard/focus, responsive behavior, async states, and appropriate regression paths. Test with representative users when the decision rests on an uncertain mental model.

Deliver the improved artifact/code, concise reasons, checks run, and limitations. Do not rewrite the application to demonstrate psychological terminology.

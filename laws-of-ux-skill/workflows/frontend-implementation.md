# Frontend implementation

Before editing, inspect repository instructions, the affected route, component library, tests, data shape, and mutation semantics. Reuse the framework and architecture already present.

Translate a selected principle into behavior and an acceptance check:

| Need | Implementation direction | Verify |
|---|---|---|
| Clear grouping | semantic headings/fieldsets plus spacing tokens | visual and reading order remain meaningful at narrow widths |
| Easier activation | actual button hit area and separation | pointer, touch, keyboard, accessible name |
| Less memory burden | retained input, active filter summary, comparison view | error/back/reload paths preserve permitted state |
| Responsive feedback | idle/pending/success/error state machine | slow request, rejection, retry, duplicate submission |
| Familiar navigation | real links for destinations and buttons for actions | browser back, deep links, active state, focus |
| Honest progress | completed stages from authoritative task state | optional and failed steps do not inflate progress |

Use native elements first. Custom dialogs need a name, sensible initial focus, contained keyboard focus, an accessible close action, and return focus; prefer the existing tested dialog primitive. Menus, comboboxes, and tabs need their appropriate keyboard behavior; a popup is not automatically an ARIA menu.

For forms, use persistent labels, suitable autocomplete/input types, plain instructions, and field-associated errors. Keep values after failure; validate on the server as well. Avoid aggressive normalization of names, credentials, or ambiguous dates. Announce status without flooding assistive technology and move focus deliberately only when needed.

For tables, keep headers and associations, expose sorting direction, and preserve row-action names. On small screens allow a labeled horizontal scroll region where two-dimensional comparison requires it; do not silently discard essential columns. Empty data, filtered-zero, loading, permission denial, and service failure require different messages and actions.

Use responsive content-driven layouts and existing typography. Respect reduced motion; animation must not delay completion. Avoid permanent live-region chatter, inaccessible icon-only controls, hidden focus, and color-only state encoding.

Run checks appropriate to the changed risk: component checks for state transitions, existing contract tests for data behavior, and real browser checks for keyboard/layout. Report what ran; compiling code does not establish usability or WCAG compliance. See the checklist and implementation example for acceptance cases.

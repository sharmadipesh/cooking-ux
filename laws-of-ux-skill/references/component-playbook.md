# From UX mechanism to component behavior

This is package-authored implementation guidance, not a list of additional Laws of UX laws. Use only the section relevant to the task. A familiar pattern is a starting hypothesis; inspect the audience, existing components, data contracts, and actual behavior before choosing it.

## Forms and registration

**Mechanisms:** reduce memory demand (Working Memory), accept understandable input (Postel), and acknowledge actions promptly (Doherty).

- Keep persistent labels, requirements before input, and field-associated text errors. Use native input semantics and existing accessible primitives. Error recovery must preserve non-sensitive context and editable values; never introduce password persistence in storage, URLs, logs, or analytics.
- Retain the endpoint, method, payload keys/types, authorization, CSRF protections, and server validation. Harmless display normalization must not alter credentials, ambiguous dates, names, or identifiers without a domain rule.
- Distinguish idle → pending → confirmed success / known rejection / unknown outcome. Prevent every enhanced native submit before checking the pending guard. A disabled visual button alone does not prevent every submission path.
- A transport failure, timeout, aborted request, unreadable response, or generic server/proxy error does not prove that creation failed. Treat a rejection as definitive only when the application contract establishes that the mutation did not commit; a 5xx status alone is not that guarantee. Preserve entries in memory and explain the uncertainty. Before offering another non-idempotent submission, use an existing reconciliation path or clearly warn that it may already have completed and explain how to check. Do not invent a status endpoint, verification email, sign-in route, or idempotency guarantee. Never automatically retry a mutation merely to improve perceived responsiveness.
- Handle field rejection with useful associated text and deliberate focus, without interrupting ongoing typing. A confirmed success can clear sensitive values; a failed request should not erase the user's work.

**Acceptance:** keyboard completion; native invalid input; server rejection and correction; slow response; repeated Enter/click; exact payload; transport uncertainty; long errors and narrow/zoomed layout. A few automated accessibility checks do not establish conformance.

## Search, filters, and data tables

**Mechanisms:** preserve context (Working Memory), organize by task (Chunking), and communicate changing state (Doherty).

| State established by evidence | Show | Useful action |
|---|---|---|
| Initial request pending | Loading and the requested scope | Wait or cancel if supported; no unverified permission-based actions |
| Successful response, empty dataset | Why the workspace is empty | Create only when authorized; otherwise useful guidance |
| Successful response, zero matches | Active filters and no matches | Clear relevant filters or edit the search |
| Permission denial | Access limitation | Existing access-help path; no unauthorized create/export |
| Request failure | Failure and retained query | Retry the same query when appropriate |
| Results | Count, labels, scope, and data | Actions using that same scope |

- Empty is a successful-data state, never a fallback for all exceptions. Treat malformed responses as unavailable/unknown rather than valid zero results.
- Preserve URL keys, deep-link hydration, back/forward behavior, saved views, sorting, pagination, and export meaning that exist in the product. Resetting a filter must not silently reset unrelated settings.
- Capture the query/scope for each request. Use request identity, a state key, cancellation, or the existing data layer so late results, errors, and permissions cannot overwrite a newer query. Cancellation alone does not undo a completed server mutation.
- Keep visible result scope and export aligned. When old data remains during refresh or failure, clearly label it as stale and avoid presenting it as the new query's results.
- Preserve real table headings, sort state, and named row actions. For necessary two-dimensional comparison, prefer a labeled scroll region to silently hiding essential columns. Pagination/virtualization must retain task access and keyboard behavior.

**Acceptance:** initial/deep-linked query, empty, filtered-zero, 403, failure/retry, out-of-order responses, missing permission, back/forward, exports, long data, and keyboard/narrow-layout use as applicable.

## Navigation and information architecture

**Mechanisms:** match users' expectations (Mental Model, Jakob), structure choices (Hick), and group related tasks (Chunking).

- Inventory destinations and the user's main tasks before reorganizing. Preserve useful direct access and route contracts. Use real links for navigation and buttons for actions.
- Prefer domain labels, visible current location, meaningful groups, and discoverable secondary options. Do not apply a seven-item cap or assume every expert command belongs in an overflow menu.
- Distinguish saving, publishing, leaving, and discarding. For consequential changes, inspect draft and recovery behavior before choosing a confirmation or undo pattern.

**Acceptance:** representative findability tasks, deep links, back/forward, unsaved state, active location, keyboard order, and mobile navigation. A shorter menu is not itself success.

## Empty states and onboarding

**Mechanisms:** support learning while doing (Active User), show real distance to a goal (Goal-Gradient), and enable resumption (Zeigarnik).

Explain what happened, why the view is empty, and the next useful action. Make a sample optional and label sample content. Distinguish required from optional setup. Derive progress from actual meaningful completion, keep help available, and allow dismissal/resumption where appropriate. Do not introduce fake progress or make a mandatory tour the price of entry.

**Acceptance:** first use, return after interruption, skipped optional steps, authorization, failure, truthful completion, and useful navigation away from the flow.

## Dialogs, menus, feedback, and motion

**Mechanisms:** maintain context (Working Memory), use familiar behavior (Jakob), and signal important changes (Selective Attention).

Use the existing accessible primitive. A dialog needs a name, deliberate initial focus, contained focus while modal, reachable close/cancel, and sensible return focus. Essential instructions must not exist only on hover. Do not assign menu/tab roles without their associated keyboard model. Keep status announcements concise and avoid stealing focus for routine updates. Respect reduced motion and never delay a completed action for decoration.

**Acceptance:** keyboard entry/exit, Escape where appropriate, return focus, outside click behavior, pending/error states, accessible names, and motion preferences.

## Hierarchy, typography, and responsive composition

**Mechanisms:** clarify relationships (Proximity/Common Region), maintain meaning (Similarity), and reserve emphasis (Von Restorff).

Start with the information and action needed for the task. Group related labels, values, supporting text, and controls. Use fewer emphasis levels rather than making everything prominent. Reuse actual fonts, spacing tokens, and component variants. Choose heading/body/metadata sizing and line-height deliberately for desktop, tablet, and mobile; no law prescribes a universal pixel scale. Keep important labels readable, align content consistently, and constrain long text without dropping information.

**Acceptance:** real content rather than ideal short copy; long labels and values; narrow widths; zoom/text spacing; visible focus; contrast measurements; preserved grouping and reading order. Screenshots establish visual evidence, not comprehension or task success.

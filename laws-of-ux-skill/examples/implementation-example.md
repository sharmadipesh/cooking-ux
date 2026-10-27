# Implementation example: registration error recovery

Illustrative framework-independent fragment. Existing authentication, payload validation, and backend behavior must be inspected before integrating it. This example demonstrates retained values and honest status, not a complete registration backend or accessibility certification.

**Decision:** Working Memory supports keeping values after failure; Postel supports helpful boundary feedback; Doherty supports timely pending feedback. Do not normalize passwords or report success before the request confirms it.

```html
<form id="registration" action="/register" method="post">
  <label for="email">Email address</label>
  <input id="email" name="email" type="email" autocomplete="email"
         required aria-describedby="email-help email-error">
  <p id="email-help">We will send your confirmation here.</p>
  <p id="email-error"></p>
  <button type="submit">Create account</button>
  <p id="registration-status" role="status"></p>
</form>
```

Integration pseudocode (adapt to existing state and error contracts):

```text
on valid native form submit:
    if enhanced submit is unavailable: allow native submission and return
    prevent default for every enhanced submit event
    if request already pending: return
    keep all field values
    mark pending; prevent duplicate requests; show "Creating account…"
    send using existing security, CSRF, payload, and API conventions
    if authoritative response confirms account creation:
        show confirmed result and truthful next step
    else if response identifies invalid email:
        set email error text and aria-invalid=true
        focus email so the associated error can be discovered
    else:
        show a recoverable message using the existing error contract
        for an uncertain network outcome, offer status check/retry safely
    finally:
        clear pending; restore submission availability
on correction:
    update error state consistently; do not erase unrelated values
```

The action URL is an example; do not replace a working application endpoint with it. Client validation supplements server validation. Any required password or other fields need their own persistent labels and error associations. Do not blindly retry a non-idempotent operation after an unknown outcome.

Suggested scoped CSS, subordinate to existing tokens:

```css
label { display: block; margin-block-end: .375rem; }
input { max-inline-size: 100%; box-sizing: border-box; }
button { min-block-size: 2.75rem; padding-inline: 1rem; }
:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; }
```

The button size is an illustrative comfort choice, not a dimension mandated by Fitts. Check rendered contrast, zoom, long error text, and existing focus styles.

For a runnable sandbox implementation and independent browser checks, see [the implementation evaluation](../tests/implementation-evaluation.md). It uses intercepted API responses and is not a production registration service.

## Acceptance cases

- Invalid email gets an associated understandable error; entered values remain.
- Slow response shows pending and suppresses duplicate submits, including repeated Enter presses. Every enhanced submit cancels the native event before checking pending state.
- Rejected request restores submission and offers recovery.
- Unknown outcome does not claim definite failure or success without checking.
- Confirmed success displays the real next step.
- Keyboard focus remains logical; errors and status are available to assistive technology.
- Mobile, tablet, desktop, zoom, and long localized text retain controls and messages.

These are intended checks. They have not been executed against an application as part of this example.

# UX audit — Teamline access request and rejection recovery

## Executive assessment

The local sandbox lets a first-time coordinator reach and submit the access form using a keyboard. Rejection recovery is the main weakness: a 422 response says “Use a different email address,” clears both fields, leaves focus on the submit button, and presents the response without live-region or alert semantics. Narrow layouts also require horizontal scrolling to read the heading and introductory text.

Prioritize preserving correction context, exposing rejection feedback programmatically, and making the form container reflow. Keep the clear heading, short form, native input validation, visible keyboard focus, and plainly labeled primary action. No account was created; the sandbox explicitly says it does not create accounts. Repeated rejection in this environment is not reported as a production acceptance defect.

## Scope and evidence

- **Audience/task:** first-time coordinators requesting account access and recovering from rejection, as supplied in the audit brief. Their real email eligibility rules and familiarity with Teamline are unknown.
- **Source:** `http://127.0.0.1:53413/registration.html`, page title “Teamline access request — audit sandbox.” Inspected 2026-10-27, approximately 10:39–10:42 UTC. No release identifier was exposed.
- **Method:** rendered, headless Chromium through Playwright; actual screenshot captures, keyboard operation, DOM/computed-style and geometry observations, and observed request responses. All screenshots listed below were opened and visually inspected. No repository or server files were read or changed. Only the supplied local origin was visited.
- **Viewports:** desktop 1440×1000, tablet 768×1024, mobile 390×844, and 320×800 CSS pixels. These are desktop-browser viewport simulations, not physical touch-device tests.
- **Actions:** empty submission, five-character password validation, synthetic valid-format email/password submission, mobile rejection, keyboard-only submission and retry with a different synthetic email. Four submitted attempts returned 422 with the same message. Synthetic passwords are not retained in these evidence files.
- **Not assessed:** genuine acceptance/account creation, email delivery, eligibility policy, production backend, login or later onboarding, network-error/pending states, actual assistive technology, other browser engines, physical touch/virtual keyboards, browser zoom beyond the 320 CSS-pixel reflow test, or user research. No broad WCAG conformance claim is made.

All E01–E13 originate from the route above on the audit date. `fullPage` captures at narrow widths expand to the 924-pixel document width; E10–E12 deliberately capture only the viewport so clipping is visible.

| Evidence ID | Source / step | Method and provenance | Viewport / state | Supports / limits |
|---|---|---|---|---|
| E01 | Entry / form | [Observed screenshot](E01-desktop-entry.png) | 1440×1000, empty, full page | Heading, action, placeholder-only field identification, no visible password rule. |
| E02 | First keyboard stop | [Observed screenshot](E02-keyboard-focus.png) | 1440×1000, email focused | Visible email focus. DOM observation confirms email → password → button order. |
| E03 | Empty submit | [Observed screenshot](E03-empty-validation.png) | 1440×1000, empty form | Email receives focus; native validation text is recorded in E14. Native popup is not visible in the screenshot. |
| E04 | Short password | [Observed screenshot](E04-short-password.png) | 1440×1000, filled, password focused | Placeholders disappear when populated. E14 records native minimum-eight-character validation; screenshot alone does not show its popup. |
| E05 | Rejection | [Observed screenshot](E05-desktop-rejected.png) | 1440×1000, 422 response | Both inputs empty and error below button. Response/field values confirmed in E14. |
| E06 | Tablet entry | [Observed screenshot](E06-tablet-entry.png) | 768×1024, full page | Document expands to 924 pixels; use E12 for visible viewport. |
| E07 | Mobile entry | [Observed screenshot](E07-mobile-entry.png) | 390×844, full page | Expanded document layout; not a claim that all content fits on screen. |
| E08 | Reflow entry | [Observed screenshot](E08-reflow-320-entry.png) | 320×800, full page | Expanded document layout; use E11 for clipping. |
| E09 | Mobile rejection | [Observed screenshot](E09-mobile-rejected.png) | 390×844, full page | Same clearing and rejection message at mobile width. |
| E10 | Mobile rejection viewport | [Observed screenshot](E10-mobile-viewport-rejected.png) | 390×844, viewport only | Heading/instructions clipped at right; controls and rejection text remain reachable. |
| E11 | Reflow viewport | [Observed screenshot](E11-reflow-320-viewport.png) | 320×800, viewport only | Heading/instructions need horizontal scrolling to read. |
| E12 | Tablet viewport | [Observed screenshot](E12-tablet-viewport.png) | 768×1024, viewport only | Visible task text fits here, although measured document width still exceeds viewport. |
| E13 | Keyboard rejection | [Observed screenshot](E13-keyboard-rejected.png) | 1440×1000, keyboard submit | Focus outline remains on button, error is below it. |
| E14 | Form controls, responses, geometry, focus | [Direct runtime observation log](observations.json) | All tested widths; entry, validation, rejection, retry | Selectors `input[name=email]`, `input[name=password]`, `button`, `#status`; measured geometry, validation messages, response status, field lengths, attributes and focus. DOM evidence does not establish actual screen-reader speech. |

## Journey and coverage

| Step | User goal/action | Observed outcome | Findings / limits |
|---|---|---|---|
| J1 | Understand the request | Clear account-request heading, sandbox explanation, two fields and one action. At 390/320 pixels, text extends beyond the visible viewport. | UX-03 |
| J2 | Identify and fill fields | Email/password identified only by placeholders; these disappear during entry. No visible password-length instruction. | UX-04, UX-06 |
| J3 | Correct local errors | Empty submission focuses email with native required validation. Five-character password is blocked with a native message specifying eight characters. | Working native validation; UX-06 |
| J4 | Submit | Pointer and keyboard submission reach the local endpoint; tested valid-format attempts return 422. | Acceptance is intentionally outside verified scope. |
| J5 | Understand rejection | “Use a different email address.” appears beneath the button; no live-region/alert semantics or focus movement; no specific eligibility guidance or help action. | UX-02, UX-05 |
| J6 | Correct and retry | Both values have been erased. Keyboard user can reverse-tab twice to email, refill, and retry. Different email returns the same rejection in this sandbox. | UX-01; retry is possible, acceptance unverified. |

| Dimension | Coverage | Evidence / result / limit |
|---|---|---|
| Usability and task clarity | Inspected | Clear purpose/action; weak eligibility and password guidance (E01, E05, E14). |
| Accessibility | Partial | Keyboard order/focus, form associations, status semantics, hit-area geometry and 320-pixel reflow examined. No screen reader or comprehensive WCAG evaluation. |
| Visual hierarchy and readability | Inspected | Heading/action hierarchy and populated fields viewed at tested widths (E01, E04, E10–E12). No numerical contrast claim. |
| Consistency | Partial | Both fields and rejection layouts compared; one page only. |
| Navigation and information architecture | Partial | Entry, correction and retry examined; no links on form. No broader product navigation available. |
| Journey and flow | Partial | Request → rejection → retry traversed; real acceptance and downstream handoffs unavailable. |
| Interaction and system feedback | Partial | Validation and rejection tested; loading and network-failure timing not tested. |
| Responsive/content resilience | Inspected | Four viewport sizes; measurable overflow and narrow-screen clipping. All breakpoints/zoom settings are not covered. |
| Friction and cognitive load | Inspected | Re-entry, disappearing field cues, and undisclosed rule observed; user impact inferred. |
| Error prevention and recovery | Inspected | Native validation works; clearing, semantics and guidance problems reproduced. |
| Trust and user control | Partial | Honest sandbox disclosure present; real account/privacy/security behavior unassessed. |

## Prioritized findings

Severity describes consequence; priority describes recommended sequence, independently of severity. Confidence concerns the observed problem, not a measured conversion effect. No analytics, reach estimates or effort estimates were available.

| ID | Issue / location | Severity | Priority / action | Confidence |
|---|---|---|---|---|
| UX-01 | Rejection erases correction context / form | Moderate | P1 — implement | High |
| UX-02 | Rejection lacks programmatic notification / `#status` | Major | P1 — implement | High for DOM/focus failure; user impact inferred |
| UX-03 | Container fails narrow reflow / page | Moderate | P1 — implement | High |
| UX-04 | Field identification disappears while typing / inputs | Moderate | P2 — implement | High |
| UX-05 | Rejection does not explain a workable next step / error copy | Moderate | P2 — validate policy, then implement | Medium |
| UX-06 | Password-length rule appears only after error / password | Minor | P2 — implement | High |

### UX-01 — Rejection erases correction context

- **Location/evidence:** J5–J6, E05/E09/E13/E14. Fill both fields with synthetic values, submit, receive 422, then inspect the fields: both values have length zero. Reproduced on desktop, mobile, and keyboard retry.
- **Inferred impact:** coordinators must re-enter both fields even though the message only concerns email, and cannot compare the rejected address against their intended address. This adds work and may encourage repeated attempts.
- **Severity:** Moderate; recoverable by re-entry, but directly undermines the requested recovery task.
- **Priority:** P1; directly reproducible task friction on every tested rejection and a prerequisite for efficient correction. Engineering effort is unknown.
- **Confidence:** High for clearing; abandonment or repeated-error rates are unmeasured.
- **Recommendation:** retain the email value for editing and associate the rejection with that field. Avoid resetting unrelated input automatically. Decide password retention deliberately with product/security requirements; if it must be cleared, explain that and preserve non-sensitive correction context. Do not persist passwords to storage.
- **Pattern/rationale:** field-level server validation with retained permissible input.
- **Acceptance check:** submit a rejected address, verify the email remains editable, the appropriate field is identified, and retry needs only intended corrections on desktop/mobile and keyboard paths. Verify the agreed password policy separately.
- **Limits:** no claim that retaining a password is always appropriate or that the sandbox response reflects real eligibility policy.

### UX-02 — Rejection is visually present but not programmatically notified

- **Location/evidence:** J5, E13/E14. Keyboard submission updates plain `<p id="status">`; it has no role or `aria-live`. Focus remains on the button. Email has no `aria-invalid` or `aria-describedby` association. Forward Tab reaches the document body rather than the message.
- **Inferred impact:** a screen-reader user may not learn that the request was rejected or which field to correct. Keyboard operation is possible; the issue is notification and correction context, not a keyboard trap.
- **Severity:** Major; missing rejection feedback can seriously disrupt recovery for users who cannot see the text.
- **Priority:** P1; consequential, reproducible feedback semantics problem on the central task.
- **Confidence:** High for DOM/focus observations. Actual announcement behavior was not tested with assistive technology.
- **Recommendation:** present rejection in an appropriate live error region or alert, and expose a specific error associated with email. Mark email invalid when applicable. Keep focus behavior intentional: either focus the correction field with its associated error or provide a focusable error summary; avoid redundant announcements.
- **Applicable criterion:** the observed dynamically inserted outcome lacks programmatic status semantics or focus notification, supporting a scoped [WCAG 2.2 SC 4.1.3, AA](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) failure in this tested state. This is not a full accessibility verdict.
- **Acceptance check:** in NVDA/Firefox and VoiceOver/Safari, submit by keyboard, verify the rejection is announced once without needing to search, and that the correction field exposes its specific error. Recheck focus and retry order.
- **Limits:** actual screen-reader output and other browser behavior remain unverified; the linked standard was supplied by the skill reference, not newly browsed.

### UX-03 — Narrow layouts require horizontal scrolling to read task text

- **Location/evidence:** E06–E12/E14. At 768, 390 and 320 CSS-pixel viewport widths, measured `documentElement.scrollWidth` and main width are 924 pixels. At 390/320, viewport screenshots show truncated heading and introductory text. Tablet text happens to fit despite overflow. Controls remain visible.
- **Inferred impact:** mobile users and users needing narrow reflow must pan horizontally to understand the page; the incomplete introduction obscures its explanation.
- **Severity:** Moderate; content can be recovered by horizontal scrolling and the form remains operable.
- **Priority:** P1; directly observed cross-width layout defect affects entry comprehension and the reflow requirement.
- **Confidence:** High; measured DOM geometry and inspected viewport captures agree.
- **Recommendation:** constrain the container to available width with border-box sizing, responsive padding and natural text wrapping. Preserve the clear vertical form arrangement. Do not merely hide horizontal overflow and lose content.
- **Applicable criterion:** the ordinary form text requires two-dimensional scrolling at 320 CSS pixels; this supports a scoped [WCAG 2.2 SC 1.4.10, AA](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) failure. This is not content requiring a two-dimensional layout.
- **Acceptance check:** at 320/390/768/1440 CSS pixels, verify the complete heading, instructions, fields and rejection fit without horizontal panning. Check equivalent 400% zoom and long translated/error content separately.
- **Limits:** physical mobile rendering and browser zoom were not tested; the standard link comes from the skill reference.

### UX-04 — Field identification disappears during entry

- **Location/evidence:** E01/E04/E14. Both inputs have placeholders but no visible persistent label, associated `<label>`, `aria-label`, or `aria-labelledby`. Once values are entered, the placeholder text vanishes.
- **Inferred impact:** a first-time coordinator must remember what each filled field means when reviewing or correcting it. This is especially unhelpful with masked password content and narrow input widths.
- **Severity:** Moderate; field types/order provide a workaround, but review requires recall.
- **Priority:** P2; meaningful comprehension improvement after the recovery blockers.
- **Confidence:** High for disappearing labels and DOM structure; actual user confusion is unmeasured.
- **Recommendation:** add visible persistent “Email address” and “Password” labels associated with their controls. Use placeholders only for optional examples, not as the sole field identification.
- **Pattern/rationale:** stable labels support recognition during input and correction. Placeholder fallback can contribute an accessible name in browsers; this report does not claim both controls are necessarily unnamed to all assistive technology.
- **Acceptance check:** labels stay visible in empty, filled, focused and rejected states, and clicking a label focuses its control. Verify accessible names in the browser accessibility tree and with assistive technology.
- **Limits:** no screen-reader naming test was performed.

### UX-05 — The rejection gives too little guidance for a confident retry

- **Location/evidence:** J5–J6, E05/E09/E14. The complete message is “Use a different email address.” No eligibility explanation or help action is displayed. A different synthetic address produces the same sandbox response.
- **Inferred impact:** a coordinator who does not know which address is eligible must guess or seek assistance outside the page. This may create a rejection loop; real-world prevalence is unknown.
- **Severity:** Moderate; another address can be attempted, but a useful route depends on undisclosed policy.
- **Priority:** P2; confirm actual eligibility and support policy first, then supply safe actionable guidance. Do not infer those rules from the sandbox.
- **Confidence:** Medium; absence of guidance is observed, while whether the backend can safely provide a more specific reason is unknown.
- **Recommendation:** explain the permitted next step at the level policy safely allows (for example, an organization-approved address, only if that rule is real). Provide a verified help/contact route when users lack another eligible address. Do not reveal sensitive account-existence information.
- **Pattern/rationale:** error messages should name the correction and an alternate route when users cannot perform it.
- **Acceptance check:** test actual policy branches with controlled fixtures; each rejection offers a true next action or verified assistance route. Ask first-time coordinators to explain what they would do next without coaching.
- **Limits:** repeated sandbox rejection does not prove all real addresses fail, and no support destination was assumed or fabricated.

### UX-06 — The password rule is disclosed only after invalid entry

- **Location/evidence:** E01/E04/E14. No visible length requirement at entry; a five-character password is blocked with “Please lengthen this text to 8 characters or more …”. DOM records `minLength: 8`.
- **Inferred impact:** coordinators can avoid a preventable correction cycle if they see the rule before choosing a password.
- **Severity:** Minor; native validation clearly explains the rule and retains the value, so recovery is low cost.
- **Priority:** P2; small but task-relevant instructional improvement, suited to the label/error work. Effort has not been estimated.
- **Confidence:** High; rule and missing advance instruction were directly observed.
- **Recommendation:** place the actual requirement beside the persistent password label and associate it as help text. Keep native validation or an equally accessible equivalent; do not invent additional requirements.
- **Acceptance check:** a first-time visitor can find the minimum before typing; short input still gets an understandable associated error and keyboard focus.
- **Limits:** only the exposed eight-character minimum was verified; no broader password policy is inferred.

## Improvement sequence

1. Fix rejection notification and retain correction context together (UX-02, UX-01). Retest keyboard and assistive-technology correction as one journey.
2. Make the container reflow and verify narrow entry and rejection states (UX-03).
3. Add persistent labels and advance password guidance (UX-04, UX-06), then refine rejection guidance after confirming real policy and help destinations (UX-05).

Preserve native required/email/minimum-length validation, the logical three-control tab order, visible focus outlines, the 203×52 CSS-pixel input hit areas and approximately 138×48 button, the clear heading and primary action, and the explicit sandbox disclosure. These observations do not certify every target-size or accessibility criterion.

## Validation gaps and handoff

This report verifies a rendered local rejection journey, not production onboarding. Real acceptance, email delivery, policy branches, slow/offline responses, duplicate submissions, interruption/resumption, browser history behavior, actual touch devices and screen readers need separate checks. Proposed acceptance checks above have not been executed against fixes because this was a read-only audit.

Before shipping changes, run controlled accepted/rejected/backend-error scenarios with the actual policy, verify data-preservation rules, and repeat mobile/reflow and keyboard/assistive-technology journeys. User tests should validate comprehension and recovery; no conversion loss, completion rate or satisfaction score is inferred here.

Report verification: all evidence paths exist; E01–E13 were visually inspected; numeric geometry and validation claims come from E14; route, selectors and response text were observed at runtime. No other agent reports, examples, baseline reports, or test/oracle files were consulted.

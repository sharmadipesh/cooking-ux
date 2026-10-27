# UX audit — plan selection and account access

The clearest supported changes are to make essential terms readable, add persistent field labels, and express field errors in text. The written journey also needs clearer verification and onboarding outcomes. Those journey gaps are **questions to resolve in the design**, not confirmed product failures.

## Scope and evidence

Reviewed offline on 27 October 2026 for first-time small-team coordinators choosing a plan and requesting account access. The sources are original synthetic test artifacts: [design-observations.md](../../../../ux-audit-skill/tests/fixtures/design-observations.md) and [flow.md](../../../../ux-audit-skill/tests/fixtures/flow.md). Their snapshot dates/versions are unspecified. No screenshots, live Figma file, prototype, browser, implementation, analytics, or user research were inspected. Findings concern supplied descriptions; user impacts are predictions.

| Evidence | Supplied locator and state | Method / support and limits |
|---|---|---|
| D01 | Frame `10:1`, “Create account / Desktop”, 1280×900 | Supplied description: email/password placeholders without persistent visible labels; blue “Create account” button. No visual or semantic inspection. |
| D02 | Frame `10:2`, “Create account / Mobile”, 360×800 | Supplied description: help layer extends 38px beyond right edge. Not an auditor measurement; runtime clipping/reflow unknown. |
| D03 | Component `10:8`, “Terms explanation”, 14px normal essential text | Supplied opaque #9A9A9A on #FFFFFF; locally calculated contrast 2.81:1 using sRGB relative luminance. No runtime verification. |
| D04 | Component `10:9`, “Close” | Supplied 18×18px visible icon beside another with 2px gap. Hit area, name, keyboard behavior unknown. |
| D05 | Desktop error variant; node unspecified | Supplied red-border-only error presentation, no textual description represented. Programmatic behavior unknown. |
| F01 | Plans, initial yearly selection | Written artifact: three plans priced per user/month. Visibility of annual total before submission unspecified. |
| F02 | Create account, initial form | Written artifact: email/password. Loading, validation, network recovery, back navigation, retention undocumented. |
| F03 | Confirm email | Written artifact: “Check your email” and Continue. Resend timing and change-email behavior unspecified. |
| F04 | Empty team dashboard | Written artifact: “Start here” heading, no next action represented. No access-request or approval state documented. |

These IDs are the evidence ledger and supplied locators, not links to real Figma nodes.

## Journey and coverage

| Step | Coordinator goal | Supplied outcome / audit implication |
|---|---|---|
| F01 | Understand and choose a plan | Yearly is selected; confirm commitment disclosure (UX-05). |
| F02 | Enter account details | Placeholder-only labels and a described error variant need improvement (UX-02/03); recovery untested. |
| F03 | Verify email and proceed | Continue is shown; verification gating and recovery unresolved (UX-04). |
| F04 | Understand access status and start setup | Empty dashboard lacks a represented action (UX-04). |

| Dimension | Coverage | Result / limit |
|---|---|---|
| Usability and task clarity | Partial | D01, F01–F04: wording/order reviewed from text only. |
| Accessibility | Partial | D03 contrast calculated; D01/D05 design risks. Semantics, keyboard and assistive technology unassessed. |
| Visual hierarchy/readability | Partial | D03 readable contrast assessed; no screens available for visual hierarchy judgment. |
| Consistency | Not assessed | Insufficient equivalent states/components for comparison. |
| Navigation/information architecture | Partial | F01–F04 order known; backtracking/return paths undocumented. |
| Journey and flow | Inspected | Supplied four-step artifact traced; hidden branches and actual behavior untested. |
| Interaction/system feedback | Partial | D05, F03 documented states only; transitions and timing untested. |
| Responsive/content resilience | Partial | D02 supplied overflow observation only; runtime responsiveness unassessed. |
| Friction/cognitive load | Partial | Label memory, commitment and next-action risks inferred from supplied material. |
| Error prevention/recovery | Partial | D05 visible error description reviewed; F02/F03 recovery gaps unresolved. |
| Trust/user control | Partial | F01 commitment and F03 email correction require validation. |

## Prioritized findings

Severity describes consequence if encountered; priority describes the next action. Reach, frequency, implementation effort and business impact are unknown.

| ID | Issue / location | Severity | Priority | Confidence |
|---|---|---|---|---|
| UX-01 | Essential terms have insufficient contrast, `10:8` | Moderate | P1, implement design fix | High |
| UX-02 | Fields lose visible identification after entry, `10:1` / F02 | Moderate | P1, implement design fix | Medium |
| UX-03 | Error represented by border alone, desktop error variant / F02 | Moderate | P1, implement design fix | Medium |
| UX-04 | Verification and access outcome are underspecified, F03–F04 | Moderate risk | P1, investigate then specify | Medium |
| UX-05 | Annual commitment disclosure is unknown, F01 | Moderate risk | P2, investigate | Low |
| UX-06 | Help text extends beyond mobile frame, `10:2` | Moderate design risk | P2, inspect then adjust | Medium |

### UX-01 — Make essential terms readable

**Evidence:** D03 supplies exact opaque colors and normal 14px text. Calculated contrast is **2.81:1**, below the 4.5:1 requirement for normal text in [WCAG 2.2 AA, 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). This establishes a contrast failure in the described design, not production conformance.

**Impact/severity:** Moderate: coordinators may struggle to read essential instructions and make an informed submission. **Priority:** P1 because the issue is measurable and affects required information. **Confidence:** High for the supplied design values; impact has not been user tested.

**Recommendation:** Use an existing text token that meets 4.5:1 on white, preserving the component’s instructional role. **Acceptance:** Recalculate actual foreground/background combinations in every relevant state; essential normal text reaches at least 4.5:1. Verify runtime styles separately.

### UX-02 — Keep email and password labels visible

**Evidence:** D01 states placeholders are the only visible field labels on desktop. **Impact/severity:** Moderate: after typing, a first-time coordinator may need to recall which field contains which value, complicating review and correction. **Priority:** P1 because identifying required input supports the core task. **Confidence:** Medium: supplied symptom is explicit; user difficulty and mobile parity are untested.

**Recommendation:** Add persistent “Email” and “Password” labels; reserve placeholders for optional examples and place password requirements nearby. Retain the clear “Create account” action. **Acceptance:** Both fields remain identifiable when empty, filled, focused, autofilled and invalid. Check programmatic associations in implementation; their absence is not established here.

### UX-03 — Explain errors and corrective action

**Evidence:** D05 represents errors with a red border alone. **Impact/severity:** Moderate: users may notice a problem without understanding how to fix it; color perception can further reduce recognition. **Priority:** P1 because correction is necessary to complete F02. **Confidence:** Medium: the visual description is explicit, but actual error messages/announcements are unknown.

**Recommendation:** Add concise field-specific text explaining the issue and remedy; retain the border as a supplementary cue. Preserve entered values where appropriate. **Acceptance:** A described invalid email/password state identifies the field, problem and correction without relying on color. Later test keyboard focus and programmatic error association; no runtime accessibility violation is asserted.

### UX-04 — Specify what Continue means and what access enables

**Evidence:** F03 shows “Check your email” with Continue; F04 shows only “Start here”. The flow does not explain whether Continue checks verification, where access is requested/granted, or what to do on arrival. **Impact/severity:** Moderate risk: a new coordinator may be unsure whether access is complete or how to proceed. **Priority:** P1 investigation because the intended task endpoint is unresolved. **Confidence:** Medium for the artifact gap; no runtime blockage is proven.

**Recommendation:** Confirm the access model first. Specify verified/unverified Continue outcomes, a useful resend/change-email route, and an explicit F04 next action appropriate to the coordinator’s permissions. If approval is required, show request status and the next expected event rather than implying access is ready.

**Acceptance:** In a revised flow or prototype, a coordinator can explain their current verification/access state and complete the next permitted action. Cover unverified email, wrong email and an empty team. Test these branches; they were not traversed in this audit.

### UX-05 — Verify annual billing clarity before submission

**Evidence:** F01 selects yearly billing while displaying per-user/month prices; annual total disclosure is unspecified. **Impact/severity:** Moderate risk: users may mistake a monthly equivalent for the actual commitment; no misleading charge is established. **Priority:** P2 investigation: resolve the disclosure gap before designing further billing behavior. **Confidence:** Low about the product issue because the information may already exist outside this artifact.

**Recommendation:** Inspect the actual plan/commitment states. If missing, show billing cadence, annual commitment and the basis for seat-dependent totals before a consequential submission. Clarify whether requesting access creates any billing obligation. **Acceptance:** Coordinators can state what they commit to, when payment occurs and how seats affect the amount. No purchase or payment behavior was tested.

### UX-06 — Contain mobile help text without losing meaning

**Evidence:** D02 reports a help layer 38px beyond frame `10:2` at 360×800. **Impact/severity:** Moderate design risk if essential help is clipped or inaccessible; overflow alone does not prove clipping. **Priority:** P2 because the supplied frame warrants correction/inspection, while runtime harm is unknown. **Confidence:** Medium: supplied geometry is explicit, actual rendering is unavailable.

**Recommendation:** Inspect the frame and intended overflow; constrain and wrap the help layer within the content area when it is intended to be read there. **Acceptance:** Updated 360×800 design retains all help text with readable wrapping; later check runtime at 320 CSS pixels/equivalent zoom, long content and applicable reflow behavior. No WCAG reflow failure is established.

## Sequence and handoff

Resolve the intended access endpoint (UX-04) alongside the supported form/readability fixes (UX-01–03). Then verify commitment disclosure and mobile overflow (UX-05–06). Preserve the short four-step structure, limited initial fields and explicit account-creation action; expand only the information and states needed for confident completion.

The next review needs actual frames/prototype and implementation access. Check D04’s interactive bounds and spacing before claiming a target-size failure: 18px visible bounds are insufficient evidence. Check accessible names, focus, keyboard operation, announcements, F02 network/validation recovery and retained input, and F03 resend/change-email behavior. Missing documentation is not proof these features are absent. Finally, test the revised journey with first-time coordinators; no usability sessions or runtime checks have been completed.

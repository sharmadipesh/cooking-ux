# Example — partial design/flow audit

This is an illustrative excerpt based on the package's original synthetic design observations and written flow. It is not an audit of a real Figma file or production site. A complete report should cover the requested scope; this excerpt demonstrates how findings and limits are expressed.

## Executive assessment

The supplied account-access artifacts raise actionable readability and form-guidance concerns. Resolve those design concerns first, then verify billing and recovery decisions in the actual flow. No live design, prototype, browser, users, or production behavior was inspected.

## Scope and evidence

Audience: first-time coordinators choosing a plan and requesting account access. Sources: [supplied design observations](../tests/fixtures/design-observations.md) and [written flow](../tests/fixtures/flow.md). D01–D05 and F01–F04 are supplied IDs. They are not invented live Figma links or independently retrieved layers.

| Evidence | Locator/state | Provenance | Supports / limit |
|---|---|---|---|
| D01 | `10:1`, Create account / Desktop | Supplied description, 1280×900 | Placeholder-only labeling represented; DOM names unknown |
| D02 | `10:2`, Create account / Mobile | Supplied description, 360×800 | Help text exceeds frame by 38px; browser behavior unknown |
| D03 | `10:8`, Terms explanation | Supplied opaque colors, 14px normal | #9A9A9A on white; supports a design contrast calculation |
| D05 | Desktop error variant | Supplied description | Red border without represented error text; programmatic errors unknown |
| F01 | Plans | Supplied written flow | Yearly default/per-user monthly price; final disclosure not documented |

The journey is supplied as Plans → Create account → Confirm email → Team dashboard. Prototype links, email behavior, runtime recovery, and actual completion were not tested.

## Findings

### UX-01 — Essential instructions lack sufficient design contrast

- **Evidence/location:** D03, node `10:8`. From the supplied opaque sRGB colors, linearize channels, compute relative luminance, and use `(Llighter + .05)/(Ldarker + .05)`: approximately 2.81:1. This is a calculation from supplied values, not a live measurement.
- **Impact:** Users with low vision may be unable to read required instructions. User performance has not been observed.
- **Severity:** Major design risk — essential information may be difficult to access; production rendering is unknown.
- **Priority:** P1 — correct the well-supported design issue in the next improvement cycle.
- **Confidence:** High for the color calculation and design criterion; user-outcome impact remains predicted.
- **Recommendation/pattern:** Use a darker foreground that meets the applicable normal-text contrast requirement while retaining the existing text hierarchy. [WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) applies to the stated 14px normal essential text.
- **Verify:** Recalculate the final opaque pair at ≥4.5:1, then measure actual rendered states. No full conformance claim follows from this one check.

### UX-02 — Field identity is not persistent in the represented form

- **Evidence/location:** D01, frame `10:1`: email/password use placeholders with no visible persistent labels.
- **Impact:** Users may lose the field's purpose while reviewing/correcting entered data. Accessible names cannot be inferred.
- **Severity:** Moderate design issue — recoverable but repeated interpretation effort.
- **Priority:** P1 — a focused form improvement with clear design evidence; actual effort is unknown.
- **Confidence:** Medium — supplied visual symptom is clear; implementation and user impact are untested.
- **Recommendation/pattern:** Add visible labels, separate help text, and field-associated errors. Preserve native labels/associations in implementation rather than relying on placeholders.
- **Verify:** Review the filled/error variants; in the product, check accessible names, keyboard correction, and retained values. Do not claim a programmatic label failure from the frame alone.

### UX-03 — Billing commitment is not established by the flow

- **Evidence/location:** F01 documents a yearly default and monthly per-user price but not final annual-total disclosure.
- **Impact:** Users could misunderstand the commitment if disclosure is absent in the product. That absence has not been established.
- **Severity:** Potential Major risk if users commit without understanding charges; currently a documentation gap.
- **Priority:** P1 investigate — verify the actual pre-commitment state before writing a production-defect ticket.
- **Confidence:** Low for the product risk; High that the supplied artifact omits this detail.
- **Recommendation/pattern:** Document the selected cadence, seat basis, and annual total at the decision/commitment points. Preserve the choice across subsequent steps.
- **Verify:** Inspect F01 and the final commitment screen; ask representative users to explain the charge and timing. No conversion or revenue estimate is asserted.

### UX-04 — Mobile help text exceeds its supplied frame

- **Evidence/location:** D02, frame `10:2`, supplied 38px overflow at 360px width.
- **Impact:** Instructions may be clipped or require extra navigation if the same problem appears in implementation.
- **Severity:** Moderate design issue — relevant content may be harder to read; runtime effect is unknown.
- **Priority:** P2 — repair the design layout and validate implementation as part of responsive review.
- **Confidence:** Medium — supplied frame observation; no browser measurement.
- **Recommendation/pattern:** Constrain the text layer to the content area and wrap text; preserve label/help grouping.
- **Verify:** Inspect the corrected frame, then test real narrow widths and text enlargement without losing instructions. A fixed frame does not prove browser reflow.

## Coverage and handoff

Usability, hierarchy, and responsive design are Partial from supplied descriptions. Accessibility is Partial for design color/label concerns; semantics, keyboard, and assistive technology are Not assessed. Navigation, consistency, and interactions are Partial at the written-artifact level only. Journey, friction, recovery, and trust are Partial; missing branches need clarification, not assumed failure.

Preserve the meaningful Create account action and existing journey sequence unless evidence warrants a change. First fix UX-01/02; investigate UX-03 before a commitment decision; address UX-04 in responsive design work. Obtain prototype connections, error/recovery variants, and the live interface for the remaining checks. Other concerns in the supplied artifacts, such as red-border-only errors and the empty dashboard's next action, belong in a full audit; this excerpt is intentionally not exhaustive.

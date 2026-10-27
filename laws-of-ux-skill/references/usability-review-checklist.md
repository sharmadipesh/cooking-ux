# Usability review checklist

Use relevant rows; record evidence, device/state, observed/hypothesized impact, and unassessed items. This is a task-oriented review, not a complete accessibility certification.

| Dimension | Inspect and exercise | Useful principles |
|---|---|---|
| Clarity and hierarchy | Purpose, primary action, headings, labels, legibility, type/spacing consistency | Proximity, Similarity, Von Restorff |
| Navigation and architecture | Task labels, current location, grouping, deep links, back behavior | Mental Model, Jakob |
| Cognitive load and density | Required recall, comparison effort, units, visible constraints | Cognitive Load, Chunking, Working Memory |
| Consistency and familiarity | Same styling means same behavior; existing conventions remain useful | Similarity, Jakob |
| Feedback and status | Slow request, pending, saved/unsaved, success, failure, retry | Doherty, Peak-End |
| Affordances and discovery | Interactive appearance, meaningful labels, hidden options, contextual help | Active User, Mental Model |
| Error prevention and recovery | Destructive confirmation/undo, correction, draft preservation, duplicate submit | Postel, Tesler |
| Accessibility | Semantics, names/labels, reading order, keyboard, focus visibility/return, non-color cues, contrast, status announcements | Supplementary WCAG guidance |
| Responsive behavior | Narrow mobile, tablet, desktop, zoom/reflow, text spacing, long/localized content | Proximity, Fitts, supplementary WCAG |
| Decision friction | Comparable options, clear costs, defaults, reversible choices, expert access | Hick, Choice Overload |
| Effort and completion | Repeated input, unnecessary steps, interruption/resume, genuine ending | Flow, Goal-Gradient, Working Memory |

## Supplementary accessibility baseline

Source: [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/), with focused explanations of [contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), and [resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html). These checks are not additional Laws of UX laws.

- Verify keyboard access without traps; logical focus order, visible focus, and focus not entirely obscured. Include dialogs and responsive navigation.
- Check labels, instructions, text error identification, and programmatically determinable name/role/state. Do not use placeholders as the only label.
- Check text contrast: generally 4.5:1, or 3:1 for qualifying large text; applicable non-text UI contrast is 3:1. Evaluate actual rendered colors and relevant exceptions.
- At WCAG 2.2 AA, target size minimum is 24 by 24 CSS pixels or a qualifying exception such as sufficient spacing. The enhanced AAA criterion uses 44 by 44 with its own exceptions. Larger comfortable controls may suit the context. Neither figure is specified by Fitts’s Law.
- Check text resizing to 200% and reflow at 320 CSS-pixel width where applicable; necessary two-dimensional content has exceptions. Check user text-spacing overrides for clipping and loss of functionality.
- Do not rely on color alone. Honor reduced-motion preferences as implementation practice and assess applicable moving/flashing content criteria. A reduced-motion media query alone is not a complete accessibility assessment.

If measurements or assistive-technology testing are unavailable, state that explicitly. For a conformance decision, review all applicable success criteria rather than treating this sample as exhaustive.

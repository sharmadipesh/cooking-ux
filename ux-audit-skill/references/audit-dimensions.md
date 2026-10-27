# Audit coverage

Review dimensions relevant to the task and explicitly mark the rest. “Inspected” means a dimension was examined, not that the entire product passed it. Tie each finding to a screen/component/step and evidence ID. Use the source-acquisition limits when choosing what can be checked.

| Dimension | Questions and checks | Practical patterns to consider |
|---|---|---|
| Usability and task clarity | Is the purpose, required input, next action, and outcome understandable? Is terminology appropriate to the audience? | Clear labels, visible requirements, useful next steps |
| Accessibility | What can users perceive and operate? Check names/labels, reading structure, contrast, non-color cues, keyboard/focus, errors/status, and alternative content with suitable evidence. | Native controls, field-associated errors, logical focus and semantic headings |
| Visual hierarchy and readability | Do emphasis, type, spacing, grouping, units, and content order support the task? | A clear type hierarchy, task-based grouping, restrained emphasis |
| Consistency | Do equivalent elements look/behave alike? Are differences meaningful? | Existing tokens, component variants, consistent labels and state patterns |
| Navigation and information architecture | Can users identify where they are, find destinations, go back, and retain context? | Real links, active location, task labels, predictable history |
| Journey and flow | Are prerequisites, decisions, handoffs, commitment, completion, and return paths coherent? | Progressive disclosure without hiding required detail, clear cross-channel handoffs |
| Interaction and system feedback | Are affordances, pending, saved/unsaved, success, unknown outcomes, and errors truthful? | Explicit state handling, current-scope request protection, honest confirmation |
| Responsive and content resilience | At inspected widths, zoom, or supplied frames, do controls/content retain meaning and access? | Reflow, wrapping, intentional table scrolling, preserved reading order |
| Friction and cognitive load | Must users memorize, repeat entry, infer labels, compare hidden data, or make unnecessary decisions? | Retained permitted state, visible scope, comparable options, meaningful defaults |
| Error prevention and recovery | Can mistakes be prevented, corrected, or safely resumed? Are retries appropriate? | Validation, undo where possible, draft preservation, reconciliation for unknown mutations |
| Trust and user control | Are costs, permissions, consequences, cancellation, and genuine progress clear? | Transparent commitments, reversible choices, permission-aware actions |

## Accessibility evidence boundaries

Use [W3C's preliminary evaluation guidance](https://www.w3.org/WAI/test-evaluate/preliminary/) to plan checks, not to declare full conformance. For criterion claims, cite an applicable WCAG version/level and the specific supporting evidence. Leave untested requirements unassessed.

- [Contrast, WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): evaluate actual foreground/background combinations, font size/weight, and applicable exceptions. Normal text generally needs 4.5:1; qualifying large text 3:1. Layer colors can establish a design contrast issue; uncertain screenshot colors cannot establish a precise ratio.
- [Target size, WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): AA minimum is 24×24 CSS pixels or a qualifying exception, including adequate spacing. Measure the interactive hit area; an icon's visible bounds alone are insufficient.
- [Reflow, WCAG 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): inspect applicable content at 320 CSS-pixel width or equivalent zoom without loss; necessary two-dimensional content has exceptions. A mobile frame is not a tested browser.
- [Labels/instructions, WCAG 3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html): inspect required information and understandable labels. Persistent visible labeling, accessible names, and associations require their respective evidence; do not infer DOM semantics from pixels.
- [Focus visibility, WCAG 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html): operate keyboard paths and inspect the actual focused state. A design focus variant does not prove implementation or absence of keyboard traps.
- [Status messages, WCAG 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html): inspect programmatic presentation or actual assistive-technology behavior where available. A screenshot of a toast cannot prove it is announced.

These are selected checks, not every WCAG criterion. A scan with zero detected violations, a polished prototype, or a completed checklist does not certify accessibility. Keep measured facts, design risks, runtime findings, and user-testing hypotheses distinct.

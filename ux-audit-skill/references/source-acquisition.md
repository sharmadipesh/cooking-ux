# Acquire the right evidence

Use the applicable branch. All branches feed the same evidence ledger and report. Tools and credentials belong to the host environment; do not invent their availability.

## Figma designs and prototypes

1. Resolve the supplied file and node/frame. With a Figma connector, use its available read/metadata and screenshot capabilities, following that environment's tool instructions. Fetch the targeted section rather than the entire organization/file. File access does not imply access to linked libraries or every page.
2. Inspect screenshots and relevant layer/component details: labels, type, spacing, colors, constraints/auto-layout, variants, and relationships. Record actual node IDs, page/frame names, dimensions, variant, and supplied/retrieved status. Do not assume a visible icon's bounding box equals its interactive hit area.
3. Inspect the connected prototype only when accessible. Trace the requested start/end and meaningful branches; identify which links/states were actually traversed. A screen list or connector screenshot is not a tested interaction flow. If the tool cannot execute the prototype, record the connections that were supplied and leave interaction behavior untested.
4. Compare available desktop/tablet/mobile frames without assuming they prove runtime responsiveness. Distinguish an absent mobile artifact from a broken mobile implementation.
5. Link to real nodes using the supplied or retrieved URL/identifier. Never fabricate a file key or turn synthetic fixture IDs into live Figma links.

If a file is private or tools are unavailable, use accessible exports/screenshots/specs and label the result “design artifact review.” Ask for missing access/export only when necessary. A public marketing page about Figma is not evidence about the target design. Do not write comments or change nodes as part of a read-only audit.

## Live web pages

1. Open the exact URL in an available browser. Record the route, relevant account role, environment, time/version if known, and initial state. Check redirects, login walls, error pages, cookie overlays, loading, and whether the target is actually visible.
2. Capture the important states before assigning visual findings. Save and inspect the actual captured image if local files are used; reject blank, wrong-route, or unintended captures. DOM/text observations can support a partial structural audit when images are unavailable, not a complete visual verdict.
3. Trace the specified task with relevant links, input, keyboard navigation, focus, feedback, error/recovery, back/forward, and interruption/resumption. Respect the authorized action boundary. Do not enter real personal data or submit real transactions merely to complete an audit.
4. Inspect relevant mobile, tablet, and desktop widths when responsive behavior is in scope. Record exact tested widths and states. Check long content, zoom/reflow, and key controls where possible. Three screenshots do not validate every breakpoint or touch behavior.
5. Measure before making numeric claims: use actual colors/styles or a contrast tool, target hit areas, focus behavior, or layout dimensions. State the method. Label unavailable DOM/assistive-technology checks as unassessed.

A fetched HTML page without rendering does not establish layout or visual quality. Source code can support an implementation inference, but dynamic conditions still need runtime evidence. Treat a 403/blocked environment as an access limit, not proof the intended authenticated product has broken navigation.

## User flows, journey maps, and written artifacts

1. List the supplied steps, actors, entry/exit points, decisions, and handoffs. Preserve their original identifiers and distinguish explicit steps from your inferred connections.
2. Inspect task order, prerequisites, information requested, cost/commitment disclosures, branching, backtracking, error/recovery, cancellation, re-entry, permissions, and completion/next actions.
3. Separate a documented obstacle from an omitted branch. “The supplied flow has no recovery step” is evidence; “The application loses all work” requires more evidence. Missing documentation may justify validation or design work, not a confirmed runtime failure.
4. Evaluate cross-channel transitions such as email confirmation or handoffs without pretending those channels were tested. State dependencies and assumptions.
5. Use step IDs as finding locations. Mark visuals, responsive behavior, contrast, semantics, keyboard, and timing unassessed when the artifact does not establish them.

## Mixed or conflicting material

Keep evidence provenance for each item. Do not use a live page's behavior to claim a Figma component is implemented identically. If a prototype differs from production, report the discrepancy with both locators and the relevant dates/versions; do not guess which is authoritative. Older user-supplied evidence can be reviewed as a snapshot, clearly labeled with its age and current verification limit.

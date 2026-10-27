---
name: ux-audit-skill
description: Use when asked for a UX audit or usability review of Figma designs, prototypes, user flows, screenshots, or live website URLs. Evaluate the experience and produce an evidence-based, prioritized report with practical recommendations. Use for audit deliverables rather than default frontend implementation.
license: MIT. LICENSE has complete terms
metadata:
  author: sharmadipesh/cooking-ux
  version: "1.0.0"
---
# UX Audit Skill

Produce a report that helps a designer or developer decide what to improve, why, and how to verify it. Audit what can be inspected; identify what remains unknown. This skill is independent of any provider, browser, Figma plugin, or the Laws of UX skill.

## Understand → Capture → Evaluate → Prioritize → Recommend → Verify the report

1. **Understand the task.** Identify the source, target audience, important user task, start/end of the journey, device/context, and deliverable. Infer reasonable scope from the supplied material and label assumptions. Ask only for information that blocks inspection or a consequential decision. Audit requests authorize review, not an unsolicited implementation, public comment, or publication.
2. **Capture evidence.** Read the relevant source branch in [acquisition guidance](references/source-acquisition.md). Use available connected tools before fallbacks. Open the actual target; a URL string, search snippet, login wall, or generated description is not inspection. Capture and visually inspect relevant screens/states where possible, alongside behavior/structure observations. Record source locators and evidence IDs. If screenshots are unavailable but structure/text is accessible, perform that limited review and leave visual dimensions unassessed.
3. **Evaluate the journey.** Follow the main task through entry, decisions, action, outcome, and relevant recovery/return paths. Use [the audit dimensions](references/audit-dimensions.md) to cover usability, accessibility, hierarchy, consistency, navigation, journeys, interactions, responsive behavior, and friction. Include a coverage ledger; mark each dimension Inspected, Partial, Not assessed, or Out of scope. Do not invent issues to fill categories.
4. **Build findings.** Each finding must connect a specific observation to a plausible user impact and a concrete improvement. Separate direct observation, supplied evidence, code inference, and hypothesis. A design concern can be observed while its effect on users remains a hypothesis. Group repeated occurrences of the same root cause and list affected screens; do not inflate issue counts. Preserve useful patterns and design-system conventions in recommendations.
5. **Prioritize.** Apply [the severity/priority rubric](references/severity-and-priority.md). State severity, priority, and confidence separately, each with a reason. Consider task harm, recoverability, frequency/persistence when known, affected users, dependencies, and effort when evidenced. Do not invent reach, analytics, conversion loss, engineering estimates, or an overall UX score.
6. **Report.** Use [the report template](templates/audit-report.md), scaling detail to scope. Lead with the highest-value findings, then show scope, journey/coverage, prioritized detail, recommended sequencing, and validation gaps. Every issue needs location, evidence, impact, severity, priority, confidence, an actionable recommendation, a suggested pattern when useful, and an acceptance check. Use plain language and stable IDs for designer/developer handoff.
7. **Verify the report.** Check that cited nodes/routes/steps and evidence IDs exist; measurements have a method and context; claims match the inspected source/state; priorities have reasons; recommendations address the cause; and checks are feasible. Compare against the requested scope. Report partial access or unavailable states explicitly. No findings is valid when evidence does not establish issues; inaccessible content warrants a scope/access report, not a fabricated verdict.

## Evidence contract

For each evidence item record: **ID; source locator; frame/route/step/component; viewport/state; capture or observation method; date/version when available; what it supports; and limitations.** Link actual accepted screenshots or supplied artifacts when supported. Preserve meaningful screenshot names and their connection to findings. Do not invent links or present a supplied observation as your own measurement. Redact incidental personal data; do not copy secrets into reports.

For Figma, name the actual file/page/frame/node and link to the node when the identifier was supplied or retrieved. A static frame supports design findings, not production DOM, keyboard, backend, or screen-reader conclusions. For a written flow, distinguish absent documentation from broken product behavior. For live pages, tie behavior to reproduction steps and the tested state/device.

A confirmed accessibility failure requires the applicable criterion and enough evidence. A visual suspicion is a risk to verify. Automated checks or screenshots alone do not establish WCAG compliance. Use the relevant W3C references in the checklist; label the audit's standard/version/level when one is requested.

## Scope and tool limits

- A Figma link or URL requires access and suitable reading/capture tools. This Markdown package does not grant permissions or include a browser. When direct access fails, explain the barrier and continue only on accessible supplied material. Request an export or access if the missing source prevents the intended review; do not bypass authentication or infer hidden screens.
- Reuse the user's existing tab/session when appropriate; preserve its state. Inspect before interacting. For live environments, avoid committing transactions, creating real accounts, sending invitations/messages, changing settings, or destructive actions without authorization. Use an explicitly authorized sandbox or stop at the relevant boundary and mark the rest untested.
- Do not turn every missing state into a product defect or every preference into a usability issue. Cite UX principles only when they explain a mechanism; the companion Laws of UX skill is optional. Never invent a law or force a fixed navigation/choice count.
- Do not redesign or edit source files, Figma nodes, production data, or shared components unless the task includes that work. The audit should specify an implementable improvement, not silently perform external changes.

See [the example audit](examples/artifact-audit.md) for evidence-limited reporting and [test scenarios](tests/scenarios.md) for expected behavior. The default deliverable is a readable report in the conversation; save a Markdown report and evidence files when the user requests files or when an established project workflow calls for them.

# Cognitive load and decision making

These are original explanations and package-authored applications. Examples are illustrative, not reported experiments or claims from the website. Read only entries relevant to the task.

[Choice Overload](#choice-overload) | [Chunking](#chunking) | [Cognitive Load](#cognitive-load) | [Hick’s Law](#hicks-law) | [Miller’s Law](#millers-law) | [Occam’s Razor](#occams-razor) | [Pareto Principle](#pareto-principle) | [Tesler’s Law](#teslers-law) | [Working Memory](#working-memory)

## Choice Overload

- **Definition:** A large or difficult-to-compare option set can overwhelm people and discourage decisions.
- **Core idea:** Choice quality depends on structure, familiarity, and comparison effort.
- **When to use it:** Pricing, catalogs, preference setup, or filter-heavy products.
- **Practical UI applications:** Offer relevant filters, comparable attributes, and transparent recommendations.
- **Implementation guidance:** Keep alternatives discoverable; preserve filter state and expose result counts.
- **Good example:** Plans share a side-by-side feature comparison.
- **Bad example:** Hide all but the most profitable plan and call it simplification.
- **Trade-offs and limitations:** Experts may need many visible choices; fewer options do not always improve outcomes.
- **Related laws:** Hick’s Law; Working Memory
- **Source:** https://lawsofux.com/choice-overload/

## Chunking

- **Definition:** Meaningful groups allow separate pieces of information to be processed as larger units.
- **Core idea:** Relationships make information easier to scan and retain.
- **When to use it:** Forms, navigation, dense records, or long content.
- **Practical UI applications:** Group by task or meaning and label each group.
- **Implementation guidance:** Use headings, fieldsets, lists, and consistent spacing rather than arbitrary equal-sized batches.
- **Good example:** Contact and billing fields have distinct headings.
- **Bad example:** Split an address across pages merely to make each page shorter.
- **Trade-offs and limitations:** Grouping depends on domain knowledge; excessive containers add clutter.
- **Related laws:** Miller’s Law; Law of Proximity
- **Source:** https://lawsofux.com/chunking/

## Cognitive Load

- **Definition:** Interpreting and operating an interface consumes finite mental resources.
- **Core idea:** Unnecessary interpretation competes with the user’s real task.
- **When to use it:** Dense dashboards, unfamiliar workflows, and interrupted work.
- **Practical UI applications:** Remove irrelevant stimuli, use plain labels, and preserve context.
- **Implementation guidance:** Carry entered state across steps; show units and active filters beside results.
- **Good example:** A report keeps its date range visible next to its charts.
- **Bad example:** Users memorize identifiers to compare records on another screen.
- **Trade-offs and limitations:** Necessary domain complexity remains; hiding information can increase effort.
- **Related laws:** Tesler’s Law; Working Memory
- **Source:** https://lawsofux.com/cognitive-load/

## Hick’s Law

- **Definition:** Decision time tends to increase with the number and complexity of available alternatives.
- **Core idea:** Choice structure affects selection effort.
- **When to use it:** Time-sensitive controls, menus, and branching forms.
- **Practical UI applications:** Clarify labels, organize alternatives, and reveal secondary detail when useful.
- **Implementation guidance:** Use task-based groups and search; compare total task time before adding more steps.
- **Good example:** An emergency action remains directly visible beside secondary options.
- **Bad example:** Nest every command in menus to minimize visible choice count.
- **Trade-offs and limitations:** The predictive model has conditions; expert lookup is not identical to unfamiliar choice.
- **Related laws:** Choice Overload; Jakob’s Law
- **Source:** https://lawsofux.com/hicks-law/

## Miller’s Law

- **Definition:** Miller’s historical work describes limits in immediate memory, commonly expressed as roughly seven units with variation.
- **Core idea:** Meaningful chunking matters more than a fixed item count.
- **When to use it:** Tasks requiring retention of unfamiliar information.
- **Practical UI applications:** Group meaningful content and let people recognize rather than recall it.
- **Implementation guidance:** Keep comparison data visible and carry previous selections forward.
- **Good example:** A comparison table keeps product attributes side by side.
- **Bad example:** Cut a useful 12-item navigation to seven solely to obey the law.
- **Trade-offs and limitations:** This is not a universal menu, card, or tab limit; capacity depends on task, person, and chunking.
- **Related laws:** Chunking; Working Memory
- **Source:** https://lawsofux.com/millers-law/

## Occam’s Razor

- **Definition:** When explanations account for evidence equally well, prefer the one requiring fewer assumptions.
- **Core idea:** Avoid unnecessary complexity while preserving explanatory adequacy.
- **When to use it:** Choosing between comparable UI or implementation approaches.
- **Practical UI applications:** Prefer the simplest design that still fulfills the actual task.
- **Implementation guidance:** Remove redundant wrappers and decorative controls only after checking behavior and discoverability.
- **Good example:** Use an ordinary select for a straightforward exclusive choice.
- **Bad example:** Remove error descriptions because fewer words look cleaner.
- **Trade-offs and limitations:** A principle about hypotheses becomes a design heuristic by analogy; sparse appearance is not proof of usability.
- **Related laws:** Tesler’s Law; Law of Prägnanz
- **Source:** https://lawsofux.com/occams-razor/

## Pareto Principle

- **Definition:** Outcomes are often unevenly distributed across contributing causes; 80/20 is a common illustration.
- **Core idea:** Some improvements have disproportionately large effects.
- **When to use it:** Choosing where to invest research or implementation effort.
- **Practical UI applications:** Investigate frequent and consequential tasks before cosmetic details.
- **Implementation guidance:** Use task frequency, failures, severity, and reach to order work.
- **Good example:** Fix a widespread submit failure before polishing an infrequent animation.
- **Bad example:** Ignore an accessibility barrier because it affects fewer users.
- **Trade-offs and limitations:** Do not assume the ratio without data; minority needs and severe harm can override frequency.
- **Related laws:** Cognitive Bias; Cognitive Load
- **Source:** https://lawsofux.com/pareto-principle/

## Tesler’s Law

- **Definition:** A process contains necessary complexity that must be handled somewhere in the system or by its users.
- **Core idea:** Reducing visible effort often shifts work rather than eliminates it.
- **When to use it:** Complex forms, automation, defaults, and simplification.
- **Practical UI applications:** Let software handle repeatable work while keeping consequences understandable.
- **Implementation guidance:** Prefill trustworthy data with correction paths and expose consequential automation decisions.
- **Good example:** A booking tool calculates availability but lets users choose another slot.
- **Bad example:** Hide scheduling constraints and later reject the user’s choice.
- **Trade-offs and limitations:** Automation adds failure modes and engineering cost; users may need expert control and transparency.
- **Related laws:** Occam’s Razor; Cognitive Load
- **Source:** https://lawsofux.com/teslers-law/

## Working Memory

- **Definition:** Working memory temporarily maintains and manipulates information needed for the current task.
- **Core idea:** Users have limited capacity to keep task context active.
- **When to use it:** Comparisons, multi-step forms, and interruptions.
- **Practical UI applications:** Keep relevant context visible and let the system retain state.
- **Implementation guidance:** Preserve drafts and filter values; show summaries rather than requiring cross-screen memorization.
- **Good example:** A checkout review displays entered shipping details.
- **Bad example:** Clear a long form after one validation error.
- **Trade-offs and limitations:** Capacity and duration vary; do not turn the site’s illustrative numeric ranges into universal UI limits.
- **Related laws:** Cognitive Load; Miller’s Law
- **Source:** https://lawsofux.com/working-memory/

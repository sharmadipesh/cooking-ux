# Related concepts and supplementary guidance

These are related concepts explicitly discussed in detail pages/articles, or clearly labeled package pattern syntheses. None is an additional entry in the 30-concept homepage inventory. This is a practical sub-concept inventory, not an inventory of every named theory or external reading in the website’s historical bibliographies.

## Complexity Bias

- **Definition:** A tendency to favor complicated explanations or solutions over adequate simpler ones.
- **Core idea:** Complexity may be mistaken for sophistication.
- **When to use it:** Comparing implementation proposals.
- **Practical UI applications:** Challenge additions that do not improve the task.
- **Implementation guidance:** Start with existing primitives and justify new abstraction.
- **Good example:** Keep a simple native control when it meets the need.
- **Bad example:** Build a custom widget solely to look advanced.
- **Trade-offs and limitations:** Do not assume all complexity is unnecessary.
- **Related laws:** Cognitive Bias; Occam’s Razor
- **Source:** https://lawsofux.com/articles/2024/teslers-law/

## Confirmation Bias

- **Definition:** A tendency to favor information that supports prior beliefs.
- **Core idea:** Evidence selection can distort conclusions.
- **When to use it:** Research and design reviews.
- **Practical UI applications:** Look for failed tasks and contrary feedback.
- **Implementation guidance:** Define acceptance conditions before comparing variants.
- **Good example:** Record contradictory findings.
- **Bad example:** Discard users who dislike the preferred version.
- **Trade-offs and limitations:** Diverse evidence reduces but does not eliminate bias.
- **Related laws:** Cognitive Bias
- **Source:** https://lawsofux.com/cognitive-bias/

## Banner Blindness

- **Definition:** People may overlook content resembling advertising.
- **Core idea:** Appearance and placement shape attention.
- **When to use it:** Important notices near promotional regions.
- **Practical UI applications:** Place task messages in the relevant workflow.
- **Implementation guidance:** Use persistent inline status rather than promotional styling.
- **Good example:** A failed save appears by Save.
- **Bad example:** A critical error appears in an ad-like banner.
- **Trade-offs and limitations:** A plausible explanation needs observation before diagnosis.
- **Related laws:** Selective Attention
- **Source:** https://lawsofux.com/selective-attention/

## Change Blindness

- **Definition:** Changes can go unnoticed when attention is elsewhere or cues are weak.
- **Core idea:** Visibility of a change does not ensure awareness.
- **When to use it:** Async updates and dynamic results.
- **Practical UI applications:** Signal important changes without competing distractions.
- **Implementation guidance:** Use concise status announcements and stable focus.
- **Good example:** Filter updates announce the result count.
- **Bad example:** Several panels silently change at once.
- **Trade-offs and limitations:** Avoid announcing every minor update.
- **Related laws:** Selective Attention
- **Source:** https://lawsofux.com/selective-attention/

## Recognition over Recall

- **Definition:** Recognizing available information generally imposes less memory demand than reproducing it unaided.
- **Core idea:** External context can reduce memory burden.
- **When to use it:** Comparisons and navigation.
- **Practical UI applications:** Keep relevant selections visible.
- **Implementation guidance:** Show breadcrumbs and retained filter summaries.
- **Good example:** Display shipping details on review.
- **Bad example:** Require a memorized identifier.
- **Trade-offs and limitations:** Too many visible options can still overwhelm.
- **Related laws:** Working Memory; Choice Overload
- **Source:** https://lawsofux.com/working-memory/

## Primacy and Recency

- **Definition:** Beginning and ending positions can have advantages in recall.
- **Core idea:** Sequence position can affect memory.
- **When to use it:** Instruction sequences and summaries.
- **Practical UI applications:** Introduce orientation early and close with useful next steps.
- **Implementation guidance:** Keep required steps in logical order.
- **Good example:** End with a verification summary.
- **Bad example:** Assume middle navigation links are unusable.
- **Trade-offs and limitations:** Memory experiments do not prescribe menu order.
- **Related laws:** Serial Position Effect
- **Source:** https://lawsofux.com/serial-position-effect/

## Progressive Onboarding

- **Definition:** Teach capabilities as users encounter meaningful tasks instead of presenting everything first.
- **Core idea:** Learning can happen in context.
- **When to use it:** First-run experiences.
- **Practical UI applications:** Provide usable starting points and optional guidance.
- **Implementation guidance:** Save dismissed tips and keep help available by keyboard.
- **Good example:** A sample project teaches one task.
- **Bad example:** Block all work behind a tour.
- **Trade-offs and limitations:** Necessary safety training may still be explicit.
- **Related laws:** Paradox of the Active User; Flow
- **Source:** https://lawsofux.com/articles/2024/onboarding-for-active-users/

## Progressive Disclosure

- **Definition:** Reveal additional detail when it becomes useful while keeping it discoverable.
- **Core idea:** Reduce initial demand without hiding necessary choices.
- **When to use it:** Advanced settings and search refinements.
- **Practical UI applications:** Keep frequent tasks visible and label secondary controls.
- **Implementation guidance:** Retain expanded state and expose grouped options clearly.
- **Good example:** Show advanced filters behind a named control.
- **Bad example:** Hide required fees until submission.
- **Trade-offs and limitations:** A package pattern synthesis, not a separate homepage law; extra steps may burden experts.
- **Related laws:** Hick’s Law; Tesler’s Law
- **Source:** https://lawsofux.com/articles/2015/design-principles-for-reducing-cognitive-load/

## Familiarity versus Novelty

- **Definition:** Familiar patterns aid transfer, while a novel pattern can support differentiation or exploration.
- **Core idea:** Conventions serve a purpose rather than forbidding change.
- **When to use it:** New interaction models and experiential sites.
- **Practical UI applications:** Choose novelty only when it serves the task.
- **Implementation guidance:** Prototype unfamiliar behavior with clear cues and test it.
- **Good example:** An exploration view retains clear exit and navigation controls.
- **Bad example:** Replace checkout conventions only to look different.
- **Trade-offs and limitations:** Benefits require audience evidence and validation.
- **Related laws:** Jakob’s Law; Mental Model
- **Source:** https://lawsofux.com/articles/2024/familiar-vs-novel/

## Intrinsic and Extraneous Cognitive Load

- **Definition:** Intrinsic load relates to the task and its content; extraneous load comes from processing that does not help accomplish it.
- **Core idea:** Remove avoidable effort without erasing necessary understanding.
- **When to use it:** Complex forms and dense tools.
- **Practical UI applications:** Clarify terms and remove irrelevant distractions.
- **Implementation guidance:** Keep necessary domain detail accessible and preserve context.
- **Good example:** Explain a required financial term inline.
- **Bad example:** Delete essential constraints to make a form shorter.
- **Trade-offs and limitations:** Distinguishing the two depends on the audience and task.
- **Related laws:** Cognitive Load; Tesler’s Law
- **Source:** https://lawsofux.com/cognitive-load/

## Other supporting distinctions

The articles also discuss mental-model mismatch, the ethics of attention capture, and contextual guidance; apply these through Mental Model, Cognitive Bias, and Active User rather than inventing new laws. The site mentions artificial progress; this package instead requires honest, user-relevant progress. The card deck and book advertise further concepts and methods, but their paid contents were not accessed or presented as verified entries. Accessibility and responsive implementation recommendations in the checklist are supplementary practice informed by W3C, not definitions supplied by Laws of UX.

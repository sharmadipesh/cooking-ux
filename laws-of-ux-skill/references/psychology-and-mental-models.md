# Psychology and mental models

These are original explanations and package-authored applications. Examples are illustrative, not reported experiments or claims from the website. Read only entries relevant to the task.

[Cognitive Bias](#cognitive-bias) | [Jakob’s Law](#jakobs-law) | [Mental Model](#mental-model) | [Peak-End Rule](#peak-end-rule) | [Serial Position Effect](#serial-position-effect)

## Cognitive Bias

- **Definition:** Predictable patterns in judgment can systematically distort how people interpret evidence and make decisions.
- **Core idea:** Mental shortcuts are useful but can introduce error.
- **When to use it:** Research synthesis, recommendations, defaults, or design critiques.
- **Practical UI applications:** Seek disconfirming evidence and make consequential defaults visible.
- **Implementation guidance:** Document assumptions; compare alternatives using the same criteria and avoid manipulative preselection.
- **Good example:** An audit distinguishes observed errors from designer expectations.
- **Bad example:** Declare a preferred mockup best after showing only supportive comments.
- **Trade-offs and limitations:** Knowing about bias does not remove it; a UI cannot diagnose an individual’s reasoning.
- **Related laws:** Aesthetic-Usability Effect; Peak-End Rule
- **Source:** https://lawsofux.com/cognitive-bias/

## Jakob’s Law

- **Definition:** People bring expectations learned from other products to a new interface.
- **Core idea:** Familiar patterns reduce the need to learn interaction rules.
- **When to use it:** Navigation, checkout, controls, and redesigns.
- **Practical UI applications:** Use established conventions appropriate to the audience.
- **Implementation guidance:** Reuse the existing design system and preserve routes; explain justified departures with clear cues.
- **Good example:** A cart opens a familiar order summary and checkout sequence.
- **Bad example:** A familiar-looking checkbox unexpectedly submits payment.
- **Trade-offs and limitations:** Familiarity differs across audiences; innovation can be appropriate when benefits are validated.
- **Related laws:** Mental Model; Law of Similarity
- **Source:** https://lawsofux.com/jakobs-law/

## Mental Model

- **Definition:** A mental model is someone’s internal explanation of how a system works.
- **Core idea:** Users act on their understanding, which may differ from the implementation.
- **When to use it:** Information architecture, terminology, permissions, and complex workflows.
- **Practical UI applications:** Align visible concepts with users’ tasks and explain unexpected consequences.
- **Implementation guidance:** Use domain labels and previews; distinguish saving a draft from publishing it.
- **Good example:** A clear draft/published state matches editorial expectations.
- **Bad example:** A button labeled “Save” silently publishes to customers.
- **Trade-offs and limitations:** Models vary and evolve; designer intuition is not evidence of the audience’s model.
- **Related laws:** Jakob’s Law; Cognitive Bias
- **Source:** https://lawsofux.com/mental-model/

## Peak-End Rule

- **Definition:** Memories of an experience can be disproportionately shaped by intense moments and its ending.
- **Core idea:** Retrospective judgment is not a simple average of every moment.
- **When to use it:** Checkout, support, recovery, and completion states.
- **Practical UI applications:** Make stressful moments clear and endings useful.
- **Implementation guidance:** Show confirmed outcome, receipt or reference, and next steps; handle uncertain outcomes honestly.
- **Good example:** An order confirmation explains delivery and how to get help.
- **Bad example:** Show confetti after a failed payment and ignore the error.
- **Trade-offs and limitations:** Do not sacrifice the rest of the journey; remembered satisfaction differs from actual task success.
- **Related laws:** Cognitive Bias; Doherty Threshold
- **Source:** https://lawsofux.com/peak-end-rule/

## Serial Position Effect

- **Definition:** Recall can favor items at the beginning and end of a sequence.
- **Core idea:** Position can influence memory differently across a series.
- **When to use it:** Instruction sequences, summaries, and ordered content.
- **Practical UI applications:** Put orientation early and useful next steps at the end.
- **Implementation guidance:** Preserve logical task order and make important actions discoverable throughout.
- **Good example:** A guide opens with prerequisites and ends with a verification checklist.
- **Bad example:** Bury a required middle step because it is less memorable.
- **Trade-offs and limitations:** Recall is not the same as navigation findability; effects depend on sequence and testing conditions.
- **Related laws:** Working Memory; Peak-End Rule
- **Source:** https://lawsofux.com/serial-position-effect/

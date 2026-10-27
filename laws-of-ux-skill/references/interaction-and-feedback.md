# Interaction and feedback

These are original explanations and package-authored applications. Examples are illustrative, not reported experiments or claims from the website. Read only entries relevant to the task.

[Doherty Threshold](#doherty-threshold) | [Fitts’s Law](#fittss-law) | [Flow](#flow) | [Goal-Gradient Effect](#goal-gradient-effect) | [Paradox of the Active User](#paradox-of-the-active-user) | [Parkinson’s Law](#parkinsons-law) | [Postel’s Law](#postels-law) | [Zeigarnik Effect](#zeigarnik-effect)

## Doherty Threshold

- **Definition:** Rapid system responses support a continuous, productive interaction rhythm; the site highlights a roughly 400 ms threshold.
- **Core idea:** Waiting disrupts interaction and attention.
- **When to use it:** Search, save actions, uploads, and asynchronous requests.
- **Practical UI applications:** Acknowledge input promptly and communicate real pending, success, and error states.
- **Implementation guidance:** Measure input-to-feedback and task latency; use honest status text and cancellable work where practical.
- **Good example:** Save immediately shows “Saving”, then confirms persistence.
- **Bad example:** Delay a finished task to make it appear valuable.
- **Trade-offs and limitations:** 400 ms is a contextual historical guideline, not a universal SLA or permission to fake progress.
- **Related laws:** Flow; Peak-End Rule
- **Source:** https://lawsofux.com/doherty-threshold/

## Fitts’s Law

- **Definition:** Pointing time depends on target distance and effective target size.
- **Core idea:** Small or distant targets demand more motor effort.
- **When to use it:** Touch controls, repeated row actions, menus, and primary buttons.
- **Practical UI applications:** Make frequent controls easy to acquire and separate destructive neighbors.
- **Implementation guidance:** Enlarge the actual hit area, preserve layout spacing, and provide keyboard operation.
- **Good example:** A delete icon sits inside a clearly labeled, adequately sized button.
- **Bad example:** A large visual icon has a tiny clickable center.
- **Trade-offs and limitations:** Pointer acquisition does not cover comprehension or keyboard access; numeric accessibility requirements come from WCAG.
- **Related laws:** Law of Proximity; Hick’s Law
- **Source:** https://lawsofux.com/fittss-law/

## Flow

- **Definition:** Flow is a state of absorbed engagement associated with an appropriate balance of challenge and skill.
- **Core idea:** Clear goals and feedback can sustain focused work.
- **When to use it:** Editors, learning tasks, and repeated expert workflows.
- **Practical UI applications:** Reduce interruptions and expose progress and useful next actions.
- **Implementation guidance:** Preserve focus and drafts; provide discoverable shortcuts alongside ordinary controls.
- **Good example:** An editor autosaves without stealing focus.
- **Bad example:** Repeated celebratory dialogs interrupt every successful action.
- **Trade-offs and limitations:** Interfaces can support but cannot guarantee flow; productive stopping and user control still matter.
- **Related laws:** Doherty Threshold; Cognitive Load
- **Source:** https://lawsofux.com/flow/

## Goal-Gradient Effect

- **Definition:** Motivation to approach a goal can increase as people perceive themselves getting closer to completion.
- **Core idea:** Visible distance to a meaningful goal can influence effort.
- **When to use it:** Onboarding, applications, and multi-stage setup.
- **Practical UI applications:** Show completed steps and the genuine remaining work.
- **Implementation guidance:** Derive progress from real task state; distinguish optional steps and allow later resumption.
- **Good example:** Setup says “2 of 3 required steps complete”.
- **Bad example:** Start everyone at a fabricated 80% completion.
- **Trade-offs and limitations:** Perceived progress differs from actual value; never invent completion or pressure unwanted actions.
- **Related laws:** Zeigarnik Effect; Peak-End Rule
- **Source:** https://lawsofux.com/goal-gradient-effect/

## Paradox of the Active User

- **Definition:** People often start using software to achieve immediate goals instead of first investing in instruction.
- **Core idea:** Short-term task motivation can displace learning that might help later.
- **When to use it:** Onboarding, unfamiliar features, and contextual assistance.
- **Practical UI applications:** Let people begin useful work and make help available at the point of need.
- **Implementation guidance:** Provide dismissible, keyboard-accessible help; do not put essential instructions only in hover tooltips.
- **Good example:** An empty editor offers a sample and a short inline explanation.
- **Bad example:** Force users through a long tour before they can work.
- **Trade-offs and limitations:** The site’s “never read” wording is an observation, not a literal universal; some tasks require explicit training.
- **Related laws:** Flow; Mental Model
- **Source:** https://lawsofux.com/paradox-of-the-active-user/

## Parkinson’s Law

- **Definition:** Work can expand to consume the time allocated to it.
- **Core idea:** Unnecessary work and open-ended processes can inflate duration.
- **When to use it:** Task flows with repeated entry or avoidable setup.
- **Practical UI applications:** Remove redundant steps and offer useful autofill.
- **Implementation guidance:** Reuse permitted known data and preserve edits; measure completion effort rather than imposing deadlines.
- **Good example:** A booking form prepopulates known contact information for confirmation.
- **Bad example:** Add a countdown to rush a complex application.
- **Trade-offs and limitations:** Originally an observation about work, not a universal user timing equation; speed must not replace comprehension.
- **Related laws:** Cognitive Load; Flow
- **Source:** https://lawsofux.com/parkinsons-law/

## Postel’s Law

- **Definition:** The robustness principle advocates restrained, consistent output and tolerance of understandable input variation.
- **Core idea:** Users should not have to match needless formatting demands.
- **When to use it:** Dates, telephone numbers, search, and imports.
- **Practical UI applications:** Accept harmless variation and explain real boundaries.
- **Implementation guidance:** Normalize only unambiguous formatting; validate authoritative constraints on the server and keep raw edits recoverable.
- **Good example:** A phone field accepts spaces before validating the country-aware number.
- **Bad example:** Silently reinterpret an ambiguous date or accept unsafe input.
- **Trade-offs and limitations:** Originated in network protocols; tolerance does not justify weakened security, ambiguous coercion, or silent data corruption.
- **Related laws:** Tesler’s Law; Mental Model
- **Source:** https://lawsofux.com/postels-law/

## Zeigarnik Effect

- **Definition:** Incomplete or interrupted activities can remain more memorable than completed ones.
- **Core idea:** Unfinished work can keep a task mentally salient.
- **When to use it:** Drafts, resumable applications, and optional learning plans.
- **Practical UI applications:** Make unfinished work recoverable and progress understandable.
- **Implementation guidance:** Save genuine state, show a resume action, and let users dismiss optional reminders.
- **Good example:** A drafts list shows the actual next required step.
- **Bad example:** Manufacture incomplete tasks to keep people anxiously returning.
- **Trade-offs and limitations:** Memory effects do not guarantee completion or benefit; avoid coercion and fabricated progress.
- **Related laws:** Goal-Gradient Effect; Working Memory
- **Source:** https://lawsofux.com/zeigarnik-effect/

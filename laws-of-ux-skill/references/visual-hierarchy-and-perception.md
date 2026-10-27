# Visual hierarchy and perception

These are original explanations and package-authored applications. Examples are illustrative, not reported experiments or claims from the website. Read only entries relevant to the task.

[Aesthetic-Usability Effect](#aesthetic-usability-effect) | [Law of Common Region](#law-of-common-region) | [Law of Proximity](#law-of-proximity) | [Law of Prägnanz](#law-of-prägnanz) | [Law of Similarity](#law-of-similarity) | [Law of Uniform Connectedness](#law-of-uniform-connectedness) | [Selective Attention](#selective-attention) | [Von Restorff Effect](#von-restorff-effect)

## Aesthetic-Usability Effect

- **Definition:** Visual appeal can improve perceived ease of use, even when actual task performance does not improve.
- **Core idea:** Perceived quality and measured usability can diverge.
- **When to use it:** Polishing a trustworthy product or evaluating a visually attractive redesign.
- **Practical UI applications:** Use consistent type, alignment, and restrained color while preserving clear controls.
- **Implementation guidance:** Reuse tokens and semantic components; measure task success separately from appearance ratings.
- **Good example:** A polished checkout still exposes fees and field errors.
- **Bad example:** An elegant icon-only form conceals confusing requirements.
- **Trade-offs and limitations:** Attractiveness can mask defects; aesthetics cannot establish accessibility or reliability.
- **Related laws:** Jakob’s Law; Cognitive Bias
- **Source:** https://lawsofux.com/aesthetic-usability-effect/

## Law of Common Region

- **Definition:** Elements inside the same bounded area tend to be perceived as a group.
- **Core idea:** Enclosure signals shared context.
- **When to use it:** Related metrics, settings sections, or option sets.
- **Practical UI applications:** Use a restrained background or boundary where a relationship needs clarification.
- **Implementation guidance:** Pair visual containment with a semantic section and heading.
- **Good example:** A filter panel groups controls affecting the same report.
- **Bad example:** Put unrelated alerts inside the payment summary container.
- **Trade-offs and limitations:** Too many nested cards obscure hierarchy; proximity may be sufficient.
- **Related laws:** Law of Proximity; Law of Uniform Connectedness
- **Source:** https://lawsofux.com/law-of-common-region/

## Law of Proximity

- **Definition:** Nearby elements tend to be interpreted as belonging together.
- **Core idea:** Spatial separation communicates relationships.
- **When to use it:** Labels, field errors, cards, captions, and action groups.
- **Practical UI applications:** Keep supporting information close to its referent and separate unrelated groups.
- **Implementation guidance:** Use smaller within-group spacing than between-group spacing; preserve relationships at responsive widths.
- **Good example:** A validation error appears directly below its field.
- **Bad example:** A caption lies closer to the next chart than its own.
- **Trade-offs and limitations:** Crowding harms legibility and target separation; visual proximity needs semantic equivalents.
- **Related laws:** Chunking; Fitts’s Law
- **Source:** https://lawsofux.com/law-of-proximity/

## Law of Prägnanz

- **Definition:** People tend to organize ambiguous or complex visual input into relatively simple, coherent forms.
- **Core idea:** Perception seeks understandable visual structure.
- **When to use it:** Icons, chart shapes, composition, and visual grouping.
- **Practical UI applications:** Use recognizable silhouettes, aligned structures, and clear figure relationships.
- **Implementation guidance:** Reduce gratuitous overlapping shapes; retain labels needed to interpret symbols.
- **Good example:** A simple chart legend identifies unambiguous series markers.
- **Bad example:** Replace essential labels with an abstract minimalist glyph.
- **Trade-offs and limitations:** This is a perceptual tendency, not proof that fewer features or words are always better.
- **Related laws:** Occam’s Razor; Law of Similarity
- **Source:** https://lawsofux.com/law-of-pr%C3%A4gnanz/

## Law of Similarity

- **Definition:** Visually similar elements tend to be perceived as related.
- **Core idea:** Shared appearance creates expectations of shared meaning or behavior.
- **When to use it:** Links, button variants, status markers, and repeated components.
- **Practical UI applications:** Give equivalent actions consistent styling and distinguish different roles.
- **Implementation guidance:** Reuse component variants; combine color with text, shape, or icons for meaning.
- **Good example:** All text links have a consistent visible link treatment.
- **Bad example:** Decorative badges look identical to clickable buttons.
- **Trade-offs and limitations:** Similarity can mislead when behaviors differ; color alone excludes users.
- **Related laws:** Jakob’s Law; Von Restorff Effect
- **Source:** https://lawsofux.com/law-of-similarity/

## Law of Uniform Connectedness

- **Definition:** Visually connected elements tend to be perceived as related.
- **Core idea:** An explicit connection can make relationships apparent.
- **When to use it:** Process diagrams, linked records, and multi-step sequences.
- **Practical UI applications:** Use connectors only for real relationships and label their meaning.
- **Implementation guidance:** Provide an ordered list or textual relationship alongside visual lines.
- **Good example:** A workflow line connects genuinely dependent stages.
- **Bad example:** Decorative lines imply dependencies between unrelated metrics.
- **Trade-offs and limitations:** Complex connectors can overwhelm; visual lines alone are inaccessible.
- **Related laws:** Law of Common Region; Law of Proximity
- **Source:** https://lawsofux.com/law-of-uniform-connectedness/

## Selective Attention

- **Definition:** People attend to a subset of available information, often guided by their current goals.
- **Core idea:** Visible content can still go unnoticed.
- **When to use it:** Alerts, changes in results, instructions, and dense screens.
- **Practical UI applications:** Place relevant cues near the task and avoid competing emphasis.
- **Implementation guidance:** Announce meaningful async status appropriately; preserve focus and make critical messages persistent.
- **Good example:** A failed save shows a message beside the editor action.
- **Bad example:** Put a critical warning in an ad-like rotating banner.
- **Trade-offs and limitations:** Attention varies; salience cannot guarantee noticing, understanding, or assistive-technology access.
- **Related laws:** Von Restorff Effect; Cognitive Load
- **Source:** https://lawsofux.com/selective-attention/

## Von Restorff Effect

- **Definition:** An item that differs from otherwise similar items can be more memorable.
- **Core idea:** Distinctiveness depends on a surrounding pattern.
- **When to use it:** Primary actions, important changes, and exceptional states.
- **Practical UI applications:** Reserve emphasis for the most relevant information.
- **Implementation guidance:** Use text and visual hierarchy together; honor reduced-motion preferences.
- **Good example:** One primary action stands out among secondary actions.
- **Bad example:** Every card flashes a different accent color.
- **Trade-offs and limitations:** Remembered does not mean understood or chosen; excessive emphasis destroys contrast.
- **Related laws:** Selective Attention; Law of Similarity
- **Source:** https://lawsofux.com/von-restorff-effect/

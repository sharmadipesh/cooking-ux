# UI review example

**Illustrative fixture, not a live audit:** an operations dashboard screenshot shows equal emphasis on 18 metrics, a date selector far above the chart, and an empty table reading “No data”. No runtime access, analytics, or user sessions are available.

## Issue 1: reporting period is visually detached

- **Problem/evidence:** Observed in the fixture: the date selector is separated from the chart by several unrelated panels.
- **Impact:** Hypothesis: reviewers may misattribute a chart to the wrong period or expend effort finding its scope.
- **Principle:** [Working Memory](../references/cognitive-load-and-decision-making.md#working-memory) and [Proximity](../references/visual-hierarchy-and-perception.md#law-of-proximity).
- **Recommendation:** Show a concise period label beside the chart title.
- **Priority:** Medium: recurring interpretation friction is plausible; incorrect business decisions are not established from the image.
- **Implementation:** Reuse the selected-period state for the label; do not introduce a second date source. Acceptance: changing the period updates results and label together.
- **Assumptions/limitations:** Audience/task inferred; behavior and responsiveness not tested.

## Issue 2: empty state does not explain a recovery action

- **Problem/evidence:** Observed: the table contains only “No data”. The screenshot does not reveal the cause.
- **Impact:** Hypothesis: users cannot distinguish a new workspace from filters excluding existing data.
- **Principle:** [Mental Model](../references/psychology-and-mental-models.md#mental-model) and [Active User](../references/interaction-and-feedback.md#paradox-of-the-active-user).
- **Recommendation:** Distinguish new, filtered-zero, loading, failure, and permission-denied states.
- **Priority:** Medium pending task evidence; raise to High if it blocks a core task without a usable workaround.
- **Implementation:** Branch on existing request/data/permission/filter state. Offer “Clear filters” only for filtered-zero; offer creation only with permission. Acceptance: each state has truthful copy and a relevant action.
- **Assumptions/limitations:** The screenshot establishes copy ambiguity, not missing application state handling. Inspect the component before editing.

**Next validation:** inspect live table states, keyboard operation, and narrow layout; test whether representative reviewers understand reporting scope. No usability score or live acceptance is claimed.

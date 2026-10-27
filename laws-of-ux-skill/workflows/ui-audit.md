# UI audit

1. Establish audience, task, interface version, route, permissions, device, and available evidence. If you cannot access the interface, request the minimum artifact or provide a clearly labeled preliminary assessment of the supplied material.
2. Capture or record relevant screens/states where tools permit, then attempt the task and recovery. Record reproduction steps and actual behavior. Screenshots establish visual observations; keyboard and runtime behavior require interaction or code evidence.
3. Inspect the checklist in references/usability-review-checklist.md across relevant dimensions. Mark inaccessible or out-of-scope states “not assessed”.
4. Select only principles that explain a specific issue. Distinguish a directly observed problem from a predicted user impact that requires research. Cite source entries for significant reasoning.
5. Prioritize using the definitions in SKILL.md. Consider severity, frequency/reach, confidence, and effort; do not invent those values. Accessibility exclusion and rare severe loss must not disappear behind a majority-use argument.
6. Report each issue using this template:

> **Problem/evidence:** [observed or hypothesis; location, state, reproduction/evidence].
> **Impact:** [task consequence; distinguish prediction from observation].
> **Principle:** [name and source/reference].
> **Recommendation:** [specific change].
> **Priority:** Critical / High / Medium / Low — [reason].
> **Implementation:** [component/layout/interaction change and acceptance condition].
> **Assumptions/limitations:** [unknown audience, missing access, untested behavior].

Finish with the most useful next actions and the validation scope. No numerical score unless the user has a transparent, agreed rubric. Do not claim to have observed findings from this workflow alone.

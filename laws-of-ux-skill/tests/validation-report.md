# Validation report

Date: 2026-10-27.

## 1.1.0: evaluation evidence moved out of the package

The installable package now contains only what an agent needs at install time. The sandbox fixtures, the optional Playwright runner with its lockfile, the implementation evaluation and its raw results, and the behavioral smoke results moved into the repository’s `evaluation/laws-of-ux-skill/` folder with Git history preserved. Links from this package to that evidence are repository URLs because an installed copy does not include it. The scenario prompts, expected behaviors, source manifest, Python regression tests, and this report stay in the package. Recorded fixture paths in the raw results and relative links in the moved files were rewritten for the new location; dates, hashes, outcomes, and findings were not edited. The rebuilt ZIP contains 28 files.

## Skill upgrade: implemented sandbox validation

The entrypoint now selects the requested deliverable explicitly, uses a concrete evidence/mechanism/change/check chain, and routes to component and decision playbooks. Detailed guidance covers unknown mutation recovery, async request scope, truthful data states, permissions, navigation, responsive hierarchy, and competing principles. Original law definitions and source attribution remain unchanged.

Two fresh agents implemented actual interfaces using the upgraded skill. Review corrected generic 503 handling in the final reference and strengthened a success assertion; an explicit negative-control run confirms that unconfirmed responses are rejected by the oracle. The independent browser suite passes all **13 acceptance checks** across the completed registration and records fixtures. The prior-skill artifacts pass 11/13; the observed gaps concerned recovery guidance after an unknown mutation outcome and generic server-error handling. This small comparison is not a general causal claim. See [the implementation evaluation](https://github.com/sharmadipesh/cooking-ux/blob/main/evaluation/laws-of-ux-skill/implementation-evaluation.md) and its artifact/result evidence.

All **16 Python integrity/packaging regression tests** pass, including a check that SKILL.md declares a license and a semantic `metadata.version`. Other checks ensure optional browser dependencies are neither scanned as skill content nor included in the ZIP. Browser dependencies are pinned and optional; core skill use stays offline and framework independent. A repository workflow is configured for Linux/Windows package validation on Python 3.9/3.13 and a Chromium acceptance job; remote run results must be checked separately before claiming CI success. Git attributes enforce LF for text checkout so Windows line-ending conversion does not create false ZIP byte mismatches. ZIP files remain binary.

The entrypoint is approximately 1,077 whitespace-separated words after the 2026-10-27 worked-example and frontmatter updates. File and test counts quoted in the dated sections below are historical snapshots from earlier reviews. At that release the ZIP included the updated skill, focused references, original law inventory, fixture artifacts, and optional test runner, with generated dependencies/caches excluded; since 1.1.0 the fixtures and runner live in the repository’s evaluation folder.

## Earlier validator improvement checks

A subsequent review found and corrected two reproducible validator issues: locale-dependent reads failed in a non-UTF-8 environment, and invalid/incomplete manifest JSON raised exceptions instead of validation diagnostics. All package reads and test mutations now specify UTF-8. Manifest records are checked before use. The optional validator's Python 3.9 minimum is now documented.

The registration example previously applied its pending guard before canceling the native submit event. Its instructional order is corrected: allow native fallback only when enhancement is unavailable; otherwise prevent default on every submit, then check pending state. The acceptance cases include repeated Enter presses. This is a reviewed pseudocode correction, not a live application test.

At that review, offline validation and all **13 regression tests** passed, including new non-UTF-8 locale, malformed/incomplete manifest, stale ZIP, missing member/archive, and cache-exclusion cases. The packaging script builds the shareable ZIP and verifies CRC, exact members, and byte equality; `--check` detects drift without rebuilding. The rebuilt ZIP contains 27 package files. No user-facing application or usability study was run in this review.

## Initial release checks

- Source research: the 30 English homepage concepts and eight publicly linked articles were fetched successfully and consulted. Source inventory, URLs, status, and snapshot hashes are recorded in source-manifest.json. The paid book/deck and all external bibliography studies were not verified.
- Remote URL validation: `python3 -B scripts/validate.py --online` checked 49 distinct public source/documentation URLs. All returned HTTP 200 on this date. This verifies accessibility of the URLs, not scientific accuracy or future availability.
- Offline integrity: `python3 -B scripts/validate.py` passed entrypoint metadata/context budget, 30 unique entries with all ten required fields, inventory/attribution correspondence, relative links and heading anchors, and T1–T7 scenario/rubric coverage.
- Validator regression tests: `python3 -B -m unittest discover -s tests -p 'test_*.py' -v` passed six tests. They cover a valid package and detection of a missing workflow, missing implementation guidance, incorrect attribution, broken anchor, and missing scenario. An initial test exposed path resolution differences through a temporary-directory symlink; the validator was corrected and all six tests rerun successfully.
- Skill-creator's independent `quick_validate.py` reported “Skill is valid!” using PyYAML in a temporary environment. This dependency is for that external validator only; the bundled validator uses Python's standard library.
- Behavioral smoke evaluation: a separate agent read the package without browsing and produced actual proposals for all seven scenarios. See [actual responses](https://github.com/sharmadipesh/cooking-ux/blob/main/evaluation/laws-of-ux-skill/behavioral-smoke-results.md). The proposals met the assessed selection, actionability, trade-off, and evidence-honesty criteria. T7 passed as a proposal. This batch used one shared context, not seven isolated runs.
- Baseline: before loading this skill, the same evaluator already rejected the seven-item navigation claim and fabricated progress. No baseline failure or measured improvement is claimed.

## One-command installation check

On 2026-10-27, the third-party Skills CLI discovered the skill directly from the GitHub repository URL. A non-interactive installation into an isolated temporary project for Codex installed all 25 package files byte-for-byte, and the installed package passed the bundled validator. The test used `--skill laws-of-ux-skill --agent codex --yes --copy`; no personal installation was modified. Interactive selection, other agents, and the global-install path were not exercised. The README documents the CLI’s project/default and global options and its Node.js prerequisite based on official Skills CLI documentation. A paste-into-agent installation message is guidance, not a universal automatic-install feature.

## Limits

At the initial release, no application repository, implementation fixture, live product, or representative user study was supplied. That proposal smoke pass does not establish successful frontend implementation, runtime behavior, accessibility conformance, or usability outcomes; the later sandbox evaluation above adds narrower implementation evidence. Implementation acceptance checks remain documented for a recipient to run against real fixtures. Structural checks cannot prove recommendation quality. The example form is illustrative and was not run as an application.

The initial entrypoint was approximately 864 whitespace-separated words, with detail loaded from focused references. Runtime use requires no internet access. No copied source article corpus, artwork, paid content, or third-party code dependencies are bundled.

## Archive verification

The sibling laws-of-ux-skill.zip is built from this directory with the package folder at its root. Release packaging verifies the ZIP CRC, exact member set, byte-for-byte equality with source files, and offline validation after extraction. The archive contains no unrelated workspace files or caches. Rebuild and repeat these checks after changing any package file.

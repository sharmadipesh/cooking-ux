# Validation report

Date: 2026-10-27.

## Completed checks

- Source research: the 30 English homepage concepts and eight publicly linked articles were fetched successfully and consulted. Source inventory, URLs, status, and snapshot hashes are recorded in source-manifest.json. The paid book/deck and all external bibliography studies were not verified.
- Remote URL validation: `python3 -B scripts/validate.py --online` checked 49 distinct public source/documentation URLs. All returned HTTP 200 on this date. This verifies accessibility of the URLs, not scientific accuracy or future availability.
- Offline integrity: `python3 -B scripts/validate.py` passed entrypoint metadata/context budget, 30 unique entries with all ten required fields, inventory/attribution correspondence, relative links and heading anchors, and T1–T7 scenario/rubric coverage.
- Validator regression tests: `python3 -B -m unittest discover -s tests -p 'test_*.py' -v` passed six tests. They cover a valid package and detection of a missing workflow, missing implementation guidance, incorrect attribution, broken anchor, and missing scenario. An initial test exposed path resolution differences through a temporary-directory symlink; the validator was corrected and all six tests rerun successfully.
- Skill-creator's independent `quick_validate.py` reported “Skill is valid!” using PyYAML in a temporary environment. This dependency is for that external validator only; the bundled validator uses Python's standard library.
- Behavioral smoke evaluation: a separate agent read the package without browsing and produced actual proposals for all seven scenarios. See [actual responses](behavioral-smoke-results.md). The proposals met the assessed selection, actionability, trade-off, and evidence-honesty criteria. T7 passed as a proposal. This batch used one shared context, not seven isolated runs.
- Baseline: before loading this skill, the same evaluator already rejected the seven-item navigation claim and fabricated progress. No baseline failure or measured improvement is claimed.

## One-command installation check

On 2026-10-27, the third-party Skills CLI discovered the skill directly from the GitHub repository URL. A non-interactive installation into an isolated temporary project for Codex installed all 25 package files byte-for-byte, and the installed package passed the bundled validator. The test used `--skill laws-of-ux-skill --agent codex --yes --copy`; no personal installation was modified. Interactive selection, other agents, and the global-install path were not exercised. The README documents the CLI’s project/default and global options and its Node.js prerequisite based on official Skills CLI documentation. A paste-into-agent installation message is guidance, not a universal automatic-install feature.

## Limits

No application repository, implementation fixture, live product, or representative user study was supplied for scenario execution. The proposal smoke pass therefore does not establish successful frontend implementation, runtime behavior, accessibility conformance, or usability outcomes. Implementation acceptance checks remain documented for a recipient to run against real fixtures. Structural checks cannot prove recommendation quality. The example form is illustrative and was not run as an application.

The main entrypoint is approximately 864 whitespace-separated words, with detail loaded from focused references. Runtime use requires no internet access. No copied source article corpus, artwork, paid content, or third-party code dependencies are bundled.

## Archive verification

The sibling laws-of-ux-skill.zip is built from this directory with the package folder at its root. Release packaging verifies the ZIP CRC, exact member set, byte-for-byte equality with source files, and offline validation after extraction. The archive contains no unrelated workspace files or caches. Rebuild and repeat these checks after changing any package file.

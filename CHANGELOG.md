# Changelog

Each skill records its version in SKILL.md under `metadata.version`. When a package's content changes, bump that version, add an entry here, and rebuild the package ZIP.

## 2026-10-27, second release

### laws-of-ux-skill 1.1.0

- Sandbox fixtures, the optional browser runner, and the implementation and behavioral evaluation records moved out of the package into `evaluation/laws-of-ux-skill/`; package links to that evidence are now repository URLs, and the ZIP contains only install-time content.

### ux-audit-skill 1.1.0

- Evaluated sandbox reports, screenshots, runtime observations, and the loopback fixture server moved out of the package into `evaluation/ux-audit-skill/`; package links to that evidence are now repository URLs, and the ZIP contains only install-time content.

## 2026-10-27

### laws-of-ux-skill 1.0.0

- First versioned release. SKILL.md now declares `license` and `metadata.version`, and the bundled validator requires both.
- Guides with worked examples and workflow diagrams, a component playbook, decision and validation guidance, and sandbox browser evaluations.

### ux-audit-skill 1.0.0

- First versioned release. SKILL.md now declares `license` and `metadata.version`, and the bundled validator requires both.
- Evidence contract, coverage ledger, separate severity, priority and confidence rubric, report template, and evaluated sandbox reports.

# UX Audit Skill

A dedicated, portable skill for auditing Figma designs, prototypes, user flows, screenshots, and live web pages. It produces a structured report with evidence, user impact, separate severity/priority/confidence, practical recommendations, and acceptance checks.

Read [SKILL.md](SKILL.md). It routes to source acquisition, audit dimensions, prioritization, and a copyable report template. It does not require the companion Laws of UX skill or a specific AI provider.

## Install

```sh
npx skills add https://github.com/sharmadipesh/cooking-ux --skill ux-audit-skill
```

Select the target agent. Add `-g` for user-wide installation. The optional third-party Skills CLI requires Node.js 22.20+ and Git. Manual installation needs no Node packages: copy the whole `ux-audit-skill/` folder into your agent's documented directory.

| Local agent | Personal location | Project location | Invoke |
|---|---|---|---|
| Codex | `~/.agents/skills/ux-audit-skill/` | `.agents/skills/ux-audit-skill/` | `$ux-audit-skill` |
| Claude Code | `~/.claude/skills/ux-audit-skill/` | `.claude/skills/ux-audit-skill/` | `/ux-audit-skill` |

Preserve an existing installation rather than blindly overwriting it. Open a new session if discovery does not refresh. Other agents control their own directory/invocation conventions. A general assistant can use the full folder/ZIP as context, or SKILL.md plus the references it requests. A link alone does not grant filesystem access or install a skill in every product.

## Use

**Figma:**

> Use $ux-audit-skill to audit this Figma design: [link]. Review the account-setup journey for first-time coordinators. Prioritize issues by user impact, cite frames/nodes, and distinguish design findings from runtime behavior you cannot verify.

**Live website:**

> Use $ux-audit-skill to audit [URL] for finding and booking a service. Inspect relevant mobile, tablet, and desktop states and keyboard paths. Stop before real booking/payment submission. Give an evidence-based report with severity, priority, recommendations, and checks for the fixes.

**User flow:**

> Use $ux-audit-skill to review this supplied onboarding flow. Identify decision, handoff, navigation, recovery, and completion risks. Distinguish missing documentation from observed product defects and specify what to validate.

For Claude Code, replace the dollar invocation with `/ux-audit-skill`. Do not paste sensitive account data into prompts or reports.

## Access and output

Figma and live-site audits require appropriate access plus host-provided reading/browser tools. This package supplies instructions, not those capabilities. If direct access fails, the agent should report that limit and review accessible exports or supplied artifacts. It must not pretend a static frame establishes DOM semantics, keyboard behavior, or production responsiveness.

Default output is a readable audit in the conversation. Request a Markdown file and evidence attachments if desired. [The template](templates/audit-report.md) defines the handoff format. [The example](examples/artifact-audit.md) demonstrates a limited artifact review. Audit permission does not authorize editing the design, commenting in Figma, publishing, or submitting real transactions.

## Validate and share

Optional maintenance checks use Python 3.9+ and its standard library:

```sh
python3 -B ux-audit-skill/scripts/validate.py
python3 -B -m unittest discover -s ux-audit-skill/tests -p 'test_*.py' -v
python3 -B ux-audit-skill/scripts/package.py --check
```

From the repository parent, rebuild the sibling ZIP with `python3 -B ux-audit-skill/scripts/package.py` after changes. Share the whole folder or `ux-audit-skill.zip`, including LICENSE, references, and templates. The optional structured JSON report can be checked with `scripts/validate.py --report path/to/report.json`; it verifies structure and evidence references, not whether observations are true or recommendations are good. Markdown remains the normal deliverable.

See [scenarios](tests/scenarios.md) and [validation evidence](tests/validation-report.md) for real checks and limits. Synthetic fixtures do not establish authenticated Figma integration, production acceptance, or full accessibility conformance.

## Sources and license

Original contributions are MIT licensed; see [LICENSE](LICENSE). Standards/articles remain with their respective owners. [Source notes](references/sources.md) explain provenance and the package-specific prioritization rubric. No external articles or Figma artwork are bundled, and no endorsement is asserted.

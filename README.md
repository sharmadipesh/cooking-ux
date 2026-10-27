# Cooking UX

**Help your AI build interfaces that are easier to understand and use.**

Cooking UX is a reusable skill that turns 30 concepts from [Laws of UX](https://lawsofux.com/) into practical guidance for designing, reviewing, and improving real products.

Use it with Codex, Claude Code, other compatible coding agents, or an AI assistant that can read the included files. The skill selects principles that fit your task and translates them into concrete design and code changes.

## What can it help with?

- Build clearer landing pages, dashboards, and application screens.
- Improve navigation, forms, tables, empty states, and user flows.
- Reduce unnecessary choices, confusion, and memory demands.
- Review an interface and prioritize actionable improvements.
- Refactor frontend components while preserving working behavior.
- Consider accessibility, responsive layouts, feedback, and error recovery.

Every concept includes an original explanation, practical applications, implementation guidance, good and bad examples, limitations, and a source link. The package works offline once its files are available to the assistant.

## Get started

```sh
git clone https://github.com/sharmadipesh/cooking-ux.git
cd cooking-ux
```

Copy the complete `laws-of-ux-skill` folder to your agent’s skill directory. Choose the location for your tool, and check for an existing installation before copying:

| Tool | Personal skill directory | Invoke with |
|---|---|---|
| Codex | `~/.agents/skills/laws-of-ux-skill/` | `$laws-of-ux-skill` |
| Claude Code, local sessions | `~/.claude/skills/laws-of-ux-skill/` | `/laws-of-ux-skill` |

For example, to install in Codex when the destination does not already exist:

```sh
mkdir -p ~/.agents/skills
cp -R laws-of-ux-skill ~/.agents/skills/laws-of-ux-skill
```

Start a new agent session if needed, then try:

> Use $laws-of-ux-skill to improve this dashboard. Reuse the existing design system, preserve its functionality, and make the most important information and actions easier to find. Implement the changes and report what you verified.

For Claude Code, use `/laws-of-ux-skill` instead. For a general AI assistant, attach the folder or ZIP and ask it to read `SKILL.md` and the relevant references. Automatic discovery depends on the product and its settings.

## Explore the package

| Start here | What you will find |
|---|---|
| [Skill instructions](laws-of-ux-skill/SKILL.md) | The decision process and reference routing |
| [Full usage guide](laws-of-ux-skill/README.md) | Installation, prompts, sharing, offline use, and updates |
| [30-concept inventory](laws-of-ux-skill/references/ux-laws-index.md) | Verified concepts and original source links |
| [Workflows](laws-of-ux-skill/workflows/) | Design, audit, improvement, and implementation |
| [Examples](laws-of-ux-skill/examples/) | Practical decisions, an audit, and implementation guidance |
| [Validation report](laws-of-ux-skill/tests/validation-report.md) | Checks performed and their limitations |
| [Downloadable ZIP](laws-of-ux-skill.zip) | The complete portable skill package |

## Check the package

No third-party Python packages are required for the bundled checks:

```sh
python3 -B laws-of-ux-skill/scripts/validate.py
python3 -B -m unittest discover -s laws-of-ux-skill/tests -p 'test_*.py' -v
```

The package includes seven realistic design scenarios and expected behaviors. Integrity checks and proposal reviews do not establish live application usability or accessibility conformance; validate changes in the product you are building.

## Sources and license

This is an independent project informed by Jon Yablonski’s **Laws of UX**. It is not affiliated with or endorsed by Laws of UX. Source coverage was verified on October 27, 2026.

The package contains original explanations, workflows, and examples, with no copied article collection or artwork. The [MIT license](laws-of-ux-skill/LICENSE) covers original package contributions only. Upstream website content has its own CC BY-NC-ND 4.0 license and is not relicensed here. See [source attribution and research scope](laws-of-ux-skill/references/source-links.md).

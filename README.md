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

## Install with one command

Run this in your project’s terminal:

```sh
npx skills add https://github.com/sharmadipesh/cooking-ux
```

Select `laws-of-ux-skill` and your coding agent when prompted. The installer adds the complete skill folder, including its references and workflows. No manual clone or file copying is needed. It requires Node.js 22.20 or later and Git. This uses the third-party [open-source Skills CLI](https://github.com/vercel-labs/skills).

Want the skill available across projects? Add `-g`:

```sh
npx skills add https://github.com/sharmadipesh/cooking-ux -g
```

## Prefer to paste a link into your AI agent?

Copy this message into an agent that supports repository access and skill installation:

> Install the UX skill from https://github.com/sharmadipesh/cooking-ux into this project for my coding agent. Install the complete laws-of-ux-skill folder, including its references and workflows. Preserve any existing installation and report the installation path.

A repository link alone cannot automatically install files in every AI product. Your agent needs installation tools and access to your project. For chat assistants without installation support, attach [the ZIP](laws-of-ux-skill.zip) and ask them to read SKILL.md and the relevant files.

## Use it

After installation, start a new agent session if needed. In Codex, try:

> Use $laws-of-ux-skill to improve this dashboard. Reuse the existing design system, preserve its functionality, and make the most important information and actions easier to find. Implement the changes and report what you verified.

In Claude Code, use `/laws-of-ux-skill` instead. Automatic discovery depends on the product and its settings. See [the full guide](laws-of-ux-skill/README.md) for manual installation and offline usage.

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

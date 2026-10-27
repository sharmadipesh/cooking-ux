# Laws of UX Skill

A portable, Markdown-first skill for designers, developers, and AI assistants building or evaluating real interfaces. It turns selected UX concepts into concrete decisions, implementation guidance, and validation conditions using **Understand → Analyze → Select principles → Apply → Validate → Explain**.

Start with [SKILL.md](SKILL.md). It routes to four workflows, the verified 30-concept inventory, focused references, a component playbook, realistic examples, seven behavioral scenarios, and two runnable sandbox implementations. No API, model, JavaScript framework, network connection, or paid source is required for ordinary use. Python 3.9+ is optional for package validation.

## Quick install from GitHub

From your project terminal:

```sh
npx skills add https://github.com/sharmadipesh/cooking-ux
```

Choose `laws-of-ux-skill` and the target agent. The complete package is installed together. Add `-g` to install for your user across projects. Requires Node.js 22.20 or later and Git; installation needs internet access. This optional installer is the third-party [Skills CLI](https://github.com/vercel-labs/skills), not a built-in command shared by every agent. Manual installation below does not require Node.js.

Or paste this into an agent with repository access and installation tools:

> Install the UX skill from https://github.com/sharmadipesh/cooking-ux into this project for my coding agent. Install the complete laws-of-ux-skill folder with its references and workflows. Preserve any existing installation and report the installation path.

A link alone does not give a general chat assistant file-system access or automatic skill installation.

## Install in a local coding agent

Copy the **whole directory**, retaining its name and references. Do not copy only SKILL.md. Check that a destination does not already exist before copying; merge intentionally rather than overwrite an existing installation.

| Environment | Personal location | Project location | Explicit request |
|---|---|---|---|
| Codex | `~/.agents/skills/laws-of-ux-skill/` | `.agents/skills/laws-of-ux-skill/` | `$laws-of-ux-skill` followed by your task |
| Claude Code (local) | `~/.claude/skills/laws-of-ux-skill/` | `.claude/skills/laws-of-ux-skill/` | `/laws-of-ux-skill` followed by your task |

For example, from the directory containing this package, choose one destination:

```sh
mkdir -p ~/.agents/skills
# Run only after confirming the destination does not exist:
cp -R laws-of-ux-skill ~/.agents/skills/laws-of-ux-skill
```

Open a new session if the agent does not discover it. Verify the skill is listed or invoke it explicitly. Exact support can vary by client version and organization settings. These local conventions were checked on 2026-10-27 against [official Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [official Claude Code documentation](https://code.claude.com/docs/en/skills). They do not imply automatic loading in every desktop, cloud, or general chat product.

For another Agent Skills-compatible environment, consult its documented skill directory and copy the folder there. The [Agent Skills format](https://agentskills.io/specification) defines this package’s metadata and structure, but individual products control discovery and invocation. Do not assume a provider-specific directory or command works elsewhere.

## General AI assistant and offline use

Attach the folder or ZIP if file reading is supported. Otherwise provide SKILL.md as context, then supply the workflow and reference entries it requests. With a small context limit, provide the inventory first and only relevant entries afterward. A model cannot follow files it cannot access. Plain configuration formats such as project instruction files can point to SKILL.md; do not paste the entire knowledge base into every prompt.

Copyable instruction:

> Use the attached laws-of-ux-skill/SKILL.md. Read the appropriate workflow and only the references relevant to my task. Apply a small set of justified principles, make actionable changes, and report real validation and limitations. Use the bundled explanations without browsing unless I ask for updated research.

The full definitions and practical guidance are bundled. Internet access is needed only for opening original citations, checking current standards/tool conventions, or updating the inventory. An assistant capable of reading local files can use it offline; installation or account authentication for the agent itself may have separate requirements.

## Copyable tasks

**Build a SaaS page**

> Use $laws-of-ux-skill to build a responsive landing page for our small-team scheduling product in this repository. Reuse our design system. Prioritize explaining the benefit and starting a trial. Inspect the existing routes first; use honest content and state which integrations actually work.

**Audit a dashboard**

> Use $laws-of-ux-skill to audit this analytics dashboard for a weekly operations review. Inspect the supplied screens and interactions. Report concrete evidence, task impact, relevant principles, priority, implementation suggestions, and assumptions. Do not invent analytics or assign a numerical usability score.

**Improve a component**

> Use $laws-of-ux-skill to improve this registration form’s labels, validation, keyboard behavior, and error recovery. Preserve its payload and submission logic. Implement scoped changes, test relevant paths, and explain the few principles that materially informed them.

For Claude Code, replace `$laws-of-ux-skill` with `/laws-of-ux-skill`. In a general assistant, replace it with “Use the attached SKILL.md and its referenced files.”

## Share and maintain

Share the complete folder or laws-of-ux-skill.zip with its LICENSE and source documentation. Recipients can inspect Markdown before installing; nothing needs to execute during installation. No personal data, secrets, source artwork, or source article copies belong in the package.

To update: compare the English homepage’s linked concept set with the inventory; inspect added/changed detail pages and articles; verify definitions and caveats; update the inventory, affected entries, source-manifest date/status/hashes, and source notes together. Distinguish new homepage entries from article concepts and supplementary sources. Update agent installation conventions only after checking official documentation. Record inaccessible sources explicitly instead of presenting them as verified.

Run offline structural validation from the package directory with Python 3.9+:

```sh
python3 scripts/validate.py
python3 -B -m unittest discover -s tests -p 'test_*.py' -v
```

Optionally check current remote URLs with `python3 scripts/validate.py --online`. Network failures fail that check and are reported; HTTP success is not semantic verification. Run the scenarios in tests/test-prompts.md against the target agent and evaluate with tests/expected-behaviors.md. For executable form and records tasks, see [optional browser checks](tests/browser/README.md) and [implementation evaluation](tests/implementation-evaluation.md). The optional browser tests use pinned development dependencies, while ordinary skill use and Python checks remain independent of Node packages. Structural checks do not establish agent behavior. See tests/validation-report.md for the checks actually performed on this release.

To rebuild a shareable archive, run this from the parent directory after validating:

```sh
python3 -B laws-of-ux-skill/scripts/package.py
python3 -B laws-of-ux-skill/scripts/package.py --check
```

The packaging script excludes generated Python caches and common editor artifacts, then compares the ZIP member list and bytes with the package. The `--check` command detects stale downloads without rebuilding them. Review additional files before sharing. After editing the package, rebuild the ZIP before committing.

## Sources and licensing

Primary reference: Jon Yablonski’s [Laws of UX](https://lawsofux.com/). Research covered all 30 English homepage concept pages and eight linked public articles on 2026-10-27. No primary page failed access; paid book/deck contents and every external research citation were not verified. See [source links](references/source-links.md) for coverage and interpretation limits.

The source site identifies its content as CC BY-NC-ND 4.0. This package supplies original explanations, workflows, and examples, with no copied article corpus or artwork. Its MIT license applies only to original contributions and does not relicense the website or authorize distribution of adapted upstream expression. Read [LICENSE](LICENSE). It is an independent resource, not an official Laws of UX product or endorsement.

# Agentic Toolkit

**Reusable practices for making autonomous work easier to understand, direct, scrutinize, and maintain.**

Agents can build a great deal in a short time. They can also leave a project with muddled context, decisions buried in conversations, confident but unverified explanations, and mountains of things nobody meant to maintain.

Agentic Toolkit packages a few deliberately distinct ways of working with that reality. Each skill should be useful by itself, carry a recognizable point of view, and respect the project it enters. Use the ones that help. There's no required pipeline, shared runtime, or prescribed agent harness.

## Skills

The skills follow the [Agent Skills specification](https://agentskills.io/specification). Install any one independently, or use several together.

| Skill | What it brings | Natural default |
| --- | --- | --- |
| **[Superfan](skills/superfan/SKILL.md)** | Obsessive, opinionated, evidence-grounded attention to the seams, identity, experience, and latent potential of a subject. | Investigate deeply and deliver a substantial critique; also enriches research, design, or other work without replacing its goal. |
| **[Project Startup](skills/project-startup/SKILL.md)** | Predictable, context-sensitive homes for a project's durable knowledge. | Establish or improve an information architecture without forcing a template. |
| **[Project Shaping](skills/project-shaping/SKILL.md)** | Evidence-led stewardship as implementation, decisions, and project knowledge evolve. | Reconcile what the repository says with what is known, preserving established intent rather than inventing new taste. |
| **[Anti-Slop](skills/anti-slop/SKILL.md)** | Convention-led cleanup of accumulated agentic residue: chat-shaped docs, redundant comments, duplicated explanations, and needless maintenance noise. | Inspect, make the hygiene changes the user authorized, preserve meaningful exceptions, and verify the result. |

### Complete practices, additive perspectives

An **executable practice** supplies a complete way to approach a recognizable job. "Executable" describes a method an agent can carry out; it does not imply a bundled command-line program. Startup and Shaping are principally practices, and Anti-Slop is a self-contained cleanup practice.

An **additive perspective** changes *how* another task is approached without taking over its purpose. Superfan naturally plays this role: give a research task Superfan's curiosity and sharp taste, and the result is more revealing research—not an unrelated critique attached at the end. Anti-Slop's discipline can likewise accompany implementation without triggering a surprise whole-repository purge.

These are **descriptions of what skills do, not modes, exclusive types, or extra configuration**. Skills have sensible standalone defaults. When combined, they keep their character while adapting to the user's subject, deliverable, and permissions. No skill silently requires another.

## Installation

Install a selected skill with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add worflor/agentic-toolkit --skill superfan
npx skills add worflor/agentic-toolkit --skill anti-slop
```

Or install all currently available skills:

```bash
npx skills add worflor/agentic-toolkit --all
```

For example, to install Superfan globally for Claude Code:

```bash
npx skills add worflor/agentic-toolkit --skill superfan -g -a claude-code -y
```

While the repository is private, installation requires GitHub authentication with read access. You can also clone it using existing credentials and run `npx skills add . --skill superfan` from the checkout.

Manual installation works: copy the complete `skills/<name>/` directory to a supported skills location such as `.agents/skills/` or `.claude/skills/`. Include its references and any supporting resources.

## Give a skill a job

A name, a subject, and a clear request are usually enough. The skill handles its own method; the task determines scope and authority.

> **Superfan** this mod. Follow the actual code and design history, challenge the player experience, and don't edit anything.

> Deep-research this design space **with Superfan**. Keep the research deliverable, but obsess over hidden tensions and underexplored opportunities.

> Use **Project Startup** to give this new repository dependable places for technical knowledge, design intent, and current work. Respect what already exists.

> Use **Project Shaping** after our latest development sprint. Trace what the implementation taught us and reconcile stale documentation without inventing new product direction.

> Use **Anti-Slop** on this codebase. Clean up chat-shaped docs, redundant comments, and duplicated instructions. Preserve technical reasoning and intentional personality. Check your changes.

The defaults are complete, but **default behavior is not default authority**. A request to review isn't permission to edit. A cleanup request doesn't grant permission to redesign the product. Combining skills never expands permissions.

## What holds the collection together

**Predictability at the center; emergence around it.**

- **Understand before intervening.** Read enough of the actual artifact, code, history, and evidence to know what the work means.
- **Separate truth from intent.** A specification, an implementation, a passing test, and a predicted experience answer different questions.
- **Keep subject-specific authority local.** Reusable methodology belongs here. A project's design decisions, conventions, and taste belong to that project.
- **Protect useful weirdness.** Theatrical instructions, personality, humor, and deliberate constraints can carry meaning. Generic tidiness is not the goal.
- **Leave less process than value.** Prefer canonical information, proportionate edits, and enforceable checks over another layer of documentation.

These principles unite the collection; they don't make the skills interchangeable.

## Repository layout

```text
skills/
  <skill-name>/
    SKILL.md             # discoverable method and default behavior
    references/          # deeper guidance when useful
    scripts/             # optional utilities
README.md                # catalogue and examples
AGENTS.md                # contributor and agent guidance
scripts/validate.py      # dependency-free packaging/link checks
```

Every entry can stand alone. The canonical, long-form [Project Startup](skills/project-startup/references/method.md) and [Project Shaping](skills/project-shaping/references/method.md) methods remain available, with their former root links preserved at [Agentic Project Startup.md](Agentic%20Project%20Startup.md) and [Project Shaping.md](Project%20Shaping.md).

## Contributing and verification

Add a skill when it solves a recognizable, reusable problem and has an intelligible default. Give it a clear invocation boundary, honest limitations, and enough personality to do its job. Avoid redundant versions of shared facts or obligatory handoffs to other skills.

To check skill metadata and local Markdown links:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See [AGENTS.md](AGENTS.md) for repository-specific contribution guidance. These structural checks do **not** measure the quality of an agent's reasoning; evaluate real task behaviour separately.

## License

MIT. See [LICENSE](LICENSE).

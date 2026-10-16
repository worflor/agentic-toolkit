---
name: project-startup
description: >-
  Establish or reorganize a project's information architecture so humans and coding
  agents can find reliable context. Use when starting a repository, adopting an
  unfamiliar codebase, onboarding autonomous contributors, or organizing README,
  AGENTS.md, technical/domain design, status, working briefs, and durable reference
  material. Keep structure predictable without forcing the project into a template.
---

# Project Startup

**Give knowledge good places to live.**

Use this skill to establish or improve a project's information architecture: the canonical homes, landmarks, and navigation that make future independent work more reliable. The goal is not standardized documents for their own sake. It is a repository that humans and agents can understand, inherit, and work inside.

**Read [the complete Startup method](references/method.md) before making structural recommendations or changes.** It is the canonical methodology and is deliberately more detailed than this entry point. Do not guess its contents from the short description.

## Start from the project that exists

1. Establish what the user actually asked for: design a new structure, audit an existing one, or apply changes. If they requested analysis only, do not edit.
2. Survey the repository's actual current grammar: root, README, agent instructions, important documentation, code and assets, tests, workflows, changelog, and active work. Follow relevant links rather than reading just the front page.
3. Distinguish durable intent, technical knowledge, live status, historical reasons, working briefs, and incidental residue. Identify where the canonical version of each important fact should live.
4. Establish a small, predictable set of landmarks. Typical roles include a public README, a routing-focused AGENTS.md, durable technical/domain designs, an honest status board, bounded briefs, and reference material. **These are roles, not compulsory filenames or empty documents to generate.**
5. Preserve useful existing conventions, distinctive project taste, and historically justified exceptions. Adapt the information architecture to the project; don't coerce an app, research engine, and game into identical designs.
6. Where writing is authorized, implement proportionate changes and repair links. Otherwise supply a grounded map of the proposed structure and specific next steps.

## Guardrails

- Keep day-to-day context small: `AGENTS.md` should orient and route, not duplicate every design document.
- Prefer one canonical home for important information. Avoid creating a new Markdown file just because something can be written down.
- Treat code, tests, and runtime behavior as evidence about current implementation; they do not automatically override product intent.
- Do not turn this skill into a coding framework, CI policy, feature design review, or Superfan pass unless the user asks for those tasks.
- Never claim a build, test, or migration succeeded without checking it.

## Finish well

A good result makes it obvious where a new worker should look first, which sources are authoritative, how to resume work, and what remains unresolved. The project should be more legible, **without becoming more bureaucratic**.

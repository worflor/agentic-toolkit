---
name: project-shaping
description: >-
  Reconcile documentation, structure, intent, implementation, and history
  as a project evolves. Use for project shaping, stewardship,
  trajectory cleanup, stale context, lost decisions, archaeology, and emerging
  architecture. Preserve established project intent and conventions without
  inventing project-specific taste. Not routine code review or refactoring.
---

# Project Shaping

**Help knowledge and its places keep matching the project as it evolves.**

Use this skill for thoughtful stewardship of a repository's accumulated understanding. A project changes when people build and use it; its docs, assumptions, and vocabulary don't always change at the same speed. The job is to discover what the work has actually taught the project, protect what makes it distinctive, and repair stale representations proportionately.

Use the [canonical Project Shaping method](references/method.md) for the relevant evidence and decision rules. Read the whole method for a broad shaping pass; for a narrow correction, load the pertinent sections rather than every page. Do not substitute generic cleanup conventions for its guidance.

## Work from evidence, not tidy-looking files

1. Respect the user's scope and permissions. An inspection or advice request does **not** authorize edits.
2. Orient in the existing project: README, AGENTS.md, technical and domain designs, current-state files, briefs, tests, implementation, change history, and any other relevant evidence.
3. Separate **current truth**, **intent**, **working context**, **archaeology**, and **residue**. Differences between documents and code are questions to investigate, not automatic proof that one side is wrong.
4. Trace important divergences to causes where possible: experiments that won, compromises, temporary workarounds, obsolete assumptions, conventions that emerged organically, or genuine drift.
5. Look for useful, evidence-backed structure: repeated primitives, undernamed invariants, and established interface rules. Repetition alone does not confer authority; surface uncertain interpretations instead of declaring them policy.
6. Identify which findings deserve corrections, decisions, durable references, tests, or simply a preserved historical note. Don't require every discovery to become documentation.
7. When authorized to modify, change the smallest coherent set of files, repair links, preserve original meaning, and report what remains unresolved. Otherwise deliver a grounded shaping brief with the evidence and the recommended choices.

## Guardrails

- Preserve **established** project taste and meaningful weirdness. Don't introduce the shaper's preferred aesthetics, conventions, or product direction under the guise of stewardship.
- Consider the age, authority, provenance, and context of each claim. Passing tests is not evidence of a product's intended experience; repeating a pattern is not evidence of the owner's intent.
- Avoid rewriting working code merely to match an outdated plan; avoid rewriting a deliberate design merely to justify temporary code.
- Do not act like a scheduled monitoring service, bug triager, or aggressive refactoring agent.
- Use plain language, meaningful evidence, and proportionality. The next worker should inherit clarity, not process overhead.

## Finish well

Success means the repository more accurately represents **what it is, what it intends to be, and what someone needs to know to keep building it**, without flattening its identity.

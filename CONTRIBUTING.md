# Contributing

Rules for adding or editing concept files in this library. These are non-negotiable — the library's value comes from consistency.

## Hard Rules

1. **One concept per file.** No exceptions. If something feels like "two concepts in one file," split it.
2. **Use `TEMPLATE.md`.** Copy the template structure verbatim. All required top-matter fields must be filled.
3. **Filenames are `kebab-case.md`.** Lowercase only, hyphens between words, no underscores or camelCase.
4. **Every file must cite at least one Source ID** from `SOURCES.md` in its `**Source IDs:**` field. If the source you need is missing, add it to `SOURCES.md` first.
5. **Every file must include a `## Machine-Readable` JSON block.** The block's `id` must match the filename (without `.md`).
6. **No implementation code.** No backtest scripts, no indicator code, no broker logic. This library is definitions and citations only.
7. **No cross-references to other personal projects.** This library does not link to `proof-app`, `trading-ai-v2`, `A3 Lab`, etc.

## Required Top-Matter Fields

Every concept file MUST have:

- `**Category:**`
- `**Aliases:**`
- `**ICT Confidence:**` — `high | medium | community-attributed | disputed | demo-stage`
- `**Year Introduced:**` — `YYYY`
- `**Year Refined:**` — `YYYY` (same as introduced if never refined)
- `**Source IDs:**` — comma-separated SOURCES.md IDs
- `**Tags:**`

Missing any of these → file is incomplete.

## Confidence Field Guide

- `high` — ICT-original, taught publicly, well-documented. Default for foundational 2016–2022 concepts.
- `medium` — ICT-attributable but sourced from limited / paywalled material; cite cautiously.
- `community-attributed` — non-ICT origin (CRT by Romeo, SMC community language). Must include `## ICT vs Community` section.
- `disputed` — origin contested between ICT and community. Cite both candidates.
- `demo-stage` — concept demonstrated by ICT but not yet taught (e.g. Zircon 2026). Re-evaluate quarterly.

## When Adding a New File

1. Copy `TEMPLATE.md` into the right `concepts/NN-<dir>/` directory with kebab-case name.
2. Fill all top-matter fields.
3. Write the `## Definition`, `## Formal Criteria`, `## Formula / Math`, and `## Machine-Readable` sections — these are mandatory.
4. Write `## Visual Pattern`, `## Timeframes`, `## Examples`, `## Common Mistakes`, `## Related Concepts`, `## Citations` sections — also mandatory.
5. Add `## ICT vs Community` ONLY if confidence is `community-attributed` or `disputed`.
6. Update `INDEX.md` — add a one-line entry under the right section.
7. Update `TIMELINE.md` — add the concept under its `Year Introduced` heading.
8. If the concept introduces a new abbreviation, update `GLOSSARY.md`.
9. Run the verification checks listed in the build plan before committing.

## When Editing an Existing File

- Update `**Year Refined:**` if the change reflects new ICT material.
- Update the `year_refined` field in the JSON `## Machine-Readable` block to match.
- Append to `## Citations` rather than replacing.
- If the concept is renamed, leave a stub at the old filename pointing to the new file (and document the rename in `99-glossary/terminology-evolution.md`).

## Style

- No marketing language. No "powerful," "game-changing," "elite," etc.
- No first-person. The library is descriptive, not promotional.
- Quote ICT directly when possible; paraphrase faithfully when not.
- ASCII for visual patterns is preferred over describing pictures we can't include.
- Keep formulas precise. State variables explicitly. Use inequalities, not prose, where possible.

## What This Library Is NOT

- Not a trading course.
- Not an opinion piece on what works.
- Not a backtest record.
- Not a recommendation. ICT teaches a discretionary framework; nothing here is investment advice.

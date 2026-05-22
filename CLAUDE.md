# ICT Knowledge Library: LLM Wiki

**Mode:** adapted (not a canonical wiki-skill scaffold — see "Layout deviation" below)
**Purpose:** Canonical, machine-readable reference of every Inner Circle Trader concept (2016-2026) — LLM-maintainable knowledge base and RAG corpus.
**Owner:** Priyanshu Goyal (SrsBlack)
**Created:** 2026-05-21 (CLAUDE.md added; vault content predates this file)

---

## Read this first

The canonical schema for this vault lives in **[AGENTS.md](AGENTS.md)**. It documents file format, the 10 required sections, the 7 required top-matter fields, the SOURCES.md ID convention, and the full ingest / query / lint operations.

This `CLAUDE.md` exists only to:
1. Map the vault to the `wiki` skill's operations vocabulary.
2. Document the deliberate layout deviation from the canonical wiki-skill scaffold.
3. Provide the hot-cache location and cross-project referencing block.

Read `AGENTS.md` for everything else.

---

## Layout deviation

The `wiki` skill assumes this layout:

```
vault/
├── .raw/
├── wiki/
│   ├── index.md, log.md, hot.md, overview.md
│   ├── sources/, entities/, concepts/, domains/, comparisons/, questions/, meta/
└── CLAUDE.md
```

This vault uses a flatter, domain-specific layout instead:

```
ict-knowledge-library/
├── README.md, AGENTS.md, CLAUDE.md, CONTRIBUTING.md, TEMPLATE.md
├── INDEX.md          ← maps to wiki/index.md
├── log.md            ← maps to wiki/log.md
├── GLOSSARY.md       ← abbreviations
├── TIMELINE.md       ← chronological 2016-2026 view
├── READING-ORDER.md  ← learning tracks
├── SOURCES.md        ← citation registry (stable IDs)
├── CHANGELOG.md      ← phase-by-phase build log
├── concepts/         ← maps to wiki/concepts/
│   ├── 01-market-structure/
│   ├── 02-liquidity/
│   ├── ... 33 numbered domain folders, 226 concept files total
└── meta/
    ├── lint-report-YYYY-MM-DD.md
    └── hot.md        ← maps to wiki/hot.md (hot cache, ~500 words)
```

Reasons for the deviation:
- Pre-existing convention: the vault was scaffolded around the Karpathy LLM-Wiki pattern with kebab-case files in numbered domain folders before the `wiki` skill existed.
- Markdown relative links (`[text](../foo/bar.md)`), not Obsidian `[[wikilinks]]`. Concept files are intentionally portable outside Obsidian.
- Bold-key header metadata (`**Category:** ...`), not YAML frontmatter. Matches existing TEMPLATE.md.
- Single-purpose vault (ICT methodology only). No entities/, domains/, comparisons/, or questions/ folders are needed; disambiguation lives in `concepts/NN/<a>-vs-<b>.md` files.

When the `wiki` skill expects `wiki/index.md`, read `INDEX.md`. When it expects `wiki/log.md`, read `log.md`. When it expects `wiki/hot.md`, read `meta/hot.md`.

---

## Operations map (wiki skill → this vault)

| Wiki skill says            | Do here                                                                                |
|----------------------------|----------------------------------------------------------------------------------------|
| ingest a source            | follow `AGENTS.md` → Operations → Ingest. Steps 1-9.                                   |
| query the wiki             | follow `AGENTS.md` → Operations → Query. Read `INDEX.md` first, then drill in.         |
| lint the wiki              | follow `AGENTS.md` → Operations → Lint. Write report to `meta/lint-report-YYYY-MM-DD.md`. |
| save (file the answer)     | append to relevant concept file, or create a new one under `concepts/NN-<dir>/`.       |
| update hot cache           | rewrite `meta/hot.md` (overwrite, do not append). ~500 words.                          |
| update index               | edit `INDEX.md` in the correct domain section.                                         |
| append to log              | top-of-file in `log.md`, format `## [YYYY-MM-DD] <op> | <title>`.                       |

---

## Conventions

- All concept files live under `concepts/NN-topic/<slug>.md`.
- Filenames are `kebab-case.md`. The JSON block's `id` MUST match the filename.
- 7 required top-matter fields (bold-key, not YAML): `Category`, `Aliases`, `ICT Confidence`, `Year Introduced`, `Year Refined`, `Source IDs`, `Tags`.
- 10 required sections; see `TEMPLATE.md`.
- Links are markdown relative: `[label](../06-fair-value-gaps/fair-value-gap.md)`.
- All times are NY time. See `concepts/04-time-cycles/dst-handling.md`.
- Stable Source IDs are append-only. Never renumber `SOURCES.md`.
- `log.md` is append-only and newest-first.
- `meta/lint-report-*.md` files are one-per-run; do not edit prior reports.

For the full set of rules including ingest, query, lint procedures, see `AGENTS.md`.

---

## Cross-project referencing

Other Claude Code projects that need ICT context can read from this vault without duplicating it. In another project's `CLAUDE.md`:

```markdown
## ICT Knowledge Library
Path: C:/Users/User/ict-knowledge-library

When you need ICT methodology context:
1. Read meta/hot.md first (recent context, ~500 words).
2. If not enough, read INDEX.md (full catalog of 226 concepts).
3. For a specific topic, read the relevant concepts/NN-topic/_<slug>_.md file.
4. For chronological context, read TIMELINE.md.
5. For acronyms (BSL, FVG, OB, MSS, etc.), read GLOSSARY.md.

Do NOT read this vault for:
- General trading or coding questions unrelated to ICT.
- Strategy backtests or broker integration (the vault is definitional only).
- Personal trading advice (the vault is neutral reference, not opinion).
```

Approximate token costs: `meta/hot.md` ≈ 500 tokens. `INDEX.md` ≈ 4,000 tokens. One concept file ≈ 800-1,500 tokens.

---

## Quick recipes

- **"Ingest this new 2026 source"** → AGENTS.md → Ingest, steps 1-9. Don't forget `log.md` and `meta/hot.md` updates.
- **"What does ICT say about X?"** → AGENTS.md → Query, steps 1-5. Cite concept files inline.
- **"Lint the wiki"** → AGENTS.md → Lint, plus the dedicated `wiki-lint` skill. Write to `meta/lint-report-YYYY-MM-DD.md`.
- **"Set up Obsidian to view this"** → vault already has `.obsidian/` config; open the folder as a vault in Obsidian.

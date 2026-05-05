# ICT Knowledge Library (2016–2026)

A canonical, machine-readable reference of every Inner Circle Trader (ICT) concept, strategy, and named model published between **2016 and 2026** — designed as a persistent, LLM-maintainable wiki rather than a one-shot document.

**226 concept files** across 33 directories. Each concept lives in its own self-contained markdown file with a stable name, definition, formal criteria, formula, visual, examples, common mistakes, related-concepts cross-links, and source citations. Every file ships with a machine-readable JSON block so the library can be consumed by RAG / agent systems deterministically.

## Karpathy LLM Wiki pattern

This library implements [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a structured, interlinked collection of markdown files maintained by an LLM agent rather than re-derived on every query. The three layers Karpathy describes:

- **Raw sources** — ICT mentorship videos, X threads, public commentary. Cited by stable Source IDs in [`SOURCES.md`](SOURCES.md).
- **The wiki** — the 226 concept files in [`concepts/`](concepts/). LLM-maintained.
- **The schema** — [`AGENTS.md`](AGENTS.md), which tells the LLM how to ingest new sources, answer queries, and lint the wiki for this domain.

Two index files navigate the wiki:

- [`INDEX.md`](INDEX.md) — content-oriented catalog, organized by concept directory.
- [`log.md`](log.md) — chronological event log of activity on the wiki.

To work on this wiki with an LLM, hand it [`AGENTS.md`](AGENTS.md) — that's the operating manual.

## What's in here

```
concepts/
  01-market-structure/        12 files   swing points, BOS, CHoCH, MSS
  02-liquidity/               14 files   BSL, SSL, EQH/EQL, sweeps, IRL/ERL, DOL
  03-order-flow/               6 files   institutional flow, APD, smart-money footprint
  04-time-cycles/             10 files   90-min cycle, macros, QT, DST, TOD pivots
  05-pd-arrays/                9 files   premium/discount arrays, hierarchy, nesting
  06-fair-value-gaps/         14 files   FVG, IFVG, BPR, CE, immediate/delayed, nested
  07-order-blocks/            10 files   bullish/bearish OB, breakers, propulsion
  08-breaker-blocks/           6 files   breaker, mitigation block, failed breaker
  09-displacement/             6 files   displacement criteria, gap classification
  10-killzones/                8 files   five canonical killzones in NY time
  11-silver-bullet/            7 files   3 SB windows, rules, 2025 refinement
  12-power-of-three/           6 files   PO3 / AMD doctrine
  13-judas-swing/              4 files   judas swing variants + failure
  14-asian-range/              6 files   Asian range, sweep, projections
  15-sessions/                 9 files   Asia, London, NY AM/PM, London Close
  16-smt-divergence/           5 files   SMT, correlated pairs, indices
  17-optimal-trade-entry/      6 files   OTE 0.62 / 0.705 / 0.79
  18-mitigation/               5 files   mitigation states across structure types
  19-rejection-blocks/         3 files   wick rejection blocks
  20-turtle-soup/              4 files   turtle soup, stop hunts
  21-crt/                      4 files   Candle Range Theory (community-attributed)
  22-quarterly-theory/         9 files   QT fractal: yearly → 90-min
  23-ipda/                     6 files   IPDA + 20/40/60-day lookbacks
  24-amd-cycle/                4 files   AMD cycle as time construct
  25-htf-bias/                 7 files   monthly/weekly/daily bias + framework
  26-imbalance/                5 files   imbalance / inefficiency umbrella
  27-equilibrium/              4 files   equilibrium, mean threshold
  28-fibonacci-levels/         7 files   ICT fib set + SD projections
  29-stop-runs/                4 files   stop run + entry variants
  30-news-driven/              5 files   FOMC two-stage, NFP, CPI, blackout
  31-models/                  14 files   ICT 2022/2023/2024 + Unicorn + B&B + Diamond + Venom + Zircon + NDOG/NWOG
  32-risk-management/          7 files   R-multiple, sizing, structural SL, partials
  99-glossary/                  —        deferred (single-page GLOSSARY.md supersedes)
```

Era coverage:

- 2016: foundational mentorship (55 files)
- 2017: charter year refinements (74 files)
- 2018: block taxonomy + IFVG + IPDA (39 files)
- 2021–2024: models era (52 files combined)
- 2025–2026: Venom, Zircon (demo-stage), 2-stage FOMC, static drawdown (6 files)

## Scope

This is a **definitional library**. It does not contain:

- Trading algorithms or backtests
- Live market data feeds
- Broker integrations
- Performance results
- Personal opinions on what "works"

Those belong in separate trading projects. The library's value is precision and consistency — describe the framework neutrally, let the reader form their own conclusions.

## File format

Every concept file follows [`TEMPLATE.md`](TEMPLATE.md): 7 required top-matter fields (`Category`, `Aliases`, `ICT Confidence`, `Year Introduced`, `Year Refined`, `Source IDs`, `Tags`) and 10 required sections (`## Definition` through `## Citations`), plus a machine-readable JSON block whose `id` matches the filename.

`ICT Confidence` is one of: `high` (ICT-original, well-documented), `medium` (limited public sourcing), `community-attributed` (e.g. CRT by Romeo), `disputed` (contested origin), `demo-stage` (e.g. Zircon Jan 2026 silent demo).

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the hard rules.

## Naming convention

Files: `kebab-case.md` (e.g. `bullish-order-block.md`, `ny-am-killzone.md`). One concept per file — no exceptions. If something feels like "two concepts in one file," split it.

## How to use this

**As a human reader:** start with [`READING-ORDER.md`](READING-ORDER.md) — three learning tracks (Beginner / Intermediate / Advanced). Or jump from [`INDEX.md`](INDEX.md) to whichever concept you need.

**As an LLM agent:** read [`AGENTS.md`](AGENTS.md) for the schema and ingest/query/lint workflow. Read [`INDEX.md`](INDEX.md) first when answering queries; drill into specific concept files; cite by filename. Use [`SOURCES.md`](SOURCES.md) IDs when adding new content.

**For RAG / programmatic consumption:** every concept file has a `## Machine-Readable` JSON block with `id`, `category`, `aliases`, `criteria`, `timeframes`, `confidence`, `year_introduced`, `year_refined`, `related[]`, `sources[]`. Parse the JSON for deterministic queries; render the markdown for human-friendly output.

## Status

**Content-complete and audit-passed.** 226 files, 33 directories, all validation checks pass:

- 10/10 required sections per file
- Every JSON block parses; every `id` matches filename
- Zero broken cross-links
- Zero orphan source citations (43 stable IDs in [`SOURCES.md`](SOURCES.md))
- INDEX.md and TIMELINE.md fully aligned with disk

See [`CHANGELOG.md`](CHANGELOG.md) for the phase-by-phase build log and [`log.md`](log.md) for the chronological event log.

## License

(none yet — TBD)

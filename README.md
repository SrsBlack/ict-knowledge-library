# ICT Knowledge Library (2016–2026)

A readable, LLM-friendly reference of every Inner Circle Trader (ICT) concept, strategy, and model published between **2016 and 2026**.

## Purpose

- A canonical, searchable, machine-readable knowledge base for all ICT concepts.
- Each concept lives in **one self-contained markdown file** with a stable name, definition, formula/criteria, examples, and citations.
- Designed to be consumed by LLMs (RAG) and humans alike — no implementation code, just knowledge.

## Scope

Pure documentation. This repository does NOT contain:
- Trading algorithms or backtests
- Live market data feeds
- Broker integrations
- Performance results

Those belong in separate trading projects. **Do not mix them in here.**

## Structure

```
concepts/
  01-market-structure/        BOS, CHoCH, MSS, swing points
  02-liquidity/               BSL, SSL, EQH, EQL, liquidity pools
  03-order-flow/              institutional order flow concepts
  04-time-cycles/             session times, macro times
  05-pd-arrays/               premium / discount arrays
  06-fair-value-gaps/         FVG, IFVG, BPR, balanced range
  07-order-blocks/            bullish/bearish OB, mitigated OB
  08-breaker-blocks/          breakers, mitigation blocks
  09-displacement/            displacement, gap classification
  10-killzones/               London / NY / Asia kill zones
  11-silver-bullet/           SB strategy + variants
  12-power-of-three/          AMD: accumulation, manipulation, distribution
  13-judas-swing/             Judas swing entries
  14-asian-range/             Asian session range, sweep
  15-sessions/                London / NY / Asia / lunch
  16-smt-divergence/          Smart Money Technique divergence
  17-optimal-trade-entry/     OTE, fib zones
  18-mitigation/              mitigation logic and blocks
  19-rejection-blocks/        rejection block patterns
  20-turtle-soup/             turtle soup, false breakouts
  21-crt/                     Candle Range Theory
  22-quarterly-theory/        quarterly cycles, Q1-Q4
  23-ipda/                    Interbank Price Delivery Algorithm
  24-amd-cycle/               accumulation-manipulation-distribution
  25-htf-bias/                higher-time-frame bias models
  26-imbalance/               imbalance, inefficiency
  27-equilibrium/             equilibrium, mean-of-range
  28-fibonacci-levels/        ICT-specific fib levels (.62, .705, .79, etc)
  29-stop-runs/               stop hunts, runs on liquidity
  30-news-driven/             high-impact news handling
  31-models/                  named models (2022, 2023, 2024 model)
  32-risk-management/         position sizing, R-multiples
  99-glossary/                terms, abbreviations
```

## File Format

Every concept file follows this template:

```markdown
# <Concept Name>

**Category:** <directory>
**Aliases:** <other names>
**First Documented:** <year, source if known>
**Tags:** <keywords>

## Definition

<one-paragraph plain-English definition>

## Formal Criteria

<bullet list of strict, testable conditions>

## Formula / Math

<exact formula, ranges, or quantitative criteria>

## Visual Pattern

<ASCII or description of how it appears on chart>

## Timeframes

<which TFs it applies to>

## Examples

<labeled examples with conditions>

## Common Mistakes

<misidentifications and edge cases>

## Related Concepts

<links to other files in this library>

## Citations

<source: ICT video, mentorship year, tweet, etc.>
```

## Naming Convention

Files: `kebab-case.md` (e.g. `bullish-order-block.md`, `ny-am-killzone.md`).

One concept per file. No exceptions. If something feels like "two concepts in one file," split it.

## Status

Initial scaffold. Concepts will be added file-by-file. See `INDEX.md` for current coverage.

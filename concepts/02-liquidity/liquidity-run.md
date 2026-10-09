# Liquidity Run

**Category:** 02-liquidity
**Aliases:** run on liquidity
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY-RUNS, ICT-2016-LIQUIDITY-POOLS, ICT-2016-REINFORCING-LIQUIDITY, ICT-2022-MENTORSHIP-EP23, ICT-2022-MENTORSHIP-EP35, ICT-2022-MENTORSHIP-EP02
**Tags:** liquidity, run, sweep, foundational

> ⚠ **Rewritten 2026-10-08.** This page previously defined a run as the broader sequence containing a sweep, with "run-and-reverse" as one branch. That is **contradicted** by ICT: he uses *run* and *sweep* as **alternative outcomes**, not a superset/subset pair — a sweep reverses, a run doesn't look back. "Run-and-reverse" and "run-and-continue" are **0 hits** in both corpora (153 2016-17/2020-21 packets, 40 captioned 2022 episodes) and should not be read as ICT vocabulary. The page previously cited only placeholder sources (`ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`) and dated the term 2017; the term is the title of a September 2016 lecture.

## Definition

A liquidity run is price **driving through** a pool and **continuing** — the opposite resolution to a [liquidity-sweep](liquidity-sweep.md), not a container for it. ICT, contrasting the two directly: "the vocabulary I'm using here is running the Tuesday high, not sweeping the Tuesday high. The difference between sweeping would be… a real shallow little run above that red line… running Tuesday's high means it runs right over top of it and it just doesn't look back" (`ICT-2022-MENTORSHIP-EP23`, 04:20–05:16); "if I'm saying we're going to run an old high for relative equal highs, that means we're going to run through it and continue" (EP23, 05:39). ICT's own **2016-origin taxonomy** classifies runs by how much opposing structure stands between price and the target, not by whether the move reverses afterward — see Formal Criteria.

## Formal Criteria

ICT's taxonomy (September 2016, *Liquidity Runs* lecture) splits runs by **resistance**, i.e. how much intervening structure stands in the way:

- **High resistance liquidity run** — a stack of old highs/lows stands between price and the target pool; "the least probable trading condition to look for longs"; usually only breaks on a sharp catalyst such as NFP or FOMC, or a black-swan event (`ICT-2016-LIQUIDITY-RUNS`, 07:33–10:20).
- **Low resistance liquidity run** — the region opened by a one-way expansion, with little intervening structure; "it's like a hot knife through butter" (`ICT-2016-LIQUIDITY-RUNS`, 19:33).
- The two are duals of the same chart: a high resistance run toward one side becomes a low resistance run back toward the other once it resolves (`ICT-2016-LIQUIDITY-RUNS`, 20:15).
- **HTF-sync rule** (December 2016): a run is framed low resistance when it's aligned with the higher-timeframe draw — "every time a run above an old high is expected, that's going to be framed as a low resistance liquidity run" (`ICT-2016-REINFORCING-LIQUIDITY`, 12:35–12:41).

ICT gives no "with or without close beyond" criterion, and no bar-count window, for where a run begins or ends — that formula is not in the corpus.

## Formula / Math

ICT gives no inequality-based formula for a run. The only quantitative content is the resistance classification above, which is structural (count of intervening highs/lows), not a price or bar-count threshold.

## Machine-Readable

```json
{
  "id": "liquidity-run",
  "category": "02-liquidity",
  "aliases": ["run-on-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "price_drives_through_pool_and_continues == true (the alternative to a sweep, not its superset)"},
    {"id": "c2", "expr": "classification: high_resistance (stacked opposing structure) vs low_resistance (little opposing structure)"},
    {"id": "c3", "expr": "low_resistance_if_aligned_with_HTF_draw == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["liquidity-sweep","liquidity-pool","draw-on-liquidity","stop-run-definition","judas-swing"],
  "sources": ["ICT-2016-LIQUIDITY-RUNS","ICT-2016-LIQUIDITY-POOLS","ICT-2016-REINFORCING-LIQUIDITY","ICT-2022-MENTORSHIP-EP23","ICT-2022-MENTORSHIP-EP35","ICT-2022-MENTORSHIP-EP02"]
}
```

## Visual Pattern

```
  High resistance run                 Low resistance run

   old high  ─█─  stacked            old high
   old high  ─█─  structure          ────────  (little structure
   old high  ─█─  slows the run                 between here and
       ↑                                         the target pool)
   approach                          ──────────────→  runs straight
                                        "like a hot knife through butter"
```

## Timeframes

Same as sweep. Most actionable on M5–H4; the resistance classification is read relative to whichever higher timeframe bias is in play.

## Examples

**Example 1 — low resistance run through BSL:**
- London opens, rallies toward an old high with no stacked structure in the way and HTF bias agrees.
- Price runs straight through with little hesitation — "it runs right over top of it and it just doesn't look back" (EP23, 05:16).
- → low resistance liquidity run.

**Example 2 — high resistance run:**
- A stack of old highs sits between current price and the target pool, with no catalyst scheduled.
- ICT: "this is the least probable trading condition to look for longs" (`ICT-2016-LIQUIDITY-RUNS`, 07:58).
- → high resistance liquidity run; not favored for entries.

## Common Mistakes

- **Treating a sweep-then-reversal as a "run."** In ICT's own vocabulary that is a *sweep*; *run* is reserved for the continuation case. A library or engine that labels a reversed sweep a "run-and-reverse" is using inverted terminology.
- **Classifying resistance by candle count instead of structure.** ICT's high/low-resistance split is about how much opposing swing structure stands in the way, not a bar-count or percentage rule.
- **Ignoring HTF alignment.** The same chart distance can be high resistance against the HTF draw and low resistance with it.

## Related Concepts

- [liquidity-sweep](liquidity-sweep.md) — the alternative resolution (reversal), not a subset of a run.
- [liquidity-pool](liquidity-pool.md) — what gets run.
- [draw-on-liquidity](draw-on-liquidity.md) — pool selection that drives runs.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — overlapping concept.
- [judas-swing](../13-judas-swing/judas-swing.md) — a session-open pattern built on either a run or a sweep.

## Citations

- `ICT-2016-LIQUIDITY-RUNS` (07:33, 07:58) "we view this as a high resistance liquidity run… this is the least probable trading condition to look for longs"; (08:31, 10:20) only a sharp catalyst or black-swan event reliably breaks a defended level; (11:25) "a low resistance liquidity run would be in the form of something similar to this"; (19:33) "it's like a hot knife through butter"; (17:42) "this run from this high, taking out these lows, is referred to as a low resistance liquidity run"; (20:15) the two are duals of the same chart.
- `ICT-2016-LIQUIDITY-POOLS` (08:58) "we are going to sell short in the form of a run on liquidity or a liquidity pool."
- `ICT-2016-REINFORCING-LIQUIDITY` (12:35–12:41) "every time a run above an old high is expected, that's going to be framed as a low resistance liquidity run."
- `ICT-2022-MENTORSHIP-EP23` (04:20–05:16) sweep-vs-run vocabulary; (05:39) "if I'm saying we're going to run an old high for relative equal highs, that means we're going to run through it and continue."
- `ICT-2022-MENTORSHIP-EP35` (11:44) "that's a high resistance liquidity run — not that it can't happen, but it's likely to not form."
- `ICT-2022-MENTORSHIP-EP02` (42:53) "what you're looking for is a run on liquidity — buy stops or sell stops."

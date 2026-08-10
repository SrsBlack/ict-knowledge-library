# Stop Run — Definition

**Category:** 29-stop-runs
**Aliases:** stop-run, stop hunt, stop sweep, run on stops
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-TIMEFRAME-SELECTION
**Tags:** stop-run, foundational

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2017`,
which matched neither cited source (`ICT-2016-LIQUIDITY`, 2016, and
`ICT-2022-MENTORSHIP-OVERVIEW`, 2022 — both build-time placeholders). The term is in use in
the **Month 1** (September 2016) lecture *Equilibrium Vs. Discount* — "we come all the way
back down and take out a stop; **stop runs** is what's going to be a different profile"
(`ICT-2016-EQUILIBRIUM-DISCOUNT`, 32:12–32:17) and "that means **a stop run**, like we
defined here and here, where the market went lower than a previous low… and then you
anticipate the market to expand to the upside" (45:08–45:18). By **Month 03** (November
2016) it is one of ICT's three named setups and is equated with turtle soup outright:
"there's stop runs, which we classically call the turtle soup, which is a false breakout"
(`ICT-2016-TIMEFRAME-SELECTION`, 40:00). Re-dated to **2016**. ⚠ `Year Refined: 2022` is
retained but remains **uncited**.

## Definition

A **stop run** is the algorithmic action of **deliberately moving price to take out resting stops** beyond a known liquidity level. Stop runs are how the algorithm fills institutional positions: by triggering retail breakout entries and stopping out resting positions, the algorithm gathers the counter-flow needed to fill in size. Stop runs are the **mechanism**; the resulting price patterns are [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [turtle-soup](../20-turtle-soup/turtle-soup.md), or run-and-continue. The "stop run" framing emphasizes the **intent**: it's a deliberate hunt, not a random move.

## Formal Criteria

A stop run consists of:

- An identifiable cluster of resting stops above (BSL) or below (SSL) a known structural level.
- A directional approach phase toward the cluster.
- A take event — wick or close through the level.
- Resolution: reversal (Turtle Soup outcome) or continuation (run-and-continue).

The resolution determines the trading interpretation but the stop-run mechanic itself is shared.

## Formula / Math

```
stop_run(level):
    approach: price moves toward level
    take_event: wick/close through level
    resolution:
      if reversal_after_take: turtle_soup outcome
      else: run_and_continue outcome

intent = "deliberate algorithmic move targeting stops"
```

## Machine-Readable

```json
{
  "id": "stop-run-definition",
  "category": "29-stop-runs",
  "aliases": ["stop-run", "stop-hunt", "stop-sweep", "run-on-stops"],
  "criteria": [
    {"id": "c1", "expr": "resting stops at known level"},
    {"id": "c2", "expr": "price approach + take event"},
    {"id": "c3", "expr": "intent is algorithmic, not random"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["stop-run-into-fvg","stop-run-into-ob","stop-run-into-breaker","liquidity-sweep","liquidity-run","turtle-soup","stop-hunt-pattern","judas-swing"],
  "sources": ["ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-TIMEFRAME-SELECTION"]
}
```

## Visual Pattern

```
   stop run + Turtle Soup outcome:           stop run + continuation:

        █  ← takes stops then reverses               █
        █                                            █  ← takes stops, continues
   ─────█──── stop level                       ──────█──── stop level
                                                     █
        ▲▲▲ rally                                    █  with displacement
                                                     █
```

## Timeframes

All TFs.

## Examples

**Example 1 — stop run + Turtle Soup outcome at SSL:**
- PDL = 1.0850.
- M15 wicks 1.0844, closes 1.0858.
- → stop run + Turtle Soup. Bullish setup follows.

## Common Mistakes

- **Stop run = guaranteed reversal.** Continuation is real and frequent.
- **Skipping the structural-level check.** Random wicks aren't stop runs; the level must contain known stops (swing high/low, EQH/EQL, session extreme).

## Related Concepts

- [stop-run-into-fvg](stop-run-into-fvg.md), [stop-run-into-ob](stop-run-into-ob.md), [stop-run-into-breaker](stop-run-into-breaker.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [liquidity-run](../02-liquidity/liquidity-run.md), [turtle-soup](../20-turtle-soup/turtle-soup.md), [stop-hunt-pattern](../20-turtle-soup/stop-hunt-pattern.md), [judas-swing](../13-judas-swing/judas-swing.md).

## Citations

- `ICT-2016-EQUILIBRIUM-DISCOUNT` (32:12–32:17) "stop runs is what's going to be a different profile"; (45:08–45:18) "that means a stop run like we defined here and here where the market went lower than a previous low… and then you anticipate the market to expand to the upside"; (52:55–52:57) "it's a run on stops."
- `ICT-2016-TIMEFRAME-SELECTION` (39:36–40:06) the three setups ICT trades — optimal trade entry, order blocks, and "stop runs, which we classically call the turtle soup, which is a false breakout"; (42:22–42:43) the stop run needs a higher-timeframe reason; (47:25–47:41) "you can see the turtle soup run on stops — that's your pattern."

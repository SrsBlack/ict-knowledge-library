# Stop Run — Definition

**Category:** 29-stop-runs
**Aliases:** stop-run, stop hunt, stop sweep, run on stops
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** stop-run, foundational

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
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["stop-run-into-fvg","stop-run-into-ob","stop-run-into-breaker","liquidity-sweep","liquidity-run","turtle-soup","stop-hunt-pattern","judas-swing"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
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

- `ICT-2016-LIQUIDITY`, `ICT-2022-MENTORSHIP-OVERVIEW`.

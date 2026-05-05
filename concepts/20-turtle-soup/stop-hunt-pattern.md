# Stop Hunt Pattern

**Category:** 20-turtle-soup
**Aliases:** stop hunt, stop run pattern, liquidity grab pattern
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** stop-hunt, turtle-soup-related, foundational

## Definition

The **stop hunt pattern** is the broader umbrella for any price action that **deliberately targets resting stops** — a superset that includes Turtle Soup, liquidity sweeps, and Judas swings. The stop hunt emphasizes the **intent**: the algorithm is going for the stops, not pursuing fair-value delivery. ICT teaches the stop hunt as the dominant explanation for sudden, fast wicks against a recent trend — they're not "random spikes," they're engineered moves to fill institutional orders. The deeper file at [stop-run-definition](../29-stop-runs/stop-run-definition.md) covers the same phenomenon from the stop-runs directory.

## Formal Criteria

- Price approaches a known stop cluster (above swing high for buy stops; below swing low for sell stops).
- A fast move (often a single wide wick or 1–2 candle burst) takes the level.
- One of two outcomes:
  - **Stop hunt + reversal** = Turtle Soup outcome (price returns inside).
  - **Stop hunt + continuation** = run-and-continue (price keeps going, stops were fuel).
- Bias direction post-hunt determines which outcome occurred.

## Formula / Math

```
stop_hunt_pattern(level):
  approach_phase: price moves toward level
  hunt_event: high(n) > level (for BSL) OR low(n) < level (for SSL)
  resolution:
    if close returns inside within 3 bars: turtle_soup_outcome
    else: continuation_with_displacement
```

## Machine-Readable

```json
{
  "id": "stop-hunt-pattern",
  "category": "20-turtle-soup",
  "aliases": ["stop-hunt", "stop-run-pattern", "liquidity-grab-pattern"],
  "criteria": [
    {"id": "c1", "expr": "approach_to_known_stop_cluster"},
    {"id": "c2", "expr": "fast_move_takes_level"},
    {"id": "c3", "expr": "outcome: turtle_soup OR run_and_continue"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["turtle-soup","bullish-turtle-soup","bearish-turtle-soup","liquidity-sweep","liquidity-run","stop-run-definition","judas-swing"],
  "sources": ["ICT-2016-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   stop hunt outcomes:

   Turtle Soup (reversal):              Run-and-continue:

        █  ← spike + close back          █  ← spike
        █                                █
   ─────█── stop level                ───█── stop level
                                         █
        ▲▲▲ rally up                     █  ← continues through
                                         █  with displacement
```

## Timeframes

All TFs.

## Examples

**Example 1 — stop hunt with Turtle Soup outcome:**
- M15 PWL at 1.0850 has known sell stops below.
- 02:55 NY: M15 wicks 1.0843, closes 1.0858.
- → stop hunt + Turtle Soup. Long bias for the rest of London.

**Example 2 — stop hunt with run-and-continue:**
- M15 PWL at 1.0850, HTF bearish.
- 02:55 NY: M15 wicks 1.0843; next M15 closes 1.0838 (continuation through).
- → stop hunt was fuel for the bearish move, not a reversal trigger.

## Common Mistakes

- **Treating every stop hunt as a Turtle Soup.** Run-and-continue is real and frequent; require close-back-inside to confirm Turtle Soup.
- **Single-direction reading.** Stop hunts happen on both sides; check both BSL and SSL relative to current price.

## Related Concepts

- [turtle-soup](turtle-soup.md), [bullish-turtle-soup](bullish-turtle-soup.md), [bearish-turtle-soup](bearish-turtle-soup.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [liquidity-run](../02-liquidity/liquidity-run.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md), [judas-swing](../13-judas-swing/judas-swing.md).

## Citations

- `ICT-2016-LIQUIDITY`, `ICT-2022-MENTORSHIP-OVERVIEW`.

# Stop Run into Breaker

**Category:** 29-stop-runs
**Aliases:** stop run + breaker entry, breaker-anchored stop run
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2023
**Source IDs:** ICT-2018-BLOCKS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** stop-run, breaker, entry

## Definition

A "stop run into breaker" is the sequence where a stop run sweeps a level, and on the retest, an existing **breaker block** in the post-sweep direction provides the entry zone. Distinct from stop-run-into-FVG (FVG entry) and stop-run-into-OB (fresh OB entry), this variant uses a previously-formed breaker as the structural anchor. Often sees high conviction because the breaker has already validated the bias-flip context and the stop run confirms the algorithmic intent.

## Formal Criteria

The sequence:

1. A breaker block already exists from a prior CHoCH/MSS event.
2. **Stop run event** — wick takes a known structural level near the breaker zone.
3. **Displacement** in the breaker's polarity direction.
4. **Entry on breaker retest** (typically at the breaker zone's MT or relevant edge).
5. **SL beyond the swept extreme** or beyond the breaker's invalidation edge.

## Formula / Math

```
stop_run_into_breaker(setup):
    breaker_block_exists_from_prior_event
    AND sweep_at_or_near_breaker_zone
    AND displacement_in_breaker_direction
    AND entry on breaker retest
    AND SL beyond sweep / breaker invalidation
```

## Machine-Readable

```json
{
  "id": "stop-run-into-breaker",
  "category": "29-stop-runs",
  "aliases": ["stop-run-breaker-entry", "breaker-anchored-stop-run"],
  "criteria": [
    {"id": "c1", "expr": "breaker_block_already_exists"},
    {"id": "c2", "expr": "sweep_at_or_near_breaker"},
    {"id": "c3", "expr": "displacement_in_breaker_direction"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2023",
  "related": ["stop-run-definition","stop-run-into-fvg","stop-run-into-ob","breaker-block","bullish-breaker","bearish-breaker","liquidity-sweep","mitigation-of-breaker"],
  "sources": ["ICT-2018-BLOCKS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish stop run into bullish breaker:

   bullish breaker zone (originally bearish OB, flipped after CHoCH up)
   ─────────
        │
        ▼  ← stop run wick into / near breaker zone
        ╲╱
         ▲▲   ← bullish reaction at breaker
         ▲▲▲   displacement up
                       ↓
                       entry on breaker retest at MT
```

## Timeframes

M15+.

## Examples

**Example 1 — bullish stop run into bullish breaker:**
- Bullish breaker zone exists at 1.0945–1.0955 (originally bearish OB, flipped after CHoCH-up two days ago).
- 09:00 NY: M15 wicks 1.0942 (SSL just below breaker swept).
- 09:15 NY: M15 prints 22-pip green displacement, FVG up.
- 09:30 NY: M15 retraces into breaker zone at 1.0950 (MT).
- Long entry at 1.0950 with SL 1.0938 (below sweep + buffer); risk 12 pips.
- Targets: -1.5 SD or PWH BSL.

## Common Mistakes

- **Trading retest of failed breakers.** If the breaker has already failed once, a stop run into it is lower-conviction.
- **Confusing breaker with raw OB.** This variant specifically uses a flipped (breaker) zone, not a fresh OB.

## Related Concepts

- [stop-run-definition](stop-run-definition.md), [stop-run-into-fvg](stop-run-into-fvg.md), [stop-run-into-ob](stop-run-into-ob.md).
- [breaker-block](../08-breaker-blocks/breaker-block.md), [bullish-breaker](../08-breaker-blocks/bullish-breaker.md), [bearish-breaker](../08-breaker-blocks/bearish-breaker.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [mitigation-of-breaker](../18-mitigation/mitigation-of-breaker.md).

## Citations

- `ICT-2018-BLOCKS`, `ICT-2022-MENTORSHIP-OVERVIEW`.

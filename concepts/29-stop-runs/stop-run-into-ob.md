# Stop Run into OB

**Category:** 29-stop-runs
**Aliases:** stop run + OB entry, OB-anchored stop run
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** stop-run, ob, entry

## Definition

A "stop run into OB" is the variant where the post-sweep displacement creates an order block — the **last opposite-color candle before the displacement** — and the OB body becomes the precise entry zone. Stop-run-into-OB setups are entered at the OB's MT (mean threshold) on retest, with SL beyond the sweep extreme. Mechanically similar to [stop-run-into-fvg](stop-run-into-fvg.md) but uses the OB body instead of an FVG as the algorithmic anchor.

## Formal Criteria

The sequence:

1. **Stop run event** — wick takes a known structural level.
2. **Last opposite-color candle** — qualifies as an OB per [order-block-criteria](../07-order-blocks/order-block-criteria.md).
3. **Displacement** breaks structure (BOS or CHoCH/MSS).
4. **Entry on OB retest at MT**.
5. **SL beyond the sweep extreme** (typically below OB low for longs, above OB high for shorts, with buffer).

## Formula / Math

```
stop_run_into_ob(setup):
    sweep_event
    AND last_opposite_color_candle qualifies as OB
    AND displacement_breaks_structure
    AND entry at OB MT on retest
    AND SL beyond sweep + buffer
```

## Machine-Readable

```json
{
  "id": "stop-run-into-ob",
  "category": "29-stop-runs",
  "aliases": ["stop-run-OB-entry", "OB-anchored-stop-run"],
  "criteria": [
    {"id": "c1", "expr": "sweep + OB qualification + displacement + BOS"},
    {"id": "c2", "expr": "entry at OB MT"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["stop-run-definition","stop-run-into-fvg","stop-run-into-breaker","bullish-order-block","bearish-order-block","mean-threshold","liquidity-sweep"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish stop run into OB:

   ─── known SSL ─────
        │
        ▼  ← stop run wick
        ▼
        ▼   ← LAST bearish candle (this becomes the bullish OB)
            ▲▲▲   ← displacement up
           ▲▲▲▲   ← BOS through prior swing high
           ▲▲▲▲▲
                       ↓
                       retest to OB MT = entry
```

## Timeframes

M5–H4.

## Examples

**Example 1 — bullish stop run into OB:**
- HTF bullish; Asian SSL 1.0850.
- 02:55 NY: M15 wicks 1.0844; same M15 candle: O=1.0852, C=1.0848, L=1.0844, H=1.0855. Body [1.0848, 1.0852], MT 1.0850.
- 03:15 NY: next M15 = 22-pip green displacement, breaks prior M15 swing high (BOS).
- → bullish OB at 14:00 candle; on retest, entry at MT 1.0850; SL 1.0842 (sweep low - 2-pip buffer); risk 8 pips.

## Common Mistakes

- **Using a non-OB candle.** The candle must qualify per OB criteria (last opposite-color + displacement + structure-break).
- **Wide-range OBs.** OB body should be reasonably tight; wide OBs (large body, no clear MT) produce loose entries.

## Related Concepts

- [stop-run-definition](stop-run-definition.md), [stop-run-into-fvg](stop-run-into-fvg.md), [stop-run-into-breaker](stop-run-into-breaker.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.

# Symmetrical Price Projections

**Category:** 28-fibonacci-levels
**Aliases:** SPP, symmetrical projection, equal-distance projection, leg-mirror projection
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** projections, symmetry, targets

## Definition

Symmetrical Price Projection (SPP) is an ICT projection method where the **next leg is expected to mirror the previous leg's size**. After an OTE entry, the projection is: from the entry point, move by exactly the prior leg's distance in the new direction. SPP is a complement to standard-deviation projections — both target the same broad area but anchor differently. SPP is often the first tactical TP target (≈ 1× leg = approximately the same as -1.0 if you measured from leg_end).

## Formal Criteria

For a long entry after a bullish leg from `leg_start` to `leg_end`:

- Prior leg size = `leg_end - leg_start`.
- SPP target from entry = `entry_price + leg_size`.
- For shorts: symmetric in the opposite direction.

SPP is symmetric to the *reaction leg* — it assumes the next push will be the same magnitude as the move that produced the OTE setup.

## Formula / Math

```
leg_size = leg_end - leg_start

SPP_target_long  = entry_price + leg_size
SPP_target_short = entry_price - leg_size

# Bullish leg 1.0800 → 1.0900, OTE entry at 1.08295:
SPP_target = 1.08295 + 100 = 1.09295
```

## Machine-Readable

```json
{
  "id": "symmetrical-price-projections",
  "category": "28-fibonacci-levels",
  "aliases": ["SPP", "symmetrical-projection", "equal-distance-projection"],
  "criteria": [
    {"id": "c1", "expr": "target == entry +/- leg_size"},
    {"id": "c2", "expr": "anchored_to_prior_leg_size == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["ict-fib-overview","standard-deviation-projections","fib-705","ote-overview"],
  "sources": ["ICT-2017-OTE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
                                     ─── SPP target
                                              (= entry + leg_size)
   leg_end ────                               ↑
   ↑                                          ↑
   leg_size ──── retrace ──── entry ──── leg_size ────
   ↓                          (e.g. 0.705)
   leg_start ──── 0.0

   The next push is projected to mirror the prior leg's size.
```

## Timeframes

All TFs.

## Examples

**Example 1 — SPP TP with multiple targets:**
- Bullish leg 1.0800 → 1.0900 (100 pips).
- OTE entry at 1.0830 (0.705).
- SPP target = 1.0830 + 100 = 1.0930.
- Compare with SD projections: -1.5 SD = 1.1050.
- TP ladder: SPP (1.0930) as first take, -1.5 SD (1.1050) as extended target.

## Common Mistakes

- **Using SPP as the only projection.** ICT's standard practice is to combine SPP with SD projections and HTF DOL — multiple methods converging produces stronger targets.
- **Ignoring leg quality.** If the prior leg was a clean displacement, SPP works well; if the prior leg was choppy and overlapping, SPP is less reliable.
- **Symmetry strictness.** SPP is approximate — expect ±10–20% slippage; don't treat it as pixel-precise.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [standard-deviation-projections](standard-deviation-projections.md), [fib-705](fib-705.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.

> Confidence is `medium` because SPP is taught informally across the ICT community with naming variations; the underlying concept (equal-distance projection) is core to ICT but the specific "Symmetrical Price Projection" label varies.

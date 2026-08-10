# Symmetrical Price Projections

**Category:** 28-fibonacci-levels
**Aliases:** SPP, symmetrical projection, equal-distance projection, leg-mirror projection
**ICT Confidence:** medium
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-MMT-FALSE-BREAKOUT, ICT-2017-OTE
**Tags:** projections, symmetry, targets

## Definition

Symmetrical Price Projection (SPP) is an ICT projection method where the **next leg is expected to mirror the impulse leg's size**. ICT's own name for it is the **symmetrical price swing**, and he defines it as a 100% measured move of the impulse leg duplicated from the leg's own extreme: "what's a measured move — the impulse leg low to high, that move is the same thing just **added to the high** up; okay, so that's a perfectly symmetrical price swing" (`ICT-2017-OTE`, 14:03). On his OTE fib preset it is the **−1.0 level** — "and then negative one for a symmetrical price swing" (`ICT-2017-OTE`, 11:29). SPP is a complement to standard-deviation projections — both target the same broad area but anchor differently. It is the **most extended** rung of the OTE target ladder (old high → 127 extension → 162 extension → symmetrical price swing), not the first take.

⚠ **Dating and formula corrected 2026-08-10.** This page previously carried `Year Introduced: 2018`
sourced to `ICT-2017-OTE` and the placeholder `ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 02**
lecture *Market Maker Trap False Breakouts* (Oct 2016) already teaches equal-distance projection as
a delivery objective — "it's a measured move ... it gives you an approximation of where the
algorithm will reach for to offer price" [16:58] and "the second leg in price higher **is equal to
that first one**" [17:23], worked through to a projected 1.0980 that "was handsomely hit" [17:58].
Re-dated to 2016. **Separately, the anchor stated on this page was wrong**: it projected from the
*entry price*, and claimed that was "approximately the same as −1.0 measured from leg_end".
`ICT-2017-OTE` anchors the symmetrical price swing at the **leg extreme**, so with a 0.705 OTE entry
the two differ by 0.705 × leg_size — 70% of the leg, not a rounding difference. The formula,
criteria and worked example below have been corrected.

## Formal Criteria

For a long entry after a bullish impulse leg from `leg_start` to `leg_end`:

- Impulse leg size = `leg_end - leg_start`.
- SPP target = `leg_end + leg_size` — equivalently the `-1.0` level of a fib anchored `leg_start` → `leg_end`.
- For shorts: symmetric in the opposite direction.

SPP is symmetric to the *impulse leg* — it assumes the next push will be the same magnitude as the move that produced the OTE setup. The entry price does not enter the calculation; it only determines how much of the projected distance is captured as R.

## Formula / Math

```
leg_size = leg_end - leg_start

SPP_target_long  = leg_end + leg_size     # == fib -1.0 anchored leg_start -> leg_end
SPP_target_short = leg_end - leg_size

# Bullish leg 1.0800 → 1.0900, OTE entry at 1.08295:
SPP_target = 1.0900 + 100 pips = 1.1000
```

## Machine-Readable

```json
{
  "id": "symmetrical-price-projections",
  "category": "28-fibonacci-levels",
  "aliases": ["SPP", "symmetrical-projection", "equal-distance-projection"],
  "criteria": [
    {"id": "c1", "expr": "target == leg_end +/- leg_size"},
    {"id": "c2", "expr": "target == fib_level(-1.0, anchor_low=leg_start, anchor_high=leg_end)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["ict-fib-overview","standard-deviation-projections","fib-705","ote-overview"],
  "sources": ["ICT-2016-MMT-FALSE-BREAKOUT","ICT-2017-OTE"]
}
```

## Visual Pattern

```
                                     ─── SPP target  (fib -1.0)
                                              ↑        = leg_end + leg_size
                                              │
                                          leg_size
                                              │
   leg_end ──── 1.0 ───────────────────────── ┴ ────  old high, first scaling
   ↑                        ╲
   leg_size                  ╲── retrace ──── entry (e.g. 0.705)
   ↓
   leg_start ──── 0.0

   The next push is projected to mirror the impulse leg's size, measured
   from leg_end — NOT from the entry.
```

## Timeframes

All TFs.

## Examples

**Example 1 — SPP as the far rung of the TP ladder:**
- Bullish leg 1.0800 → 1.0900 (100 pips).
- OTE entry at 1.0830 (0.705).
- Ladder, in ICT's order: first scaling at/just under the old high 1.0900; 127 extension (fib -0.27) = 1.0927; 162 extension (fib -0.62) = 1.0962; **SPP (fib -1.0) = 1.0900 + 100 = 1.1000**.
- ICT leaves only "a small piece on for a measured move type effect" (`ICT-2017-OTE`, 14:40) — SPP is the runner's target, not the first take.

## Common Mistakes

- **Anchoring the projection at the entry.** The measured move is duplicated from `leg_end`, not from your fill. Anchoring at a 0.705 entry understates the target by ~70% of the leg.
- **Treating SPP as the first take.** It is the last rung; ICT's first scaling is at or just below the old high, precisely because the market may fail there (`ICT-2017-OTE`, 14:18).
- **Using SPP as the only projection.** ICT's standard practice is to combine SPP with SD projections and HTF DOL — multiple methods converging produces stronger targets.
- **Ignoring leg quality.** If the prior leg was a clean displacement, SPP works well; if the prior leg was choppy and overlapping, SPP is less reliable.
- **Symmetry strictness.** SPP is approximate — expect ±10–20% slippage; don't treat it as pixel-precise.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [standard-deviation-projections](standard-deviation-projections.md), [fib-705](fib-705.md), [ote-overview](../17-optimal-trade-entry/ote-overview.md).

## Citations

- `ICT-2016-MMT-FALSE-BREAKOUT` — earliest located teaching of equal-distance projection as a
  delivery objective: "it's a measured move ... it gives you an approximation of where the algorithm
  will reach for to offer price" [16:58]; "the second leg in price higher is equal to that first
  one" [17:23]; the projection carried to 1.0980 and hit [17:58].
- `ICT-2017-OTE` — the definition and the anchor: "the impulse leg low to high, that move is the
  same thing just added to the high up ... that's a perfectly symmetrical price swing" [14:03], and
  its place on the fib preset, "negative one for a symmetrical price swing" [11:29].

> Confidence is `medium` because SPP is taught informally across the ICT community with naming variations; the underlying concept (equal-distance projection) is core to ICT but the specific "Symmetrical Price Projection" label varies — ICT's own term is "symmetrical price swing".

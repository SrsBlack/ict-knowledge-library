# Symmetrical Price Projections

**Category:** 28-fibonacci-levels
**Aliases:** SPP, symmetrical projection, equal-distance projection, leg-mirror projection
**ICT Confidence:** medium
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-MMT-FALSE-BREAKOUT, ICT-2017-OTE, ICT-2017-STT-MM-TEMPLATES
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

**Continuation form** — for a long entry after a bullish impulse leg from `leg_start` to `leg_end`:

- Impulse leg size = `leg_end - leg_start`.
- SPP target = `leg_end + leg_size` — equivalently the `-1.0` level of a fib anchored `leg_start` → `leg_end`.
- For shorts: symmetric in the opposite direction.

SPP is symmetric to the *impulse leg* — it assumes the next push will be the same magnitude as the move that produced the OTE setup. The entry price does not enter the calculation; it only determines how much of the projected distance is captured as R.

**Reversal form (`ICT-2017-STT-MM-TEMPLATES`)** — where the measured swing is the *manipulation* leg into a weekly extreme rather than an impulse leg, ICT anchors the duplication at the swing's **origin**, so the projected leg mirrors the manipulation leg back through it:

- Bearish week, swing up from Tuesday's low `L` to Wednesday's high `H`, `R = H - L`. The **swing projection fulcrum** is that swing (21:38).
- 127 and 168 extensions are taken **from `H`**: "That range in terms of pips times that by 1.27 and that'll give you your range that you **subtract from Wednesday's high**" (31:17), and the same with 1.68 (31:32).
- The symmetrical swing is taken **from `L`**: "or perfect symmetrical price swing or that of Tuesday's low to Wednesday's high. That range **subtracted from Tuesday's low**. That would be a perfect symmetrical price swing" (21:43–21:55).
- Both anchors describe the same fib run `H → L` — 1.27 and 1.68 are the ordinary extensions, and the symmetrical swing is the `2.0` level of that run. It therefore sits **beyond** the 168, which is consistent with `ICT-2017-OTE` placing the symmetrical swing at the far end of the target ladder.
- In this module the level never stands alone: it must overlap an opposing PD array on a timeframe *lesser* than the entry array's — see [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md).

## Formula / Math

```
# CONTINUATION FORM (ICT-2017-OTE)
leg_size = leg_end - leg_start

SPP_target_long  = leg_end + leg_size     # == fib -1.0 anchored leg_start -> leg_end
SPP_target_short = leg_end - leg_size

# Bullish leg 1.0800 → 1.0900, OTE entry at 1.08295:
SPP_target = 1.0900 + 100 pips = 1.1000

# REVERSAL FORM (ICT-2017-STT-MM-TEMPLATES) — manipulation leg L -> H, projected down
R = H - L                                 # the swing projection fulcrum
ext_127 = H - 1.27 * R                    # "subtract from Wednesday's high"
ext_168 = H - 1.68 * R
SPP     = L - 1.00 * R                    # "that range subtracted from Tuesday's low"
        = H - 2.00 * R                    # i.e. the 2.0 level of the fib run H -> L

assert SPP < ext_168 < ext_127            # symmetrical swing is the FARTHEST rung
```

## Machine-Readable

```json
{
  "id": "symmetrical-price-projections",
  "category": "28-fibonacci-levels",
  "aliases": ["SPP", "symmetrical-projection", "equal-distance-projection"],
  "criteria": [
    {"id": "c1", "expr": "continuation form: target == leg_end +/- leg_size"},
    {"id": "c2", "expr": "continuation form: target == fib_level(-1.0, anchor_low=leg_start, anchor_high=leg_end)"},
    {"id": "c3", "expr": "reversal form: swing L->H, target == L - (H-L) == fib 2.0 of the run H->L"},
    {"id": "c4", "expr": "reversal form: 127 and 168 extensions are subtracted from H, the symmetrical swing from L"},
    {"id": "c5", "expr": "symmetrical swing is strictly farther than the 168 extension in both forms"},
    {"id": "c6", "expr": "in the 2017 short-term module the level must overlap a lesser-timeframe opposing PD array"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["ict-fib-overview","standard-deviation-projections","fib-705","ote-overview","market-maker-manipulation-template","one-shot-one-kill"],
  "sources": ["ICT-2016-MMT-FALSE-BREAKOUT","ICT-2017-OTE","ICT-2017-STT-MM-TEMPLATES"]
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
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the 2017 short-term module's use of the level, always paired with a lesser-timeframe PD array.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — the model that consumes the projection.

## Citations

- `ICT-2016-MMT-FALSE-BREAKOUT` — earliest located teaching of equal-distance projection as a
  delivery objective: "it's a measured move ... it gives you an approximation of where the algorithm
  will reach for to offer price" [16:58]; "the second leg in price higher is equal to that first
  one" [17:23]; the projection carried to 1.0980 and hit [17:58].
- `ICT-2017-OTE` — the definition and the anchor: "the impulse leg low to high, that move is the
  same thing just added to the high up ... that's a perfectly symmetrical price swing" [14:03], and
  its place on the fib preset, "negative one for a symmetrical price swing" [11:29].
- `ICT-2017-STT-MM-TEMPLATES` — the **reversal-anchored** form and the densest single use of the term
  in this corpus (17 mentions across the twelve weekly templates). "a 100% symmetrical price swing or
  what I classify as a perfect market structure swing" [03:46]; "preferably a perfect symmetrical
  price swing of 100%" [04:20]; "Basically, a 100% duplication or measured move of the price swing"
  [06:44]; the fulcrum — "Tuesdays low to Wednesday's high, that price swing up, that's what you're
  going to be anchoring your FIB on" [21:38]; the anchor split — "That range subtracted from Tuesday's
  low. That would be a perfect symmetrical price swing" [21:52–21:55] versus "times that by 1.27 and
  that'll give you your range that you subtract from Wednesday's high" [31:17] and 1.68 [31:32]; "The
  swing projection fulcrum is the highest high at which the market starts to retrace from" [27:33];
  and the standing confluence requirement — "We're not just simply looking for 127 and 168 extensions"
  [16:12].

> Confidence is `medium` because SPP is taught informally across the ICT community with naming variations; the underlying concept (equal-distance projection) is core to ICT but the specific "Symmetrical Price Projection" label varies — ICT's own term is "symmetrical price swing".

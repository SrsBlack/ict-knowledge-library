# Silver Bullet — Rules

**Category:** 11-silver-bullet
**Aliases:** SB rules, SB checklist, silver bullet criteria
**ICT Confidence:** disputed
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP20, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP25, ICT-2022-MENTORSHIP-EP40, ICT-2017-BREAD-BUTTER-SELL, ICT-2017-MEGA-BOND, ICT-2017-MEGA-STOCK
**Tags:** silver-bullet, rules, checklist

## Definition

The Silver Bullet rules, as commonly circulated, are an operational checklist for
taking an SB entry inside a 60-minute window. `ICT Confidence: disputed` — not because
the mechanics are wrong, but because the 60-minute-window "Silver Bullet" packaging
itself has no located source, and two of its items are contradicted by content this
library does have.

⚠ **Corpus status: no Silver Bullet teaching exists in either corpus searched for this
audit** (153 2016-17/2020-21 packets + the 41-episode 2022 YouTube mentorship).
`grep -c -i "silver bullet"` across both corpora: **5 hits in 4 files, all idiomatic** —
"They're not a silver bullet" (`ICT-2017-BREAD-BUTTER-SELL`, 19:18); "interest rate SMT
is going to be that little silver bullet" (`ICT-2017-MEGA-BOND`, 03:35); index SMT "is
the silver bullet" (`ICT-2017-MEGA-STOCK`, 25:15, 51:22); "not going to give you a
silver bullet that removes losing trades" (ep10 [28:38]) — none names a dedicated
Silver Bullet setup. Window searches for `10 and 11`, `3 and 4 a.m`, `2 and 3 p.m` near
Silver-Bullet-shaped language found only the London-close profit-taking statement
(`ICT-2022-MENTORSHIP-EP40`, 17:18) and "I want to try to be positioned before 11:00"
(ep05 [10:50]) — neither names a Silver Bullet. `ICT-2022-SILVER-BULLET` and
`ICT-2025-MACRO-PRECISION` are both **stub Source IDs** (registered in `SOURCES.md`
without an attached video). The named "Silver Bullet" setup is **late-2022/2023
YouTube material, outside this corpus** — the header's `Year Introduced: 2022` /
`Year Refined: 2025` rest on those two stub IDs and are themselves **unverified**, not
confirmed dates.

Per this library's handling of unverifiable content: the checklist below is kept
because it is a coherent restatement of mechanics taught elsewhere in the corpus
(killzones, sweeps, displacement, FVG), but **none of it should be read as a verified
ICT "Silver Bullet" teaching**, and two items are directly contradicted by the 2022
mentorship's closest analogous model (see Formal Criteria, items 6–7, and
[ict-2022-model](../31-models/ict-2022-model.md)).

## Formal Criteria — The commonly-circulated SB Checklist

1. **Inside one of three 60-minute windows** — 03:00–04:00 / 10:00–11:00 / 14:00–15:00 NY. `# ICT gives no number for these windows in this corpus.`
2. **HTF bias direction confirmed** — long SBs only on bullish bias; shorts on bearish. Consistent with [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), not SB-specific.
3. **Liquidity sweep occurred** — consistent with the 2022 model's sweep step: "look for periods where price runs above an old high then it breaks down" (`ICT-2022-MENTORSHIP-EP06`, 15:14).
4. **Displacement after sweep** — consistent with the 2022 model's MSS/displacement step (`ICT-2022-MENTORSHIP-EP24`, 33:30).
5. **FVG formed** in or after the displacement — consistent with 2022 FVG-after-MSS teaching (`ICT-2022-MENTORSHIP-EP25`, 32:46–33:13).
6. **Entry trigger: lower-TF MSS / FVG retest at CE** — ⚠ **CONTRADICTED by the closest 2022 analogue.** The 2022 model's entry is a **limit order at the FVG edge**, not the consequent encroachment (CE): "put your limit order in to sell short right at that price right there or plus one pip" (`ICT-2022-MENTORSHIP-EP18`, 32:47); "we're just going to use the actual candle high that would be your limit order entry" (`ICT-2022-MENTORSHIP-EP20`, 14:19). `consequent` has zero hits in the 2022 episodes; no 2025 source is in this corpus.
7. **SL beyond the swept liquidity pool** — ⚠ **CONTRADICTED.** The 2022 model places the stop **above the FVG candle or the swing high**, not beyond the swept pool: "where's your stop loss going to be above the high of candle number two or you can use above candle number one which creates a swing high" (`ICT-2022-MENTORSHIP-EP06`, 36:06).
8. **Targets defined** — at minimum first SD projection or HTF DOL; broadly consistent with the 2022 model's target step, though SD is only a how-far gauge there, not the primary target (see [ict-2022-model](../31-models/ict-2022-model.md)).

Items 6–7 above are **not** supported by this corpus as written and should not be treated as verified ICT rules.

## Formula / Math

```
# ICT gives no number for the three SB windows in this corpus.
sb_entry_unverified := in_claimed_sb_window        # unverified window
                        AND htf_bias_clear
                        AND sweep_just_occurred
                        AND displacement_after_sweep
                        AND fvg_formed
                        AND entry_at_fvg_edge_by_limit_order   # NOT "CE" — see item 6
                        AND sl_above_fvg_candle_or_swing_high  # NOT "beyond the sweep" — see item 7
                        AND targets_defined
```

## Machine-Readable

```json
{
  "id": "silver-bullet-rules",
  "category": "11-silver-bullet",
  "aliases": ["SB-rules", "SB-checklist"],
  "criteria": [
    {"id": "c1", "expr": "named 'Silver Bullet' teaching and its 3 windows: NOT IN CORPUS"},
    {"id": "c2", "expr": "entry trigger per 2022 model analogue: limit order at FVG edge, NOT CE"},
    {"id": "c3", "expr": "stop per 2022 model analogue: above FVG candle or swing high, NOT beyond the swept pool"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "disputed",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-london","silver-bullet-ny-am","silver-bullet-ny-pm","silver-bullet-failure-modes","htf-bias-framework","liquidity-sweep","displacement-definition","fair-value-gap","ict-2022-model"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP20","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP25","ICT-2022-MENTORSHIP-EP40","ICT-2017-BREAD-BUTTER-SELL","ICT-2017-MEGA-BOND","ICT-2017-MEGA-STOCK"]
}
```

## Visual Pattern

```
   Commonly-circulated SB checklist (bullish example) — UNVERIFIED packaging:

   ☐ Time inside 03-04 / 10-11 / 14-15 NY?    [no number in corpus]
   ☐ HTF bias bullish?                         [D / W check]
   ☐ Liquidity sweep occurred?
   ☐ Displacement candle after sweep?
   ☐ Bullish FVG inside or after displacement?
   ☐ Entry: LIMIT ORDER at the FVG edge        [NOT "CE retest" — contradicted]
   ☐ SL: above the FVG candle / swing high     [NOT "beyond the sweep" — contradicted]
   ☐ TP defined (SD projection / DOL)?
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — mechanics consistent with the 2022 model's analogue, not a verified "Silver Bullet":**
- 10:05 NY, inside a commonly-claimed window (unverified).
- HTF bullish.
- 09:55: M5 wicked sub-pre-NY-AM low, swept.
- 10:10: 18-pip green displacement.
- Bullish FVG at 1.0930–1.0934.
- Entry: limit order at the FVG edge (1.0930), not a CE retest.
- SL: above the displacement-leg swing high, not merely beyond the sweep low.
- TP: HTF liquidity target, SD as a how-far gauge only.

## Common Mistakes

- **Treating this page as a verified ICT "Silver Bullet" teaching.** It is not — see Corpus status above.
- **Citing the three 60-minute windows as ICT's numbers.** No clocked Silver Bullet window exists in this corpus.
- **Entering at CE.** The 2022 model's closest analogue enters by limit order at the FVG edge.
- **Stopping beyond the swept pool.** The 2022 model's closest analogue stops above the FVG candle or the swing high.
- **Requiring a fill inside the window.** Even for the killzones that are verified, ICT's own rule is: "You don't need to have your entry filled inside that kill zone window. Your order idea and your order placement need to be considered at that time" (`ICT-2022-MENTORSHIP-EP18`, 48:30).

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-london](silver-bullet-london.md), [silver-bullet-ny-am](silver-bullet-ny-am.md), [silver-bullet-ny-pm](silver-bullet-ny-pm.md), [silver-bullet-failure-modes](silver-bullet-failure-modes.md) — should carry this page's corpus-status caveat; not edited in this cluster, so unconfirmed as of this pass.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md).
- [ict-2022-model](../31-models/ict-2022-model.md) — the closest corpus analogue; its entry/stop mechanics contradict items 6–7 above.

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION` — stub Source IDs; no attached video in this corpus.
- `ICT-2022-MENTORSHIP-EP06` (15:14) "look for periods where price runs above an old high then it breaks down"; (36:06) "where's your stop loss going to be above the high of candle number two or you can use above candle number one which creates a swing high."
- `ICT-2022-MENTORSHIP-EP18` (32:47) "put your limit order in to sell short right at that price right there or plus one pip"; (48:30) "You don't need to have your entry filled inside that kill zone window."
- `ICT-2022-MENTORSHIP-EP20` (14:19) "we're just going to use the actual candle high that would be your limit order entry."
- `ICT-2022-MENTORSHIP-EP25` (32:46–33:13) FVG forms after the market-structure-shift displacement.
- `ICT-2022-MENTORSHIP-EP40` (17:18) London-close profit-taking hour, the one adjacent time-of-day statement found in a Silver-Bullet-shaped search.
- `ICT-2022-MENTORSHIP-EP05` (10:50) "I want to try to be positioned before 11:00" — the other adjacent time-of-day statement found; does not name a Silver Bullet.
- `ICT-2022-MENTORSHIP-EP10` (28:38) "not going to give you a silver bullet that removes losing trades" — idiomatic use, not a named setup.
- `ICT-2022-MENTORSHIP-EP24` (33:30) "find the nearest short term low because that right there is going to be your trigger" — the MSS/displacement step quoted at item 4.
- `ICT-2017-BREAD-BUTTER-SELL` (19:18) "They're not a silver bullet" — idiomatic use.
- `ICT-2017-MEGA-BOND` (03:35) "interest rate SMT is going to be that little silver bullet" — idiomatic use.
- `ICT-2017-MEGA-STOCK` (25:15), (51:22) index SMT "is the silver bullet" — idiomatic use, both instances.

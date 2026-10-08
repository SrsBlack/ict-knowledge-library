# Equal Lows (EQL)

**Category:** 02-liquidity
**Aliases:** EQL, double bottom liquidity, relative equal lows (REL)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-WHAT-TO-FOCUS-ON, ICT-2016-LIQUIDITY-VOIDS, ICT-2016-LIQUIDITY-POOLS, ICT-2016-DOUBLE-TOP-BOTTOM, ICT-2022-MENTORSHIP-EP09, ICT-2022-MENTORSHIP-EP16
**Tags:** liquidity, eql, sellside, foundational

## Definition

Equal lows are two or more swing lows at (approximately) the same price level — the densest form of [sell-side-liquidity](sell-side-liquidity.md). Mirror of [equal-highs](equal-highs.md). ICT: "relative equal lows, there's going to be sell side building up below that — sell stops — okay, when it starts to go higher, anyone that was long overnight, they're going to jam their stop loss right underneath that" (`ICT-2022-MENTORSHIP-EP09`, 14:47); "we never trust double bottoms and double tops… seeking liquidity below them in the form of sell stops" (`ICT-2016-DOUBLE-TOP-BOTTOM`, 12:12–12:25).

## Formal Criteria

- Two or more swing lows print in **close proximity** to each other — the same verbal (not numeric) qualifier as equal highs: "when a low is formed and another low is equally formed in close proximity to the initial one, that's a big area for sell stops to pull or build up underneath those lows" (`ICT-2016-WHAT-TO-FOCUS-ON`, 16:04).
- A swing high must exist between them (otherwise they're consecutive bars in a single downleg, not distinct pivots) — **library convention, not stated by ICT**; "intervening" is 0/0 in both corpora, though trivially true of two distinct swing lows.
- ICT uses "equal lows" and "relative equal lows" **interchangeably**, including for an exact match — see [relative-equal-highs-lows](relative-equal-highs-lows.md) and `equal-highs` for the corrected (non-dichotomous) framing.

## Formula / Math

ICT gives **no numeric pip/tick tolerance** for equal lows (0 hits for "tolerance" in either corpus). The library's prior "strict EQL = 0, relative EQL = small ε > 0" dichotomy is **contradicted**: "relatively equal — not exactly — that's why I named them relatively equal lows" (`ICT-2022-MENTORSHIP-EP16`, 04:13), stated of a pair he treats as the same phenomenon regardless of exactness. A figure such as "10+ pips on EURUSD H1 is too loose" is not sourced to ICT — do not present it as his rule.

```
equal_lows(SL_1, SL_2) := L(SL_1) "in close proximity to" L(SL_2)   [no ICT-given numeric bound]
                           AND exists(SH between SL_1 and SL_2)
```

## Machine-Readable

```json
{
  "id": "equal-lows",
  "category": "02-liquidity",
  "aliases": ["EQL", "double-bottom-liquidity", "REL"],
  "criteria": [
    {"id": "c1", "expr": "L(SL_1) close_in_proximity_to L(SL_2) — ICT gives no numeric tolerance"},
    {"id": "c2", "expr": "exists_SH_between(SL_1, SL_2) == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equal-highs","sell-side-liquidity","relative-equal-highs-lows","liquidity-sweep","liquidity-pool","swing-low"],
  "sources": ["ICT-2016-WHAT-TO-FOCUS-ON","ICT-2016-LIQUIDITY-VOIDS","ICT-2016-LIQUIDITY-POOLS","ICT-2016-DOUBLE-TOP-BOTTOM","ICT-2022-MENTORSHIP-EP09","ICT-2022-MENTORSHIP-EP16"]
}
```

## Visual Pattern

```
                  /\
                 /  \
                /    \
       /\    /
      /  \  /
     /    \/
    /         ← SH between
  SL_1            SL_2          ← equal / relative-equal lows
   ──────┴──────────────┴─────────  EQL liquidity pool
```

## Timeframes

Every TF.

## Examples

**Example 1 — Asian-range EQL:**
- During Asia, M5 prints two lows at 1.0830 and 1.0831 separated by a brief rally — in close proximity, per ICT's own qualifier.
- Asian SSL pool established. London open often sweeps these before reversing; if HTF bias is bullish, the sweep is the long entry trigger.

## Common Mistakes

- **Inventing a numeric tolerance.** ICT gives none; calibrate by judgment ("close proximity"), not an invented pip figure.
- **Treating "equal" and "relative equal" as different strictness levels.** ICT uses them interchangeably.
- **No intervening pivot.** Two adjacent bars at the same low are not EQL.
- **Reversal certainty.** EQL sweep often reverses but not always; require PD-array / session confluence.

## Related Concepts

- [equal-highs](equal-highs.md) — mirror.
- [sell-side-liquidity](sell-side-liquidity.md) — what EQL represents.
- [relative-equal-highs-lows](relative-equal-highs-lows.md) — same concept, not a separate strictness tier.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior.
- [swing-low](../01-market-structure/swing-low.md) — building block.

## Citations

- `ICT-2016-WHAT-TO-FOCUS-ON` (16:04) "when a low is formed and another low is equally formed in close proximity to the initial one, that's a big area for sell stops."
- `ICT-2016-LIQUIDITY-VOIDS` (13:15) "it trades lower… and makes it run down below the equal lows that's been formed on the 15th of December and the 16th of December."
- `ICT-2016-LIQUIDITY-POOLS` (17:59) "relative equal lows."
- `ICT-2016-DOUBLE-TOP-BOTTOM` (12:12–12:25) "we never trust double bottoms and double tops… seeking liquidity below them in the form of sell stops."
- `ICT-2022-MENTORSHIP-EP09` (14:47) "relative equal lows, there's going to be sell side building up below that… they're going to jam their stop loss right underneath that."
- `ICT-2022-MENTORSHIP-EP16` (04:13) "relatively equal — not exactly — that's why I named them relatively equal lows."

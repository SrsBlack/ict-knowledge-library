# Silver Bullet — Rules

**Category:** 11-silver-bullet
**Aliases:** SB rules, SB checklist, silver bullet criteria
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, rules, checklist

## Definition

The Silver Bullet rules are the operational checklist for taking an SB entry — the discipline that distinguishes a high-probability ICT setup from random fib-FVG entries during the 60-minute window. Every confirmed SB must check ALL items.

## Formal Criteria — The SB Checklist

A valid Silver Bullet entry requires ALL of:

1. **Inside one of the three SB windows** — 03:00–04:00 / 10:00–11:00 / 14:00–15:00 NY.
2. **HTF bias direction confirmed** — long SBs only on bullish bias; shorts on bearish.
3. **Liquidity sweep occurred** — a known pool was taken (Asian range, lunch range, prior session high/low, PDH/PDL).
4. **Displacement after sweep** — strong directional candle in the bias direction.
5. **FVG formed** in or after the displacement.
6. **Entry trigger** — typically lower-TF MSS / FVG retest at CE.
7. **SL beyond the swept liquidity pool** — protects against the original sweep being followed by a continuation in that direction.
8. **Targets defined** — at minimum first SD projection or HTF DOL.

Missing any item significantly reduces conviction. Items 1–4 are non-negotiable; 5–8 can be substituted in special cases.

## Formula / Math

```
sb_entry_valid := in_sb_window
                   AND htf_bias_clear
                   AND sweep_just_occurred
                   AND displacement_after_sweep
                   AND fvg_formed
                   AND entry_trigger_present
                   AND sl_beyond_sweep
                   AND targets_defined
```

## Machine-Readable

```json
{
  "id": "silver-bullet-rules",
  "category": "11-silver-bullet",
  "aliases": ["SB-rules", "SB-checklist"],
  "criteria": [
    {"id": "c1", "expr": "all 8 checklist items pass"},
    {"id": "c2", "expr": "items 1-4 are non-negotiable"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-london","silver-bullet-ny-am","silver-bullet-ny-pm","silver-bullet-failure-modes","htf-bias-framework","liquidity-sweep","displacement-definition","fair-value-gap","ce-as-primary-entry"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   SB checklist (bullish example):

   ☐ Time inside 03-04 / 10-11 / 14-15 NY?    [SB window]
   ☐ HTF bias bullish?                         [D / W check]
   ☐ Liquidity sweep occurred (e.g. Asian SSL or lunch low)?
   ☐ Displacement candle after sweep?
   ☐ Bullish FVG inside or after displacement?
   ☐ M5 entry trigger (FVG CE retest, MSS, etc)?
   ☐ SL beyond sweep low + small buffer?
   ☐ TP defined (SD projection / DOL)?

   All checked → take entry.
   Missing 1-4 → skip.
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — checklist pass on bullish NY AM SB:**
- 10:05 NY ✓ (in window).
- HTF bullish ✓.
- 09:55 macro: M5 wicked sub-pre-NY-AM low, swept ✓.
- 10:10: 18-pip green displacement ✓.
- Bullish FVG at 1.0930-1.0934 ✓.
- 10:25: M5 retests CE 1.0932; bullish wick rejection (entry trigger) ✓.
- SL 1.0908 (sweep low - 2-pip buffer) ✓.
- TP -1.5 SD = 1.0975 ✓.
- → Take entry. Risk 24 pips, reward 43 pips → 1.8R.

## Common Mistakes

- **Skipping the sweep.** SB without a sweep beforehand is just a directional FVG entry — much lower probability.
- **No HTF check.** Bias-misaligned SBs fail at much higher rates.
- **No defined target.** SBs without a target tend to get held into reversal; pre-define TPs.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-london](silver-bullet-london.md), [silver-bullet-ny-am](silver-bullet-ny-am.md), [silver-bullet-ny-pm](silver-bullet-ny-pm.md), [silver-bullet-failure-modes](silver-bullet-failure-modes.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`.

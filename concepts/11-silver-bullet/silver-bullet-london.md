# Silver Bullet — London

**Category:** 11-silver-bullet
**Aliases:** London SB, LDN silver bullet, 3am SB
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, london

## Definition

The London Silver Bullet is the **03:00–04:00 NY** Silver Bullet window — the SB inside the London Open killzone (02:00–05:00). It overlaps the 02:50–03:10 macro time and is typically the window where the **post-Asian-range Judas swing reverses and London's true delivery begins**. Medium probability versus the higher-probability NY AM SB, but the cleanest of the three when the Asian range is well-defined.

## Formal Criteria

- Time window: 03:00 – 04:00 NY.
- Inside London Open killzone.
- Sequence: Asian-range sweep (often inside or just before SB window) → displacement → FVG → CE retest entry.
- Targets: Asian-range projections, PDH/PDL, HTF DOL.

## Formula / Math

```
ldn_sb_window     = [03:00, 04:00] NY
overlapping_macro = [02:50, 03:10] NY
parent_killzone   = [02:00, 05:00] NY
```

## Machine-Readable

```json
{
  "id": "silver-bullet-london",
  "category": "11-silver-bullet",
  "aliases": ["London-SB", "LDN-SB", "3am-SB"],
  "criteria": [
    {"id": "c1", "expr": "time in [03:00, 04:00] NY"},
    {"id": "c2", "expr": "Asian-range sweep is typical setup"},
    {"id": "c3", "expr": "HTF bias agreement"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-rules","london-open-killzone","asian-range","asian-range-sweep","macro-time-0250-0310","judas-swing","london-judas-swing"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   02:00 ── 02:50 ─ 03:00 ──── 03:10 ─── 04:00 ── 05:00 NY
              █████ macro
                     ██████████████████ ← London SB window
   ────── London Open KZ ───────────────
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — bullish London SB:**
- HTF bullish; Asian range 1.0850–1.0875.
- 02:55 NY (macro): M5 wicks 1.0846 (Asian SSL swept), closes 1.0853.
- 03:10 NY: M5 displacement candle (16-pip green), bullish FVG at 1.0858–1.0862.
- 03:25 NY: M5 pulls back to FVG CE 1.0860. Long entry.
- SL below 1.0844 (sweep low - 2-pip buffer). Risk = 16 pips.
- Target: 1× Asian-range projection above asian_high = 1.0900 → ~40 pips → ~2.5R.

## Common Mistakes

- **Pre-window trades.** Setups firing before 03:00 are still in the macro / killzone but outside the formal SB window — apply SB rules with caution.
- **Counter-Asian-bias SBs.** Reading bias only from Asia (without HTF) leads to wrong-side SB entries.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-rules](silver-bullet-rules.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [asian-range](../14-asian-range/asian-range.md), [asian-range-sweep](../14-asian-range/asian-range-sweep.md), [macro-time-0250-0310](../04-time-cycles/macro-time-0250-0310.md), [judas-swing](../13-judas-swing/judas-swing.md), [london-judas-swing](../13-judas-swing/london-judas-swing.md).

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`.

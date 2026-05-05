# Silver Bullet — 2025 Formalization

**Category:** 11-silver-bullet
**Aliases:** SB 2025 update, SB micro-execution, refined SB
**ICT Confidence:** high
**Year Introduced:** 2025
**Year Refined:** 2025
**Source IDs:** ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, 2025-refinement

## Definition

In 2025 ICT formalized several refinements to Silver Bullet execution that had been informally taught since 2022. The 2025 SB framework adds: (1) explicit micro-execution timing within each window, (2) integration with the 2025 CE-primary-entry framing, (3) tighter sweep-quality requirements, and (4) updated target frameworks combining SD projections with HTF DOL.

## Formal Criteria

The 2025 refinements:

- **Micro-execution timing** — entries are most reliable in the first 25–30 minutes of the SB window (e.g., 10:00–10:25 in NY AM SB), with the macro overlap (~10:00–10:10) producing the highest concentration.
- **CE as default entry** — per [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md), entries default to FVG CE rather than far-edge.
- **Sweep quality** — sweep must produce a long wick (≥ 60% of candle range) and close back inside the swept zone.
- **Target framework** — at minimum a -1.5 SD target; with HTF DOL coincidence, that level becomes the primary TP.

## Formula / Math

```
high_concentration_micro_window := first 25 min of SB window

sb_entry_2025 := standard_SB_rules
                  AND entry_at_FVG_CE
                  AND sweep_wick_pct >= 0.60
                  AND target_at_min_-1.5_SD_or_HTF_DOL
```

## Machine-Readable

```json
{
  "id": "silver-bullet-formalized-2025",
  "category": "11-silver-bullet",
  "aliases": ["SB-2025-update", "SB-micro-execution"],
  "criteria": [
    {"id": "c1", "expr": "execute in first 25 min of SB window"},
    {"id": "c2", "expr": "entry at FVG CE (2025 default)"},
    {"id": "c3", "expr": "sweep_wick_pct >= 0.60"},
    {"id": "c4", "expr": "target at min -1.5 SD or HTF DOL"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2025",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-rules","ce-as-primary-entry","macro-times-overview","standard-deviation-projections","draw-on-liquidity"],
  "sources": ["ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

```
   2025 micro-execution focus (NY AM SB example):

   10:00  10:05  10:10  10:15  10:20  10:25  10:30 ── 11:00 NY
   ████████████████████████ ←  highest density window (25 min)
                               most setups complete here
                            ─────────────────  late SB window
                                              fewer fresh setups
```

## Timeframes

M1 / M5.

## Examples

**Example 1 — applying 2025 framing on NY AM SB:**
- 09:55 macro: sweep candle with 15-pip wick on 22-pip range = 68% wick (>60% threshold) ✓.
- 10:08: M5 displacement, FVG forms 1.0930–1.0934, CE 1.0932.
- 10:18: M5 retests CE; entry at 1.0932 (within 25-min window ✓).
- SL 1.0908 (sweep-low buffer); risk 24 pips.
- Target -1.5 SD aligns with PWH at 1.0972; primary TP. Risk 24, reward 40 → 1.7R.

## Common Mistakes

- **Late entries.** SB setups firing at 10:35–11:00 are lower-probability; the "first 25 min" rule reflects historical execution density.
- **Pre-2025 entry depths.** Entering at FVG far-edge (older convention) instead of CE costs both fill rate and R:R.
- **Sweep without 60% wick.** A "sweep" with a small wick is indecisive; require the 60% threshold to confirm the rejection.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-rules](silver-bullet-rules.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md), [macro-times-overview](../04-time-cycles/macro-times-overview.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2025-MACRO-PRECISION` — 2025 SB precision update.

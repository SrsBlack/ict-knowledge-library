# Venom Model

**Category:** 31-models
**Aliases:** ICT Venom, Venom setup
**ICT Confidence:** high
**Year Introduced:** 2025
**Year Refined:** 2025
**Source IDs:** ICT-2025-VENOM
**Tags:** model, venom, 2025, indices

## Definition

The **Venom Model** is ICT's named **90-minute intraday strategy** released in April 2025, designed primarily for **US equity indices** (NQ, ES, YM). It builds on Power-of-Three but specifies a precise execution pattern: sweep the 08:00–09:30 NY pre-cash-open range, trigger a fake breakout, then reverse into the opposite-side liquidity. The Venom is the first **genuinely new** ICT model since the 2022 framework.

## Formal Criteria

The Venom Model sequence:

1. **Pre-cash-open range** — high and low formed during 08:00–09:30 NY (before US equities cash open).
2. **Sweep one bound** — typically the BSL or SSL of the pre-open range.
3. **False breakout** — wick continues briefly past the swept bound.
4. **Reversal** — back through the pre-open range with displacement.
5. **Target** — opposite side of the pre-open range, then HTF DOL.
6. Window: ~90 minutes from 09:30 → 11:00 NY captures most of the play.

## Formula / Math

```
venom_pre_open_range = [
  high(08:00-09:30 NY),
  low (08:00-09:30 NY),
]

venom_setup:
    sweep_one_bound_after_09:30
    AND wick_briefly_past_swept_bound
    AND reversal_displacement_back_through_range
    AND opposite_bound_targeted
```

## Machine-Readable

```json
{
  "id": "venom-model",
  "category": "31-models",
  "aliases": ["ICT-Venom", "Venom-setup"],
  "criteria": [
    {"id": "c1", "expr": "pre-cash-open range 08:00-09:30 NY"},
    {"id": "c2", "expr": "sweep + fake breakout + reversal pattern"},
    {"id": "c3", "expr": "primarily US indices (NQ, ES, YM)"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2025",
  "year_refined": "2025",
  "related": ["ict-2022-model","ict-2024-model","silver-bullet-ny-am","ny-am-open-range-model","power-of-three","liquidity-sweep","ny-am-killzone"],
  "sources": ["ICT-2025-VENOM"]
}
```

## Visual Pattern

```
   bullish Venom (NQ example, US indices):

   08:00-09:30 NY: pre-cash-open range, e.g. NQ [17500, 17530]
                     ▲
                    ▲▲   ← false breakout above 17530 around 09:35
                   ▲▲▲
   ────────────── 17530 (BSL)
       (range)
   ────────────── 17500 (SSL)
                                  ↓ reversal back through range
                                  ↓ displacement
                                  ↓ target the SSL at 17500 then below
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — bearish Venom on NQ:**
- 08:00–09:30 NY: NQ pre-open range 17500–17530.
- 09:35: NQ wicks 17545 (BSL swept above range); closes 17525 (back inside).
- 09:50 (NY pre-open macro): NQ displaces -50 points down.
- 10:10: NQ retests bearish FVG at 17518; short entry.
- Target: range low 17500 (~18 points → 1+R from tight stop), then -1.5 SD projection.

## Common Mistakes

- **Applying Venom to FX.** Designed for US indices; FX setups don't follow the same pre-cash-open structure (FX is 24-hour).
- **Skipping the sweep.** Venom requires a sweep + fake breakout; a clean breakout without sweep is a different setup (NY AM continuation).
- **Wrong window.** Pre-open range is 08:00–09:30 NY specifically; using a different range invalidates the Venom framing.

## Related Concepts

- [ict-2022-model](ict-2022-model.md), [ict-2024-model](ict-2024-model.md), [silver-bullet-ny-am](../11-silver-bullet/silver-bullet-ny-am.md), [ny-am-open-range-model](ny-am-open-range-model.md), [power-of-three](../12-power-of-three/power-of-three.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md).

## Citations

- `ICT-2025-VENOM` — ICT's April 3 2025 release video.

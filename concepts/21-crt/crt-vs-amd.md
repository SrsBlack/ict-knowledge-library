# CRT vs AMD — Disambiguation

**Category:** 21-crt
**Aliases:** none (disambiguation page)
**ICT Confidence:** community-attributed
**Year Introduced:** 2024
**Year Refined:** 2024
**Source IDs:** ROMEO-2024-CRT, ICT-2016-PO3, ICT-CRT-RESPONSE
**Tags:** crt, amd, disambiguation, terminology

## Definition

This page clarifies the **relationship** between **CRT (Candle Range Theory, community-attributed)** and **AMD / PO3 (ICT-original)** — two frameworks that describe overlapping market behavior from different angles.

**Short version:**
- **AMD / PO3 (ICT, 2016)** = three-phase fractal cycle (Accumulation → Manipulation → Distribution).
- **CRT (community, 2024)** = candle-range-based interpretation: each candle's high/low are reference levels; sweeps + reversals.

CRT can be seen as a **specialized read of the M-phase** (manipulation) of AMD applied at the single-candle level — when a CRT sweep occurs, it's structurally a manipulation phase within the candle's range. ICT's response to CRT (`ICT-CRT-RESPONSE`) acknowledged this lineage: "based on my ideas but not my concept."

## Formal Criteria

### AMD (ICT-original)

- Multi-bar phase sequence: A → M → D.
- Fractal across all TFs.
- Emphasis: structural delivery across many candles.

### CRT (community)

- Single-HTF-candle reference.
- Sweep + reversal mechanic.
- Emphasis: trade execution at HTF candle bounds.

### Relationship

```
CRT setup ≈ M-phase of AMD applied to a single HTF candle's range
```

CRT sweeps the candle's high/low (which is essentially the engineered liquidity from the candle's prior accumulation), then the reversal IS the manipulation-to-distribution transition. The frameworks operate at different scales:

- AMD = multi-candle session/day cycle.
- CRT = single-HTF-candle event.

## Formula / Math

```
amd_cycle:
    multi_candle_window
    accumulation -> manipulation -> distribution

crt_event:
    single_htf_candle_reference
    sweep_one_bound -> reversal_to_opposite_bound

# CRT as AMD-applied-to-single-candle:
crt_event_inside_one_candle ≈ AMD_phase_M_within_that_candle's_range
```

## Machine-Readable

```json
{
  "id": "crt-vs-amd",
  "category": "21-crt",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "AMD = multi-candle ICT-original cycle"},
    {"id": "c2", "expr": "CRT = single-candle community-attributed reversal model"},
    {"id": "c3", "expr": "CRT can be seen as AMD M-phase at candle scale"}
  ],
  "timeframes": ["H1","H4","D","W"],
  "confidence": "community-attributed",
  "year_introduced": "2024",
  "year_refined": "2024",
  "related": ["candle-range-theory","crt-rules","ict-response-to-crt","power-of-three","amd-cycle-overview","manipulation-phase"],
  "sources": ["ROMEO-2024-CRT","ICT-2016-PO3","ICT-CRT-RESPONSE"]
}
```

## Visual Pattern

```
   AMD (multi-candle):                       CRT (single HTF candle):
   
   ──── A ──── M ──── D ────                 H4 candle: high
       (Asia)  (LDN)  (NY)                            ↑
                                              sweep above
                                                   ↓
                                              reverse to low
                                                   ↓
                                              (this single-candle
                                               sweep+reverse ≈ M phase
                                               at the candle scale)
```

## Timeframes

Both apply at HTF; CRT is more often traded at H1/H4 specifically.

## Examples

**Example A — AMD (intraday):**
- Asia: tight range (A).
- London open: wicks Asian low (M).
- NY AM: 60-pip rally to PDH (D).

**Example B — CRT (single H4 candle):**
- H4 candle's range high 1.0900, low 1.0860.
- Future M5 wicks 1.0905 (sweep / mini-M).
- Reversal to 1.0865 (mini-D toward opposite bound).

Both are "manipulation → distribution" patterns; AMD is multi-candle structural, CRT is single-candle execution.

## Common Mistakes

- **Treating CRT as a replacement for AMD.** They describe overlapping but different phenomena at different scales.
- **Citing CRT as ICT.** CRT is community-attributed; AMD is ICT-original.
- **Trading single CRT events without HTF context.** Even within CRT teaching, HTF bias is required for high-conviction setups.

## Related Concepts

- [candle-range-theory](candle-range-theory.md), [crt-rules](crt-rules.md), [ict-response-to-crt](ict-response-to-crt.md).
- [power-of-three](../12-power-of-three/power-of-three.md), [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md), [manipulation-phase](../12-power-of-three/manipulation-phase.md).

## Citations

- `ROMEO-2024-CRT` — Romeo's CRT primary thread.
- `ICT-2016-PO3` — original AMD/PO3 introduction.
- `ICT-CRT-RESPONSE` — ICT's framing of CRT vs his framework.

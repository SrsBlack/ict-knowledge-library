# Candle Range Theory (CRT)

**Category:** 21-crt
**Aliases:** CRT, the missing piece, candle-range model
**ICT Confidence:** community-attributed
**Year Introduced:** 2024
**Year Refined:** 2024
**Source IDs:** ROMEO-2024-CRT, TTRADES-CRT-EXPLAINER, ICT-CRT-RESPONSE
**Tags:** crt, community-attributed, romeo, candle-range

## Definition

**Candle Range Theory (CRT)** is a community-attributed model — popularized in 2024 by Romeo (and extensively explained by TTrades) — that frames price delivery in terms of **the range of each candle** rather than the structural pivots / FVG / OB framework ICT teaches. CRT treats every candle as a "micro-range" with high/low/open as liquidity reference points; sweeping one bound predicts a reversal toward the opposite. **CRT is NOT ICT-original** — ICT publicly stated it is "based on my ideas but not my concept." This file documents CRT for completeness because the trading community frequently mixes CRT with ICT discussions, and disambiguating them prevents conceptual confusion.

## Formal Criteria

CRT's core claim:

- Each candle's range = high to low.
- Sweeping the high or low of a meaningful candle (typically a HTF candle: H1, H4, D, W) predicts a reversal back through the candle's range.
- The "CRT setup" is: identify a HTF candle with a sweep of one bound, then trade the reversal back through to the opposite bound.
- Time-of-day filters often added: 02:00, 03:00, 05:00, 09:00, 13:00 NY (varies by source).

## Formula / Math

```
crt_setup(htf_candle):
    sweep_event := high(future_candle) > high(htf_candle)
                    OR low(future_candle) < low(htf_candle)
    target := opposite_bound(htf_candle)

# Example: H4 candle high 1.0900, low 1.0860
# Sweep above 1.0900 -> trade short toward 1.0860 (the opposite bound)
```

The math is straightforward but the **selection criteria** (which HTF candle, which time filter, when to enter the reversal) varies widely across CRT teachers.

## Machine-Readable

```json
{
  "id": "candle-range-theory",
  "category": "21-crt",
  "aliases": ["CRT", "candle-range-model", "the-missing-piece"],
  "criteria": [
    {"id": "c1", "expr": "uses HTF candle range as reference"},
    {"id": "c2", "expr": "sweep of one bound predicts reversal to opposite"},
    {"id": "c3", "expr": "NOT_ICT_original"}
  ],
  "timeframes": ["H1","H4","D","W"],
  "confidence": "community-attributed",
  "year_introduced": "2024",
  "year_refined": "2024",
  "related": ["crt-rules","crt-vs-amd","ict-response-to-crt","power-of-three","liquidity-sweep","turtle-soup"],
  "sources": ["ROMEO-2024-CRT","TTRADES-CRT-EXPLAINER","ICT-CRT-RESPONSE"]
}
```

## Visual Pattern

```
   bearish CRT (sweep of HTF candle high → reversal to low):

   HTF candle:
        high ──── 1.0900     ← sweep with future wick
        body
        low  ──── 1.0860     ← target

   Future candle wicks 1.0905 (sweep), closes back inside.
   Trade: short with target 1.0860.
```

## Timeframes

H1+ (lower TFs produce too-noisy "candles" for CRT framing).

## Examples

**Example 1 — bearish CRT setup:**
- H4 candle prints high 1.0900, low 1.0860 over a 4-hour window.
- Next H4 wicks 1.0908 (sweeps the prior H4 high), closes 1.0890 (back inside).
- Per CRT: short with target 1.0860 (the prior H4 low).
- Stop above sweep at 1.0912.
- Risk = 22 pips, reward = 30 pips → 1.4R.

## ICT vs Community

**This is the canonical ICT-vs-Community disambiguation case.** CRT is widely promoted in the ICT-adjacent community as if it were ICT-original. It is not.

- **Romeo** (2024) is the primary popularizer. Romeo himself credits ICT for inspiration.
- **TTrades** publishes the most-watched CRT explainer videos.
- **ICT** has publicly responded that CRT "is based on my ideas but not my concept" — acknowledging the conceptual lineage from his Power-of-Three teaching but declining to endorse CRT as an extension of his framework.

This library treats CRT as **community-attributed** with `confidence: community-attributed`. Use CRT alongside ICT material if you choose, but do NOT cite CRT as if ICT taught it.

## Common Mistakes

- **Citing CRT as ICT-original.** ICT did not author CRT. Always credit Romeo / TTrades when discussing CRT specifically.
- **Treating CRT as a replacement for PO3 / OB / FVG framework.** CRT is a parallel candle-range framing; ICT's structural framework (BOS/CHoCH/PD-arrays) operates at a different level of analysis.
- **Single-candle CRT trades.** CRT requires HTF candle-range context; intraday M5 "CRT setups" are noise-prone.

## Related Concepts

- [crt-rules](crt-rules.md), [crt-vs-amd](crt-vs-amd.md), [ict-response-to-crt](ict-response-to-crt.md).
- [power-of-three](../12-power-of-three/power-of-three.md) — ICT's structural analogue (different but related).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [turtle-soup](../20-turtle-soup/turtle-soup.md) — ICT-original concepts that CRT setups overlap with structurally.

## Citations

- `ROMEO-2024-CRT` — Romeo's CRT primary thread.
- `TTRADES-CRT-EXPLAINER` — TTrades CRT explainer video(s).
- `ICT-CRT-RESPONSE` — ICT public commentary that CRT is "based on my ideas but not my concept."

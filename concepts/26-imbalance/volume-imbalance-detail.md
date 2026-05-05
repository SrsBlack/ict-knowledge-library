# Volume Imbalance — Detail

**Category:** 26-imbalance
**Aliases:** VI, body imbalance, body-vs-body gap
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** imbalance, volume, body-gap

## Definition

A volume imbalance is a small body-vs-body gap between two consecutive candles where one candle's body opens away from the prior candle's body close — but the wicks may overlap. It is **not** a Fair Value Gap (which requires non-overlapping wicks across 3 candles), but it IS an imbalance. Volume imbalances form during fast directional moves where market orders consumed all liquidity at the touched levels, creating a no-trade body region.

## Formal Criteria

For a bullish volume imbalance:

- Candle n-1 closes at price `C_{n-1}`.
- Candle n opens at price `O_n` strictly higher: `O_n > C_{n-1}`.
- The body gap is from `C_{n-1}` to `O_n`.
- Wicks of n-1 and n may overlap (this is what makes it NOT an FVG).

For bearish: `O_n < C_{n-1}`.

## Formula / Math

```
bullish_volume_imbalance(n) := O_n > C_{n-1}
                                AND L_n could overlap H_{n-1}

bearish_volume_imbalance(n) := O_n < C_{n-1}
                                AND H_n could overlap L_{n-1}

vi_size = |O_n - C_{n-1}|
```

A volume imbalance is meaningful when the body gap is substantial (≥ 30% of average candle body); tiny 1-tick gaps don't carry weight.

## Machine-Readable

```json
{
  "id": "volume-imbalance-detail",
  "category": "26-imbalance",
  "aliases": ["VI", "body-imbalance", "body-vs-body-gap"],
  "criteria": [
    {"id": "c1", "expr": "open_n != close_{n-1}"},
    {"id": "c2", "expr": "wicks_may_overlap == true"},
    {"id": "c3", "expr": "vi_size >= 0.3 * avg_body_size"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["imbalance-definition","imbalance-vs-fvg","fair-value-gap","volume-imbalance","displacement-definition"],
  "sources": ["ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Volume imbalance (NOT an FVG):

         ▲
         █ ← candle n: opens above prior close
         █    (body gap from C_{n-1} up to O_n)
         O_n
         ──────────────  ← gap region (volume imbalance)
         C_{n-1}
         █
         █ ← candle n-1
         ▼
       (wicks of n-1 and n may overlap visually,
        but the bodies do not)
```

## Timeframes

M5+ generally. Lower TFs have noise-driven body gaps that aren't institutional in origin.

## Examples

**Example 1 — bullish VI inside displacement:**
- M15: candle n-1 closes at 1.0852 with high 1.0855.
- Candle n opens at 1.0858 with low 1.0856.
- Body gap = 6 pips; wicks overlap from 1.0855 to 1.0856.
- → bullish volume imbalance, not an FVG.
- Algorithm tendency: revisit the body-gap region before continuing further; entries consider this zone as a secondary discount reference.

## Common Mistakes

- **Conflating with FVG.** A volume imbalance has overlapping wicks; an FVG does not. Don't call body gaps "FVGs."
- **Counting tiny gaps.** 1–2 tick body gaps from broker-side feed jitter aren't real volume imbalances.
- **Ignoring ATR scale.** A 10-pip body gap on EURUSD is significant; a 10-pip body gap on XAUUSD is noise. Calibrate by instrument.

## Related Concepts

- [imbalance-definition](imbalance-definition.md), [imbalance-vs-fvg](imbalance-vs-fvg.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2017-DISPLACEMENT`, `ICT-2022-MENTORSHIP-OVERVIEW`.

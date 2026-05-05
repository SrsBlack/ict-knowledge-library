# Imbalance Rebalance

**Category:** 26-imbalance
**Aliases:** rebalance, fill, reaction, mitigate (in some communities)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2024
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-FVG-CLASSIFICATION
**Tags:** imbalance, rebalance, mitigation, fvg

## Definition

Imbalance rebalance is the act of price returning to an existing imbalance and partially or fully filling the unworked region — providing the two-sided trade that was missing when the imbalance formed. ICT teaches that rebalance is the algorithm's standard behavior: imbalances act like magnets that pull price back at some future point. Rebalance is **the entry signal** at most ICT setups: enter at the imbalance during rebalance, with the imbalance bound as invalidation.

## Formal Criteria

A rebalance event has stages:

1. **Touch** — price reaches the imbalance's near edge (closest to current price when entering the zone).
2. **CE rebalance** — price reaches consequent encroachment (50% midpoint of the imbalance). ICT's 2025 framing treats CE as the **primary entry zone**.
3. **Full rebalance** — price reaches the far edge.
4. **Beyond rebalance** — price overshoots; the imbalance is fully consumed and may flip into an inversion.

ICT's 2024 classification ([ICT-2024-FVG-CLASSIFICATION](../06-fair-value-gaps/fvg-classification-2025.md)):

- **Immediate rebalance** — closes within 1–2 bars of formation. Continuation signal.
- **Delayed rebalance** — stays open for many bars; expected to be revisited later.

## Formula / Math

```
imbalance_low  = lower bound of the imbalance zone
imbalance_high = upper bound
imbalance_CE   = (imbalance_low + imbalance_high) / 2

touch_event(t)  := price(t) within [imbalance_low, imbalance_high]
ce_rebalance(t) := price reaches imbalance_CE
full_rebalance(t) := price reaches the far_edge of the imbalance
```

## Machine-Readable

```json
{
  "id": "imbalance-rebalance",
  "category": "26-imbalance",
  "aliases": ["rebalance", "fill", "imbalance-fill"],
  "criteria": [
    {"id": "c1", "expr": "price_returns_to_existing_imbalance == true"},
    {"id": "c2", "expr": "stage in [touch, CE, full, beyond]"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2024",
  "related": ["imbalance-definition","fair-value-gap","consequent-encroachment","ce-as-primary-entry","immediate-rebalance-fvg","delayed-rebalance-fvg","fvg-mitigation","mitigation-of-fvg"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-FVG-CLASSIFICATION"]
}
```

## Visual Pattern

```
   bullish imbalance (FVG) at 1.0860–1.0865:

   ─────── 1.0865 (imbalance_high / far edge from below)
            │
            │ ← full rebalance to 1.0865
            │
   ─────── 1.0862.5 (CE)
            │ ← CE rebalance: primary entry per 2025 ICT framing
            │
   ─────── 1.0860 (imbalance_low / near edge)
            │
            ↑ approach from below (price returning up after sweep)
            │
   ......... current price 1.0858
```

## Timeframes

All TFs. The size of the imbalance scales with TF.

## Examples

**Example 1 — bullish CE rebalance entry:**
- HTF bullish; M15 bullish FVG at 1.0860–1.0866.
- CE = 1.0863.
- Setup: enter long on M5 retest of 1.0863 with SL at 1.0855 (below FVG low + buffer).
- Target: PDH BSL at 1.0925.

**Example 2 — full rebalance + reversal (failed FVG):**
- M15 bullish FVG at 1.0860–1.0866.
- Price returns, fills to 1.0866 (full rebalance), then displaces below 1.0855 with bearish FVG.
- → FVG fully consumed; the original bullish FVG is now an [inversion-fvg](../06-fair-value-gaps/inversion-fvg.md).

## Common Mistakes

- **Insisting on full rebalance.** ICT's 2025 framing emphasizes CE as the primary entry; many setups never reach the far edge. Holding for full rebalance often misses the entry.
- **No invalidation buffer.** Entry exactly at CE with SL exactly at imbalance_low gets stopped on small noise. Use a small buffer.
- **Confusing rebalance with mitigation.** Rebalance = imbalance gets filled. Mitigation has a slightly different sense in OB context (testing the OB body). The terms overlap; see [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md) and [mitigation-definition](../18-mitigation/mitigation-definition.md).

## Related Concepts

- [imbalance-definition](imbalance-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md).
- [consequent-encroachment](../06-fair-value-gaps/consequent-encroachment.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).
- [immediate-rebalance-fvg](../06-fair-value-gaps/immediate-rebalance-fvg.md), [delayed-rebalance-fvg](../06-fair-value-gaps/delayed-rebalance-fvg.md).
- [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md), [mitigation-of-fvg](../18-mitigation/mitigation-of-fvg.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2024-FVG-CLASSIFICATION`.

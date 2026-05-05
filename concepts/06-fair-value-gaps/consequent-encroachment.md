# Consequent Encroachment (CE)

**Category:** 06-fair-value-gaps
**Aliases:** CE, FVG midpoint, 50% of FVG, fair value midpoint
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2025
**Source IDs:** ICT-2018-CE, ICT-2025-CE-PRIMARY-ENTRY
**Tags:** ce, fvg, midpoint, foundational

## Definition

Consequent Encroachment is the **50% midpoint of an FVG** — the FVG-scale equivalent of equilibrium and OB mean threshold. ICT teaches CE as the algorithmic "fair value" point inside an FVG: when price returns to rebalance the FVG, CE is the most-frequent stopping point. CE is the **primary entry zone** in the FVG-based ICT setup playbook. The 2025 ICT framing (`ICT-2025-CE-PRIMARY-ENTRY`) elevated CE to *the* default entry depth — see [ce-as-primary-entry](ce-as-primary-entry.md) for the full elaboration.

## Formal Criteria

For any FVG:

- `ce = (fvg_low + fvg_high) / 2`.
- A "CE rebalance" event is when price reaches CE (touching the level with at least a wick, ideally with a closing candle showing reaction).
- ICT teaches that FVGs frequently rebalance to CE without going further — CE is the **median rebalance depth**.

## Formula / Math

```
ce = (fvg_low + fvg_high) / 2

# For bullish FVG with low=H_{n-1}, high=L_{n+1}:
ce_bullish_fvg = (H_{n-1} + L_{n+1}) / 2

# For bearish FVG with low=H_{n+1}, high=L_{n-1}:
ce_bearish_fvg = (H_{n+1} + L_{n-1}) / 2
```

## Machine-Readable

```json
{
  "id": "consequent-encroachment",
  "category": "06-fair-value-gaps",
  "aliases": ["CE", "FVG-midpoint", "50%-of-FVG"],
  "criteria": [
    {"id": "c1", "expr": "ce == (fvg_low + fvg_high) / 2"},
    {"id": "c2", "expr": "applies_to_any_FVG == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2025",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","ce-as-primary-entry","equilibrium-definition","mean-threshold","imbalance-rebalance","fvg-mitigation"],
  "sources": ["ICT-2018-CE","ICT-2025-CE-PRIMARY-ENTRY"]
}
```

## Visual Pattern

```
   bullish FVG with CE marked:

   ─── L_{n+1} (FVG high / far edge) ────
       
       
   ─── CE = midpoint ───────────────────  ← primary entry zone
       
       
   ─── H_{n-1} (FVG low / near edge) ────
```

## Timeframes

All TFs.

## Examples

**Example 1 — CE entry on M15 bullish FVG:**
- M15 bullish FVG: low 1.0860, high 1.0866. Size 6 pips.
- CE = 1.0863.
- HTF bullish; price returns up to 1.0863 (CE).
- Long entry at CE with SL below 1.0858 (FVG low - 2-pip buffer). Risk = 5 pips.
- Targets via SD projections.

## Common Mistakes

- **Insisting on full fill instead of CE.** Many FVGs rebalance to CE and continue without ever filling fully; demanding full fill misses entries.
- **Pixel-precision at CE.** Use a buffer of 0.5–1 pip on FX; CE entries don't need tick-perfect fills.
- **CE without confluence.** A CE entry without HTF bias agreement, PD-array confluence, or structural support is just hoping.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [ce-as-primary-entry](ce-as-primary-entry.md) — 2025 elevation to default entry.
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md), [mean-threshold](../27-equilibrium/mean-threshold.md) — analogous midpoint concepts at different scales.
- [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md), [fvg-mitigation](fvg-mitigation.md).

## Citations

- `ICT-2018-CE` — CE introduced.
- `ICT-2025-CE-PRIMARY-ENTRY` — CE elevated to default entry zone.

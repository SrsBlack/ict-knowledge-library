# Mean Threshold

**Category:** 27-equilibrium
**Aliases:** MT, mean-threshold-of-OB, OB midpoint
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** equilibrium, mean-threshold, ob, operational

## Definition

Mean threshold (MT) is the **50% midpoint of an order block's body** — the OB-scale equivalent of dealing-range EQ or FVG CE. ICT teaches MT as a primary entry refinement inside OBs: when price returns to a bullish OB, the long entry is taken at the OB's MT (50% of the body) rather than at the OB's far edge. MT functions as the OB's equilibrium and is one of ICT's higher-conviction entry references.

## Formal Criteria

For a bullish OB:

- The OB candle has open `O`, close `C`, high `H`, low `L`.
- Bullish OB body = the down-candle body before the bullish displacement: from `O` to `C` (where `C < O`).
- MT = `(O + C) / 2` — body midpoint.
- Some ICT references use the **full range** midpoint instead: `(H + L) / 2`. Both forms exist; the body version is more common.

For bearish OB: symmetric, body from `O` to `C` with `C > O`.

## Formula / Math

```
# Bullish OB body version:
MT_body = (open(OB_candle) + close(OB_candle)) / 2

# Full range version (sometimes used):
MT_range = (high(OB_candle) + low(OB_candle)) / 2

# By default this library uses MT_body unless stated.
```

## Machine-Readable

```json
{
  "id": "mean-threshold",
  "category": "27-equilibrium",
  "aliases": ["MT", "mean-threshold-of-OB", "OB-midpoint"],
  "criteria": [
    {"id": "c1", "expr": "MT == (open + close) / 2 of OB candle (body version)"},
    {"id": "c2", "expr": "or MT == (high + low) / 2 (range version, less common)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["equilibrium-definition","equilibrium-as-decision-point","bullish-order-block","bearish-order-block","order-block-criteria","consequent-encroachment"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB candle (down-close, last bearish before displacement up):

          H
          ─────
          │
          O   ← top of body
          ───── MT_body (50% of body)
          C   ← bottom of body
          │
          ─────
          L

   Long entry on retest at MT_body, SL below L (or below the FVG / breaker
   the OB anchored).
```

## Timeframes

All TFs that support OBs (M5+ generally; M1 OBs are noisy).

## Examples

**Example 1 — bullish OB MT entry:**
- H1 bullish OB candle: O=1.0830, C=1.0820, H=1.0832, L=1.0815.
- MT_body = (1.0830 + 1.0820) / 2 = 1.0825.
- HTF bullish; price returns to 1.0825.
- Long entry at MT, SL below L at 1.0812 (3-pip buffer).
- Risk = 13 pips; target PDH BSL at 1.0900 = 75 pips reward → ~5.7R setup.

## Common Mistakes

- **Confusing body MT and range MT.** Pick one and use consistently. Body MT is the more common ICT convention.
- **Entering at OB far edge instead of MT.** Far-edge entries get worse R:R and are more often skipped before MT is reached.
- **MT without confirmation.** Even at a clean MT, require post-touch confirmation (lower-TF FVG, structure shift, etc.) before commitment.

## Related Concepts

- [equilibrium-definition](equilibrium-definition.md), [equilibrium-as-decision-point](equilibrium-as-decision-point.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md).
- [consequent-encroachment](../06-fair-value-gaps/consequent-encroachment.md) — FVG-scale equivalent.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.

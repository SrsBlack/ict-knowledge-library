# Static Drawdown (2026 Adaptation)

**Category:** 32-risk-management
**Aliases:** static DD, fixed drawdown, 2026 prop firm rule shift
**ICT Confidence:** medium
**Year Introduced:** 2026
**Year Refined:** 2026
**Source IDs:** ICT-2026-STATIC-DD
**Tags:** risk, static-drawdown, 2026, prop-firm

## Definition

Static drawdown is the **prop-firm rule shift** observed in 2026 where firms transition from **trailing drawdown** (the drawdown limit moves up with realized profits) to **static drawdown** (the limit is fixed at the starting equity level minus the firm's max drawdown). ICT addressed this in 2026 commentary as an **execution adaptation**: with static drawdown, traders can hold winning positions longer without accumulated profit being threatened by minor pullbacks — encouraging fewer/larger wins versus many/smaller wins. ICT's 2026 advice: **trail SL to BOS/CHoCH instead of panic-closing on pullbacks**.

## Formal Criteria

Static drawdown vs trailing drawdown:

| Aspect | Trailing | Static |
|---|---|---|
| DD floor | Moves up with profit | Fixed at start - max DD |
| Profit-protection | Each new high raises floor | No automatic raise |
| Best strategy | Lock profits aggressively | Hold longer for big winners |
| ICT-recommended SL trail | Tight (preserve profit) | To structural BOS / CHoCH |

ICT's 2026 adaptations:

1. Trail SL to confirmed BOS/CHoCH levels rather than tight fixed-pip trail.
2. Hold OBs longer; let mitigation play out.
3. Reduce panic-close behavior on minor pullbacks.
4. Size to standard 0.5–1% per trade; no need for ultra-tight risk.

## Formula / Math

```
trailing_dd_floor(t) = max(account_high_water_mark - max_dd, starting_equity - max_dd)
static_dd_floor      = starting_equity - max_dd        # fixed

# Example: $50K account, $5K max DD
# trailing: as profit grows to $55K, DD floor = $50K
# static:   regardless of profit, DD floor stays at $45K
```

## Machine-Readable

```json
{
  "id": "static-drawdown-2026",
  "category": "32-risk-management",
  "aliases": ["static-DD", "fixed-drawdown", "2026-prop-firm-rule-shift"],
  "criteria": [
    {"id": "c1", "expr": "DD floor fixed regardless of profit"},
    {"id": "c2", "expr": "encourages longer-hold strategies"},
    {"id": "c3", "expr": "ICT recommends trailing SL to structural BOS/CHoCH"}
  ],
  "timeframes": ["all"],
  "confidence": "medium",
  "year_introduced": "2026",
  "year_refined": "2026",
  "related": ["risk-per-trade","r-multiple","partial-takes","stop-placement-by-pd-array","bos-bullish","bos-bearish","choch-bullish","choch-bearish"],
  "sources": ["ICT-2026-STATIC-DD"]
}
```

## Visual Pattern

A risk-management discipline rather than a chart pattern. Key behavioral shift:

```
   Old (trailing DD):
      Panic-close on -3R pullback to preserve account high
      Many small wins

   New (static DD):
      Trail SL to nearest BOS / CHoCH; hold for 5R+
      Fewer, larger wins
```

## Timeframes

All TFs.

## Examples

**Example 1 — adapting to static DD:**
- $50K account, $5K static DD, currently up $3K (= $53K).
- Standard SL behavior would tight-trail to lock the $3K.
- 2026 adaptation: trail SL to recent BOS structure (10-15% of position's reach).
- Result: position can pull back deeper without stopping out, allowing larger Rs.

## Common Mistakes

- **Conflating static and trailing DD.** Verify which the prop firm uses; behavior differs substantially.
- **Over-loosening SL.** Static DD doesn't mean "no SL." It means SL based on structure, not on locked profit.
- **Ignoring max DD.** Static DD still has a max. Don't size positions assuming the floor never matters.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [partial-takes](partial-takes.md), [stop-placement-by-pd-array](stop-placement-by-pd-array.md).
- [bos-bullish](../01-market-structure/bos-bullish.md), [bos-bearish](../01-market-structure/bos-bearish.md), [choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md).

## Citations

- `ICT-2026-STATIC-DD`.

> Confidence is `medium` because static-drawdown adoption varies by firm; verify the specific rule set per prop firm before adapting strategy.

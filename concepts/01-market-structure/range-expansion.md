# Range Expansion

**Category:** 01-market-structure
**Aliases:** expansion, expansion phase
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-ELEMENTS-OF-A-TRADE-SETUP, ICT-2017-DAYTRADE-ESSENTIALS, ICT-2016-MARKET-EFFICIENCY-PARADIGM, ICT-2017-EXPLOSIVE-MARKETS
**Tags:** structure, expansion, momentum, trade-setup-condition

## Definition

Expansion is one of ICT's four conditions a market can be in at any time — "expansion," "retracement," "reversal," "consolidation" — and "they can only be one of these four conditions" (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [01:59]–[02:36], Sep 2016, lesson 1 of Month 1). ICT's own definition: "expansion is when price moves quickly from a level of equilibrium" ([10:28]), and "when price leaves a level quickly, this indicates a willingness on the part of the market makers to reveal their intended repricing model" ([10:42]). Expansion couples directly with the order block as its companion tool ([10:32]).

## Formal Criteria

- Price moves quickly away from equilibrium, in one of the four mutually-exclusive market conditions ICT names (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [02:36]).
- "Eventually, the market will move outside of the consolidation. ... It moves away from the equilibrium price point." ([12:02]–[12:09]).
- The phrase "range expansion" is ICT's own, used across the corpus: "range expansion on a weekly chart is a gold mine" (`ICT-2017-DAYTRADE-ESSENTIALS` [30:17]); "after the high or low is formed, the range will start expanding" (`ICT-2016-MARKET-EFFICIENCY-PARADIGM` [15:25]).
- ICT gives no numeric trigger, multiple, or percentage for when expansion begins or ends — it is taught qualitatively throughout both corpora.

## Formula / Math

```
# ICT gives no number for this. Expansion is identified qualitatively:
# price moving quickly, away from equilibrium, with the market no longer
# in consolidation/retracement/reversal.
```

ICT teaches expansion qualitatively, not with a fixed numerical filter. This library does not supply a substitute formula where ICT gives none.

## Machine-Readable

```json
{
  "id": "range-expansion",
  "category": "01-market-structure",
  "aliases": ["expansion-phase"],
  "criteria": [
    {"id": "c1", "expr": "price_moves_quickly_away_from_equilibrium == true"},
    {"id": "c2", "expr": "numeric_trigger: not given by ICT"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["bos-bullish","bos-bearish","displacement-definition","equilibrium-definition"],
  "sources": ["ICT-2016-ELEMENTS-OF-A-TRADE-SETUP","ICT-2017-DAYTRADE-ESSENTIALS","ICT-2016-MARKET-EFFICIENCY-PARADIGM","ICT-2017-EXPLOSIVE-MARKETS"]
}
```

## Visual Pattern

```
   equilibrium level
   ──────────────────────
                 \
                  \   ← price leaves EQ quickly: expansion
                   \
                    \
```

Qualitative signature only: fast, directional movement away from the equilibrium price point. ICT names no candle-geometry test for it (contrast with [displacement-definition](../09-displacement/displacement-definition.md), which does have a quality description for individual candles).

## Timeframes

ICT applies "range expansion" from weekly charts ("a gold mine," `ICT-2017-DAYTRADE-ESSENTIALS` [30:17]) down to intraday price action. No TF restriction is stated.

## Examples

**Example 1 — the four-condition framework (ICT's own structure):**
- A market is, at any moment, in exactly one of: expansion, retracement, reversal, consolidation (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [02:36]).
- Expansion is identified by price leaving the prior equilibrium level quickly ([10:28]).

**Example 2 — order block as the companion tool:**
- Price expands away from an order block. ICT: "We don't want to chase price. We're going to wait for price to come back down into the order block." ([11:03]–[11:05]) — i.e. the entry is the retracement into the level that produced the expansion, not the expansion move itself.

## Common Mistakes

- **Citing a numeric ATR multiple, close-direction percentage, or "ends when displacement subsides" rule as ICT's.** No such figures appear in either corpus; expansion is taught qualitatively.
- **Treating "contraction" as expansion's stated complementary phase.** ICT's complementary set is the four conditions (expansion / retracement / reversal / consolidation, `ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [02:36]). "Contraction" is a separate, narrower idea he teaches as a volatility filter — "a contraction idea where price moves from a large range down to a small range," measured on candle bodies, not wicks (`ICT-2017-EXPLOSIVE-MARKETS` [21:27]–[22:04]). Do not collapse the two.
- **Requiring an "external BOS of the dealing range" as the expansion trigger.** Not stated anywhere in either corpus; ICT's trigger is leaving equilibrium/consolidation, with the order block as the companion tool.
- **Chasing the expansion move itself.** ICT explicitly teaches waiting for the retracement into the order block instead ([11:03]–[11:05]).

## Related Concepts

- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — a structure break often accompanies the start of expansion, though ICT does not state it as the formal trigger.
- [displacement-definition](../09-displacement/displacement-definition.md) — the candle-level signature often seen during expansion.
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md) — the level expansion moves away from.

## Citations

- `ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [01:50]–[02:36], [10:20]–[10:42], [11:03]–[11:08], [12:02]–[12:09] — the four conditions; expansion defined; order block as companion tool (Sep 2016).
- `ICT-2017-DAYTRADE-ESSENTIALS` [30:11]–[30:17] — "range expansion on a weekly chart is a gold mine."
- `ICT-2016-MARKET-EFFICIENCY-PARADIGM` [15:24]–[15:28] — "range expansion" named after the Judas swing (Sep 2016).
- `ICT-2017-EXPLOSIVE-MARKETS` [21:24]–[22:08] — contraction as a separate, body-measured volatility filter.

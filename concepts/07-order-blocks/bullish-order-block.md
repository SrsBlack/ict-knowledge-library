# Bullish Order Block

**Category:** 07-order-blocks
**Aliases:** bullish OB, BOB, demand OB (SMC), demand zone (SMC), demand block (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-ORDERBLOCKS, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP13, ICT-2022-MENTORSHIP-EP16, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP19, ICT-2022-MENTORSHIP-EP21, ICT-2022-MENTORSHIP-EP30, ICT-2022-MENTORSHIP-EP35
**Tags:** order-block, bullish, foundational

⚠ **Rewritten 2026-10-08 against an audit of `raw/*/report.md` (153 packets) and `m22/ep*.txt`
(41 episodes).** The page previously defined a bullish OB as "the last bearish candle before a
bullish displacement move that breaks structure" and named MT the default entry. Neither survives:
the 2016 definition has no structure-break clause, and 2022 explicitly rejects the "last candle"
framing and the fresh-zone premise. See [order-block-criteria](order-block-criteria.md) for the
shared multi-candle/confirmation rules this page inherits.

## Definition

**2016 (ICT-2016-ORDERBLOCKS):** "Definition of a bullish order block is the lowest candle or price
bar with a down close that has the most range between open to close and is near a support level."
[00:59–01:08]. "Near a support level" means an HTF old high or low: "that can be in the form of an
old low on a long term or higher time frame chart. It could be an old high." [02:20–02:27]. No
structure-break clause is stated anywhere in this lecture.

**2022 restatement (ERA-SPLIT — do not collapse into the 2016 wording):** ICT explicitly rejects the
"last candle" framing taught elsewhere, including by his own earlier students: "the order block is
one consecutive series of up closed candles it's not the last candle before the down move" (EP12
[43:34]); "order block theory is much more than just simply the last up close candle before down
move or the last down closed candle before the up move — that's not it" (EP12 [44:09]); "it does not
need to get up into this last up close candle … that's what everybody says an order block is. It is
not that." (EP18 [40:13–40:41]). The 2022 definition is functional, not candle-counted: "what is an
order block? … it's just [a] change in the state of delivery" (EP03 [24:16]); "this series of up
close candles begin with this candle's opening right there — that opening, once this candle trades
below it, that changes the state of delivery" (EP03 [24:16–24:45]); "What is an order block? It's a
change in the state of delivery. The algorithm changes its state of delivery. As soon as we get below
this candle's open, the market starts delivering sell side." (EP18 [46:23–46:48]).

Bullish OBs are discount-array references when sitting below current price.

**"Demand OB" is not ICT's term.** ICT never labels his order block a demand zone and explicitly
rejects the framing: "that's why it's not supply and demand" (EP18 [40:41]); "I'm not supplying
demand" (EP19 [23:07]). Kept above only as an SMC-community alias.

## Formal Criteria

Per [order-block-criteria](order-block-criteria.md) for the shared multi-candle/confirmation rules.
Bullish-specific:

- 2016: the **lowest** candle or price bar with a down close, having the **most** open-to-close range
  of the candidates, sitting near an HTF support level (old high/low).
- 2022: the candle(s) nearest price in a run of down-close candles, qualified by an **imbalance** —
  "what makes an order block valid? It has to have an imbalance. Without the imbalance, there is no
  order block." (EP18 [40:41]); "that is how you determine your high probability bullish order
  block — it must have the imbalance coupled with the down closed candle and the underlying narrative
  that it's likely to go higher." (EP13 [17:22–17:52]). A market structure shift is a **quality**
  marker on the move away, not a defining criterion.
- **Not fresh-only.** Both eras permit repeated return visits: the 2016 lecture walks a monthly block
  re-traded multiple times — "so how many times did price move away from this down candle?"
  (ICT-2016-ORDERBLOCKS [22:08]) — and 2022 states it outright: "supply and demand requires fresh
  zones, okay? That's nonsense. I have no affinity for anything like that." (EP18 [40:41–41:12]);
  "we have [an] order block — it trades into that multiple times" (EP30 [04:55]).
- Not sold/bought as supply-and-demand: "that's why it's not supply and demand" (EP18 [40:41]).

## Formula / Math

```
bullish_ob_high := open(n)       # since close < open for the OB candle
bullish_ob_low  := close(n)
bullish_ob_mt   := (open(n) + close(n)) / 2     # mean threshold — see Entry below

# 2016 selection rule among candidates — WRITER'S FORMALISATION of a conjunctive rule ICT states in
# prose, not ICT's own notation: "the lowest candle … that has the most range … and is near a
# support level" [00:59–01:08] (lowest AND most range AND near support — all three jointly, not a
# tie-break hierarchy):
candidate_ob := argmin(low) over down-close candles near an HTF support level,
                tie-broken by max(open - close)   # "most range between open to close"
```

Body, not wicks: "any down candle, the body is going to begin with the opening and ends with the
close." (ICT-2016-ORDERBLOCKS [08:05]); "where's the open on that series of down closed candles right
here — that's the price level extending out in time" (EP03 [15:12]); "the opening price on this down
close candle — that's the order block" (EP16 [07:29]).

## Machine-Readable

```json
{
  "id": "bullish-order-block",
  "category": "07-order-blocks",
  "aliases": ["bullish-OB", "BOB", "demand-OB (SMC)", "demand-zone (SMC)", "demand-block (SMC)"],
  "criteria": [
    {"id": "c1", "expr": "candle is bearish (close < open), lowest among candidates, max(open-close) range, near an HTF support level (2016)"},
    {"id": "c2", "expr": "2022: nearest-to-price down-close candle(s) in a run, qualified by an imbalance left on the move away"},
    {"id": "c3", "expr": "validated (2016) when a later candle's high trades through the OB candle's high"},
    {"id": "c4", "expr": "NOT fresh-only: HTF blocks and 2022 doctrine both permit repeated return visits"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["order-block-criteria","bearish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","discount-array","bullish-fvg","propulsion-block"],
  "sources": ["ICT-2016-ORDERBLOCKS","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP13","ICT-2022-MENTORSHIP-EP16","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP19","ICT-2022-MENTORSHIP-EP21","ICT-2022-MENTORSHIP-EP30","ICT-2022-MENTORSHIP-EP35"]
}
```

## Visual Pattern

```
   bullish OB (2016 reading):

   ▼               ← lowest down-close candle, most open-to-close range,
   ▼                 near an HTF support level
                   body: open at top, close at bottom
                   ▲
                   ▲   ← later candle trades through the OB candle's high
                   ▲       (validation)
                       ▲
                       ▲   ← imbalance left behind (2022 validity requirement)
                       ▲

   On retest: entry at the body extreme nearest price (high/open), NOT at MT.
   MT is the allowance/invalidation line, not the plan.
```

## Timeframes

M1 through monthly. 2016: "you can refine these as small as you want by going into as low as a
five minute chart" (ICT-2016-ORDERBLOCKS [33:38]). 2022 trades M1 blocks directly: "we're looking at
one minute candles — that is the order block with a fair value — got buy it there" (EP19 [103:45]).

## Examples

**Example 1 — H1 bullish OB (2016-style selection):**
- 14:00 NY H1 bearish candle, the lowest among recent down-close candidates with the greatest
  open-to-close range, sitting near an old daily low: O=1.0830, C=1.0820, L=1.0815, H=1.0832. Body:
  [1.0820, 1.0830]. MT = 1.0825.
- 15:00 NY: bullish displacement; later candle's high trades through 1.0832 (validation).
- Entry on retest at the candle's high/open (1.0830 or a few pips above), not at MT. MT (1.0825) is
  the depth price should ideally not exceed. SL below the candle's low/close (primarily the close),
  with an optional buffer.

## Common Mistakes

- **Calling it "the last candle before displacement."** ICT rejects this framing outright in 2022
  (EP12 [44:09], EP18 [40:13–40:41]); the 2016 rule is a selection among candidates (lowest, most
  range, near support), not a position rule.
- **Entering at MT by default.** MT is the tolerance/invalidation depth, not the entry: "ideally, the
  best order blocks will not see price trade down below the midway point of the entire body of the
  candle" (ICT-2016-ORDERBLOCKS [09:59]); the entry is the body extreme nearest price (high/open):
  "key off your demo entries on the down candles body of the candle, the high or the opening in
  this instance" [07:54–08:01].
  In 2022: "the low of the daily order block, the open of the order block and the mean threshold
  halfway, and then the high of the order block being the less likely level [to be] traded to"
  (EP21 [04:51]).
- **Requiring freshness.** Both eras tolerate repeated visits, especially on HTF; see Formal Criteria.
- **Requiring an engulfing/doji candle.** ICT states no candlestick-pattern requirement exists — only
  the imbalance, the down-close candle, and the narrative: "there is no engulfing candle, does this
  [dojis — auto-caption renders "does this"] forget all that — you don't need that, okay? It's the
  gap plus the down closed candle plus the idea that's likely to go for [buy] side liquidity, that's
  it." (EP13 [17:22–17:52]).

## Related Concepts

- [order-block-criteria](order-block-criteria.md), [bearish-order-block](bearish-order-block.md), [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md).
- [mean-threshold](../27-equilibrium/mean-threshold.md), [discount-array](../05-pd-arrays/discount-array.md).
- [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md), [propulsion-block](propulsion-block.md).

## Citations

- `ICT-2016-ORDERBLOCKS` [00:59–01:08] definition; [02:20–02:27] "near a support level" = HTF old high/low; [07:54–08:01], [09:43–09:46] entry at the down candle's body/high/open; [09:59], [10:35] MT as the depth not to exceed; [10:44–10:58], [02:00–02:06] stop placement and stop-raise; [05:47–05:49] bodies, not wicks; [22:08] a monthly block re-traded repeatedly; [33:38] M5 refinement.
- `ICT-2022-MENTORSHIP-EP03` [24:16–24:45] change in the state of delivery; [15:12] the open as the price level.
- `ICT-2022-MENTORSHIP-EP12` [24:22–24:54], [43:34], [44:09] rejects the last-candle framing.
- `ICT-2022-MENTORSHIP-EP13` [17:22–17:52] imbalance requirement.
- `ICT-2022-MENTORSHIP-EP16` [07:29] opening price is the order block.
- `ICT-2022-MENTORSHIP-EP18` [40:13–41:12], [46:23–46:48] imbalance mandatory, change-in-state-of-delivery, rejects fresh-zone premise.
- `ICT-2022-MENTORSHIP-EP19` [103:45] M1 order block traded directly.
- `ICT-2022-MENTORSHIP-EP21` [04:51] level ranking: low, open, MT, high.
- `ICT-2022-MENTORSHIP-EP30` [04:55] a block traded into multiple times.
- `ICT-2022-MENTORSHIP-EP35` [00:36] low/open/MT as the three sensitive areas.

# Mean Threshold

**Category:** 27-equilibrium
**Aliases:** MT, mean threshold of an order block, OB midpoint, half the order block
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-ORDERBLOCKS, ICT-2016-MITIGATE-LOSING-TRADES, ICT-2016-PROPULSION-BLOCK, ICT-2016-INSTITUTIONAL-ORDER-FLOW, ICT-2017-SWING-REDUCE-RISK, ICT-2022-MENTORSHIP-EP19, ICT-2022-MENTORSHIP-EP35, ICT-2016-NO-FEAR-LOSING
**Tags:** equilibrium, mean-threshold, ob, validity

## Definition

Mean threshold (MT) is the **50% midpoint of an order block's body** (open-to-close, never the wicks): "You're going to measure the open to the close on the down candle to measure where the middle of it is. Do not use the wicks." (`ICT-2016-ORDERBLOCKS` [10:08]–[10:13]). ICT's **primary use of MT is as a validity line that should not be violated**, not as his default entry reference: "Ideally, the best order blocks will not see price trade down below the midway point of the entire body of the candle." ([09:59]). The entry he names is the open of the down candle, with MT as the line he watches: "We identify the entry at the open of the down candle. That's our buy point ... But we want to focus our attention in the midway point of that down candle. That's going to be in the form of the mean threshold." ([09:43]–[09:56]).

## Formal Criteria

For a bullish OB:

- The OB candle has open `O`, close `C`, high `H`, low `L`.
- Bullish OB body = the down-candle body before the bullish displacement: from `O` to `C` (where `C < O`).
- MT = `(O + C) / 2` — body midpoint only. **No full-range `(H + L) / 2` variant exists in either corpus** — ICT is explicit: "Do not use the wicks. Don't use the very high or the very low." ([10:13]–[10:14]). (An adjacent phrase — "middle of the range or mean threshold," `ICT-2016-PROPULSION-BLOCK` [01:41] — sits beside "half of the body's height," [01:28], confirming "range" there means the candle's body, not its wick-to-wick high/low.)
- MT's stated role is a **must-not-be-violated-much line**: "you just don't want to see price drive down deeper than the mean threshold by very much ... the better order blocks won't do it at all." ([10:28]–[10:40]); "we don't want to see the middle of the down candle on a bullish order block be violated" (`ICT-2016-MITIGATE-LOSING-TRADES` [01:33]); the propulsion block's definitional test is the same: "It should never see the mean threshold break." (`ICT-2016-PROPULSION-BLOCK` [01:24]).
- ICT also uses MT on a closing basis for invalidation: "The middle of that candle, we're going to be using that as a mean threshold. In other words, we don't want to see that violated on a closing basis." (`ICT-2016-NO-FEAR-LOSING` [03:29]–[03:34], Oct 2016).
- MT does occur as an entry reference on HTF order blocks: "entering up at that mean threshold from the older block from October 2009" (`ICT-2017-SWING-REDUCE-RISK` [22:21]). It is a legitimate entry reference, not "ICT's primary entry rather than the far edge" as a general rule.
- In 2022, MT is listed as one of several price targets inside an OB, alongside the candle's low, open, and high: "you have the candle low, the open, the mean threshold, half the order block, and you have the high" (`ICT-2022-MENTORSHIP-EP19` [80:56]).

For bearish OB: symmetric, body from `O` to `C` with `C > O`.

## Formula / Math

```
# Body midpoint — the only form ICT states:
MT = (open(OB_candle) + close(OB_candle)) / 2

# NOT ICT's: a full-range (H + L) / 2 variant. "Do not use the wicks."
```

## Machine-Readable

```json
{
  "id": "mean-threshold",
  "category": "27-equilibrium",
  "aliases": ["MT", "mean-threshold-of-an-order-block", "OB-midpoint"],
  "criteria": [
    {"id": "c1", "expr": "MT == (open + close) / 2 of OB candle (body only)"},
    {"id": "c2", "expr": "full_range_variant == false"},
    {"id": "c3", "expr": "primary_role == validity_line (should_not_be_violated_much); entry is one of several listed uses"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equilibrium-definition","bullish-order-block","bearish-order-block","order-block-criteria","propulsion-block"],
  "sources": ["ICT-2016-ORDERBLOCKS","ICT-2016-MITIGATE-LOSING-TRADES","ICT-2016-PROPULSION-BLOCK","ICT-2016-INSTITUTIONAL-ORDER-FLOW","ICT-2017-SWING-REDUCE-RISK","ICT-2022-MENTORSHIP-EP19","ICT-2022-MENTORSHIP-EP35","ICT-2016-NO-FEAR-LOSING"]
}
```

## Visual Pattern

```
   bullish OB candle (down-close, last bearish before displacement up):

          H
          ─────
          │
          O   ← top of body — ICT's stated entry reference
          ───── MT (50% of body — the line that "should not be violated by very much")
          C   ← bottom of body
          │
          ─────
          L

   Do not use H or L for MT — body only.
```

## Timeframes

All TFs that support OBs. (M1 OBs being noisy is library guidance, not an ICT statement in either corpus.)

## Examples

**Example 1 — MT as the validity line, open as the entry (ICT's own framing):**
- H1 bullish OB candle: O=1.0830, C=1.0820.
- Entry reference = the open, 1.0830 ("that's our buy point," [09:43]); MT = (1.0830+1.0820)/2 = 1.0825 is the line that should not be violated by much ([10:28]).

**Example 2 — MT as a direct entry on an HTF block:**
- A much older, higher-timeframe order block is retested; ICT enters "at that mean threshold from the older block" (`ICT-2017-SWING-REDUCE-RISK` [22:21]) — a legitimate but HTF-specific usage, not stated as the general rule.

## Common Mistakes

- **Using the full range `(H + L) / 2` as an alternate MT.** ICT states the opposite directly: "Do not use the wicks." No full-range variant is supported by either corpus.
- **Treating MT as ICT's primary, default entry — "rather than the OB's far edge."** His stated primary role is a line that "should not be violated by very much" or "on a closing basis"; the open of the candle is the entry reference he names in the same lecture (`ICT-2016-ORDERBLOCKS` [09:43]–[09:56]). MT-as-entry does occur (HTF blocks, `ICT-2017-SWING-REDUCE-RISK` [22:21]) but is not "the" primary rule.
- **Confusing body MT and a range MT.** Only the body version is ICT's.
- **Dating this to 2017.** The underlying teaching is taught by Oct 2016 — most explicitly, "The middle of that candle, we're going to be using that as a mean threshold" (`ICT-2016-NO-FEAR-LOSING` [03:29], Oct 2016, Month 02) and "we don't want to see the middle of the down candle on a bullish order block be violated" (`ICT-2016-MITIGATE-LOSING-TRADES` [01:33], Oct 2016, Month 02) — and Nov 2016 ("we always look at the middle of the up candle mean threshold," `ICT-2016-INSTITUTIONAL-ORDER-FLOW` [05:01]).

## Related Concepts

- [equilibrium-definition](equilibrium-definition.md) — the broader 50%-midpoint concept; EQ and MT are related but not interchangeable (EQ = dealing-range/leg/void midpoint; MT = order-block body midpoint specifically).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md).
- [propulsion-block](../07-order-blocks/propulsion-block.md) — defined by never seeing its own mean threshold break.

## Citations

- `ICT-2016-ORDERBLOCKS` [09:43]–[10:58] — entry at the open; MT as the don't-violate-much line; body-only measurement; stop below the low or the close (Dec 2016).
- `ICT-2016-MITIGATE-LOSING-TRADES` [01:33]–[03:33] — MT must not be violated; stop placed just below MT (worked losing-trade example, Oct 2016).
- `ICT-2016-NO-FEAR-LOSING` [03:29]–[03:34] — "the middle of that candle, we're going to be using that as a mean threshold ... we don't want to see that violated on a closing basis" (Oct 2016).
- `ICT-2016-PROPULSION-BLOCK` [01:24]–[01:46] — propulsion block defined by never breaking its own mean threshold.
- `ICT-2016-INSTITUTIONAL-ORDER-FLOW` [05:01] — "we always look at the middle of the up candle mean threshold" (Nov 2016).
- `ICT-2017-SWING-REDUCE-RISK` [22:21] — MT used directly as an HTF entry reference (Feb 2017).
- `ICT-2022-MENTORSHIP-EP19` [78:54]–[80:56] — MT listed among several OB price targets.
- `ICT-2022-MENTORSHIP-EP35` [00:36] — MT among the "three sensitive areas" (low, open, mean threshold).

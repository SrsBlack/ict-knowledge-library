# Liquidity Void vs FVG — Disambiguation

**Category:** 06-fair-value-gaps
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2016-LIQUIDITY-VOIDS, ICT-2017-HTF-PD-ARRAYS, ICT-2022-MENTORSHIP-EP38
**Tags:** fvg, liquidity-void, disambiguation, terminology

⚠ **Rewritten 2026-11-09 against ICT's own words.** The prior version gave a liquidity void
fixed thresholds (≥ 80 % directional closes, ≤ 30 % pullback, "5+ bars") and said a void
contains **1-3** FVGs on the same chart. None of those numbers is in the corpus. Searched both corpora
(153 2016-17/2020-21 packets, 40 captioned 2022 Mentorship episodes) — see
[liquidity-void](../02-liquidity/liquidity-void.md), Formula / Math, for the search (bar-count search, "five/5 candles|bars" near void: no hits either). ICT's main
link between the two is a **timeframe** link.
Re-dated 2017 → 2016: both concepts and their relationship are taught in December 2016.

## Definition

**Short version:** ICT links the two by **timeframe**: a gap printed on the chart you are studying is
*typically* seen on a lower timeframe as several one-sided candles — a liquidity void. On a single
chart he still lists them as separate PD arrays in his hierarchy (`ICT-2017-HTF-PD-ARRAYS` [19:05],
[20:16]–[20:28]).

- **FVG** — "a range in price delivery where one side of the market liquidity is offered and
  typically confirmed with a liquidity void on the lower timeframe charts in the same range of
  price" (`ICT-2016-FVG-REINFORCED` [00:36]–[00:46]).
- **Liquidity void** — "a range in price delivery where one side of the market liquidity is shown in
  wide or long one-sided ranges or candles" (`ICT-2016-LIQUIDITY-VOIDS` [00:57]).
- **The link, in ICT's words:** "if we're studying a specific timeframe, the gap occurs on the
  timeframe you're looking at. You can break this down further into smaller timeframes, but in the
  smaller timeframes, you'll probably end up seeing a liquidity void where the gap would be indicated
  here on this timeframe" (`ICT-2016-FVG-REINFORCED` [05:04]–[05:14]); "on a lower timeframe, it would
  many times appear as a liquidity void where it's multiple candles that create that open space of
  range" ([05:26]). He then walks through "the overlap of liquidity voids and fair value gaps" on a chart
  ([09:43]); the arrays "overlap … in a lot of different ways" ([09:01]).

So when an FVG and a void cover the same range on two timeframes, ask **which timeframe's candles you
are describing**. ICT's hedges ("typically", "probably", "many times") and his separate hierarchy slots
mean this is a tendency, not an identity.

## Formal Criteria

### FVG (geometric, on the chart being studied)

- 3 candles, `L_{n+1} > H_{n-1}` (bullish) or `H_{n+1} < L_{n-1}` (bearish). See
  [fair-value-gap](fair-value-gap.md).

### Liquidity void (descriptive)

- Long or wide one-sided candles where price was delivered in one direction only
  (`ICT-2016-LIQUIDITY-VOIDS` [00:57], [03:08]: "long bodied candles where price has only been
  delivered on the downside and has a small little gap in between the two biggest down candles").
- ICT gives **no** directional-close percentage, pullback fraction, or minimum bar count.

### Relationship

- An FVG on timeframe T is *typically* seen as a liquidity void on a lower timeframe over the same
  price range ([00:42], [05:14]). "Typically" / "probably" / "many times" are ICT's hedges — it is a
  tendency, not a rule.
- ICT gives no count of FVGs inside a void. He does point to "a small little gap in between the two
  biggest down candles" inside his one-minute void (`ICT-2016-LIQUIDITY-VOIDS` [03:08]) and to a gap
  inside the lower-timeframe void in the FVG drill (`ICT-2016-FVG-REINFORCED` [10:49]–[11:05]).
- On one chart, ICT ranks them as separate arrays — "the next order of hierarchy is liquidity void …
  The next thing, is there a fair value gap?" (`ICT-2017-HTF-PD-ARRAYS` [20:16]–[20:28]) — and both
  can be present: "there is a gap and it may be a liquidity void and a gap" ([28:30]).

## Formula / Math

```
# ICT's relationship (ICT-2016-FVG-REINFORCED [00:42], [05:14], [05:26]):
fvg(tf=T, range=R)  ~typically~  liquidity_void(tf=lower_than_T, range≈R)

# NOT ICT's (removed 2026-11-09, no corpus source):
#   directional_close_pct(span) >= 0.8
#   max_pullback_pct(span) <= 0.3
#   void.bar_count >= 5
#   "void contains 1-3 FVGs on the same chart"   (a gap inside a void is shown; the count is not)
```

Any numeric void detector is the user's own operationalisation and should be labelled that way.

## Machine-Readable

```json
{
  "id": "liquidity-void-vs-fvg",
  "category": "06-fair-value-gaps",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "fvg == 3-candle wick gap on the timeframe being studied"},
    {"id": "c2", "expr": "liquidity_void == wide/long one-sided candles; no numeric threshold in ICT"},
    {"id": "c3", "expr": "fvg on timeframe T typically appears as a liquidity void on a lower timeframe over the same range"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","liquidity-void","imbalance-definition","displacement-definition","gap-classification"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2016-LIQUIDITY-VOIDS","ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-EP38"]
}
```

## Visual Pattern

```
   Daily (timeframe T)            Lower timeframe, same price range
   ───────────────────            ─────────────────────────────────
        │  c3                          █
        │                              █
   ░░░░░░░  ← FVG (c1 high → c3 low)   █   ← several one-sided candles
        █  c2                          █      = liquidity void
        │  c1                          █
```

## Timeframes

All. The relationship is relative: whatever timeframe shows the FVG, a lower one tends to show the void.

## Examples

**ICT's own drill (`ICT-2016-FVG-REINFORCED` [09:43]–[10:54]):** on a five-minute chart at the
104.75 level (the caption says "euro dollar"; "104.75" is read as spoken pips), price runs above an
old high that also sits in the fair value gap he has been marking — "it's trading into the fair value gap" ([10:47]) — and
ICT points out the lower-timeframe picture of that same gap: "I said on the lower time frames, many
times this will create a liquidity void" ([10:49]).

## Common Mistakes

- **Applying invented thresholds as ICT's rule.** The 80 % / 30 % / 5-bar numbers were this library's
  own and have been removed.
- **Counting the HTF FVG and the LTF void over the same range as two confirmations.** When they are the
  same range seen on two timeframes, that is one delivery (library guidance, from ICT's timeframe link
  [05:14]). This does not merge the two PD arrays in general — ICT ranks them separately
  (`ICT-2017-HTF-PD-ARRAYS` [20:16]–[20:28]).
- **Insisting a void must refill.** Era-split: 2016 "price typically will want to revisit this porous
  range" (`ICT-2016-LIQUIDITY-VOIDS` [01:09]), "there's no specific time limit" ([02:19]); 2022 "I'm not
  trying to insist that these imbalances completely rebalance" (`ICT-2022-MENTORSHIP-EP38` [04:56]–[05:26]).
  See [liquidity-void](../02-liquidity/liquidity-void.md).

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [liquidity-void](../02-liquidity/liquidity-void.md), [gap-classification](../09-displacement/gap-classification.md), [imbalance-definition](../26-imbalance/imbalance-definition.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-REINFORCED` [00:36]–[00:46], [05:04]–[05:26], [09:01], [09:43], [10:47]–[11:05].
- `ICT-2016-LIQUIDITY-VOIDS` [00:57], [01:09], [02:19], [03:08].
- `ICT-2017-HTF-PD-ARRAYS` [19:05], [20:16]–[20:28], [28:30].
- `ICT-2022-MENTORSHIP-EP38` [04:56]–[05:26].

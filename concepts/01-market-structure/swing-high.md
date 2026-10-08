# Swing High

**Category:** 01-market-structure
**Aliases:** pivot high, fractal high, short-term high (STH), intermediate-term high (ITH), long-term high (LTH), old high
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-INSTITUTIONAL-SWING-POINTS, ICT-2016-EQUILIBRIUM-PREMIUM, ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP31, ICT-2022-MENTORSHIP-EP40, ICT-2017-OTE, ICT-2017-OPEN-FLOAT-L12
**Tags:** structure, pivot, fractal, swing, foundational

## Definition

A swing high is a local price peak — a candle (or bar) whose high is greater than the highs of the candles to its immediate left and right. ICT credits the 3-candle swing definition to his own mentor: "That's what I learned from my mentor Larry Williams." (`ICT-2017-INSTITUTIONAL-SWING-POINTS` [00:56]). Swing highs are the building blocks of market structure — every structure break/shift and liquidity raid is referenced against a swing high or swing low.

## Formal Criteria

The 3-bar ICT definition:

- A candle at index `n` qualifies as a swing high if and only if `H_n > H_{n-1}` AND `H_n > H_{n+1}`.
- Wicks count — the comparison uses the candle high, not the close or body: "it does not matter what the close of the candles are it has absolutely no bearing on what I'm showing you here because the swing points are where liquidity is going to be placed" (`ICT-2022-MENTORSHIP-EP05` [14:42]).
- The swing high is confirmed only after candle `n+1` closes: "as soon as this candle closed here i'm gonna go right here at this candle" (`ICT-2022-MENTORSHIP-EP31` [06:31]).
- Not a 5-candle Williams fractal: "This is why I do not use the Williams fractal that requires five candles. ... I only need three candles." (`ICT-2016-EQUILIBRIUM-PREMIUM` [11:53]–[11:58]); restated in 2022 ("you do not need a Williams fractal", EP10 [18:31]).

ICT aggregates swing points into a fractal hierarchy with **two routes** to each higher tier:

- **Short-Term High (STH):** any 3-bar swing high.
- **Intermediate-Term High (ITH) — route 1 (geometric):** an STH whose adjacent STHs are both lower — "term high is any high that has a short-term high to the left of it and to the right of it, think of it like a head and shoulders top formation" (`ICT-2017-OPEN-FLOAT-L12` [20:15]–[20:21]).
- **Intermediate-Term High (ITH) — route 2 (rebalance, 2022):** a high PRINTED BY a move that trades up to rebalance an imbalance is immediately an ITH, independent of the geometric test — the imbalance being rebalanced sits elsewhere on the chart, not at the high itself: "intermediate term highs there's two classifications — it is a short-term High that has a lower short-term High to the left of it and a lower short-term High to the right of it, **or** — and this is the main one here — it trades back up to rebalance an[d, ASR] imbalance that immediately becomes an inter[mediate, ASR 'interm'] term high" (`ICT-2022-MENTORSHIP-EP12` [41:23]). ICT calls the rebalance route "the main one," not a secondary shortcut.
- **Long-Term High (LTH):** an ITH whose adjacent ITHs are both lower — "every time you see a intermediate term high that has a lower intermediate term high to the left of it and intermediate term high to the right of it, that's actually a long-term high" (`ICT-2017-OPEN-FLOAT-L12` [20:27]–[20:31]).

This produces: LTH ⊃ ITH ⊃ STH, with the ITH tier reachable by either the geometric or the rebalance route.

A 2016-specific wrinkle for the equilibrium setup (not part of the swing definition itself): after a swing high forms, ICT additionally waits for a fourth, move-away candle before acting: "Once you see a high form, you need four candles. ... one candle to the left, one candle in the center of the most highest one, then a lower candle to the right. That's a swing high, and then you got to see price go lower." (`ICT-2016-EQUILIBRIUM-DISCOUNT` [10:04]–[10:15]). The fourth candle confirms the move away from the swing — it is not part of the 3-candle swing test itself.

## Formula / Math

```
swing_high(n) := H_n > H_{n-1} AND H_n > H_{n+1}

short_term_high(n) := swing_high(n)

# ITH — route 1 (geometric):
intermediate_term_high_geometric(n) := short_term_high(n)
                                        AND H_n > H_{prev_STH}
                                        AND H_n > H_{next_STH}

# ITH — route 2 (rebalance, ICT calls this "the main one"):
intermediate_term_high_rebalance(n) := high_n rebalances_an_imbalance

intermediate_term_high(n) := intermediate_term_high_geometric(n)
                              OR intermediate_term_high_rebalance(n)

long_term_high(n) := intermediate_term_high(n)
                      AND H_n > H_{prev_ITH}
                      AND H_n > H_{next_ITH}
```

Where `H_n` is the high (including upper wick) of candle at index `n`.

## Machine-Readable

```json
{
  "id": "swing-high",
  "category": "01-market-structure",
  "aliases": ["pivot-high", "fractal-high", "STH", "ITH", "LTH"],
  "criteria": [
    {"id": "c1", "expr": "H_n > H_{n-1}"},
    {"id": "c2", "expr": "H_n > H_{n+1}"},
    {"id": "c3", "expr": "ITH := geometric_route(n) OR rebalances_imbalance(n)"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["swing-low","bos-bullish","mss","internal-structure","external-structure"],
  "sources": ["ICT-2017-INSTITUTIONAL-SWING-POINTS","ICT-2016-EQUILIBRIUM-PREMIUM","ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP31","ICT-2022-MENTORSHIP-EP40","ICT-2017-OTE","ICT-2017-OPEN-FLOAT-L12"]
}
```

## Visual Pattern

```
    n
    |
   /|\
  / | \
 /  |  \
n-1     n+1
```

Three-candle pattern. The middle candle (`n`) has a high strictly greater than both neighbors. The body color does not matter; only the high price. An ITH can also be the high formed when price trades up to rebalance an imbalance — no neighboring-STH geometry required for that route.

## Timeframes

Applies to every timeframe ICT teaches: M1 through MN1. Higher-timeframe swing highs carry more structural weight. On lower timeframes, noise creates many short-term highs that get aggregated into intermediate-term and long-term highs as you zoom out.

## Examples

**Example 1 — generic 3-bar pattern:**
- Candle n-1 high = 1.0850
- Candle n high = 1.0875
- Candle n+1 high = 1.0860
- → n is a swing high (a short-term high).

**Example 2 — STH that is NOT an ITH by the geometric route, but is a plain 3-bar pattern:**
- "we have a three bar pattern — one candle, the lower candle to the left, a lower candle to the right — that's a swing high, pretty simple stuff" (`ICT-2022-MENTORSHIP-EP40` [05:17]).

**Example 3 — ITH by the rebalance route:**
- Price rallies up into a prior imbalance (e.g. a bearish FVG) and turns down.
- The high printed by that rebalancing move is immediately an ITH, whether or not it has lower STHs beside it (`ICT-2022-MENTORSHIP-EP12` [41:23]) — the imbalance being rebalanced is the earlier gap it rallied into, not something sitting at the high itself.

## Common Mistakes

- **Using close instead of high.** ICT swing definitions use the candle high (wick top), not the close.
- **Calling an unconfirmed candle a swing high.** A swing high is only confirmed after the next candle closes.
- **Treating the geometric test as the only route to ITH status.** ICT names the rebalance route "the main one" for intermediate-term highs (EP12 [41:23]); a page or engine that only implements the geometric (STH-neighbor) test is missing ICT's primary ITH class.
- **Equal highs.** Two adjacent equal highs do NOT form a single swing high; they form an EQH liquidity pool. See [equal-highs](../02-liquidity/equal-highs.md).

## Related Concepts

- [swing-low](swing-low.md) — mirror concept on the sell side.
- [bos-bullish](bos-bullish.md) — references a prior swing high.
- [mss](mss.md) — structure shift referenced against swing highs/lows.
- [internal-structure](internal-structure.md) — swing highs inside a larger range.
- [external-structure](external-structure.md) — higher-order swings; see [dealing-range](../05-pd-arrays/dealing-range.md) for ICT's actual range anchors (most recent energetic swing, not LTH/LTL).
- [equal-highs](../02-liquidity/equal-highs.md) — what two equal-priced highs form instead of a single swing.

## Citations

- `ICT-2017-INSTITUTIONAL-SWING-POINTS` [00:32]–[00:56] — 3-bar definition; Larry Williams attribution (Jan 2017).
- `ICT-2016-EQUILIBRIUM-PREMIUM` [11:52]–[11:58] — "I only need three candles," not the 5-candle Williams fractal (Sep 2016).
- `ICT-2016-EQUILIBRIUM-DISCOUNT` [09:49]–[10:15] — 4th move-away candle for the equilibrium setup specifically.
- `ICT-2022-MENTORSHIP-EP05` [14:02]–[14:42] — 3-candle pattern, wicks count, no bearing on close.
- `ICT-2022-MENTORSHIP-EP10` [18:31] — restates "you do not need a Williams fractal."
- `ICT-2022-MENTORSHIP-EP12` [41:23] — ITH two classifications; rebalance route called "the main one."
- `ICT-2022-MENTORSHIP-EP31` [06:31] — confirmation on candle close.
- `ICT-2022-MENTORSHIP-EP40` [05:17] — "three bar pattern," plain statement.
- `ICT-2017-OPEN-FLOAT-L12` [20:15]–[20:31] — "any high that has a short-term high to the left of it and to the right of it, think of it like a head and shoulders top formation ... that's actually a long-term high" — ITH route 1 (geometric) and the LTH tier (Jan 2017).
- `ICT-2017-OTE` [34:20]–[34:27] — "a high that has two lower highs on either side of it ... as it nests out" — an independent restatement of the same geometric nesting.

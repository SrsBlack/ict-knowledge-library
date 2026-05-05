# Swing High

**Category:** 01-market-structure
**Aliases:** pivot high, fractal high, short-term high (STH), intermediate-term high (ITH), long-term high (LTH)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-MENTORSHIP-OVERVIEW, ICT-2017-CHARTER-OVERVIEW
**Tags:** structure, pivot, fractal, swing, foundational

## Definition

A swing high is a local price peak — a candle (or bar) whose high is greater than the highs of the candles to its immediate left and right. ICT uses swing highs as the building blocks of market structure: every break-of-structure (BOS), change-of-character (CHoCH), and liquidity raid is referenced against a swing high or swing low.

## Formal Criteria

The simplest (3-bar) ICT definition:

- A candle at index `n` qualifies as a swing high if and only if `H_n > H_{n-1}` AND `H_n > H_{n+1}`.
- Wicks count — the comparison uses the candle high, not the close or body.
- The swing high is confirmed only after candle `n+1` closes; it is unconfirmed in real time on the active candle.

ICT also teaches a fractal hierarchy by aggregating swing points:

- **Short-Term High (STH):** any 3-bar swing high.
- **Intermediate-Term High (ITH):** an STH whose adjacent STHs are both lower than it.
- **Long-Term High (LTH):** an ITH whose adjacent ITHs are both lower than it.

This produces a recursive structure: LTH ⊃ ITH ⊃ STH.

## Formula / Math

```
swing_high(n) := H_n > H_{n-1} AND H_n > H_{n+1}

short_term_high(n)        := swing_high(n)
intermediate_term_high(n) := short_term_high(n)
                              AND H_n > H_{prev_STH}
                              AND H_n > H_{next_STH}
long_term_high(n)         := intermediate_term_high(n)
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
    {"id": "c2", "expr": "H_n > H_{n+1}"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["swing-low","bos-bullish","choch-bullish","internal-structure","external-structure"],
  "sources": ["ICT-2016-MENTORSHIP-OVERVIEW","ICT-2017-CHARTER-OVERVIEW"]
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

Three-candle pattern. The middle candle (`n`) has a high strictly greater than both neighbors. The body color does not matter; only the high price.

## Timeframes

Applies to every timeframe ICT teaches: M1 through MN1. Higher-timeframe swing highs carry more structural weight (a daily swing high is more significant than an M5 swing high). On lower timeframes, noise creates many short-term highs that get aggregated into intermediate-term and long-term highs as you zoom out.

## Examples

**Example 1 — generic 3-bar pattern:**
- Candle n-1 high = 1.0850
- Candle n high = 1.0875
- Candle n+1 high = 1.0860
- → n is a swing high (a short-term high).

**Example 2 — STH that is NOT an ITH:**
- Three consecutive STHs at 1.0875, 1.0890, 1.0880.
- The middle STH (1.0890) IS an ITH because both adjacent STHs are lower.
- The first STH (1.0875) is NOT an ITH because the next STH is higher.

## Common Mistakes

- **Using close instead of high.** ICT swing definitions use the candle high (wick top), not the close. A long upper wick that exceeds neighboring highs creates a valid swing high.
- **Calling an unconfirmed candle a swing high.** A swing high is only confirmed after the next candle closes. On the live candle you have at most a candidate.
- **Confusing STH/ITH/LTH levels.** Most retail platforms only mark STHs; the fractal hierarchy is what gives swing highs their structural meaning in ICT.
- **Equal highs.** Two adjacent equal highs do NOT form a single swing high; they form an EQH liquidity pool. See [equal-highs](../02-liquidity/equal-highs.md).

## Related Concepts

- [swing-low](swing-low.md) — mirror concept on the sell side.
- [bos-bullish](bos-bullish.md) — defined as a close above a prior swing high.
- [choch-bullish](choch-bullish.md) — first close above a swing high after a bearish leg.
- [internal-structure](internal-structure.md) — swing highs inside a larger range.
- [external-structure](external-structure.md) — the LTH/LTL swings that define the larger range itself.
- [equal-highs](../02-liquidity/equal-highs.md) — what two equal-priced highs form instead of a single swing.

## Citations

- `ICT-2016-MENTORSHIP-OVERVIEW` — original 3-bar swing definition.
- `ICT-2017-CHARTER-OVERVIEW` — STH / ITH / LTH fractal hierarchy formalized.

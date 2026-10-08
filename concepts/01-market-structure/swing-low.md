# Swing Low

**Category:** 01-market-structure
**Aliases:** pivot low, fractal low, short-term low (STL), intermediate-term low (ITL), long-term low (LTL), old low
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-INSTITUTIONAL-SWING-POINTS, ICT-2016-EQUILIBRIUM-PREMIUM, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP12, ICT-2017-OPEN-FLOAT-L12
**Tags:** structure, pivot, fractal, swing, foundational

## Definition

A swing low is a local price trough — a candle whose low is less than the lows of the candles to its immediate left and right. The mirror image of a swing high. Swing lows are the structural anchors below price; ICT references them for structure shifts and sell-side liquidity: "One candle with a higher candle to the left of it and a higher candle to the right of it. That's a swing low. That's what I learned from my mentor Larry Williams." (`ICT-2017-INSTITUTIONAL-SWING-POINTS` [00:50]–[00:56]).

## Formal Criteria

3-bar definition:

- Candle `n` is a swing low iff `L_n < L_{n-1}` AND `L_n < L_{n+1}`.
- Wicks count — uses candle low, not body or close: "a swing low prior to 8:30 — that's a candle that has a higher low to the left and a higher low to the right of it, it's three candles again, it does not matter what the close of the candles are" (`ICT-2022-MENTORSHIP-EP05` [14:42]).
- Confirmation requires candle `n+1` to close: "this swing low forms once this candle closes" (`ICT-2022-MENTORSHIP-EP03` [17:49]).
- Not a 5-candle Williams fractal (mirrors [swing-high](swing-high.md)): "This is why I do not use the Williams fractal that requires five candles. ... I only need three candles." (`ICT-2016-EQUILIBRIUM-PREMIUM` [11:53]–[11:58], Sep 2016).

ICT aggregates swing lows into the same two-route hierarchy as swing highs:

- **Short-Term Low (STL):** any 3-bar swing low. The plain 3-candle definition — "it creates a swing low, that means a low with a higher low to the right of it and a higher low to the left of it, so it's three candles that make up a swing" (`ICT-2022-MENTORSHIP-EP10` [18:04]) — is this STL test, not the ITL test below.
- **Intermediate-Term Low (ITL) — route 1 (geometric):** an STL whose adjacent STLs are both higher: "now invert that and you'll have the same thing that would be said for an intermediate term low or a long-term low" (`ICT-2017-OPEN-FLOAT-L12` [20:36]–[20:42]); "intermediate term low has a higher short-term low to the right of it and a higher short-term low to the left of it" (`ICT-2022-MENTORSHIP-EP12` [14:15]).
- **Intermediate-Term Low (ITL) — route 2 (rebalance, 2022):** a low formed by rebalancing an imbalance immediately becomes an ITL, independent of the geometric test — "anytime an imbalance like this big candle up is rebalanced that becomes an intermediate term low" (`ICT-2022-MENTORSHIP-EP12` [16:58]); "this intermediate term low forms by rebalancing" (EP12 [14:15]).
- **Long-Term Low (LTL):** an ITL whose adjacent ITLs are both higher (geometric route only is stated for this tier; `ICT-2017-OPEN-FLOAT-L12` [20:36]–[20:42]).

## Formula / Math

```
swing_low(n) := L_n < L_{n-1} AND L_n < L_{n+1}

short_term_low(n) := swing_low(n)

# ITL — route 1 (geometric):
intermediate_term_low_geometric(n) := short_term_low(n)
                                       AND L_n < L_{prev_STL}
                                       AND L_n < L_{next_STL}

# ITL — route 2 (rebalance):
intermediate_term_low_rebalance(n) := low_n rebalances_an_imbalance

intermediate_term_low(n) := intermediate_term_low_geometric(n)
                             OR intermediate_term_low_rebalance(n)

long_term_low(n) := intermediate_term_low(n)
                     AND L_n < L_{prev_ITL}
                     AND L_n < L_{next_ITL}
```

Where `L_n` is the low (including lower wick) of candle at index `n`.

## Machine-Readable

```json
{
  "id": "swing-low",
  "category": "01-market-structure",
  "aliases": ["pivot-low", "fractal-low", "STL", "ITL", "LTL"],
  "criteria": [
    {"id": "c1", "expr": "L_n < L_{n-1}"},
    {"id": "c2", "expr": "L_n < L_{n+1}"},
    {"id": "c3", "expr": "ITL := geometric_route(n) OR rebalances_imbalance(n)"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["swing-high","bos-bearish","mss","internal-structure","external-structure"],
  "sources": ["ICT-2017-INSTITUTIONAL-SWING-POINTS","ICT-2016-EQUILIBRIUM-PREMIUM","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP12","ICT-2017-OPEN-FLOAT-L12"]
}
```

## Visual Pattern

```
n-1     n+1
 \  |  /
  \ | /
   \|/
    |
    n
```

Middle candle (`n`) has a low strictly less than both neighbors. Body color irrelevant. An ITL can also be the low printed by a move that rebalances an imbalance (EP12 [14:15], [16:58]) — no neighboring-STL geometry required for that route.

## Timeframes

Same as swing-high: applies M1 through MN1. HTF swing lows are structurally heavier.

## Examples

**Example 1 — basic 3-bar pattern:**
- Candle n-1 low = 1.0850
- Candle n low = 1.0830
- Candle n+1 low = 1.0845
- → n is a swing low (STL).

**Example 2 — ITL by the rebalance route:**
- A short-term low forms with no higher-STL neighbors on either side (fails the geometric test).
- The low formed as price rebalanced a prior imbalance (big up candle) on the way down.
- → that low is now an ITL by the rebalance route (`ICT-2022-MENTORSHIP-EP12` [16:58]), even though it never satisfied route 1.

## Common Mistakes

- **Body-only comparisons.** Use the candle low (wick bottom), not the close.
- **Calling the live candle a swing low.** Confirmation requires the next candle's close (`ICT-2022-MENTORSHIP-EP03` [17:49]).
- **Treating the geometric test as the only route to ITL status.** ICT states a second, rebalance-based route for intermediate-term lows (EP12 [14:15], [16:58]); a page or engine using only the geometric (STL-neighbor) test misses this class.
- **Citing the plain 3-candle swing-low definition (EP10 [18:04]) as if it were the ITL test.** It is the STL (any swing low) test; the ITL test requires adjacent STLs to be higher (`ICT-2017-OPEN-FLOAT-L12` [20:36]–[20:42]) or the rebalance route above.
- **Equal lows.** Two adjacent equal-priced lows form an [equal-lows](../02-liquidity/equal-lows.md) liquidity pool, not a single swing low.

## Related Concepts

- [swing-high](swing-high.md) — mirror.
- [bos-bearish](bos-bearish.md) — references a prior swing low.
- [mss](mss.md) — structure shift referenced against swing highs/lows.
- [equal-lows](../02-liquidity/equal-lows.md) — what two equal-priced lows form.
- [sell-side-liquidity](../02-liquidity/sell-side-liquidity.md) — stops resting below swing lows.

## Citations

- `ICT-2017-INSTITUTIONAL-SWING-POINTS` [00:50]–[00:56] — 3-bar definition; Larry Williams attribution (Jan 2017).
- `ICT-2016-EQUILIBRIUM-PREMIUM` [11:53]–[11:58] — "I only need three candles," not the 5-candle Williams fractal (Sep 2016).
- `ICT-2022-MENTORSHIP-EP03` [17:49] — confirmation on candle close.
- `ICT-2022-MENTORSHIP-EP05` [14:42] — wicks count, close irrelevant.
- `ICT-2022-MENTORSHIP-EP10` [18:04] — plain 3-candle swing-low (STL) definition, not the ITL test.
- `ICT-2022-MENTORSHIP-EP12` [14:15], [16:58] — ITL geometric and rebalance routes.
- `ICT-2017-OPEN-FLOAT-L12` [20:36]–[20:42] — ITL route 1 (geometric) and the LTL tier, by inversion of the ITH statement (Jan 2017).

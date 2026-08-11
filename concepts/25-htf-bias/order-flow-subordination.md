# Order Flow Subordination

**Category:** 25-htf-bias
**Aliases:** subordination, LTF subordination, trading in consolidations, fading the consolidation breakout
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-CONSOLIDATION-TRADING
**Tags:** htf-bias, order-flow, consolidation, equilibrium, liquidity, stop-runs

## Definition

Order flow subordination is ICT's rule that **lower-timeframe price action is subordinate to
daily and H4 institutional order flow** — and its main practical use is deciding what a
consolidation breakout means. Whichever way the daily or H4 points, "that's going to be the
direction of the move **outside** of the consolidation most often" (04:56–05:19); a break the
*other* way is a liquidity raid, not a structure break.

The mechanism is stated as a role reversal at the equilibrium: "**retail traders chase
expansions that originate from the equilibrium, and smart money fades the expansions that
originate from the equilibrium**" (06:04–06:11). The consolidation itself is the
[open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md) builder — "the longer the consolidation is, the
more orders are allowed to build up" (03:30–04:07).

ICT's own framing for the reference point is deliberately *not* support and resistance: "we're
more focused on the **equilibrium price point**, because we understand premium and discount —
not just simply what price did at an old high or low" (07:16–07:35).

## Formal Criteria

**The inputs**

- **Direction** comes from the **daily and/or H4** institutional order flow, arrived at via the
  PD array matrix — "the four-hour chart is your **last line of defence** in terms of
  determining directional bias" (00:51–01:05). Preferably both agree (01:05–01:12).
- **The consolidation** is found on a **lower** timeframe, typically H1 or M15 (01:12–01:28).
- **The equilibrium** — the midpoint of that consolidation — is the reference, not the range
  bounds.

**Bullish daily / H4 order flow**

- A break **below** the consolidation low is **accumulation of sell stops**, not weakness:
  "any moves below the consolidation would be viewed as smart money **accumulating the sell
  stops for a move higher**" (05:31–05:43).
- A **short-term low broken on an expansion away from equilibrium** is the entry signal, read
  as "a sweep on sell stops to accumulate new longs", after which they "run for the other end
  of the consolidation or just outside of it for the liquidity, for the buy stops" (09:04–09:18).
- The retail counterparty is explicit: traders who bought the old low as support have stops
  "just below that previous short-term low", and those stops are what the raid is for
  (11:35–12:17).

**Bearish daily / H4 order flow**

- A break **above** the consolidation high is **distribution into buy stops**: "smart money
  knocking out buy stops and accumulating short positions" (05:43–05:56).
- A **short-term high broken above equilibrium** is the short entry — "once that short-term
  high is broken, that's an accumulation on buy stops … that's where we look to go short, and
  we aim for the liquidity resting **below the previous low**" (15:45–16:06).

**The target rule**

- **Take the return to equilibrium; do not assume the opposite extreme.** "We're looking for
  price to return back to equilibrium. We **do not anticipate or always hold for the opposite
  end** of the consolidation — we don't know that, we have no idea if that's going to occur
  with any validity" (12:24–12:43). The justification is mean reversion inside a range:
  "price, while in consolidations, is always going to want to **gravitate back to the mean**"
  (12:43–12:49).

**Day-trade specialisation**

- The short-term low or high being swept is often a named session level: "that short-term low
  could be in many cases the **Asian session low**, or it could be a **previous day's low**"
  (19:19–19:31).
- Day-trade consolidations are brief by design — "as a day trader we're **not** going to expect
  a long phase of consolidation; it can be rather brief" (04:07–04:15).

## Formula / Math

```
htf_flow := institutional_order_flow(D)            # H4 as the fallback / confirmation
cons     := consolidation on H1 or M15
eq       := (cons.high + cons.low) / 2             # equilibrium, the reference point

# the signal is an expansion AWAY FROM eq that breaks a short-term level
if htf_flow == bullish:
    signal := break_below(short_term_low) where short_term_low < eq
    read   := sell-stop raid -> accumulation
    action := long
    target := eq                                    # NOT cons.high
    stretch:= cons.high .. just above it (buy stops) — only if it develops

if htf_flow == bearish:
    signal := break_above(short_term_high) where short_term_high > eq
    read   := buy-stop raid -> distribution
    action := short
    target := eq
    stretch:= cons.low .. just below it (sell stops)

# retail mirror (the counterparty being traded against)
retail_reads(break) := "break in structure" -> chases the breakout direction
```

## Machine-Readable

```json
{
  "id": "order-flow-subordination",
  "category": "25-htf-bias",
  "aliases": ["ltf-subordination", "trading-in-consolidations", "fading-the-consolidation-breakout"],
  "criteria": [
    {"id": "c1", "expr": "direction from institutional_order_flow(D) and/or H4; H4 is the last line of defence"},
    {"id": "c2", "expr": "consolidation located on a lower timeframe (H1 or M15)"},
    {"id": "c3", "expr": "reference point == equilibrium of the consolidation, not its bounds"},
    {"id": "c4", "expr": "bullish HTF: break below cons.low == sell-stop accumulation, buy it"},
    {"id": "c5", "expr": "bearish HTF: break above cons.high == buy-stop distribution, sell it"},
    {"id": "c6", "expr": "entry trigger == expansion away from eq breaking a short-term high/low"},
    {"id": "c7", "expr": "target == return to equilibrium; opposite extreme NOT assumed"},
    {"id": "c8", "expr": "consolidation duration proportional to open float built"},
    {"id": "c9", "expr": "swept level is often the asian session low/high or the previous day's low/high"},
    {"id": "c10", "expr": "a break WITH the HTF flow is the expected exit direction, not the entry"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["daily-bias", "htf-bias-framework", "bias-confluence", "top-down-analysis", "equilibrium-definition", "open-float-liquidity-pool", "turtle-soup", "stop-hunt-pattern", "range-contraction", "accumulation-phase", "pd-array-matrix", "asian-range-low", "day-trade-routine"],
  "sources": ["ICT-2017-CONSOLIDATION-TRADING"]
}
```

## Visual Pattern

```
  BULLISH daily / H4 — the break DOWN is the entry

        cons.high ─────────────────────────────── buy stops rest here
                    ╱╲      ╱╲                     (the stretch target)
        eq ────────╱──╲────╱──╲──────── ◄── TARGET: return to equilibrium
                          ╲╱     ╲
        cons.low ──────────────────╲────────────
                                    ╲___●  ◄── ENTRY
                                           sell stops swept below an
                                           old low; retail sells "the
                                           break in structure" here

  BEARISH daily / H4 — exact mirror: the break UP above cons.high is the short.

  WRONG READ (retail):  break below -> "weakness" -> sell
  RIGHT READ (subordinate to HTF):  break below in a bullish market -> buy the raid
```

## Timeframes

Bias on **D** and **H4**; the consolidation and the trigger on **H1** and **M15**. The rule
does not apply upward — a daily consolidation is not subordinated to a weekly read by this
lesson.

## Examples

**Example 1 — bullish HTF, retail support broken (11:35–12:21):**
- Setup: daily and H4 order flow bullish. An H1 consolidation has an old low that produced a
  short-term bounce.
- Retail: price returns to that equal low; they buy it as support and place stops "just below
  that previous short-term low".
- Trigger: price trades **below** the previous low, outside the consolidation. "That's where
  we're looking to be a buyer, and **we're buying up those sell stops**."
- Outcome: "that creates our **low-risk, high-probability entry**"; the first objective is the
  return to equilibrium, not the range high.

**Example 2 — bearish HTF, the false "break in structure" (14:54–16:06):**
- Setup: daily / H4 bearish; price consolidating.
- Trigger: an expansion up **away from equilibrium** breaks a short-term high that sat just
  above the equilibrium. "Retail traders are going to see that as a **break in structure** and
  they're going to look to buy … and expect an ABC type formation."
- Outcome: that high is where the shorts are paired — "we aim for the liquidity resting
  **below the previous low** that creates the consolidation support".

## Common Mistakes

- **Reading a consolidation breakout as directional information.** In this framework the break
  itself carries no direction; the daily/H4 flow assigns the meaning.
- **Using the range bounds as the reference.** ICT works from the **equilibrium** — the bounds
  are where the liquidity sits, not where the decision is made.
- **Holding for the opposite extreme.** Explicitly ruled out: take equilibrium, because "we
  have no idea if that's going to occur with any validity" (12:36).
- **Applying it without an HTF read.** With no daily or H4 order flow the rule has no input and
  degenerates into guessing which side breaks.
- **Trading breakouts on strength or weakness.** The retail behaviour the whole model is
  counterparty to: "they think about **selling weakness and buying strength**, and they have no
  understanding what fair value is and how to use it with the equilibrium" (18:46–18:56).
- **Expecting a long consolidation intraday.** Day-trade consolidations "can be rather brief";
  duration scales the open float, not the validity.

## Related Concepts

- [daily-bias](daily-bias.md), [htf-bias-framework](htf-bias-framework.md), [top-down-analysis](top-down-analysis.md) — where the subordinating direction comes from.
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md) — the reference point and the first target.
- [open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md) — what the consolidation is building.
- [turtle-soup](../20-turtle-soup/turtle-soup.md), [stop-hunt-pattern](../20-turtle-soup/stop-hunt-pattern.md) — the pattern the raid takes; ICT names turtle soup directly at 01:28.
- [range-contraction](../01-market-structure/range-contraction.md), [accumulation-phase](../12-power-of-three/accumulation-phase.md) — the consolidation in structural and AMD terms.
- [asian-range-low](../14-asian-range/asian-range-low.md) — a common identity for the swept short-term level on day trades.
- [day-trade-routine](day-trade-routine.md) — the May-2017 procedure this lesson sits inside.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md), [bias-confluence](bias-confluence.md).

## Citations

- `ICT-2017-CONSOLIDATION-TRADING` (00:15–00:25) "welcome back folks to **lesson four of the May 2017 ICT mentorship**, ICT amplified day trading and scalping — this teaching is **trading in consolidations**" — dates the source; (00:25–00:51) "the first thing you need to understand is the focus on the **daily and/or four-hour order flow subordination**"; (00:51–01:12) "**four-hour chart is your last line of defence** in terms of determining directional bias — you want to be trading in preferably **both the daily and four-hour** suggesting higher prices or lower prices"; (01:12–01:37) "looking for consolidations in price on a **lower time frame** … an hourly chart or a 15-minute time frame … a buildup of orders to then look for a rejection, basically **turtle soup**"; (01:52–02:11) "retail traders are going to be looking for **breakouts** to establish a directional bias … they're basically **chasing after price**"; (02:11–02:49) "**smart money will engineer or fade breakouts** of a consolidation"; (02:49–03:23) "retail traders buy the previous low and sell the previous high … **liquidity rests just above an old high or below an old low**"; (03:23–03:39) "the consolidation itself is permitting the **open float**, which is the buildup of orders above and below current market action"; (03:39–04:15) "**the longer the consolidation is, the more orders are allowed to build up** … as a day trader we're not going to expect a long phase of consolidation, it can be rather brief"; (04:15–04:56) "**a great deal of near-term open float** … the open interest above the marketplace will start to concentrate, the open interest below the marketplace begins to concentrate, and you'll have a lot of liquidity basically **bracketing the market price**"; (04:56–05:19) "whatever the direction of daily or four-hour is, **that's going to be the direction of the move outside of the consolidation most often**"; (05:31–05:43) "if daily and/or four-hour order flow is **bullish**, any moves below the consolidation would be viewed as smart money **accumulating the sell stops for a move higher**"; (05:43–05:56) "if the daily or four-hour order flow is **bearish**, any move above the consolidation, above an old high, is going to be viewed as smart money **knocking out buy stops** and accumulating short positions"; (06:04–06:11) "**retail traders chase expansions that originate from the equilibrium, and smart money fades the expansions that originate from the equilibrium**"; (07:16–07:35) "we're more focused on the **equilibrium price point**, because we understand **premium and discount** — not just simply what price did at an old high or low"; (09:04–09:18) "we see that as a **sweep on sell stops to accumulate new longs**, and they're going to run for the other end of the consolidation or just outside of it for the liquidity, for the buy stops"; (11:35–12:21) "when retail traders see this, they're trading the old low as classic support and resistance … guess where they're going to put their stop loss — **just below that previous short-term low** … that's where we're looking to be a buyer, and we're **buying up those sell stops** … that creates our **low-risk, high-probability entry**"; (12:24–12:49) "we're looking for price to **return back to equilibrium** — we **do not anticipate or always hold for the opposite end** of the consolidation, we don't know that, we have no idea if that's going to occur with any validity … price, while in consolidations, is always going to want to **gravitate back to the mean**"; (14:54–15:18) "when that short-term high is broken, retail traders are going to see that as a **break in structure** and they're going to look to buy going long, and they're going to look for an **ABC** type formation"; (15:45–16:06) "once that short-term high is broken, **that's an accumulation on buy stops** … that's where we look to go short, and we aim for the **liquidity resting below the previous low**"; (18:46–18:56) "they think about **selling weakness and buying strength**, and they have **no understanding what fair value is** and how to use it with the equilibrium"; (19:19–19:31) "that short-term low could be in many cases the **Asian session low**, or it could be a **previous day's low**"; (19:49–20:00) "it all stems from the **subordination** that price is going to hold relative to the **daily and four-hour directional bias** based on institutional order flow".

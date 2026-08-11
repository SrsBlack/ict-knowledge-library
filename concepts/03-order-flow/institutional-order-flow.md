# Institutional Order Flow

**Category:** 03-order-flow
**Aliases:** institutional flow, smart-money flow, IOF
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-INSTITUTIONAL-ORDER-FLOW, ICT-2016-MENTORSHIP-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, institutional, foundational, monthly, weekly, bodies-not-wicks

## Definition

Institutional order flow is **the market's seeking of large institutional liquidity** — and in
its defining lecture ICT locates that liquidity precisely: "what you're doing is what
institutional order flow is. It's the seeking of large institutional liquidity. And it's going
to be found on the monthly and the weekly. And you see that being traded into on the daily"
(`ICT-2016-INSTITUTIONAL-ORDER-FLOW`, 27:47–28:04).

Operationally it is a **directional state of the chart, not a signature to spot**. Between a
higher-timeframe bullish order block and the bearish order block above it, order flow is
bullish; from that bearish order block down to the sell stops below, it is bearish. ICT shades
the monthly chart in exactly these alternating bands and then reads the weekly and daily inside
them: "we have an area at which institutional order flow is bearish until we get down to here.
Then, what is it going to do? It's going to look for the liquidity on the upside" (10:13–10:22).

The stops that matter are not retail's. "It's not our liquidity. It's not our stops it's
looking for. It's looking for the stops found on the monthly and the weekly and daily because
that's where the whales reside" (29:53–30:03) — "when I say whales, I'm talking about big funds,
large funds… The banks cannot counterparty with you and I. We're just not big enough. Even
collectively, we're not big enough" (28:28–28:46).

⚠ **The bodies rule.** This is the lecture that states it outright: "classic technical analysis
will say, well, this wick is the low. And what I teach is **it's the bodies of the candle is
where all the volume is**… the wick is always going to be directly related to retail" (06:03–06:22).

## Formal Criteria

**1. Build the map on the monthly, in alternating bands.**

- Mark the higher-timeframe order blocks: the last down candle before an up move (bullish), the
  last up candle before a down move (bearish).
- Between a bullish order block and the bearish order block above it, order flow is **bullish**
  — "as price is rallying up, this is all bullish. So, institutional order flow is bullish here"
  (10:25–10:31).
- On reaching the bearish order block it flips: "once it gets to this point here, we're looking
  for what? The stops below these lows here. So, we would see institutional order flow swing to
  the downside" (10:31–10:44).
- Step down: monthly → weekly → daily, carrying the same levels. "if you start with your monthly
  and you break down into the weekly chart, we can go down to a daily chart now. You can see a
  lot more definition on the daily chart" (21:34–21:45).

**2. Measure everything on bodies, never wicks.**

- "if we have the bodies of the candles defined here as the real low and allowing all this to be
  viewed as retail… price trades just below the bodies of the candle as it would in terms of
  seeking the truest form of volume from an institutional order flow standpoint" (06:52–07:18).
- "the wicks are no significant barrier in terms of institutional order flow" (08:49).
- Satisfaction threshold: "It stabs through it to go below the bodies of the candle. It doesn't
  necessarily have to go through the wicks. **We only need it to reach below the bodies of the
  candle**" (11:34–11:43).
- Entry into an order block is likewise a body event: "notice it wicks through that, but the body
  of the candle… trades right into this candle here. So that's all it's required to trade into
  [a] bullish order block" (08:28–08:42).
- Wick overshoot is expected and is a broker artefact: "you're going to have to allow that
  erroneous price action where it will run farther than you probably would expect it to because
  of your broker… they allow them to open the spread up a little bit more" (05:18–05:34).

**3. Rebalance is symmetric.** "the market has delivered price going down. It has to close in
that gap by trading it on the upside. So wherever there is a black candle, there must be a green
candle" (03:30–03:44).

**4. Confirmation of the flip is the violated candle.** "See this candle here… This last up
candle, that's the last green one. When that candle is violated right there… now you're going to
be expecting price to expand on the downside" (14:19–14:34); on the bullish side, "we have to
wait for price to want to show a break above a short-term high. We see that short-term high
violated here. So now we know buyers are in the market again" (22:52–23:01).

**5. Everything is hedged between the extremes.** "in between these two extremes, there's going
to be hedging. There's going to be bookmaking where the bank can have a net bearish book here
and be making money as it's going lower. But they have to be buying too" (16:22–16:38). A
counter-trend order block is often that unwinding: "This sell is unwinding the longs that they
put here" (16:01).

**6. Where flow is bearish, take one of three re-entries.** "when price breaks down, you're going
to be waiting for a return back to a, either a breaker or a bearish order block. Or you can look
for a stop run on an old high" (25:12–25:22).

## Formula / Math

```
# --- state, not signature ---
for each pair of adjacent HTF order blocks (monthly, then weekly):
    band(bullish_OB -> bearish_OB_above) := IOF is BULLISH
    band(bearish_OB -> sell_stops_below) := IOF is BEARISH

# --- everything measured on bodies ---
body_low(c)  := min(open(c), close(c))
body_high(c) := max(open(c), close(c))

reached(target_candle) := price <= body_low(target_candle)     # for a downside objective
                          # wicks need NOT be taken           (11:34-11:43)
traded_into(OB)        := body of the arriving candle enters the OB's range   (08:28)

# --- rebalance ---
for every down-close (black) candle leg there must exist
    an up-close (green) candle leg that closes the range        (03:37)

# --- flip confirmation ---
bearish_flip := close < body_low(last_up_candle_before_the_decline)
bullish_flip := break above the most recent short-term high

# --- where the objectives live ---
objective_pool := stops resting at monthly / weekly body extremes
                  # NOT retail stops:
                  #   "The banks cannot counterparty with you and I"   (28:39)
```

No probability or percentage is attached to any of it.

## Machine-Readable

```json
{
  "id": "institutional-order-flow",
  "category": "03-order-flow",
  "aliases": ["institutional-flow", "smart-money-flow", "IOF"],
  "criteria": [
    {"id": "c1", "expr": "IOF is a directional band between adjacent HTF order blocks, not a per-candle signature"},
    {"id": "c2", "expr": "bullish band := from a bullish OB up to the bearish OB above; bearish band := from that bearish OB down to the sell stops below"},
    {"id": "c3", "expr": "map built on the monthly, carried to weekly, executed on the daily"},
    {"id": "c4", "expr": "all levels measured on candle BODIES; wicks are retail and are no barrier"},
    {"id": "c5", "expr": "an objective is satisfied when price reaches beyond the BODY extreme; the wick need not be taken"},
    {"id": "c6", "expr": "an order block is traded into when the arriving candle's BODY enters its range"},
    {"id": "c7", "expr": "rebalance is symmetric: every down-close leg requires an up-close leg that closes the range"},
    {"id": "c8", "expr": "bearish flip confirmed by violation of the last up candle; bullish flip by a break of the short-term high"},
    {"id": "c9", "expr": "counter-directional order blocks inside a band are the bank unwinding the opposite side"},
    {"id": "c10", "expr": "re-entries in a bearish band: breaker, bearish order block, or a stop run on an old high"},
    {"id": "c11", "expr": "the targeted stops are fund-level, resting at monthly/weekly body extremes, not retail stops"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["algorithmic-price-delivery","bullish-order-flow","bearish-order-flow","order-flow-shift","smart-money-footprint","institutional-sponsorship","market-efficiency-paradigm","displacement-definition","fair-value-gap","liquidity-sweep","liquidity-void","bullish-order-block","bearish-order-block","mitigation-definition","market-maker-manipulation-template","high-resistance-liquidity-run"],
  "sources": ["ICT-2016-INSTITUTIONAL-ORDER-FLOW","ICT-2016-MENTORSHIP-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   MONTHLY — alternating bands, drawn between HTF order blocks

   ▓▓ bearish OB (last up candle)  ─────────────────────────  ← objective of the bullish band
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ░  IOF BULLISH: buy the down candles, sell into the OB  ░
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ▓▓ bullish OB (last down candle) ────────────────────────
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▒  IOF BEARISH: sell the up candles, cover at the lows  ▒
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ─── body lows ───  ← the objective. Wicks hang below and DO NOT
        |  |  |  |       have to be taken:  "We only need it to reach
        v  v  v  v       below the bodies of the candle"      (11:40)
```

## Timeframes

**Monthly and weekly are where the flow is defined; the daily is where it is traded.** "The
biggest moves that take place are always going to be found on that monthly and weekly basis.
Because that's where all the large whales are" (28:19–28:28). "if you can find the levels on the
monthly and weekly chart, keep them on your daily chart, you'll be able to see all these major
shifts in price" (28:53–29:04).

⚠ ICT is explicit that the signals are *not* generated on the daily itself: "notice there's no
bullish order block in here. There's no any kind of point of which you would see, oh, this is
what that would be. No. It's found on the weekly and the monthly. That's why you see this
response here" (24:28–24:38).

## Examples

**Example 1 — EURUSD monthly → weekly → daily, mid-2008 to mid-2012 (`ICT-2016-INSTITUTIONAL-ORDER-FLOW`, 00:59–24:57):**
- Setup: a monthly bearish order block at the 1.5197 open / 1.5151 high, with sell stops pooled
  below the body lows beneath it (00:59–02:26).
- Trigger: price runs those stops, returns to a monthly bullish order block, and flow flips
  bullish toward the up candle above (04:13–04:36).
- Outcome: "we've mapped out this entire euro dollar from mid-2008 all the way to mid-2012, just
  by understanding what the monthly levels on institutional order flow will give us" (12:24–12:43).
  On the daily, every subsequent down candle inside a bullish band is bought — "Every new buying
  finds a down candle" (23:54).

**Example 2 — the daily-chart trap inside a bullish monthly band (22:39–23:07):**
- Setup: on the daily, price is "dropping lower, lower, lower, lower".
- Trigger: "the institutional order flow on the monthly is telling you to get ready for a buy…
  But we have to wait for price to want to show a break above a short-term high."
- Outcome: the short-term high is violated, the monthly bullish order block is retested on the
  daily, and price expands.

## Common Mistakes

- **Reading order flow off the execution timeframe.** The defining lecture puts the levels on the
  monthly and weekly and states that no order block is visible on the daily at the level that
  produces the reaction (24:28).
- **Measuring to wicks.** The whole lecture is built on the opposite rule. Wicks are retail
  pricing and broker spread; the objective is the body extreme.
- **Waiting for the wick to be taken before calling an objective met.** "It doesn't necessarily
  have to go through the wicks" (11:38).
- **Treating a counter-directional order block inside a band as a reversal.** It is often the
  bank unwinding the other side of its book (16:22–16:47).
- **Confusing order flow with [institutional-sponsorship](institutional-sponsorship.md).** Order
  flow says which way; sponsorship says whether the path will be defended. They are consecutive
  lessons of the same month.
- **Importing later vocabulary.** The word "array" appears nowhere in this lecture, nor in any
  Sep–Dec 2016 packet. The 2016 terms here are "order block", "liquidity void", "breaker",
  "mitigation block", "mean threshold".

## Related Concepts

- [institutional-sponsorship](institutional-sponsorship.md) — the next lesson in the same month; the defence of the path this concept selects.
- [market-efficiency-paradigm](market-efficiency-paradigm.md) — invoked at 02:44 as the perspective the whole read is taken from.
- [algorithmic-price-delivery](algorithmic-price-delivery.md), [bullish-order-flow](bullish-order-flow.md), [bearish-order-flow](bearish-order-flow.md), [order-flow-shift](order-flow-shift.md), [smart-money-footprint](smart-money-footprint.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md) — the band boundaries.
- [mitigation-definition](../18-mitigation/mitigation-definition.md) — "this wick down to the body is a mitigation block" (19:11).
- [liquidity-void](../02-liquidity/liquidity-void.md) — the imbalance that must be rebalanced (03:37).
- [high-resistance-liquidity-run](../02-liquidity/high-resistance-liquidity-run.md) — the Month-1 filter that grades how hard a given objective is to reach.
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the profile ICT names at 16:56.
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2016-INSTITUTIONAL-ORDER-FLOW` (00:26) "This is **lesson two of November, or the third month of the ICT Mentorship**" — the dating anchor; (00:59–01:17) the monthly EURUSD order block at 1.5197 / 1.5151 / 1.5143; (01:57–02:26) "look at how the bodies of the candles basically merge at that same general area. I want you to **ignore the wicks**"; (02:44–02:55) "when we're looking at institutional order flow, the idea is thinking like that **market efficiency paradigm**. You're the market maker"; (03:30–03:44) "**wherever there is a black candle, there must be a green candle**"; (05:00–05:08) mean threshold as the middle of the up candle, and how the bodies respect it; (05:18–05:34) broker spread as the source of erroneous wick extension; (06:03–06:22) ⚠ "classic technical analysis will say, well, this wick is the low. And what I teach is **it's the bodies of the candle is where all the volume is**… the wick is always going to be directly related to **retail**"; (06:26–06:40) "the bulk of the bodies close to the interbank price is you're going to get"; (06:52–07:18) analysis is done around the bodies; (08:28–08:42) an order block is traded into on the **body**; (08:49–08:56) "the wicks are no significant barrier in terms of institutional order flow"; (10:13–10:44) the alternating bullish and bearish bands and the flip at each order block; (11:34–11:43) "**We only need it to reach below the bodies of the candle**"; (12:24–12:52) the full 2008–2012 EURUSD map, "that's the recipe for all the trading you're ever going to want to do"; (12:43–12:49) ⚠ "understanding those points of reference I showed you in **September, what to focus on**" — independent primary confirmation that Month 1 = September and that the Month-1 charting protocol is prerequisite; (12:56–13:08) "you have to find them on the higher timeframe… because this is where the large funds have their money"; (14:19–14:34) the flip confirmed by violation of the last up candle; (16:01–16:07) "This sell is unwinding the longs that they put here. Everything is a hedge on the interbank level"; (16:22–16:47) hedging and bookmaking between the range extremes; (16:56–17:18) the market-maker sell profile named as a sequence — "consolidation, return to consolidation, accumulation, reaccumulation, smart money reversal, low risk short, and redistribution"; (19:11) "this wick down to the body is a **mitigation block**"; (21:34–21:45) monthly → weekly → daily step-down; (22:39–23:07) the daily-chart trap inside a bullish monthly band, resolved by a break of the short-term high; (23:54) "Every new buying finds a down candle"; (24:28–24:38) ⚠ no order block is visible on the daily at the level producing the reaction — "It's found on the weekly and the monthly"; (25:12–25:22) the three bearish re-entries — breaker, bearish order block, or a stop run on an old high; (25:51–26:11) a monthly order block returned to becomes a mitigation block on the daily; (27:47–28:04) ⚠ **the definition** — "It's the seeking of large institutional liquidity. And it's going to be found on the monthly and the weekly. And you see that being traded into on the daily"; (28:04–28:28) "The daily chart will always seek the fund level institutional order flow… The biggest moves that take place are always going to be found on that monthly and weekly basis"; (28:28–28:46) whales are big funds, "The banks cannot counterparty with you and I. We're just not big enough"; (28:53–29:22) transposing monthly and weekly levels onto the daily; (29:53–30:03) "It's not our liquidity. It's not our stops it's looking for"; (30:04–30:24) why price goes to those levels — to remove participants or draw them in as counterparties.
- `ICT-2016-MENTORSHIP-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW` — course-level index references. ⚠ These were this page's only sources before the primary lecture was read; the earlier body text described the concept as a catalogue of FVG / CHoCH / MSS "signatures", none of which appear in the defining lecture. That framing has been replaced by the primary-source definition above.

# Institutional Sponsorship

**Category:** 03-order-flow
**Aliases:** sponsorship, bank sponsorship, institutional support, the elephant in the pool
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-INSTITUTIONAL-SPONSORSHIP, ICT-2016-GROWING-SMALL-ACCOUNTS
**Tags:** order-flow, institutional, order-blocks, midnight-open, displacement, trade-filtering

## Definition

Institutional sponsorship is **the willingness of large participants to protect a price swing
that is already underway** — the evidence, visible in price, that banks and funds are defending
the levels a setup depends on. ICT defines it outright: "what is institutional sponsorship
specifically? It's the willingness to protect an underlying price swing that has high
probability of unfolding" (`ICT-2016-INSTITUTIONAL-SPONSORSHIP`, 05:15–05:25), and again in
plain terms — "institutional sponsorship is just the impact of large institutions, banks, and
big equity traders coming in to fund the side of the marketplace that you anticipate seeing it
run towards" (05:25–05:47).

It is a **filter, not an entry**. Sponsorship is what separates a setup that will be defended
from one that will be allowed to fail: "if you're seeing that come to fruition in your charts,
you are seeing and identifying institutional sponsorship. Every one of your successful trades
will have this hallmark" (42:37–42:48). Its absence is an exit signal: "If you see the lack of
that, chances are you're probably offside and you're either going to want to reduce the risk on
the trade or maybe go to the sidelines" (43:39–43:50).

The lecture's image for it is the elephant: an elephant stepping into a child's paddling pool
displaces the water over the brim. "This is the evidence of a large body or entity that has a
lot more money than us. And they got into the marketplace here. How do we know that? Because
price surged" (15:32–16:16).

## Formal Criteria

ICT numbers three setup criteria, then a set of confirming hallmarks.

**The three criteria (long setups; reverse for shorts, 00:38–04:21):**

1. **Higher-timeframe price displacement** — "that can come in the form of a reversal, an
   expansion, or a return to fair value" (00:45–01:02). A daily chart "[is] not going to move
   that dynamic without sponsorship behind it by banks or large institutions or big equity
   traders" (12:20–12:33).
2. **An intermediate-term imbalance** — "a move to discount or a sell-side liquidity run… price
   is going to actually retrace or it can begin by going below an old low to run out the sell
   stops" (01:02–01:18).
3. **Short-term buy liquidity above the marketplace** — "ideal for pairing long exits to sell
   to" (01:18–01:34), paired with a time-of-day filter, "i.e. London Open for the low of the
   day or a New York Session low formation" (01:34–01:46).

**The confirming hallmarks:**

- **Immediate dynamic response at the origin level.** "to identify institutional sponsorship in
  a particular segment of price action, you need to see immediate dynamic response. If it's
  lethargic, if it's not willing to move right away, that means there is no institutional orders
  in that area" (13:27–13:47).
- **A traceable origin.** "That higher timeframe price displacement has to have a root price
  level at which we can classify as an institutional sponsorship level" (12:52–13:02) — in the
  worked case, the last down candle, "We're using the body of that candle here. Not so much the
  wick" (13:17–13:19).
- **Refusal to give the level back.** "the whole premise behind this teaching is institutional
  sponsorship should protect price from ever coming back down into this area here" (21:35–21:47);
  "we would look for the fact that price has an unwillingness to go lower. That would be evidence
  of what? Institutional sponsorship" (27:10–27:21).
- **Accumulation below the midnight New York opening price.** "what I'm delineating there is the
  opening price at midnight in New York… if we're expecting a price to move higher, what we see
  in the form of institutional sponsorship is price when it goes below the opening price at
  midnight should be accumulated" (31:04–31:39). Successive days repeat it (32:11–32:40).
- **Order blocks that are re-bought session after session.** "You're referencing old bullish
  order blocks from the previous day or maybe three sessions ago. And you can buy old bullish
  order blocks because they're going to do what? Recapitalize them. That's institutional
  sponsorship. They're defending specific levels" (40:01–40:22).
- **Session tagging on every level used.** "Every order block that we refer to here is linked to
  a London session or a New York session" (41:40–41:48).

**The four-stage grade of the protected swing** (22:12–22:42, 27:45–28:02). Origin → first grade
→ equilibrium (midpoint) → terminus. "institutional sponsorship should support price at those
logical areas in price."

**What sponsorship forbids.** Once market structure has shifted bullish on the higher timeframe,
the deep retracement is off the table: "don't think just because we rallied up here, let's go
back down here and let's wait for price to go and give us a buy signal here… No, that's not how
it's going to happen" (21:47–21:58).

## Formula / Math

```
# Setup gate (long; mirror for short)
sponsored_long := htf_displacement                    # reversal | expansion | return-to-fair-value
                  AND intermediate_imbalance          # move to discount OR sell-stop run below an old low
                  AND short_term_bsl_above            # the exit target
                  AND time_of_day in {London open low, NY session low}

# Origin of the sponsored swing
origin := body of the last down candle before the displacement leg   # bullish OB
          # "Not so much the wick"                                    (13:17)

# Confirmation on return to origin
confirmed := response_is_immediate_and_dynamic(origin)
disconfirmed := response_is_lethargic(origin)
  -> action: reduce risk, halve the position, or exit         (13:47–14:01)

# Daily accumulation signature
for each day D in the sponsored swing:
    O_D := opening price at 00:00 New York
    expect: price trades BELOW O_D and is bought
    expect: close(D) > low(D)              # "a low up to a higher close"   (36:11–36:32)
# i.e. the power-of-three profile, applied daily

# Four-stage grade of the swing
origin  ->  grade_1  ->  equilibrium (midpoint)  ->  terminus
# sponsorship should hold price up at each
```

No probability, percentage or count is attached to any of these. ICT explicitly declines the
guarantee: "I don't want to sell the idea that it's always going to go to your levels" (43:16).

## Machine-Readable

```json
{
  "id": "institutional-sponsorship",
  "category": "03-order-flow",
  "aliases": ["sponsorship", "bank-sponsorship", "institutional-support"],
  "criteria": [
    {"id": "c1", "expr": "higher-timeframe displacement present (reversal | expansion | return to fair value)"},
    {"id": "c2", "expr": "intermediate-term imbalance: move to discount or a sell-stop run below an old low (mirror for shorts)"},
    {"id": "c3", "expr": "short-term buy-side liquidity identified above as the exit pairing (mirror for shorts)"},
    {"id": "c4", "expr": "time-of-day filter: London open low or New York session low formation"},
    {"id": "c5", "expr": "origin == body of the last down candle before the displacement leg, not the wick"},
    {"id": "c6", "expr": "response on return to origin must be immediate and dynamic; lethargic response == no sponsorship"},
    {"id": "c7", "expr": "price below the 00:00 New York opening price is accumulated on each day of the swing"},
    {"id": "c8", "expr": "each daily bar closes higher than its low (power-of-three profile repeated daily)"},
    {"id": "c9", "expr": "prior-session order blocks (previous day or ~3 sessions back) are recapitalised rather than abandoned"},
    {"id": "c10", "expr": "swing graded in four stages: origin, first grade, equilibrium, terminus"},
    {"id": "c11", "expr": "absence of sponsorship == reduce risk, halve, or exit"},
    {"id": "c12", "expr": "no probability or percentage is attached; ICT declines to guarantee the objective"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["institutional-order-flow", "market-efficiency-paradigm", "smart-money-footprint", "bullish-order-block", "mitigation-definition", "liquidity-pool", "buy-side-liquidity", "power-of-three", "turtle-soup", "swing-trading-hallmarks", "london-open-killzone", "ny-am-killzone"],
  "sources": ["ICT-2016-INSTITUTIONAL-SPONSORSHIP", "ICT-2016-GROWING-SMALL-ACCOUNTS"]
}
```

## Visual Pattern

```
                                                    ╱ terminus  <- old high, buy stops
                                          ╱╲      ╱
                              grade 1   ╱   ╲   ╱   <- equilibrium of the swing
                          ╱╲          ╱      ╲╱
                        ╱   ╲       ╱
      origin  ▓ ──────╱      ╲────╱      each dip below the 00:00 NY open
        (last down     ╲    ╱             is bought; each day closes above
         candle body)   ╲ ╱               its own low
                  ╲    ╱
   old low  ────────╲──╱  <- sell stops taken FIRST, then the surge
                     V      ("the elephant in the pool", 15:32)

   00:00 NY open  ┊      ┊      ┊      ┊      ┊     <- one blue line per day
                  └ buy  └ buy  └ buy  └ buy  └ buy
```

The diagnostic is the shape of the *response*, not the level: a vertical move off the origin
means sponsorship, a sideways grind at it means none.

## Timeframes

Framed on the **daily** — "the reason why we focus on the daily chart is because that's where
the banks are trading off of" (12:33–12:41) — then transposed down. The lecture works the same
swing through **H4** (24:16, 28:31), **H1** (29:03) and **M15** (39:00), because "everything you
see on one timeframe is replicable on the higher timeframe and the lower timeframe" (07:28).

Below H1 the entries are still bounded by session: every order block used is tagged to a London
or New York session (41:40).

## Examples

**Example 1 — USDJPY daily, sponsorship gate (`ICT-2016-INSTITUTIONAL-SPONSORSHIP`, 06:11–20:16):**
- Setup: daily chart drops below an old low, taking the sell stops pooled there (06:18).
- Trigger: a surge off that low — higher-timeframe displacement — whose origin is the last down
  candle; price later returns to that candle's body and is bought (13:12–13:27).
- Outcome: price runs the first short-term high's buy stops, then the second, then the old swing
  high (20:10, 26:12–26:32). Market structure on the daily turns bullish (21:30) and the deep
  retracement never comes.

**Example 2 — the same swing on M15/H1, daily accumulation (31:04–36:32):**
- Setup: the 00:00 New York opening price plotted as a line on each day of the swing.
- Trigger: on each successive day, price trades below the opening price and into a down candle
  from that or a prior session; "Add five pips to that level. We could be a buyer" (34:25).
- Outcome: "a low up to a higher close" repeated day after day (36:11–36:32) — the daily
  power-of-three profile — until price reaches the first old high and consolidates there (36:39).

**Example 3 — sponsorship as the reason a 5:1 setup works (`ICT-2016-GROWING-SMALL-ACCOUNTS`, 28:04–28:22):**
- Setup: a daily-chart bullish order block after a turtle-soup run below an old low.
- Trigger: entry at the order block, target the mapped buy stops above equal highs.
- Outcome: five R-multiples. "This is what a one shot, one kill looks like. And it's framed on a
  daily level. It's going to give you institutional sponsorship… Because it's off of a daily
  order block. The banks trade off of daily levels."

## Common Mistakes

- **Treating sponsorship as an entry signal.** It is a gate on setups you already have, and a
  live check while the trade runs.
- **Waiting for the deep retracement.** Once the higher timeframe has shifted, sponsorship is
  precisely the thing preventing the pullback you are waiting for (21:47).
- **Reading old highs as resistance.** The lecture spends 36:46–37:29 on traders who short the
  first old high, get stopped through it, and supply the fuel for the next leg.
- **Fading each buy-stop level as it is taken.** "Each time the market goes up and takes out a
  level of buy stop liquidity, we don't collapse the trade entirely. We do not look for
  divergence indicators every time we get to an old high" (25:22–25:42).
- **Confusing it with institutional *order flow*.** Order flow is the directional read — where
  the market is going. Sponsorship is the defence of the path once it is going there. Both are
  taught in month three, back to back.
- **Reading it as a guarantee.** ICT declines to promise the objective is reached (43:16).
- **Importing later vocabulary.** The word "array" appears nowhere in this lecture, nor in any
  Sep–Dec 2016 packet. The 2016 terms used here are "liquidity void", "order block", "buy side
  liquidity", "discount", "fair value".

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md) — the directional read; sponsorship defends what order flow selects. Taught in the immediately preceding lesson of the same month.
- [market-efficiency-paradigm](market-efficiency-paradigm.md) — the frame ICT invokes three times in this lecture (06:57, 19:07) to justify the bank's side of the trade.
- [smart-money-footprint](smart-money-footprint.md) — the trace-reading this operationalises.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md) — the origin level sponsorship defends.
- [mitigation-definition](../18-mitigation/mitigation-definition.md) — the unwinding leg ICT reads at 19:11 as "a mitigation block".
- [power-of-three](../12-power-of-three/power-of-three.md) — named at 35:18 and applied to each day of the sponsored swing.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the run below the old low that starts the sequence (41:15).
- [liquidity-pool](../02-liquidity/liquidity-pool.md), [buy-side-liquidity](../02-liquidity/buy-side-liquidity.md) — the pools at both ends.
- [swing-trading-hallmarks](../31-models/swing-trading-hallmarks.md) — the 2017 restatement, where sponsorship is measured instead by SMT divergence against the dollar index.
- [london-open-killzone](../10-killzones/london-open-killzone.md), [ny-am-killzone](../10-killzones/ny-am-killzone.md) — the sessions every level is tagged to.

## Citations

- `ICT-2016-INSTITUTIONAL-SPONSORSHIP` (00:23) "This is **lesson three of month three** of the mentorship" — the dating anchor; (00:38–02:09) the three long-setup criteria in order; (03:19–04:08) the short-setup mirror; (05:04) "it's not cherry picking"; (05:15–05:25) "**It's the willingness to protect an underlying price swing that has high probability of unfolding**"; (05:25–05:47) "the impact of large institutions, banks, and big equity traders coming in to fund the side of the marketplace"; (06:18–06:43) the sell-stop pool below an old low; (07:21–07:48) fractality, look for the same pattern on a lower timeframe; (08:22–09:13) ⚠ "going back to the **September's content**, there were some things I told you to look for" — independent primary confirmation that *What To Focus On Right Now* is Month 1 = September; (12:03–12:33) higher-timeframe displacement as evidence of a large entity, "daily charts are not going to move that dynamic without sponsorship behind it"; (12:33–12:41) "the reason why we focus on the daily chart is because that's where the banks are trading off of"; (12:46–13:19) the origin must be traceable, and it is the **body** of the last down candle, "Not so much the wick"; (13:27–13:47) "you need to see **immediate dynamic response**. If it's lethargic… there is no institutional orders in that area"; (13:47–14:18) the action on a lethargic response — reduce risk, cut the position in half, or bail; (15:32–16:16) the elephant-in-the-paddling-pool analogy; (16:47–16:59) "focusing on this bullish order block here, that's where the institutional sponsorship is going to begin"; (18:54–19:45) where the bank unloads — the pool of buy stops above the old high, not 10 or 15 pips up; (21:35–21:58) sponsorship should prevent the return to the origin area; (22:12–22:42) the four-stage grade — origin, first grade, equilibrium, terminus; (25:22–25:42) do not collapse the trade or hunt divergence at each old high; (27:10–27:21) "price has an unwillingness to go lower. That would be evidence of what? Institutional sponsorship"; (31:04–31:39) the blue lines are "**the opening price at midnight in New York**", and price below it should be accumulated; (32:11–32:40) four successive days of the same behaviour; (33:03–33:45) entry mechanics — a down candle at or below the opening price becomes a bullish order block once violated, tradeable in London or New York; (34:23–34:28) "Add five pips to that level. We could be a buyer"; (35:18–36:32) power of three applied daily — "when you're bullish, you want to be buying near or below the opening price", producing "a low up to a higher close" repeatedly; (36:46–37:29) retail selling the old high as resistance and supplying the buy stops; (40:01–40:22) "you can buy old bullish order blocks because they're going to **recapitalize** them. That's institutional sponsorship. They're defending specific levels"; (41:02–41:27) ⚠ "that starts by looking at what we talked about in **September, which you should be focusing on right now**" — names the Month 1 lecture by title; the same passage defines the turtle soup buy and sell; (41:40–41:48) "Every order block that we refer to here is linked to a London session or a New York session"; (42:37–42:48) "Every one of your successful trades will have this hallmark"; (43:16–43:23) the explicit refusal to guarantee the objective; (43:39–43:50) absent sponsorship means reduce risk or stand aside.
- `ICT-2016-GROWING-SMALL-ACCOUNTS` (20:02–20:07) "we're going to wait to see if **the bank sponsors that level**"; (28:04–28:22) "This is what a one shot, one kill looks like. And it's framed on a daily level. **It's going to give you institutional sponsorship**… Because it's off of a daily order block. The banks trade off of daily levels."

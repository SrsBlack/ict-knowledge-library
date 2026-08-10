# Relative Strength Analysis

**Category:** 03-order-flow
**Aliases:** leadership analysis, leader vs laggard, institutionally sponsored rally, sympathetic rally, sixth sister, relative strength leadership
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-RELATIVE-STRENGTH, ICT-2017-STOCK-BUY-WATCHLIST, ICT-2017-STOCK-SELL-WATCHLIST
**Tags:** order-flow, intermarket, commodities, accumulation, distribution, leadership, dollar-index, smt

## Definition

Relative strength analysis is ICT's method for **picking which instrument inside a group to
trade** once a directional bias for the group already exists. It is a selection filter, not a
bias generator: "relative strength analysis is basically factoring your analysis around **the
most important market to be following right now when you're bullish** and the most important
market to be following when you're bearish" (`ICT-2017-RELATIVE-STRENGTH`, 04:01).

The whole method rests on one observation: when a benchmark makes a new extreme and a correlated
instrument **refuses to follow**, that refusal is institutional participation. "If it's not going
lower, there's only one reason for that — it means that they are **under accumulation** and
they're buying it. Who is? **Institutions are**" (19:40).

The instruments that refuse are **leadership**; the ones that follow the benchmark but rally
anyway are **sympathetic**. Both can be profitable; only the leaders carry the speed and
magnitude.

## Formal Criteria

**The benchmark**

| Group being ranked | Benchmark | Relationship |
|---|---|---|
| Commodities, currencies, metals, energies, debt | **US Dollar Index** | inverse — "the dollar index is like the **king**… what the dollar does sets the tone for everything else" (04:23) |
| Individual equities | **Dow Jones Industrial Average** overlay | same-direction; the divergence is against the index |

- Dollar index **higher → pressure on commodity prices**; dollar index **lower → higher commodity
  prices allowed** (04:34–04:48).
- ICT's stated method for equities: overlay `$DOWI` on the share chart via barchart.com's
  comparison / left-axis display (`ICT-2017-STOCK-BUY-WATCHLIST`, 09:44).

**The four states**

| State | Benchmark does | Instrument does | Read |
|---|---|---|---|
| **Institutionally sponsored rally** | DXY makes a **higher high** | **fails to make the lower low** | leadership long — accumulation |
| **Sympathetic rally** | DXY makes a **higher high** | **does** make the lower low, then rallies anyway | follower long — "the **sixth sister**" |
| **Institutionally sponsored decline** | DXY makes a **lower low** | **fails to make the higher high** | leadership short — distribution |
| **Sympathetic decline** | DXY makes a **lower low** | **does** make the higher high, then declines anyway | follower short |

- The failure swing is explicitly named as an SMT divergence: a commodity that "**fails to make a
  lower low**, which is basically an **SMT divergence**" (05:19).

**Confirming price behaviour, bullish leadership** (05:48–06:14, 10:53–11:06)

- **Short-term highs are seen broken** — repeatedly and easily.
- **Declines are shallow in nature.**
- **Up-closing candles and upswings are typically much larger** than the down-closing ones.
- Premium arrays offer no resistance ("premium arrays are not respecting anything in terms of
  offering resistance — it's being broken through"); discount arrays support price (36:29–36:42).

Mirror for bearish leadership: short-term **lows** broken, **rallies shallow**, down-closing
candles larger (11:58–12:32).

**The two-step order of operations** (07:03–07:34)

1. **First** form the view on the **benchmark** — "you have to have the analysis on your dollar
   index because that's going to set the tone for a prolonged move." A single divergence on its
   own is not a trade: "when one diverges, it doesn't necessarily mean that there's a trade."
2. **Then** rank the group's members by the four states and trade the leader.

**Ranking happens inside sub-groups, not only across the whole basket** (08:48–10:13)

- The commodity universe is divided into **agricultural** (grains: corn, wheat, soybeans;
  livestock: feeder cattle, lean hogs, live cattle; foods: cocoa, orange juice, coffee, sugar;
  fibers: cotton) and **financial** (debt: 30-year bond, 10-year note, 5-year note; currencies;
  metals: gold, silver, high-grade copper; energies: crude oil).
- The comparison is run **within** a sub-group: one of the three meats, one of the three grains,
  one of the three metals will show the failure swing and lead the others.

**Equity form** (`ICT-2017-STOCK-BUY-WATCHLIST`, 03:14–04:24)

- "**Leadership stocks that are aggressively bought by institutions will be found to fail to drop
  lower** during bullish months when the three major stock indices decline until **one of those
  indices fails to post a lower low** comparably."
- The equity read therefore stacks two divergences: an [index-smt](../16-smt-divergence/index-smt.md)
  divergence across NASDAQ/S&P/Dow marking the turn, and individual shares refusing to follow the
  Dow lower at the same moment.
- Bearish mirror: shares "**fail to rally higher** during bearish months when the three major
  indices rally until one of those indices fails to post a higher high"
  (`ICT-2017-STOCK-SELL-WATCHLIST`, 02:38–02:53).
- **Obviousness gate, stated for the equity form:** "the rules are, **if it's not obvious there is
  no divergence on the SMT**" (04:42).

**What it does not do**

- It supplies **no entry, stop or target**. In every worked example the entry still comes from an
  ordinary PD array — a bullish order block, a fair value gap, a turtle soup.
- It does **not** claim every group member moves. "**Not every commodity is going to rally**…
  the ones that fail to make that lower low, that's the one we are really focusing on" (08:57).

## Formula / Math

```
# --- inputs ---
benchmark := DXY            (commodities, FX, metals, energies, debt)
           | DJIA overlay   (individual equities)

# --- the four states, bullish-benchmark-topping case ---
# (benchmark expected to WEAKEN => group expected to RALLY)

leadership_long(x)  := benchmark.higher_high(t) AND NOT x.lower_low(t)
sympathetic_long(x) := benchmark.higher_high(t) AND     x.lower_low(t)
                       AND x rallies afterwards

# --- mirror (benchmark expected to STRENGTHEN => group expected to FALL) ---
leadership_short(x)  := benchmark.lower_low(t) AND NOT x.higher_high(t)
sympathetic_short(x) := benchmark.lower_low(t) AND     x.higher_high(t)
                        AND x declines afterwards

# --- confirming behaviour of a bullish leader ---
short_term_highs_broken   == true
declines                  == shallow
mean(up_candle_range)     >  mean(down_candle_range)
premium_arrays            == broken through
discount_arrays           == supporting price

# --- order of operations ---
1. bias(benchmark)                       # REQUIRED FIRST
2. rank group members by state
3. trade leader; entry from ordinary PD array

# --- gates ---
divergence_alone           => NOT a trade
divergence_not_obvious     => treat as absent
```

## Machine-Readable

```json
{
  "id": "relative-strength-analysis",
  "category": "03-order-flow",
  "aliases": ["leadership-analysis", "leader-vs-laggard", "institutionally-sponsored-rally", "sympathetic-rally", "sixth-sister"],
  "criteria": [
    {"id": "c1", "expr": "benchmark := dollar_index for commodities/FX/metals/energies/debt; DJIA overlay for equities"},
    {"id": "c2", "expr": "leadership_long := benchmark higher_high AND instrument fails to make lower low"},
    {"id": "c3", "expr": "leadership_short := benchmark lower_low AND instrument fails to make higher high"},
    {"id": "c4", "expr": "sympathetic := instrument DOES make the matching extreme but moves with the group anyway"},
    {"id": "c5", "expr": "bullish leader confirms via broken short-term highs, shallow declines, larger up-candles"},
    {"id": "c6", "expr": "benchmark bias must be formed BEFORE ranking; divergence alone is not a trade"},
    {"id": "c7", "expr": "ranking is run within sub-groups (grains, livestock, foods, fibers, metals, energies, debt, currencies)"},
    {"id": "c8", "expr": "equity form stacks index_SMT across NASDAQ/ES/YM with share-vs-DJIA refusal"},
    {"id": "c9", "expr": "if the divergence is not obvious, it does not exist"},
    {"id": "c10", "expr": "supplies_entry == false; entry still comes from a PD array"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["dollar-index", "smt-divergence", "index-smt", "interest-rate-triad", "smart-money-footprint", "accumulation-phase", "distribution-phase", "explosive-market-selection", "stock-watchlist-construction", "multi-asset-analysis", "bullish-order-block", "premium-array", "discount-array"],
  "sources": ["ICT-2017-RELATIVE-STRENGTH", "ICT-2017-STOCK-BUY-WATCHLIST", "ICT-2017-STOCK-SELL-WATCHLIST"]
}
```

## Visual Pattern

```
   BENCHMARK EXPECTED TO WEAKEN  ->  RANK THE GROUP

   DOLLAR INDEX      ╱‾╲    ╱‾‾╲   HIGHER HIGH
                    ╱   ╲__╱    ╲

   ── LEADERSHIP ─────────────────────────────────────────
   soybeans      ╲__╱‾╲___╱‾‾‾    HIGHER low  ✗ failed to follow
                                  short-term highs broken · shallow dips
                                  ►► trade this one

   ── SYMPATHETIC ────────────────────────────────────────
   corn          ╲__╱‾╲__╱‾       LOWER low  ✓ followed, then rallied
                                  slower · more lethargic · lesser magnitude
                                  "the sixth sister"

   ── NEITHER ────────────────────────────────────────────
   cocoa         ╲___╲___╲        lower lows all the way down
                                  no accumulation · never a buy

   ───────────────────────────────────────────────────────
   EQUITY FORM (two stacked divergences)

     step 1   NASDAQ / S&P / DOW  ->  one fails to make the lower low
                                       = the market turn
     step 2   share vs $DOWI overlay ->  share fails to make the lower low
                                       = this share is being accumulated
```

## Timeframes

Daily and weekly in every worked example; the commodity survey runs across **months** of daily
data (summer 2016 → June 2017). This is a swing/position-scale filter with no intraday form,
though the same failure-swing logic appears intraday as
[index-smt](../16-smt-divergence/index-smt.md).

## Examples

All from `ICT-2017-RELATIVE-STRENGTH`, ranking the commodity basket over the window in which the
dollar index topped in January 2017 and weakened thereafter (14:50–15:11).

**Example 1 — soybeans, grain leadership (17:49–19:10):**
- August–October 2016: soybeans **failed to make lower lows** while the dollar index made higher
  highs — "already indications that the soybean market was under accumulation."
- November 2016 → January 2017: a **higher low** formed against equal highs near $10.80.
- Corn and wheat both kept making **lower lows** over the same window — they were not leaders.
- Outcome quoted: about **$4,500 per contract** of move.

**Example 2 — feeder cattle, livestock leadership (19:11–21:45):**
- October–December 2016: failing to go lower while the dollar made higher highs; **short-term
  highs repeatedly broken**.
- February–March 2017: dollar index made a **higher high** near **102** while feeder cattle made a
  **higher low**, and price traded into a **bullish order block** — "we're blending PD arrays
  discount with the context that we should be seeing higher commodity prices."
- Outcome quoted: **over $19,000 per contract**.

**Example 3 — cocoa, a market that never qualified (23:48–24:36):**
- Cocoa declined continuously on a bumper crop; **no accumulation pattern at any point**.
- Verdict: "this would **never meet the criteria as a buy** while the dollar is dropping."

**Example 4 — sugar, a signal that failed (24:59–26:22):**
- A higher low against a dollar-index higher high in late December — a valid failure swing — and
  price did rally.
- It then stalled at a premium array / bullish order block near 20.50 and rolled over.
- ICT's point: "you're also going to see things that **start off like a good move and then fail**,
  and that's what real environments are going to be like for you."

**Example 5 — the currency ranking (28:47–33:33):**
- Leaders (higher low against the dollar's January higher high): **Australian dollar, Japanese
  yen, Swiss franc, euro, New Zealand dollar**.
- Not leaders: **Canadian dollar** (an equal low that "gave up the ghost in February"), **British
  pound** (a slightly lower low, "no real accumulation in this pair at all" until March).
- The Aussie and the Kiwi carried a **positive interest-rate differential** as an added bonus.

**Example 6 — Apple, the equity form (`ICT-2017-STOCK-BUY-WATCHLIST`, 04:42–06:20):**
- Mid-January 2017: the Dow Jones overlay made a **lower low**; **AAPL failed to go lower**,
  accumulating around **$118–$120** per share.
- Read: "**Apple was showing relative strength here, and that only occurs when large institutions
  come in and they sponsor buy programs.**"
- Outcome: appreciation from February through May.

## Common Mistakes

- **Running it without a benchmark view.** The dollar-index (or index) bias comes first; ICT says
  a divergence on its own does not necessarily mean there's a trade.
- **Expecting the whole group to move.** The premise is the opposite — most members will not lead,
  and several will not participate at all.
- **Trading the sympathetic member and expecting leader behaviour.** Sympathetic moves reach
  objectives "not as strong and as quick and as efficiently" — they are "more lethargic".
- **Comparing across sub-groups only.** The failure swing is looked for **within** grains, within
  livestock, within metals — otherwise leadership inside a sub-group is missed.
- **Treating it as an entry.** Every example still enters at a bullish order block, a fair value
  gap or a turtle soup.
- **Forcing a marginal divergence.** For the equity form ICT states the rule outright: if it is not
  obvious, there is no divergence.
- **Confusing it with [interest-rate-triad](interest-rate-triad.md).** That compares three points
  on one yield curve to validate a dollar-index array. This ranks the members of a group against a
  benchmark to choose *what to trade*.

## Related Concepts

- [dollar-index](dollar-index.md) — the benchmark for every non-equity group.
- [smt-divergence](../16-smt-divergence/smt-divergence.md) — the divergence mechanic this is built on; ICT names it explicitly.
- [index-smt](../16-smt-divergence/index-smt.md) — the equity-market form of the same comparison, and step 1 of the equity read.
- [interest-rate-triad](interest-rate-triad.md) — the same failure-swing logic applied to the yield curve as a validation filter.
- [stock-watchlist-construction](../31-models/stock-watchlist-construction.md) — the full equity workflow this filter sits inside.
- [multi-asset-analysis](multi-asset-analysis.md) — the four-asset-class context that decides whether the whole exercise is worth running.
- [explosive-market-selection](../31-models/explosive-market-selection.md) — the eight-hallmark checklist; this page is its intermarket-confluence layer stated as a ranking method.
- [smart-money-footprint](smart-money-footprint.md), [accumulation-phase](../12-power-of-three/accumulation-phase.md), [distribution-phase](../12-power-of-three/distribution-phase.md) — what the refusal to follow is read as.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md) — where the entry actually comes from.

## Citations

- `ICT-2017-RELATIVE-STRENGTH` (00:18–00:29) "**ICT Mentorship June 2017. Commodity Trading Lesson Number 2.** We're going to be talking about relative strength analysis and… professional accumulation and distribution" — self-dates the lecture; (00:42–03:19) the commodity basket by sub-group — grains (corn, wheat, soybeans), livestock (feeder cattle, lean hogs, live cattle), foods (cocoa, orange juice, coffee, sugar), fibers (cotton), debt (30-year bond, 10-year note, 5-year note), currencies, metals (gold, silver, high-grade copper), energies (crude oil); (04:01–04:23) "relative strength analysis is basically factoring your analysis around the **most important market to be following right now when you're bullish**"; (04:23–04:48) "**the dollar index is like the king**… if we look for the dollar index to be trading higher, that's going to **put pressure on the commodity prices**. If the dollar index is going to be trading lower, that's going to allow and incite higher commodity prices"; (04:53–05:19) "what we're actually looking at is a market that has **failed to go lower** at a time when the dollar index would be expected to go lower… the commodities that you'd be looking to be long in are a commodity that **fails to make a lower low, which is basically an SMT divergence**"; (05:34–06:14) underlying price strength — "**short-term highs are going to be seen broken and declines are going to be shallow in nature**… up-closing candles… are typically much larger than those that close lower"; (06:21–07:03) "the key is you want to be focusing on the commodities that fail to make a lower low… if the institutions step in… **they're not going to permit price to go lower**"; (07:03–07:34) "you have to have the analysis on your dollar index because that's going to set the tone for a prolonged move… **when one diverges, it doesn't necessarily mean that there's a trade**"; (08:48–10:13) the sub-group ranking worked through the meats — "one of those meats may fail to make a lower low when the dollar is starting to go lower… and when it does that, it's **showing leadership**"; (09:59–11:06) "**sympathetic price strength**… a market that tends to trade higher **in sympathy** to the leader market… you're actually buying… the **sixth sister** of the group"; (11:26–11:40) sympathetic moves "will be moving in sympathy and moving in tandem but at a **lesser degree in terms of speed, magnitude**, and it will be **more lethargic**"; (11:58–12:32) the institutionally sponsored decline and its mirror criteria; (12:57–13:41) the sympathetic decline; (14:50–15:11) the dollar-index window — rallying into January 2017, weakening after; (15:52–17:13) corn and wheat making lower lows — "we didn't see any kind of leadership buying in here at all"; (17:49–19:10) the soybean leadership read and the ~$4,500 per contract move; (19:11–21:45) feeder cattle — "**if it's not going lower, there's only one reason for that. It means that they are under accumulation and they're buying it. Who is? Institutions are**" — plus the February–March higher low against the dollar's 102 high, the bullish order block, and "**over $19,000 per contract**"; (21:48–23:46) lean hogs (~$5,600) and live cattle (~$12,000); (23:48–24:36) cocoa — "no real indication that this is under any accumulation whatsoever… this would **never meet the criteria as a buy**"; (24:59–26:22) sugar — the failure swing that rallied and then failed, "things that start off like a good move and then fail"; (26:22–27:08) cotton — "every short-term high is finding its way broken with no problem at all, and bullish order blocks are supporting price"; (27:12–28:35) the debt instruments showing no accumulation, offered as the reason "the markets have been so fickle"; (28:47–33:33) the currency ranking — Aussie, yen, franc, euro and kiwi as leaders, Canadian dollar and cable as non-leaders, with the interest-rate differential noted as a bonus for the Aussie and Kiwi; (33:35–35:29) gold, silver and copper; (35:30–35:54) crude oil "failing to make lower lows as the dollar index was rallying… under accumulation around the $43 a barrel mark"; (36:02–36:42) "**no indicators, no bells and whistles, just simply understanding what the pattern looks like when large institutions step in and buy… it's that failure swing**"; (36:42–36:51) "everything that we've shown here is **reversed when the dollar index is bullish**"; (39:14–39:50) "**not all commodities are equal, they're not going to perform the same**… focus on the ones that are giving you that **fingerprint hallmark signature**".
- `ICT-2017-STOCK-BUY-WATCHLIST` (03:14–03:20) "the **discount arrays with index SMT** will highlight companies that are under heavy accumulation during seasonally bullish months"; (03:28–04:24) "**leadership stocks that are aggressively bought by institutions will be found to fail to drop lower** during bullish months when the three major stock indices decline **until one of those indices fails to post a lower low** comparably"; (04:42–06:20) the Apple example — the Dow making a lower low in mid-January 2017 while AAPL refused, "**Apple was showing relative strength here, and that only occurs when large institutions come in and they sponsor buy programs**", accumulating at $118–$120 a share; (09:44–09:54) the method for the overlay — barchart.com, "add a comparison and do a left axis display on **dollar sign DOWI**"; (16:56–17:13) relative strength as the reason "the **strong got stronger**".
- `ICT-2017-STOCK-SELL-WATCHLIST` (02:17–02:53) "**weak stocks will have obvious bearish market structure**. The **premium arrays with index SMT** will highlight companies that are under heavy distribution during seasonally bearish months… leadership stocks that are aggressively sold by institutions will be found to **fail to rally higher** during bearish months when the three major indices rally **until one of those indices fail to post a higher high** comparably"; (04:42–04:50) "the rules are, **if it's not obvious there is no divergence on the SMT**"; (04:58–05:46) the American Express example — the Dow making higher highs into May 2015 while AXP failed to rally comparably, "**American Express was in heavy distribution**", $80 → almost $50 a share.

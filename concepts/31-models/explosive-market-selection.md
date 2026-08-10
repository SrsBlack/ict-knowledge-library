# Explosive Market Selection

**Category:** 31-models
**Aliases:** explosive swing trade hallmarks, market selection hallmarks, eight hallmarks, explosive move filter
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-EXPLOSIVE-MARKETS
**Tags:** models, swing-trading, market-selection, intermarket, cot, open-interest, seasonality, volatility, sentiment

## Definition

Explosive market selection is ICT's **eight-item checklist for deciding which market to
swing trade**, chosen for the highest probability of "dynamically moving one sided" price
action rather than a grinding move (`ICT-2017-EXPLOSIVE-MARKETS`, 00:23–00:44).

It selects a **market and a direction**; it supplies **no entry, stop or target**. The
hallmarks stack — each one added raises the expectation of magnitude, and ICT counts them
aloud ("we now have five things in our favor", 20:57). The same framework is named as a
precursor to the position-scale [mega-trade](mega-trade.md) (26:43).

## Formal Criteria

**1 — Major market analysis: at least two of four asset classes trending** (00:53–01:18, 07:42–09:32)

- The four classes are **interest rates, stocks, commodities, currencies**.
- Requirement: **at least two of the four are trending**, not held in consolidation and
  not conflicting.
- The two must come from **different groups**: one of {commodities, stocks} **and** one of
  {currencies, interest rates} — "one of those two must be in a trending environment"
  for each pair (09:16–09:32).
- All four trending is preferable but not required.

**2 — Intermarket analysis confluence** (01:32–03:14, 09:51–12:44)

- The idea must be corroborated across classes. For a **bullish dollar**: commodities at
  resistance, failing to make higher highs (or making false ones), breaking lows easily.
  For a **bearish dollar**: commodities break highs easily, hold lows, and any break below
  an old low is a turtle-soup long.
- Check breadth, not just the CRB index — the grains (soybeans, wheat, corn) are named as
  the confirmation sample (11:37–11:56).

**3 — COT hedging-program alignment** (03:32–04:36, 13:14–17:59)

- Take the commercials' net position over the **last 12 months**, mark its **highest and
  lowest** readings, and **divide that range in half**. The midpoint becomes a **new,
  recentred zero line**; the standard net-position zero line is deliberately ignored.
- Above the recentred line = commercials buying; below = selling. This resolves the case
  where commercials sit below the absolute zero line all year yet are clearly accumulating.
- See [commitment-of-traders](../03-order-flow/commitment-of-traders.md) for the full read.

**4 — Open interest** (04:40–05:04, 17:59–20:14)

- **A decline of 10–15 % or more in open interest is commercial short covering** — read as
  bullish when it coincides with the commercial net line rising toward zero.
- **A rise of 10–15 % or more while commercials increase net selling is bearish.**
- Available in futures only; this is the "X-ray view" of smart-money positioning.

**5 — Seasonal tendency** (05:04–05:22, 20:14–21:06)

- The seasonal window must point the same way as the idea.

**6 — Volatility filter** (05:24–06:23, 21:24–23:20)

- A **contraction** — price moving from a large range to a small one — immediately before
  expansion. Universal across timeframes.
- Qualifying forms: an **inside bar / inside candle** (lower high **and** higher low, with
  attention on the **bodies** rather than the wicks); the **smallest range of the last 3
  days**; the **smallest range of the last 7 days**.
- **It gives magnitude, not timing:** "it gives us an anticipatory expectation for price
  to explode… but it doesn't give you timing" (22:38).
- Direction is **not** supplied by the contraction — it comes from hallmarks 1–5.

**7 — Major news headlines, read contrarian** (06:27–06:31, 23:43–25:32)

- Bullish idea + **bearish** headlines = fuel. Bearish idea + **bullish** or record-high
  headlines = fuel. The headlines build the retail sentiment being traded against.

**8 — Market sentiment via Williams %R** (06:31–06:42, 25:32–26:38)

- ICT's one acknowledged indicator: **15-period Williams %R on the daily**.
- **At or below the 50 level = oversold / buying area; above 50 = overbought / selling area.**
- **Tiebreak at 50:** favour whichever extreme price left **most recently** — leaving
  oversold and returning to 50 still favours a buy; leaving overbought and hovering at 50
  favours the sell side.

## Formula / Math

```
# --- 1. trending breadth ---
group_A := {commodities, stocks}
group_B := {currencies, interest_rates}
breadth_ok := any(trending(c) for c in group_A) AND any(trending(c) for c in group_B)
              # i.e. >= 2 of 4, one from each group

# --- 3. COT, recentred ---
band_hi   := max(net_commercial, last 12 months)
band_lo   := min(net_commercial, last 12 months)
zero_new  := (band_hi + band_lo) / 2                 # replaces the printed zero line
cot_bull  := net_commercial(now) > zero_new

# --- 4. open interest ---
dOI_pct   := (OI(t) - OI(t-n)) / OI(t-n)
oi_bull   := dOI_pct <= -0.10  AND net_commercial rising toward zero    # short covering
oi_bear   := dOI_pct >= +0.10  AND net_commercial falling

# --- 6. volatility contraction ---
inside_bar(n)   := high(n) < high(n-1) AND low(n) > low(n-1)
narrow3(n)      := range(n) == min(range(n-2..n))
narrow7(n)      := range(n) == min(range(n-6..n))
contraction(n)  := inside_bar(n) OR narrow3(n) OR narrow7(n)
# supplies magnitude expectation only; timing and direction come from elsewhere

# --- 8. sentiment ---
wpr := WilliamsPercentR(period=15, tf=D)
sentiment := wpr <= 50 ? BUY_AREA : SELL_AREA
# at exactly 50: inherit the most recently vacated extreme

# --- score ---
hallmarks_met := count([breadth_ok, intermarket_ok, cot_bull, oi_bull,
                        seasonal_ok, contraction, headlines_contrarian, sentiment_ok])
# no threshold is taught; more hallmarks => larger expected magnitude
```

## Machine-Readable

```json
{
  "id": "explosive-market-selection",
  "category": "31-models",
  "aliases": ["explosive-swing-hallmarks", "market-selection-hallmarks", "eight-hallmarks"],
  "criteria": [
    {"id": "c1", "expr": ">=2 of 4 asset_classes trending, >=1 from {commodities,stocks} AND >=1 from {currencies,interest_rates}"},
    {"id": "c2", "expr": "intermarket_confluence_across_classes == true"},
    {"id": "c3", "expr": "cot_zero_line := midpoint(max,min of commercial_net over 12 months); position judged against it"},
    {"id": "c4", "expr": "abs(delta_open_interest) >= 0.10..0.15 paired with commercial_net direction"},
    {"id": "c5", "expr": "seasonal_tendency aligned_with idea"},
    {"id": "c6", "expr": "volatility_contraction := inside_bar OR smallest_range_3d OR smallest_range_7d"},
    {"id": "c7", "expr": "contraction supplies magnitude, not timing and not direction"},
    {"id": "c8", "expr": "news_headlines contrarian_to_idea"},
    {"id": "c9", "expr": "WilliamsPercentR(15, D) <= 50 => buy_area; > 50 => sell_area; at 50 inherit last vacated extreme"},
    {"id": "c10", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["mega-trade", "commitment-of-traders", "open-interest", "seasonal-tendency", "dollar-index", "bond-yield-analysis", "turtle-soup"],
  "sources": ["ICT-2017-EXPLOSIVE-MARKETS"]
}
```

## Visual Pattern

```
  THE EIGHT HALLMARKS, STACKED

   1  breadth        [commodities|stocks] ✓   and  [currencies|rates] ✓
   2  intermarket    dollar bullish  ->  commodities failing highs, breaking lows
   3  COT            ────────────── printed zero (ignored)
                     ══════════════ recentred zero = midpoint of 12-month range
                     commercial net now ABOVE it  -> buying
   4  open interest  OI ↓ 10-15%  +  commercial line rising  -> short covering
   5  seasonal       window points the same way
   6  volatility     ██████   large range
                       ▒▒▒    inside bar / narrowest of 3 or 7  <- the coiled spring
   7  headlines      "why gold is weak"  while you are the buyer
   8  sentiment      Williams %R(15, D) at or below 50

   ─────────────────────────────────────────────────────────────
   more hallmarks met  ->  larger expected magnitude
   direction from 1-5 · magnitude from 6 · entry from NONE of them
```

## Timeframes

Daily, weekly and monthly. The volatility filter is explicitly universal — "it can be
applied to monthly, weekly, daily, or any other time frame" (21:35) — but the checklist as
a whole is a swing-trade selection tool and has no intraday form.

## Examples

**Example 1 — the COT recentring (14:46–17:26):**
- Setup: commercials had been **below the printed zero line since January 2016** — bearish
  by the conventional Larry Williams reading.
- Method: mark the January-2016 high and the July-2016 low of the commercial line, halve
  the range, take the midpoint as the new zero.
- Observation: December 2016 crossed **above** the recentred line while still below the
  printed zero.
- Read: "they were buying again aggressively in December" — a bullish hallmark that the
  conventional reading would have called bearish.

**Example 2 — open interest confirming (19:01–19:36):**
- Observation: open interest fell from over 500,000 to about 400,000 contracts between
  November and December — "over 100,000 contracts taken off that were short".
- Coincident: the commercial net line rose toward zero.
- Read: commercial short covering; "confirmation that your trade would be a bullish
  scenario and **explosive price action should be expected**".

**Example 3 — full stack (20:14–21:24):**
- Two asset classes trending, open interest declined, commercials buying, intermarket
  analysis supportive, seasonal tendency pointing up through December into February.
- Count: "we now have five things in our favor suggesting there's going to be an explosive
  price action in this particular market."
- Expectation set: "prices should move higher, **not in small ranges**, but should be
  explosive… it shouldn't be a lethargic price action move."

## Common Mistakes

- **Using the printed COT zero line.** Hallmark 3 exists specifically to replace it. A
  market can be net short all year and still be accumulating.
- **Reading the contraction as a direction signal.** An inside bar says *how big*, never
  *which way* — and never *when*.
- **Requiring all four asset classes to trend.** Two is the stated bar; ICT expects one
  class to lag in consolidation.
- **Treating this as a setup.** Like [mega-trade](mega-trade.md), it selects the market and
  the side. Entry, stop and target come from the ordinary toolkit.
- **Taking headlines at face value.** The headline is read as *confirmation of the crowd's
  position*, which is the opposite of its literal content.
- **Applying Williams %R as a standalone signal.** It is hallmark eight of eight, and ICT
  frames it only as an overbought/oversold sentiment gauge.
- **Applying open interest to spot FX.** It exists in futures only; that is why ICT trades
  the majors and "com dollars" — the futures data is available for them (04:40–04:56).

## Related Concepts

- [mega-trade](mega-trade.md) — the position-scale sibling; ICT states these hallmarks are revisited there.
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md) — hallmark 3 in full, including the recentred zero line.
- [open-interest](../03-order-flow/open-interest.md) — hallmark 4, including the 10–15 % thresholds.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — hallmark 5.
- [dollar-index](../03-order-flow/dollar-index.md) — the hub of the intermarket confluence check.
- [bond-yield-analysis](../03-order-flow/bond-yield-analysis.md) — how the interest-rate class is judged trending or not.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the expected behaviour of commodity lows in a weak-dollar regime.

## Citations

- `ICT-2017-EXPLOSIVE-MARKETS` (00:00–00:31) "Lesson 7 … in the Swing Trading Model… the keys to selecting markets that will move explosively… the hallmarks to explosive swing trades"; (00:53–01:18) the four asset classes, "at least half of the 4 or 2 of them showing a profile where there are trending environments underway"; (01:32–03:14) intermarket confluence, the bullish- and bearish-dollar templates; (03:32–04:36) the COT hedging program — "we look back in the last 12 months on the net positions held by the commercial traders… whatever that range is we divide that in half"; (04:40–05:04) open interest as the smart-money X-ray, futures-only; (05:04–05:22) seasonal tendency; (05:24–06:23) the volatility filter — "the market going into contraction right before a big explosive type of move… that is a hallmark that spells wild profitability if you get the direction right"; (06:27–06:31) major news headlines; (06:31–06:42) market sentiment; (09:16–09:32) the grouping rule — one of {commodities, stocks} and one of {currencies, interest rates}; (11:37–12:26) grains as the breadth sample; turtle-soup lows under a weak dollar; (13:14–14:12) commercials defined; the 12-month hedging plan rationale; (14:46–15:11) the Larry Williams attribution and the printed zero line; (15:18–16:28) "I frame the last 12 months and look at the highest high and the lowest low and divide it in half, and I have a new zero line — so I ignore the zero line on the standard net trader position chart"; (16:28–17:26) the December-2016 crossing above the recentred line; (18:00–18:23) open interest as an X-ray of smart money; (19:22–19:36) "if open interest declines 10% or 15% or more, that's indicative of commercial short covering"; (19:01–19:15) the 500,000 → 400,000 contract example; (19:36–19:49) the bearish mirror — "an increase of open interest, 10% to 15% or more at a time when the commercials increase their net selling… that is bearish"; (20:14–21:24) the five-hallmark stack and the explicit magnitude expectation; (21:24–23:20) the volatility filter in detail — inside bar by lower high and higher low, bodies over wicks, smallest range in the last 3 and last 7 days, "it doesn't give you timing"; (23:43–25:32) contrarian headline reading; (25:32–26:38) "I use an indicator… it's the Williams percent R… a 15-period Williams percent R on a daily basis… anything at the 50 level or below that is oversold and a buying area", plus the tiebreak at 50; (26:43) the hallmarks are revisited when mega-trades are taught.

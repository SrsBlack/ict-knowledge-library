# Stock Watchlist Construction

**Category:** 31-models
**Aliases:** buy watchlist, sell watchlist, stock selection, Dow 30 filter, equity watchlist
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STOCK-BUY-WATCHLIST, ICT-2017-STOCK-SELL-WATCHLIST, ICT-2017-STOCK-VALUATION
**Tags:** models, equities, stock-selection, seasonality, index-smt, relative-strength, swing-trading

## Definition

Stock watchlist construction is ICT's **funnel for reducing an index's component list to two to
four tradeable names** ahead of a seasonal turn. It is run twice a year in mirror form — a **buy
watchlist** before a seasonally bullish window and a **sell watchlist** before a seasonally
bearish one — and it produces a *list*, not a trade: "**try to narrow the selection to two to four
companies** during your stock selection process" (`ICT-2017-STOCK-BUY-WATCHLIST`, 03:20).

The universe is deliberately small. ICT uses the **Dow Jones 30**: "the same application is
obviously done on the S&P 500 and NASDAQ 100, but **it's not necessary — you can make all the
stock trades you'd need just from the Dow Jones 30 stock list**" (00:43).

Equities are **swing-traded only**: "there's no getting in there **day trading stocks** — it's
nonsense, it's foolishness. You want to be in there capturing **swing trades in stocks**, that's
it" (`ICT-2017-STOCK-VALUATION`, 33:37).

## Formal Criteria

**Two named filters, then four screens**

| Step | Buy watchlist | Sell watchlist |
|---|---|---|
| **Filter 1** | is the **stock market poised to rally**? | is the **stock market poised to decline**? |
| **Filter 2** | during **bullish months**, select stocks that made a **higher low** | during **bearish months**, select stocks that made a **lower high** |
| Screen A — season | **Feb → May** and **Oct → Jan** are ideal long swing windows | **January** and **May → July** are ideal short swing windows |
| Screen B — weekly order flow | already **trending higher on the weekly** before the setup | already **trending lower on the weekly** before the setup |
| Screen C — exclusions | avoid **"safe stocks"**: Verizon, General Electric, Coca-Cola (ICT adds Microsoft and Intel as "not exciting anymore") | same exclusion list |
| Screen D — structure | **obvious bullish structure**; discount arrays + index SMT mark heavy accumulation | **obvious bearish structure**; premium arrays + index SMT mark heavy distribution |
| **Output** | **2–4 companies** | **2–4 companies** |

- The sell lecture states the primary bearish encapsulation precisely: "the entire encapsulation
  of **beginning of May to the first of August**" (`ICT-2017-STOCK-SELL-WATCHLIST`, 03:05).

⚠ **Window conflict.** The buy lecture says "**October to January** months are ideal long swing
setups" (02:09) while the sell lecture names **January** as an ideal short-swing month (01:50) and
[equity-seasonal-windows](../04-time-cycles/equity-seasonal-windows.md) records January as
**bearish** with the buy program ending at year-end. Both statements are ICT's, in the same week.
The library carries both; treat late September/October → year-end as the reliable long window.

**The core signal — a two-layer divergence** (03:28–04:24)

1. **Market layer.** The three major averages (NASDAQ, S&P, Dow) decline together into the
   seasonal date and **one of them fails to post a lower low** — "that signals the overall market
   trend change to bullishness." Mirror for the sell list: all three rally and **one fails to post
   a higher high** — "**classic fingerprint for distribution**"
   (`ICT-2017-STOCK-SELL-WATCHLIST`, 03:41).
2. **Share layer.** At that same juncture, the individual share **refuses to make the matching
   low** against a Dow Jones overlay. "If it doesn't occur for that particular stock, then
   obviously that stock is going to be **discarded**" (04:15).

- Overlay method: barchart.com, "add a comparison and do a **left axis display on `$DOWI`**"
  (09:44).
- **Obviousness gate:** "the rules are, **if it's not obvious there is no divergence on the SMT**"
  (`ICT-2017-STOCK-SELL-WATCHLIST`, 04:42).
- See [relative-strength-analysis](../03-order-flow/relative-strength-analysis.md) for the general
  form of this refusal-to-follow read.

**The extension test — what removes a name from the list** (12:05–13:05)

- "A stock from this list that was **too extended from a weekly or daily market structure** would
  **eliminate it from the list**."
- The wanted shape is a **low-resistance liquidity run**: price already sitting close beneath a
  clean old high, so the seasonal buying delivers a **weekly breakout**. "Institutions like to see
  **big breakouts, big movements higher, especially on a weekly chart**" (12:23).
- The rejected shape is a stock that "would have to rally about **$15** before it even gets to the
  old high" — "**institutions won't be that aggressive about buying this type of stock because
  it's not poised technically, regardless of what the fundamentals may be**" (16:35–16:55).
- Sell-side mirror: a name that only **drifted** lower without a rally to sell into is discarded —
  "you really want to find an area where price **wants to rally away**, kind of like a **Judas
  swing** or market protractionary state, where we **sell the rally**"
  (`ICT-2017-STOCK-SELL-WATCHLIST`, 09:35–09:54).

**Fundamental tiebreakers** (13:05, 14:38)

- **Quarterly increases in sales and profits** keep a name on the list.
- Share price **above $20** with a **reasonable float** (`ICT-2017-STOCK-VALUATION`, 14:38).
- ICT's stated stack: "blending a simple **seasonal, fundamental, and ultimately technical**
  trading process for selecting possible winning stocks."

**Where ICT's own contribution sits** (`ICT-2017-STOCK-VALUATION`, 07:35–08:26, 29:53)

- The fundamental screen ICT uses is **William J. O'Neill's CAN SLIM**, taken from *Investor's
  Business Daily* — not ICT's own work and outside this library's scope.
- ICT replaces only the final letter: "I don't believe that **William J. O'Neill's approach to
  timing the market was sufficient enough**… the last one here is **the technical basis, which is
  my own input into it**."
- That substitution is: "**institutional order flow, market structure, and… premium and discount
  array modeling, and using the divergence between the three averages**" (29:53), plus **Dow
  theory** — "the only thing that matters for stocks in terms of things that's been around forever
  is **Dow theory**" (19:28).

## Formula / Math

```
universe := DJIA_30                      # NDX-100 / SPX-500 optional, not required
exclude  := {VZ, GE, KO}                 # "safe stocks"; ICT also drops MSFT, INTC

# --- season gate ---
long_window  := month in (Feb..May) or (Oct..Jan)     # see conflict note
short_window := month in {Jan} or (May..Jul)          # primary: 1 May -> 1 Aug

# --- market layer (index SMT) ---
averages := {NASDAQ, SP500, DJIA}
bullish_turn := all averages decline into the seasonal date
                AND >=1 FAILS to post the lower low
bearish_turn := all averages rally into the seasonal date
                AND >=1 FAILS to post the higher high

# --- share layer ---
keep_long(s)  := bullish_turn AND NOT s.lower_low(t)   # vs $DOWI overlay
keep_short(s) := bearish_turn AND NOT s.higher_high(t)

# --- structural screens ---
weekly_order_flow(s) aligned with the intended direction
structure_obvious(s) == true
extension(s) := distance(price, nearest clean old high)      # long case
keep only if extension is SMALL  -> a low-resistance liquidity run
                                    delivering a weekly breakout

# --- fundamental tiebreakers ---
quarterly sales and profits increasing
share_price > $20 AND float is reasonable

# --- output ---
watchlist := 2..4 names
holding   := SWING only; day trading equities is excluded
```

## Machine-Readable

```json
{
  "id": "stock-watchlist-construction",
  "category": "31-models",
  "aliases": ["buy-watchlist", "sell-watchlist", "stock-selection", "dow-30-filter"],
  "criteria": [
    {"id": "c1", "expr": "universe := DJIA 30; SP500/NDX100 optional and unnecessary"},
    {"id": "c2", "expr": "filter1 := market poised to rally (buy) or decline (sell)"},
    {"id": "c3", "expr": "filter2 := higher-low stocks in bullish months; lower-high stocks in bearish months"},
    {"id": "c4", "expr": "long windows == Feb..May and Oct..Jan; short windows == Jan and May..Jul (primary 1 May..1 Aug)"},
    {"id": "c5", "expr": "weekly order flow must already point the intended way"},
    {"id": "c6", "expr": "exclude safe stocks {VZ, GE, KO} (ICT also drops MSFT, INTC)"},
    {"id": "c7", "expr": "signal := index SMT across {NASDAQ,SP500,DJIA} AND the share refusing the matching extreme vs a $DOWI overlay"},
    {"id": "c8", "expr": "divergence must be obvious; otherwise it does not exist"},
    {"id": "c9", "expr": "eliminate names too extended from weekly/daily market structure; require a near, clean old high (low-resistance liquidity run)"},
    {"id": "c10", "expr": "sell side requires a rally to sell into (Judas-swing shape), not a steady drift"},
    {"id": "c11", "expr": "tiebreakers := rising quarterly sales and profits; price > $20; reasonable float"},
    {"id": "c12", "expr": "output == 2..4 names; equities are swing-traded only"},
    {"id": "c13", "expr": "fundamental screen is O'Neill CAN SLIM (not ICT); ICT replaces only the market-timing letter"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["relative-strength-analysis", "equity-seasonal-windows", "index-smt", "seasonal-tendency", "liquidity-run", "institutional-order-flow", "discount-array", "premium-array", "bullish-order-block", "explosive-market-selection", "mega-trade", "multi-asset-analysis"],
  "sources": ["ICT-2017-STOCK-BUY-WATCHLIST", "ICT-2017-STOCK-SELL-WATCHLIST", "ICT-2017-STOCK-VALUATION"]
}
```

## Visual Pattern

```
   THE FUNNEL (buy side)

   DOW 30
     │  drop "safe stocks"  (VZ, GE, KO … MSFT, INTC)
     ▼
   ~25 names
     │  weekly order flow must already be bullish
     ▼
     │  MARKET LAYER — index SMT at the seasonal date
     │     NASDAQ  ╲___  lower low   ✓
     │     S&P     ╲___  lower low   ✓
     │     DOW     ╲__╱  HIGHER low  ✗   <- the turn
     ▼
     │  SHARE LAYER — share vs $DOWI overlay
     │     $DOWI   ╲___  lower low
     │     AAPL    ╲__╱  HIGHER low  ✗   <- accumulation ($118-120)
     ▼
   6 names
     │  EXTENSION TEST
     │
     │   KEEP:              ─────── old high (clean, close above)
     │                     ╱‾‾  price here  -> weekly breakout
     │
     │   DROP:             ─────── old high
     │                                  (+$15 away)
     │                     ╱‾‾  price here  -> lethargic, institutions pass
     ▼
   2-4 names  ->  swing trades only
```

## Timeframes

**Weekly** for structure and the extension test; **daily** for the SMT comparison at the seasonal
date; **monthly** for the seasonal window itself. No intraday component — equities are explicitly
swing-only.

## Examples

**Example 1 — the buy funnel, February 2017 (`ICT-2017-STOCK-BUY-WATCHLIST`, 04:42–11:54):**
- Seasonal date: mid-January 2017, the Dow Jones printing a **lower low** into the February
  bullish window.
- Six survivors of the Dow 30: **Apple, Boeing, Disney, Home Depot, McDonald's, Visa** — each
  refused to make the matching lower low.
- Apple: accumulated at **$118–$120**, then appreciated February → May.
- Boeing and Home Depot each **gapped up in January** and closed the resulting fair value gap in
  the first days of February — a discount array — before rallying.

**Example 2 — Disney, rejected on the extension test (15:47–17:24):**
- Refused the Dow's lower low, so it passed the divergence filter.
- Weekly structure was weak: a short-term high already taken out, and the 2015 high sat about
  **$15** above price.
- Verdict: "it has to have **a lot more movement** to get to a new breakout. **Institutions won't
  be that aggressive** about buying this type of stock because it's **not poised technically**."
- Outcome: traded a little above 116 and then softened, against Apple's and Boeing's clean runs.

**Example 3 — the sell funnel, May–July 2015 (`ICT-2017-STOCK-SELL-WATCHLIST`, 03:16–09:12):**
- Market layer: NASDAQ made a **higher high** while the Dow and S&P **failed to** — "classic
  fingerprint for distribution."
- Survivors: **American Express** ($80 → ~$50), **Caterpillar** (~$90 → ~$55), **Chevron**
  ($110 → $70), **Exxon Mobil** ($90 → ~$66), **Walmart** ($80 → ~$56).
- Caterpillar is used as the control: in the preceding bullish stretch it made a high but produced
  **no divergence** — "we can't do anything with it."

**Example 4 — Walmart, kept but downgraded (09:12–10:01):**
- The decline was real, but there was "**really no attempt to rally, it was just a steady drift
  lower**" — no protractionary rally to sell into.
- Verdict: the other four "would have been ones to choose from in terms of looking for put
  options."

## Common Mistakes

- **Skipping filter 1.** The market-level question comes first; a share-level divergence with no
  index-level turn is not a signal.
- **Taking every survivor.** The output is **2–4 names**, not the full survivor list — the
  extension test does the final cut.
- **Keeping an extended stock because the fundamentals are good.** ICT is explicit that
  fundamentals do not rescue poor technical positioning.
- **Shorting a steady drift.** The sell side needs a rally to sell into.
- **Forcing a marginal SMT.** If it is not obvious, there is no divergence.
- **Trading equities intraday.** Explicitly excluded.
- **Attributing CAN SLIM to ICT.** It is O'Neill's, via *Investor's Business Daily*; ICT replaces
  only the market-timing component, and this library documents only that replacement.
- **Treating the October → January long window as settled.** It conflicts with the January-bearish
  and January-short-swing statements from the same week.

## Related Concepts

- [relative-strength-analysis](../03-order-flow/relative-strength-analysis.md) — the general refusal-to-follow read that both layers of the signal are instances of.
- [equity-seasonal-windows](../04-time-cycles/equity-seasonal-windows.md) — the calendar this funnel is timed against, including the month-by-month Dow tendency table.
- [index-smt](../16-smt-divergence/index-smt.md) — the market-layer divergence across NASDAQ, S&P and Dow.
- [liquidity-run](../02-liquidity/liquidity-run.md) — the low-resistance liquidity run the extension test is screening for.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the weekly-chart requirement.
- [discount-array](../05-pd-arrays/discount-array.md), [premium-array](../05-pd-arrays/premium-array.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md) — where the entry is actually taken.
- [mega-trade](mega-trade.md) — the six-to-nine-month equity horizon these lists feed.
- [explosive-market-selection](explosive-market-selection.md) — the same seasonal-plus-intermarket stacking, for futures swing trades.
- [multi-asset-analysis](../03-order-flow/multi-asset-analysis.md) — why an FX-only trader runs this at all.

## Citations

- `ICT-2017-STOCK-BUY-WATCHLIST` (00:08–00:13) "**Lesson two of the ICT Mentorship June 2017 content. This is ICT Stock Trading, Building Buy Watch Lists**" — self-dates the lecture; (00:24–00:56) the Dow Jones Industrial composite list of 30 stocks — "the same application is obviously done on the S&P 500 and NASDAQ 100, but **it's not necessary**. You can make all the stock trades you'd need just from the **Dow Jones 30** stock list"; (01:51–02:09) "**filter number one**… is the stock market poised to rally?… **filter number two** is during bullish months, we want to be **selecting higher low stocks**"; (02:09–02:19) "the **February to May** months are ideal long swing setups and the **October to January** months are ideal long swing setups as well" ⚠ (conflicts with the January-bearish statements elsewhere in the same week); (02:40–02:52) "the majority of index stocks generally rise when the major market rallies — **in high tide, all boats rise**"; (02:52–02:59) "stocks that are **trending higher on the weekly** prior to our condition of looking to be a buyer, they're going to be ideal scenarios"; (02:59–03:08) "we want to **avoid safe stocks like Verizon, GE or General Electric or Coca-Cola**"; (03:08–03:20) "**strong stocks will have an obvious bullish structure**. The **discount arrays with index SMT** will highlight companies that are under heavy accumulation during seasonally bullish months"; (03:20–03:28) "**try to narrow the selection to two to four companies**"; (03:28–04:24) "**leadership stocks that are aggressively bought by institutions will be found to fail to drop lower** during bullish months when the three major stock indices decline **until one of those indices fails to post a lower low** comparably… if it doesn't occur for that particular stock, then obviously that stock is going to be **discarded**"; (04:42–06:20) the Apple example, accumulation at $118–$120; (06:26–07:41) Boeing — the January gap closed on the second trading day of February, "**discount array**… fair value gap traded down, closed into it, and then rallied away"; (08:27–09:23) Home Depot's liquidity void closed in February; (09:44–09:54) the barchart.com overlay method, "**dollar sign DOWI**"; (11:13–11:54) the six survivors — Apple, Boeing, Disney, Home Depot, McDonald's, Visa — with Microsoft and Intel also dropped as "just not exciting anymore"; (12:05–12:13) "a stock from this list that was **too extended from a weekly or daily market structure** would **eliminate it from the list**"; (12:13–12:48) the low-resistance liquidity run and the weekly breakout institutions want; (12:48–13:05) "if you have a market structure high that's really higher than where you're going to be entering at, generally you're going to see some **lethargic price action**"; (13:05–13:23) quarterly increases in sales and profits, and "blending a simple **seasonal, fundamental, and ultimately technical** trading process"; (15:47–17:24) the Disney rejection — "it would have to rally about **$15** before it even gets to the old high seen in 2015… **institutions won't be that aggressive** about buying this type of stock because it's **not poised technically regardless of what the fundamentals may be**"; (20:21–20:31) "**yes, I'm saying breakout, because stocks are predisposed to trade higher**"; (20:31–21:02) the full recipe restated — fundamentals, seasonals, "relative strength ideas supporting with the **SMT divergence between the indices**, and that stock is showing an **unwillingness to go lower**".
- `ICT-2017-STOCK-SELL-WATCHLIST` (00:00–00:19) "**lesson three of the ICT stock trading June 2017 content, this lesson is building sell watch lists**" — self-dates the lecture; (00:31–00:52) "not all stocks go up when there's a bullish or bearish idea; there's a **disparity amongst all the index stocks**"; (01:31–01:50) "**filter number one** is obviously the stock market must be **poised to decline**, and **filter number two**, during bearish months, we're going to be looking for stocks that make a **lower high**… the months of **January and May through July are ideal short swing setups**"; (02:00–02:17) "majority of index stocks will decline with the major market decline; stocks that are **trending lower on a weekly** prior to this setup are ideal; we're going to be **avoiding safe stocks like Verizon, GE and Coca-Cola**"; (02:17–02:53) "**weak stocks will have obvious bearish market structure**. The **premium arrays with index SMT** will highlight companies that are under heavy distribution… narrow the selection down to **two to four companies**… leadership stocks that are aggressively sold by institutions will be found to **fail to rally higher** during bearish months when the three major indices rally **until one of those indices fail to post a higher high** comparably"; (02:53–03:16) "**January generally is a bearish month**, but we're going to focus primarily on the condition from **May high through the month of July**… the entire encapsulation of **beginning of May to the first of August**"; (03:16–03:51) the 2015 May–June–July index SMT — "**NASDAQ at the top made a higher high but the Dow and the S&P at the bottom failed to make a higher high, so we have classic fingerprint for distribution**"; (04:42–04:50) "**the rules are, if it's not obvious there is no divergence on the SMT**"; (04:58–05:46) American Express, $80 → almost $50; (05:46–06:59) Caterpillar as the control case with no divergence in the preceding bullish stretch, then ~$90 → ~$55; (07:00–07:47) Chevron $110 → $70; (07:48–08:32) Exxon Mobil $90 → ~$66; (08:32–09:12) Walmart $80 → ~$56; (09:12–10:01) the Walmart downgrade — "there was really **no attempt to rally, it was just a steady drift lower**… you really want to find an area where price **wants to rally away**, kind of like a **Judas swing** or market protractionary state, where we **sell the rally**"; (10:07–11:22) institutions as rule-followers leaving repeatable footprints, "so we can **track smart money**"; (11:37–12:07) "regardless of whether we're a stock trader or a bond trader or a commodity trader or an S&P trader, **these four asset class studies that we've done this month are paramount**"; (12:07–13:10) the NASDAQ-100 homework using the same buy and sell parameters.
- `ICT-2017-STOCK-VALUATION` (00:22) "**June 2017 ICT mentorship, stock trading lesson four, valuation stock selections**" — self-dates the lecture. ⚠ This packet's YouTube title is *"Stock Trading — Using Options"*; the options lesson is the separately catalogued `ICT-2017-STOCK-OPTIONS` (`Pdpx3aSyWos`), whose own title reads *"Valuation Stock Selection"*. **The two titles are swapped relative to their content.** The bulk of this lecture is William J. O'Neill's **CAN SLIM** fundamental screen and *Investor's Business Daily* usage, which is outside this library's scope and is deliberately not documented. Cited here only for: (06:55) the CAN SLIM attribution; (07:35–08:26) "the last one here is **the technical basis, which is my own input into it** — I don't believe that **William J. O'Neill's approach to timing the market was sufficient enough**"; (14:38–14:54) "it has to be a **share price of over $20 a share** and it has to have a **reasonable float**"; (16:15–16:38) "**consider buying high and selling higher**… basically that's a **low resistance liquidity run**… we know there's going to be reaching for **buy side liquidity**"; (17:02–17:19) "the greatest market winners revealed… that **the strong got stronger, and that's the basis of how I use relative strength analysis**"; (19:28–19:48) "the only thing that matters for stocks in terms of things that's been around forever is **Dow theory**… coupled with how I look at institutional sponsorship and institutional order flow and **premium and discount arrays**"; (22:33) "you actually put **Investor's Business Daily's statistics on steroids**"; (29:53–30:20) "the stock selection process… is basically the **Investor's Business Daily CAN SLIM method but me blending in my technical analysis of institutional order flow, market structure, and… premium and discount array modeling, and using the divergence between the three averages**"; (33:37–33:51) "there's **no getting in there day trading stocks — it's nonsense, it's foolishness. You want to be in there capturing swing trades in stocks**, that's it".

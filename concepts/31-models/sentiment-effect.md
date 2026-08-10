# The Sentiment Effect

**Category:** 31-models
**Aliases:** sentiment effect, sentiment confluence, Asian-range sentiment entry
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-SENTIMENT-EFFECT
**Tags:** models, day-trading, asian-range, sentiment, williams-percent-r, judas, entry-conditions

## Definition

The sentiment effect is ICT's rule that **short-term sentiment is at its most extreme against
you at the exact moment the high-probability entry exists**: "short-term sentiment will be
**most bearish** at the time when we enter our **long** trades"
(`ICT-2017-SENTIMENT-EFFECT`, 05:46), and the mirror for shorts.

Operationally it is a set of **day-trade entry conditions** built on the Asian range and the
midnight-New-York opening price, opened by lesson 1 of the May-2017 "amplified day trading and
scalping" month. The mechanism is the [Judas swing](../13-judas-swing/judas-swing.md): "the
market will have a short-term shift in sentiment and less informed traders will chase price on
the impulse or the initial swing intraday — this is classically known… as the Judas swing"
(01:03–01:17).

## Formal Criteria

**The core asymmetry** (00:47–01:03)

- **Bearish / short days:** look to sell **above** the opening price and/or the **Asian range
  high**.
- **Bullish / long days:** look to buy **below** the opening price and/or the **Asian range low**.
- Restated as smart-money behaviour: "smart money **sells above the Asian range high**" when
  daily/H4 order flow is bearish; "smart money **buys below the Asian range low** and below
  that opening price" when it is bullish (02:05–02:20).

**The opening price** (02:20–02:48)

- Primary reference: the **midnight New York candle**.
- The **0 GMT** opening price may substitute if the range since 0 GMT has been a consolidation
  with little movement either way.

**Buy conditions — all four required** (03:17–05:53)

1. A **daily and/or minimum four-hour discount array is in play** — price has recently traded
   into it and **reacted**, showing willingness to support.
2. **Sufficient range in pips** between market price and the opposing **premium** array on the
   daily/H4. ICT's own preference: **50–60 pips**; "anything less than 40 pips and it's a scalp".
3. Price **declines under the opening price and/or the Asian range low**, ideally into a
   **logical discount array on the 15-minute chart**.
4. **Price must leave that 15-minute array sharply.** "Typically price will not spend much time
   at the discount array on the 15-minute chart… **the longer price stays or hovers near that
   15-minute discount array, the odds drop off precipitously**" — the banks will not hold a
   discount for long.

**Sell conditions — the exact mirror** (07:58–09:05)

- Daily/H4 **premium** array in play; sufficient range to the opposing discount array; price
  rallies **above the opening price and the Asian range high** into a logical **15-minute
  premium array**; and price must leave it sharply.

**The sentiment gauge** (05:53–06:33)

- **10-period Williams %R plotted on the 15-minute chart.**
- ⚠ **Not used as an overbought/oversold signal.** "We don't look at the overbought/oversold
  conditions that this indicator usually is… referred to. The conditions really are, we're
  looking at **price primarily**, and if we get a **sentiment confluence**… this gives us a
  higher odds that we probably are going to be on the right side of the marketplace."
- ⚠ **Different settings from [explosive-market-selection](explosive-market-selection.md)**,
  which uses a **15-period Williams %R on the daily** as a genuine overbought/oversold read.
  Same indicator, different period, different timeframe, different job.

**Frequency discipline** (10:09–12:44)

- The condition set does **not** appear every day: "day trading is not an everyday trading."
- The month's "20 pips per day" framing is explicitly **not** an instruction to trade daily.
- ICT names the failure mode from his own experience — becoming "pip drunk", where a winning
  streak inflates self-assessment just before a dry spell.

## Formula / Math

```
open_ref := midnight_NY_open            # or 0 GMT open if the 0 GMT range is a consolidation
AR_high, AR_low := Asian range bounds

# --- BUY ---
buy_setup :=
      daily_or_H4_discount_array_in_play AND reacted_from_it
  AND pips_to_opposing_premium_array >= ~50      # <40 pips => scalp, not a day trade
  AND price < open_ref  AND/OR  price < AR_low
  AND price reaches a 15-minute discount array
  AND time_spent_at_15m_array is SHORT           # sharp departure required
  AND short_term_sentiment is at its MOST BEARISH

# --- SELL: exact mirror ---
sell_setup :=
      daily_or_H4_premium_array_in_play AND reacted_from_it
  AND pips_to_opposing_discount_array >= ~50
  AND price > open_ref  AND/OR  price > AR_high
  AND price reaches a 15-minute premium array
  AND time_spent_at_15m_array is SHORT
  AND short_term_sentiment is at its MOST BULLISH

sentiment := WilliamsPercentR(period=10, tf=M15)   # confluence only, NOT an OB/OS trigger

# --- the decay rule ---
odds(t) decreases sharply with time_hovering_at_the_15m_array
```

## Machine-Readable

```json
{
  "id": "sentiment-effect",
  "category": "31-models",
  "aliases": ["sentiment-confluence", "asian-range-sentiment-entry"],
  "criteria": [
    {"id": "c1", "expr": "entry occurs when short_term_sentiment is maximally opposed to the trade"},
    {"id": "c2", "expr": "bullish: buy below open_ref and/or Asian_range_low; bearish: sell above them"},
    {"id": "c3", "expr": "open_ref := midnight_NY open (0 GMT open if that range is a consolidation)"},
    {"id": "c4", "expr": "daily_or_H4 discount(long)/premium(short) array in play and already reacted from"},
    {"id": "c5", "expr": "pips_to_opposing_HTF_array >= ~50; < 40 reclassifies the trade as a scalp"},
    {"id": "c6", "expr": "entry at a 15-minute discount/premium array"},
    {"id": "c7", "expr": "odds decay sharply the longer price hovers at the 15m array"},
    {"id": "c8", "expr": "sentiment := WilliamsPercentR(10, M15) used as confluence, NOT as overbought/oversold"},
    {"id": "c9", "expr": "setup does not occur daily; frequency discipline is part of the method"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["asian-range", "asian-range-high", "asian-range-low", "judas-swing", "market-protraction", "ict-day-trading-model", "explosive-market-selection", "discount-array", "premium-array"],
  "sources": ["ICT-2017-SENTIMENT-EFFECT"]
}
```

## Visual Pattern

```
   BULLISH DAY (daily/H4 discount array already respected)

     ─────────────────────────────────────────  opposing PREMIUM array
                                        ╱‾‾‾      (>= ~50 pips away)
                                     ╱‾
     ── AR high ───────────────────╱────────────
                        ╱‾╲     ╱‾
     ── open_ref ──────╱───╲──╱──────────────── midnight NY open
     ── AR low ───────╱─────╲╱─────────────────
                    ╱      ▼ 15m DISCOUNT array
                            ▲ ENTRY HERE
                              price must LEAVE SHARPLY
                              hovering = odds collapse

     sentiment at this instant: MOST BEARISH   <- that is the signal,
     Williams %R(10, M15) at its low              not a contradiction

   BEARISH DAY: mirror everything.
```

## Timeframes

Daily and H4 supply the array and the range check; the Asian range and midnight open frame the
day; entry and the sentiment gauge live on the **15-minute** chart.

## Examples

**Example 1 — the Thursday weekly low, called before the fact (06:33–07:57):**
- Context: ICT had stated during the week that the **weekly low would likely form in Thursday's
  New York session**.
- Sequence: price ran the intraday sell stops at the 08:30 NY employment release — but did so
  **before the number was released** — into a daily **old-low discount array**.
- Delivery: price rallied through two fair value gaps and stopped dead at gap resistance in the
  uppermost one, the daily premium draw.
- ICT's note: it "would otherwise be looked at as hindsight cherry picking, but we watched it
  unfold in live conditions."

**Example 2 — USDCHF short (09:05–10:09):**
- Daily: price traded up into a **rejection block** on Thursday.
- Friday: opened, **rallied above the Asian range high**, with the 10-period Williams %R showing
  sentiment at its **most bullish** as price reached the bearish order block.
- Delivery: two subsequent highs of the day formed there, then price traded down to fill the
  daily **fair value gap** — the discount array — before Friday's close.
- Intermarket note: the move was in concert with the dollar index filling a gap that week.

## Common Mistakes

- **Waiting for sentiment to agree with the trade.** The whole concept is that it will not; the
  extreme reading *is* the condition.
- **Using Williams %R as an overbought/oversold trigger here.** ICT explicitly disclaims that
  use on this page's settings — it is confluence layered on a price-based setup.
- **Carrying the 15-period daily setting over from
  [explosive-market-selection](explosive-market-selection.md).** Different period, timeframe and
  purpose.
- **Entering a slow reaction.** If price lingers at the 15-minute array, the odds "drop off
  precipitously" — the array is failing in real time.
- **Taking the trade without the HTF array already respected.** The daily/H4 array must have
  produced a reaction *before* the day in question.
- **Ignoring the range check.** Under ~40 pips to the opposing array is a scalp; sizing and
  expectations differ.
- **Trading it daily.** The conditions are deliberately infrequent, and ICT names "pip drunk"
  overtrading as the failure mode.

## Related Concepts

- [asian-range](../14-asian-range/asian-range.md), [asian-range-high](../14-asian-range/asian-range-high.md), [asian-range-low](../14-asian-range/asian-range-low.md) — the bounds the entry is measured from.
- [judas-swing](../13-judas-swing/judas-swing.md), [market-protraction](../13-judas-swing/market-protraction.md) — the move that creates the adverse sentiment.
- [ict-day-trading-model](ict-day-trading-model.md) — the April-2017 model this month builds on.
- [explosive-market-selection](explosive-market-selection.md) — the other Williams %R usage; note the different settings.
- [discount-array](../05-pd-arrays/discount-array.md), [premium-array](../05-pd-arrays/premium-array.md) — the arrays on both ends of the trade.
- [true-day-open](../22-quarterly-theory/true-day-open.md) — the 0 GMT alternative reference.

## Citations

- `ICT-2017-SENTIMENT-EFFECT` (00:10–00:22) "this is the first lesson of **May 2017** content from the ICT mentorship; this month we're teaching the ICT amplified day trading and scalping… specifically dealing with the sentiment effect"; (00:24–01:03) where buying and selling probabilities are highest — sell above the opening price and/or Asian range high on bearish days, buy below them on bullish days; (01:03–01:22) "the market will have a short-term shift in sentiment and less informed traders will chase price on the impulse or the initial swing intraday — this is classically known… as the Judas swing"; (01:22–01:44) strict conditions from daily/H4 institutional order flow plus the PD array matrix; (02:05–02:20) "smart money sells above the Asian range high… smart money buys below the Asian range low and below that opening price"; (02:20–02:48) the opening price — 0 GMT if the early range is a consolidation, otherwise the midnight New York candle; (02:48–03:17) moves beyond the Asian range "suck in street money" on the wrong side; (03:17–03:53) buy condition 1 — a daily and/or minimum four-hour discount array must be in play and already respected; (03:53–04:59) buy condition 2 — sufficient range to the opposing premium array, "50 to 60 pips… anything less than 40 pips and it's a scalp"; (04:59–05:18) buy condition 3 — decline under the opening price and Asian range low into a logical 15-minute discount array; (05:18–05:46) buy condition 4 — "expect price to sharply trade higher away from the 15 minute discount array; the longer price stays or hovers near that 15 minute discount array the odds drop off precipitously… the banks won't keep that price level at a discount very long"; (05:46–05:53) "short-term sentiment will be most bearish at the time when we enter our long trades"; (05:53–06:33) "for sentiment purposes I use a 10 period Williams percent R and I plot that on my 15 minute time frame… but we don't look at the overbought oversold conditions that this indicator usually is… referred to"; (06:33–07:57) the Thursday New York weekly-low example, including the sell-stop run before the 08:30 release; (07:58–09:05) the mirrored sell conditions; (09:05–10:09) the USDCHF example — Thursday rejection block, Friday rally above the Asian range high with sentiment most bullish, then the daily fair-value-gap fill; (10:09–10:38) "day trading is not an everyday trading"; (10:47–12:44) the "20 pips per day" caveat and the "pip drunk" overtrading failure mode.

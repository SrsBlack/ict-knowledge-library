# Interest Rate Differentials

**Category:** 03-order-flow
**Aliases:** rate differentials, central bank rates, yield differential, carry
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-RATE-DIFFERENTIALS, ICT-2017-HIGH-REWARD-SETUPS
**Tags:** order-flow, fundamentals, macro, htf-bias, fx, central-banks

## Definition

The gap between two countries' **central bank policy rates**, used as the fundamental
input to a higher-time-frame directional bias in FX. ICT places it at the start of the
macro read: "central bank interest rates — if we're going to be looking at a macro
view, it really needs to **start here**" (`ICT-2017-RATE-DIFFERENTIALS`, 00:21).

The mechanism is capital flow. Money moves toward yield, so the currency of a country
with a high or strengthening policy rate is favoured for buying, and a weak or
weakening rate signals expected currency weakness (02:26–02:43). Because a pair is
always two countries, there is "always going to be a higher interest rate among another
currency versus another country" (01:16) — the differential, not either rate alone, is
the read.

## Formal Criteria

- Source: the **central bank policy-rate table** (ICT uses fxstreet.com's list, 00:41).
- Rank the currencies **high to low** by policy rate; the read is the *spread* between
  the two sides of a pair, not an absolute level.
- **Buy side:** favour the currency with the higher / strengthening rate — capital flows
  to yield.
- **Sell side:** "if you're expecting weakness in a particular country or a country's
  economy, you can see that in the form of a weak interest rate" (02:43).
- A large differential can produce a **carrying-charge market** in FX terms, giving "a
  very easy way of finding trades directional" (`ICT-2017-HIGH-REWARD-SETUPS`, 25:26).
- **Unexpected policy moves matter:** an unanticipated hike or cut is itself the event
  (`ICT-2017-HIGH-REWARD-SETUPS`, 25:00).
- Output is a **long-term macro bias** — ICT builds "a model on a higher time frame
  basis on long term macro trades" from it (03:18). It supplies no entry.

## Formula / Math

```
differential(A, B) := policy_rate(A) - policy_rate(B)

# For a pair quoted A/B:
differential > 0 and widening  -> bias favours A (capital flows to yield)
differential < 0 and widening  -> bias favours B

# The pair's own rank position matters, not the raw number:
rank_table := sort(currencies, by=policy_rate, desc=True)

# 2017 example (ICT-2017-RATE-DIFFERENTIALS, 01:32):
#   highest on the list = Reserve Bank of New Zealand
#   low end = Swiss National Bank, Bank of Japan, ECB
#   -> NZD is the yield-favoured side against CHF / JPY / EUR
```

No threshold is taught for how wide a differential must be. The read is comparative
and discretionary.

## Machine-Readable

```json
{
  "id": "interest-rate-differentials",
  "category": "03-order-flow",
  "aliases": ["rate-differentials", "central-bank-rates"],
  "criteria": [
    {"id": "c1", "expr": "input == central_bank_policy_rate_table"},
    {"id": "c2", "expr": "read == spread_between_pair_sides (not absolute level)"},
    {"id": "c3", "expr": "higher_or_rising_rate => currency_favoured_for_buying"},
    {"id": "c4", "expr": "weak_rate => expected_currency_weakness"},
    {"id": "c5", "expr": "output == htf_macro_bias"},
    {"id": "c6", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["dollar-index", "htf-bias-framework", "seasonal-tendency", "institutional-order-flow"],
  "sources": ["ICT-2017-RATE-DIFFERENTIALS", "ICT-2017-HIGH-REWARD-SETUPS"]
}
```

## Visual Pattern

```
   Central bank policy rates, ranked (2017 example):

     RBNZ        ████████████  highest  -> yield-favoured, buy side
     RBA         █████████
     BoE         █████
     BoC         ███
     ECB         ██
     BoJ         █
     SNB         ▏             lowest   -> funding side, sell side

   Bias for a pair = which side of the table each currency sits on,
   and whether that gap is widening or narrowing.
```

## Timeframes

Daily and above. Policy rates change on a scale of months; the resulting bias is a
long-term macro overlay, not an intraday input.

## Examples

**Example 1 — 2017 rate table (`ICT-2017-RATE-DIFFERENTIALS`, 01:32–02:58):**
- Highest policy rate on the list: Reserve Bank of New Zealand; next, the Reserve Bank
  of Australia.
- Low end: Swiss National Bank, Bank of Japan, European Central Bank, Bank of Canada.
- Capital is favoured toward the high-rate side, giving a long-term macro bias for
  NZD-strength pairs against the low-rate funding currencies.

## Common Mistakes

- **Reading one rate in isolation.** A pair is two countries; the differential is the read.
- **Treating it as a trade signal.** It sets HTF bias only — no entry, stop or target.
- **Ignoring the direction of change.** A high rate that is being cut and a low rate
  being hiked both work against the static table.
- **Applying it intraday.** Policy rates move on a months-long cadence.
- **Confusing FX carry with the commodity term structure.** A carrying-charge *market*
  in commodities is a delivery-month curve — see
  [premium-vs-carrying-charge-market](premium-vs-carrying-charge-market.md). The shared
  word does not mean a shared mechanism.

## Related Concepts

- [dollar-index](dollar-index.md) — where the USD side of most differentials is read.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — where this input belongs in the stack.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the other macro overlay taught in the same mentorship year.
- [premium-vs-carrying-charge-market](premium-vs-carrying-charge-market.md) — the commodity concept sharing the "carrying charge" phrase.

## Citations

- `ICT-2017-RATE-DIFFERENTIALS` (00:00) — "Lesson 2.3 of the January 2017 ICT Mentorship… interest rate differentials"; (00:21) "central bank interest rates… if we're going to be looking at a macro view, it really needs to start here"; (00:41) the fxstreet.com policy-rate list; (01:16) "there's always going to be a higher interest rate among another currency versus another country"; (01:32) RBNZ highest, RBA second; (02:26–02:43) capital flows toward yield, and "if you're expecting weakness in a particular country or a country's economy, you can see that in the form of a weak interest rate"; (02:58) SNB, BoJ, ECB, BoC at the low end; (03:18) "we can build a model on a higher time frame basis on long term macro trades."
- `ICT-2017-HIGH-REWARD-SETUPS` (25:00–25:35) — unexpected hikes and cuts, and "we look at differentials between two interest rate markets… that creates what's called a carrying charge market where you can actually have a very easy way of finding trades directional."

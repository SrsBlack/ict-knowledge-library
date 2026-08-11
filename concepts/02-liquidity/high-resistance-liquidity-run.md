# High Resistance Liquidity Run

**Category:** 02-liquidity
**Aliases:** HRLR, high resistance liquidity run, defended liquidity, high resistance condition
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-LIQUIDITY-RUNS
**Tags:** liquidity, resistance, buy-stops, sell-stops, trade-filtering, current-trading-range

## Definition

A high resistance liquidity run is a move toward a pool of resting stops that must first
travel **through a thick body of intervening price action** — a stack of old highs and old
lows built up between current price and the target. ICT's claim is not that such a run is
impossible but that it is the **least probable** condition to trade: "we view this as a high
resistance liquidity run… this is the least probable trading condition to look for longs
because you have so many levels of resistance and old highs to encounter before you get back
to the old significant high" (`ICT-2016-LIQUIDITY-RUNS`, 07:33, 07:58–08:05).

The measurement is **structural, not fractional**. It counts what stands in the way. This is
the original 2016 form of the idea; the recursive quadrant-grading construction taught a year
later in the short-term-trading module is a different machine for the same vocabulary — see
[low-resistance-liquidity-run](low-resistance-liquidity-run.md).

The two conditions are duals of one another on the same chart: a high resistance run in one
direction *is* a low resistance run in the other. "because that's built into price action,
having a high resistance liquidity run here, it turns into a low resistance liquidity run for
you to see a move below the short term lows" (20:15–20:29).

## Formal Criteria

**Bullish target (buy stops above an old high) is high resistance when:**

- The market has been making **lower lows and lower highs** into current price (08:13).
- Between current price and the old high there is "a lot of peaks and troughs" (06:06) —
  "you have the old lows acting as standard resistance. Then you have the old highs acting as
  buy stop liquidity" (06:34–06:41).
- Reaching the target requires clearing **multiple intermediate stop levels first**: "it could
  go another level higher for these buy stops. And it could reach for this level of buy stops
  and then maybe this buy stop level here" (06:54–07:02).

**Bearish target (sell stops below an old low) is high resistance when the mirror holds** —
"as the market makes higher highs and higher lows… we can't reasonably expect the market to
just drop straight down and make a run on the sell stops below this low without encountering
first all of these higher lows and higher highs" (09:13–09:25).

**Time in the area strengthens the defence.** "the more time it's spent in this area, again,
the more unlikely it is to make a market move all the way down to this old low" (09:59–10:08).

**Only a volatility injection reliably breaks it.** "it's going to take a very sharp economic
market release, the data, kind of like non-farm payroll or FOMC. That type of event will knock
through all of these levels of resistance to run out that liquidity. But generally, without
that type of influence or injection of volatility, these old highs generally are well
defended" (08:31–08:52); repeated on the sell side with "a black swan event" added (10:20–10:36).

**The generalised read.** "the more price action there is around a specific level or a high or
a low, that is indicating a level is being defended on an institutional price model" (24:15).

**Exclusions.** Not a timeframe-specific classification — "this is not specific to any
timeframe, it's universal" (07:15).

## Formula / Math

```
Let T           = target liquidity pool (buy stops above an old high, or
                  sell stops below an old low)
Let P           = current market price
Let obstacles(P, T) = count of intervening swing highs and swing lows
                      formed between P and T

high_resistance(T) := obstacles(P, T) is LARGE
                      AND structure_between(P, T) is counter-directional
                      #   lower-lows/lower-highs for an upside target
                      #   higher-highs/higher-lows for a downside target

low_resistance(T)  := obstacles(P, T) ~ 0
                      #   the one-way expansion leg; see low-resistance-liquidity-run

# Duality on one chart
high_resistance(upside_target) => low_resistance(downside_target)
high_resistance(downside_target) => low_resistance(upside_target)

# The override
breakable(high_resistance_target) := volatility_event
                                     # NFP, FOMC, rate announcement, black swan

# Trading rule taught in this lecture
trade_direction := the side whose run is LOW resistance
avoid           := entries whose objective is a high resistance run
```

No numeric threshold on `obstacles` is given. ICT teaches it as a visual judgement, and the
lecture supplies no count, ratio or percentage anywhere.

## Machine-Readable

```json
{
  "id": "high-resistance-liquidity-run",
  "category": "02-liquidity",
  "aliases": ["HRLR", "high-resistance-liquidity-run", "defended-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "intervening swing highs and lows between current price and the target pool are numerous"},
    {"id": "c2", "expr": "structure between price and target is counter-directional (LL/LH for an upside target)"},
    {"id": "c3", "expr": "time spent building that structure increases the defence"},
    {"id": "c4", "expr": "reliably broken only by a volatility injection (NFP, FOMC, rate decision, black swan)"},
    {"id": "c5", "expr": "high_resistance(one side) implies low_resistance(the other side) on the same chart"},
    {"id": "c6", "expr": "classification is timeframe-agnostic"},
    {"id": "c7", "expr": "no numeric threshold is taught; the count of obstacles is judged visually"},
    {"id": "c8", "expr": "trade the low-resistance side; a high-resistance objective is the least probable condition"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["low-resistance-liquidity-run", "liquidity-run", "liquidity-pool", "draw-on-liquidity", "buy-side-liquidity", "sell-side-liquidity", "equal-highs", "equal-lows", "institutional-order-flow", "range-contraction"],
  "sources": ["ICT-2016-LIQUIDITY-RUNS"]
}
```

## Visual Pattern

```
  HIGH RESISTANCE — upside target                LOW RESISTANCE — downside target
  (the SAME chart, read both ways)

  old high  ─────────────  <- buy stops, the target
                 ╱╲
                ╱  ╲   ╱╲        every rally into this stack is a
          ╱╲   ╱    ╲ ╱  ╲       HIGH resistance run: the peaks and
         ╱  ╲ ╱      V    ╲      troughs must all be cleared first
        ╱    V              ╲
   ────╱                     ╲── P (current price)
                              ╲
        every short-term low below P is a LOW resistance
        run: "like a hot knife through butter" (17:31)

  The rule that falls out: the bias is bearish, so you fade every
  retracement UP (high resistance) and target the lows (low resistance).
```

## Timeframes

All. ICT states the classification is universal — "this is not specific to any timeframe"
(07:15) — and works the same diagrams for buy-side and sell-side objectives without naming a
chart interval anywhere in the lecture.

## Examples

**Example 1 — bearish chart, upside runs defended (`ICT-2016-LIQUIDITY-RUNS`, 17:15–19:20):**
- Setup: an old high to the left, price sells off through old lows.
- Trigger: the market rallies, clears one stop above a high, retraces, and shows "an
  unwillingness to go above this up candle here… institutional order flow moves back to
  bearish and expands to the downside" (17:59–18:18).
- Outcome: "This run higher is a high resistance liquidity run… we've already priced in on a
  longer term high, intermediate term high. And this high is going to have a very hard time
  struggling to get through this high" (18:31–18:48). The same structure makes the move down to
  the lows a low resistance run (19:09–19:20).

**Example 2 — bullish chart, downside runs defended (`ICT-2016-LIQUIDITY-RUNS`, 21:20–22:22):**
- Setup: a long-term low is formed, price rallies, retraces, consolidates, rallies again, so
  "we have a lot of price action here, so this old low is going to be well defended" (21:37).
- Trigger: each retracement lower.
- Outcome: "every time the market retraces, that's going to be in the form of a high resistance
  liquidity run… The old lows are going to be actually defended and you're going to see buying
  coming in the marketplace. Your focus is going to be primarily on the highs" (21:44–22:09).

## Common Mistakes

- **Reading it as "resistance" in the classical sense.** The word describes friction on the
  path to a stop pool, not a ceiling price is expected to bounce off. In this lecture old
  *lows* also "act as standard resistance" (06:34) for an upward run.
- **Treating a high resistance run as untradeable.** ICT says it is the *least probable*
  condition and that there are later teachings for it — "there are opportunities that we'll
  learn with trading with this profile" (10:42) — not that it never resolves.
- **Forgetting the duality.** Labelling one side high resistance and then ignoring that the
  opposite side is now the easy trade discards the whole point of the classification.
- **Importing the 2017 quadrant grading.** The 60-day body-anchored range and its eighths are a
  2017 construction. Nothing in this 2016 lecture measures a range, a fraction, or a percentage.
- **Importing later vocabulary.** The word "array" does not occur anywhere in this lecture, nor
  in any of the Sep–Dec 2016 packets. ICT's 2016 terms here are "old high", "old low",
  "short-term high", "buy stop liquidity", "sell stop liquidity".

## Related Concepts

- [low-resistance-liquidity-run](low-resistance-liquidity-run.md) — the dual condition, taught in the same lecture and re-derived in 2017 on a quadrant grid.
- [liquidity-run](liquidity-run.md) — the generic approach/take/resolution sequence being classified.
- [liquidity-pool](liquidity-pool.md), [buy-side-liquidity](buy-side-liquidity.md), [sell-side-liquidity](sell-side-liquidity.md) — what the run is aimed at.
- [draw-on-liquidity](draw-on-liquidity.md) — target selection once the resistance grade is known.
- [equal-highs](equal-highs.md), [equal-lows](equal-lows.md) — the clean levels that make a run *low* resistance.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the bias the classification is meant to synchronise you with (24:40).
- [range-contraction](../01-market-structure/range-contraction.md) — the accumulated price action that builds the defence.

## Citations

- `ICT-2016-LIQUIDITY-RUNS` (00:29) liquidity defined as the degree to which an asset can be bought or sold without moving price dramatically; (01:06) "Liquidity, as it relates to ICT concepts, it relates to buy orders and sell orders. It's as simple as that"; (03:55–04:17) "our first fundamental understanding is that there is going to be liquidity above old highs and below old lows"; (05:43–05:48) "The market has a tendency to run out old highs and old lows. But it has a very difficult time to do that when the market has conditions like this"; (06:00–06:08) "there is a lot of peaks and troughs here"; (06:34–06:47) old lows as standard resistance and old highs as buy stop liquidity; (06:54–07:02) the intermediate stop levels that must be cleared first; (07:15–07:38) "this is not specific to any timeframe, it's universal… we view this as a high resistance liquidity run"; (07:47–08:13) "When we trade, we are not looking for these opportunities… this is the least probable trading condition to look for longs"; (08:22–08:31) "Those individuals with stops above this old high in the form of a fund, they're actually very highly defended because of this type of price action"; (08:31–08:52) NFP / FOMC as the volatility injection that breaks a defended high; (09:04–09:54) the sell-side mirror, high resistance liquidity runs on an old low; (09:59–10:08) time spent in the area reduces the probability further; (10:08–10:36) the black-swan case; (10:37–10:58) "for shorts, we avoid these types of occurrences… this is the element of price action that we want to trade very less frequent in"; (12:50) low resistance named for the range created by a broken low; (17:15–19:20) the worked bearish example and the high-resistance rally; (20:02–20:29) the duality — a high resistance rally makes the move below short-term lows low resistance; (21:20–22:22) the worked bullish mirror, defended old lows and easy runs on the highs; (24:15–24:45) "the more price action there is around a specific level or a high or a low, that is indicating a level is being defended on an institutional price model… by doing that, you're going to be getting yourself in sync with the institutional order flow".

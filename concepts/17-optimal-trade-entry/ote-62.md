# OTE 0.62

**Category:** 17-optimal-trade-entry
**Aliases:** shallow OTE, OTE 62 entry
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2017-OTE-ANTICIPATING, ICT-2020-OTE-VOL14, ICT-2020-OTE-VOL16, ICT-2020-OTE-VOL18, ICT-2021-OTE-PRICE-ACTION-LESSON, ICT-2021-OTE-SCALPING-EXERCISE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, shallow-entry

## Definition

The OTE 0.62 entry is the **shallowest acceptable OTE entry** — the upper bound of the OTE zone. Used when price retraces only to 0.62 and finds PD-array confluence there without going deeper. It carries the **widest stop distance** of the three depths, because the taught stop sits at the leg origin regardless of entry depth. ICT: "at or very close to the 62%… I'm not going to demand 79%" (`ICT-2017-OTE`).

⚠ **Re-weighted 2026-08-11.** This page previously framed 0.62 as "the least attractive of the three" on R:R grounds. In the applied material it is the opposite: **0.62 is the default and, in the taught study protocol, the only permitted entry**, and ICT gives a mechanical reason that has nothing to do with R:R.

- **The prescription.** "Now the details are, we **always look for the 62 % retracement level** … Again, we're always using a 62 % retracement level" (`ICT-2020-OTE-VOL14`, 05:28–05:50). Restated as the entry across the series: `ICT-2020-OTE-VOL16` [11:01], `ICT-2020-OTE-VOL18` [02:12]. The 2021 backtest exercise makes it exclusive: "we're going to use 62 retracement, that's going to be your entry — **don't try to do the 70.5, don't look for the 79, use 62**" (`ICT-2021-OTE-SCALPING-EXERCISE`, 13:26–13:40).
- **The reason.** "You can finesse your entry and try to use the 70.5 level or the 79 % retracement level. But … **you're likely to miss the trade and/or the dealer spread may not be covered for your entry to fill**" (`ICT-2020-OTE-VOL14`, 05:50–06:08). The deeper levels are rejected on **fill probability and spread**, not on setup quality — "we're using the low-hanging-fruit approach … where it's really, really easy to get the 62 % retracement level and not always the 79. Everybody wants to sell at the highest level so that way their stop loss could be smaller, but **you don't need to do that**" [06:08–06:24].
- **The fill risk is symmetric, and ICT names it against himself.** Having declined to leave a resting order: "I could have had my orders at 62 % retracement level or just below it to get filled. **But it could have just simply rolled right over and went lower and I would never have gotten filled**" (`ICT-2017-OTE-ANTICIPATING`, 20:01–20:12). A limit at 0.62 can miss in *both* directions — too shallow to fill on a deep retracement, and unfilled entirely if price never returns.
- **62 as a floor, not a point.** In the 2021 lesson the 62 is "your **minimum** level to reach for for shorting" (`ICT-2021-OTE-PRICE-ACTION-LESSON`, 04:15), with an observed overshoot of three pipettes treated as a fill, not a failure [05:09–05:24].

This does not displace 0.705 as the geometric mid-point ([ote-705](ote-705.md)); it means the **executable** default sits at 0.62 whenever fill risk matters.

## Formal Criteria

- Retracement reaches 0.62 of measured leg.
- PD array (FVG / OB / breaker) present at or near 0.62.
- HTF bias agreement.
- **SL at the leg-origin extreme (fib 1.0)** — ⚠ *corrected 2026-08-05; this file previously said "beyond 0.79", which is the deepest entry, not the taught stop. See [ote-overview](ote-overview.md).*

## Formula / Math

```
OTE_62_entry = leg_end - 0.62 * leg_size
SL           = leg_start                      # fib 1.0, exactly

# Bullish leg 1.0800 → 1.0900:
OTE_62_entry = 1.08380
SL           = 1.0800
Risk         = 1.0838 - 1.0800 = 38 pips
# first target 1.0900 (fib 0.0) = 62 pips ≈ 1.6R on the Primer's leg-origin stop —
# below the Primer's 2:1 floor. The 2020 series answers this by pairing the 62 entry
# with a FIXED stop instead of the leg-origin one, which restores the ratio:
#   ICT-2020-OTE-VOL14: 62% entry 1.22681, 20-pip stop, 7 pips drawdown, ~3:1 realised
#   ICT-2021-OTE-SCALPING-EXERCISE: 62% entry, stop = old_high + 5 pips
# Entry depth and stop rule are chosen together; do not mix the shallow entry with
# the widest stop and then conclude the level is weak.
```

## Machine-Readable

```json
{
  "id": "ote-62",
  "category": "17-optimal-trade-entry",
  "aliases": ["shallow-OTE-entry"],
  "criteria": [
    {"id": "c1", "expr": "entry == leg_end - 0.62 * leg_size"},
    {"id": "c2", "expr": "PD_array_at_or_near_062 == true"},
    {"id": "c3", "expr": "SL == leg_start (fib 1.0) OR fixed_pip", "strength": "era-fork; see ote-rules item 6"},
    {"id": "c4", "expr": "062 is the default executable depth", "strength": "2020 series; exclusive in the 2021 exercise"},
    {"id": "c5", "expr": "reason_deeper_levels_declined == fill_probability AND dealer_spread"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-705","ote-79","ote-rules","fib-62"],
  "sources": ["ICT-2017-OTE","ICT-2017-OTE-ANTICIPATING","ICT-2020-OTE-VOL14","ICT-2020-OTE-VOL16","ICT-2020-OTE-VOL18","ICT-2021-OTE-PRICE-ACTION-LESSON","ICT-2021-OTE-SCALPING-EXERCISE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   leg_end ──────── 0.0
   ─────────────── 0.50 EQ
   ─────────────── 0.62  ← entry (shallowest OTE)
   ─────────────── 0.705
   ─────────────── 0.79  ← deepest ENTRY, declined here on fill/spread grounds
   leg_start ──── 1.0    ← SL (Primer branch); the 2020 branch uses a fixed stop
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 0.62 entry (Primer stop branch):**
- Leg 1.0800 → 1.0900.
- 0.62 = 1.0838; bullish FVG at 1.0836–1.0840.
- Long at 1.0838, **SL 1.0800 — the leg origin, fib 1.0.** Risk = 38 pips.
- First target 1.0900 (fib 0.0) ≈ 1.6R; the SD ladder extends beyond it.
- ⚠ *Corrected 2026-08-11: this example previously placed the stop at 1.0815, "below 0.79 + buffer", which is the very placement the 2026-08-05 correction removed from the Formal Criteria above. The page had been half-corrected.*

**Example 2 — 0.62 entry with a fixed stop (`ICT-2020-OTE-VOL14`, cable, 5-minute):**
- New York session leg; 62 % retracement gives a hypothetical entry of **1.22681**.
- **20-pip stop**, which "would take us above this high, no real jeopardy in terms of being stopped out"; realised drawdown **7 pips**.
- Scales: ~20 pips at the old low, ~40 at the half-standard-deviation, ~60 running the previous day's low → "three to one reward to risk."

## Common Mistakes

- **Skipping 0.62 because "0.705 is better."** If 0.62 has clean PD-array confluence and 0.705 may not be reached, take the 0.62 entry. In the applied material this is the *default*, not the fallback.
- **Chasing the deeper fill.** "Everybody wants to sell at the highest level so that way their stop loss could be smaller, but you don't need to do that" — the cost is missed trades and unfilled limits inside the spread (`ICT-2020-OTE-VOL14`, 06:08).
- **Unrealistic R:R expectations.** 0.62 entries have the widest stop *if* the leg-origin stop is used; calibrate position size, or use the stop rule the same source pairs with the entry.
- **Voiding the entry on a small overshoot.** "It only went three pipettes above the 62 % retracement level" is treated as the fill (`ICT-2021-OTE-PRICE-ACTION-LESSON`, 05:17).

## Related Concepts

- [ote-overview](ote-overview.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [fib-62](../28-fibonacci-levels/fib-62.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.

Added 2026-08-11:

- `ICT-2020-OTE-VOL14` (05:28–06:24) — "we **always look for the 62 % retracement level** … you can finesse your entry and try to use the 70.5 level or the 79 % retracement level, but … you're likely to miss the trade and/or **the dealer spread may not be covered for your entry to fill** … we're using the low-hanging-fruit approach."
- `ICT-2021-OTE-SCALPING-EXERCISE` (13:26–13:40) — "we're going to use 62 retracement, that's going to be your entry — **don't try to do the 70.5, don't look for the 79, use 62**."
- `ICT-2021-OTE-PRICE-ACTION-LESSON` (04:15) — "that's your 62 % retracement level, that's your **minimum** level to reach for for shorting"; (05:17) a three-pipette overshoot treated as the fill.
- `ICT-2020-OTE-VOL16` (11:01) and `ICT-2020-OTE-VOL18` (02:12) — 62 % as the stated entry on crude oil and Treasury bonds respectively.
- `ICT-2017-OTE-ANTICIPATING` (19:55–20:12) — "optimal trade entry was the idea … I could have had my orders at 62 % retracement level or just below it to get filled, but it could have just simply rolled right over and went lower and I would never have gotten filled." ⚠ **This packet's transcript is ~36 % Whisper hallucination** (spurious Sinhala/Chinese text over most of the runtime); only isolated English passages are readable, and this is one of them. Nothing else on the page rests on it.

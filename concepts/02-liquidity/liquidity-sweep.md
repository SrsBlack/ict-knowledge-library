# Liquidity Sweep

**Category:** 02-liquidity
**Aliases:** sweep, raid, liquidity raid, stop run, wick-sweep, liquidity grab (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-LIQUIDITY-POOLS, ICT-2016-MMT-FALSE-BREAKOUT, ICT-2017-PD-ARRAY-MATRIX, ICT-2022-MENTORSHIP-EP23, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP03
**Tags:** liquidity, sweep, raid, foundational

## Definition

A liquidity sweep is the act of price trading through a [liquidity-pool](liquidity-pool.md) — taking out the resting orders — and then **failing to follow through**, reversing back into the range or into expansion. ICT: "sweeping is where it just goes above or below a low or high… if we're going to sweep by [buy] side that means it's going to go up a little bit and then go down and reverse" (`ICT-2022-MENTORSHIP-EP23`, 05:16–05:39) — the auto-caption's "by side" is ASR for "buy side"; "what I'm expecting as a sweep and reverse back into the range or expansion" (EP23, 05:39). The 2016 mentorship teaches the same event as a **stop run**: "a low is swept out, that's when you anticipate a turtle soup" (`ICT-2016-EQUILIBRIUM-DISCOUNT`, 40:20). A sweep is ICT's alternative to a [liquidity-run](liquidity-run.md), not a subset of it — see that page for the vocabulary split.

## Formal Criteria

For a bullish-side (BSL) sweep:

- Price trades above a known BSL pool (swing high, EQH, trendline).
- The move fails to sustain — "it just doesn't look back" is ICT's description of the opposite case, a *run* (EP23, 05:16).
- ICT gives no close-based or wick-percentage test for where a sweep ends and a run begins (see Common Mistakes); his own distinction is depth and follow-through.
- Optional confirmation: a [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) forms in the opposite direction shortly after — "the market goes up, sweeps the highs, breaks back down below the highs, short-term lows taken out" (`ICT-2022-MENTORSHIP-EP24`, 32:07); "you'll be looking for stop hunts that lead to market structure shifts" (`ICT-2022-MENTORSHIP-EP03`, 35:33).

For a sell-side (SSL) sweep: symmetric.

## Formula / Math

ICT gives no close-based or wick-ratio formula for a sweep. The one quantitative rule in the corpus is **depth of penetration**, not candle geometry — and it is explicitly scoped by ICT to a lower-timeframe FX chart, not stated for every timeframe or instrument:

```
# Scope, verbatim: "on a lower timeframe chart like a 15 or 30 minute chart"
# (FX pips, intraday) — ICT-2016-LIQUIDITY-POOLS, 10:28-10:46.
# ICT gives no depth figure for H4/D/W or for non-FX instruments.

typical_sweep_depth := 10 to 20 pips beyond the swept level, on a 15-30 min FX chart
                        ("You can expect a 10 to 20 pip sweep below the old low",
                        ICT-2016-LIQUIDITY-POOLS, 10:46)

beyond_25_pips       := "if it starts moving beyond 25 pips, I think is a fair
                        assessment... it's probably not just a stop run" — ICT's
                        own hedge ("I think is a fair assessment"), not a firm rule
                        (ICT-2016-LIQUIDITY-POOLS, 11:30-11:39)
```

The library's prior "(high_n − close_n) > 0.6 × range_n" wick-percentage test and the "closes back below the level" close test are **not in the corpus** (0 hits for "close back"/"closes back"/"closed back" describing a sweep candle, across 153 2016-17/2020-21 packets and 41 2022 episodes). Do not treat either as ICT's rule — they are the library's own operationalisation of a behavioural distinction ICT states only in words ("doesn't look back" vs "sweep and reverse").

## Machine-Readable

```json
{
  "id": "liquidity-sweep",
  "category": "02-liquidity",
  "aliases": ["sweep", "raid", "liquidity-raid", "stop-run", "wick-sweep", "liquidity-grab"],
  "criteria": [
    {"id": "c1", "expr": "high_or_low_breaches_pool == true"},
    {"id": "c2", "expr": "move_fails_to_sustain_beyond_pool == true (ICT gives no close/wick-ratio formula for this)"},
    {"id": "c3", "expr": "on a 15-30 min FX chart only (ICT's stated scope): typical_depth_beyond_pool 10-20 pips; beyond ~25 pips ICT says (hedged, 'a fair assessment') it is probably not a sweep. No figure given for other timeframes/instruments."}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["liquidity-pool","liquidity-run","buy-side-liquidity","sell-side-liquidity","stop-run-definition","turtle-soup","judas-swing"],
  "sources": ["ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-LIQUIDITY-POOLS","ICT-2016-MMT-FALSE-BREAKOUT","ICT-2017-PD-ARRAY-MATRIX","ICT-2022-MENTORSHIP-EP23","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP03"]
}
```

## Visual Pattern

```
   bullish-side (BSL) sweep                sell-side (SSL) sweep

                █  ← wick beyond BSL          ▲   ← reverses back into range
   ─────────────█────  BSL                    █
                █                             █
                ─ reverses back              ─█──── SSL
                                              █  ← wick beyond SSL
                                              █
```

ICT marks the pool at candle **bodies**, not wicks, in the 2016-17 mentorship: "we're going to look for a sweep below the bodies of those candles" (`ICT-2016-LIQUIDITY-POOLS`, 13:08); "$109.40 is swept, moving just above the bodies of the candles" (`ICT-2016-MMT-FALSE-BREAKOUT`, 09:50); "any candle that has wicks above it, we would be noting the bodies of the candle because there would be liquidity resting just above the bodies" (`ICT-2017-PD-ARRAY-MATRIX`, 03:15). Treat the wick-vs-body choice as context-dependent, not a fixed rule.

## Timeframes

Every TF. HTF sweeps (D, H4) are major reversal triggers; LTF sweeps are entry signals inside HTF setups.

## Examples

**Example 1 — Asian range BSL sweep:**
- Asian session high 1.0875 (BSL).
- London opens; M15 wicks to 1.0888 (13 pips beyond — within ICT's stated 10-20 pip range for a 15-30 min FX chart), reverses.
- → BSL sweep. Often the start of a Judas-swing-down setup.

## Common Mistakes

- **Inventing a close-based or wick-percentage rule.** Neither appears in the corpus. ICT's distinction between a sweep (reverses) and a run (doesn't look back) is behavioural and depth-based, not a stated candle formula — see `liquidity-run` for the full vocabulary split.
- **Assuming the level is always the wick.** In the 2016-17 mentorship ICT repeatedly places the pool at candle bodies, not wicks.
- **Insisting on perfect reversal.** Some sweeps are followed by reversal; a deep penetration (ICT's own marker: beyond ~25 pips) signals continuation instead, not a sweep.

## Related Concepts

- [liquidity-pool](liquidity-pool.md) — what gets swept.
- [liquidity-run](liquidity-run.md) — ICT's alternative resolution, not a superset; see that page for the corrected vocabulary.
- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — types of pool.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — same phenomenon in different naming.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — false-breakout pattern built on sweeps.
- [judas-swing](../13-judas-swing/judas-swing.md) — session-specific sweep pattern.

## Citations

- `ICT-2016-EQUILIBRIUM-DISCOUNT` (40:20) "a low is swept out, that's when you anticipate a turtle soup."
- `ICT-2016-LIQUIDITY-POOLS` (10:28–10:46) "on a lower timeframe chart like a 15 or 30 minute chart… you can expect a 10 to 20 pip sweep below the old low"; (11:30–11:39) "if it starts moving beyond 25 pips, I think is a fair assessment… it's probably not just a stop run"; (13:08) "we're going to look for a sweep below the bodies of those candles."
- `ICT-2016-MMT-FALSE-BREAKOUT` (09:50) "$109.40 is swept, moving just above the bodies of the candles."
- `ICT-2017-PD-ARRAY-MATRIX` (03:15) "any candle that has wicks above it, we would be noting the bodies of the candle because there would be liquidity resting just above the bodies."
- `ICT-2022-MENTORSHIP-EP23` (05:16–05:39) "running Tuesday's high means it runs right over top of it and it just doesn't look back; sweeping is where it just goes above or below a low or high… go up a little bit and then go down and reverse"; "what I'm expecting as a sweep and reverse back into the range or expansion."
- `ICT-2022-MENTORSHIP-EP24` (32:07) "the market goes up, sweeps the highs, breaks back down below the highs, short-term lows taken out."
- `ICT-2022-MENTORSHIP-EP03` (35:33) "you'll be looking for stop hunts that lead to market structure shifts."

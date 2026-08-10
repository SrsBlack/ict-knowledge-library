# Turtle Soup

**Category:** 20-turtle-soup
**Aliases:** TS, false breakout, failed breakout, breakout-fade, fakeout (SMC), swing failure (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-TIMEFRAME-SELECTION, ICT-2017-STT-MM-TEMPLATES, ICT-2017-INTRADAY-TOP-DOWN
**Tags:** turtle-soup, false-breakout, foundational

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018`
sourced only to the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and
`ICT-2022-MENTORSHIP-OVERVIEW`, neither of which is a lecture. The **Month 1**
(September 2016) lecture *Equilibrium Vs. Discount* defines the pattern outright —
"So that should be a turtle soup. **Turtle soup is a false breakout pattern.** It went
below that low. We should see a responsiveness that's aggressive that moves higher"
(`ICT-2016-EQUILIBRIUM-DISCOUNT`, 32:28–32:33) — and by **Month 03** (November 2016) it is
one of the three setups ICT says he trades: "there's stop runs, which we classically call
the turtle soup, which is a false breakout" (`ICT-2016-TIMEFRAME-SELECTION`, 40:00).
Re-dated to **2016**. The provenance sentence below was also corrected: ICT credits *Street
Smarts* by Linda Raschke **and** Larry Connors, not Connors alone. ⚠ `Year Refined: 2022`
is retained but remains **uncited** — the local corpus contains no 2022-authored material.

## Definition

A **Turtle Soup** is a **failed breakout** pattern — price briefly trades through a known liquidity level (a swing high/low or session extreme), traps breakout traders, and immediately reverses back inside. Named after the original "Turtle Trader" breakout strategy that this pattern explicitly defeats. The Turtle Soup is the price-action mirror of a [liquidity-sweep](../02-liquidity/liquidity-sweep.md): the sweep is the event, the Turtle Soup is the named pattern. ICT credits the pattern to *Street Smarts* by Linda Raschke and Larry Connors — "when you look at, uh, *Street Smarts* book, where I got the inspiration for this pattern" (`ICT-2017-INTRADAY-TOP-DOWN`, 30:19) — and says the book states it too thinly ("it just gives you, here's a low, goes down below the low, buy it there; that's a little myopic in my opinion", 30:23), so the ICT version adds the requirement that the sweep land in a higher-timeframe discount/premium array.

## Formal Criteria

A bullish Turtle Soup (failed bearish breakout):

- Price has been respecting a known SSL (swing low, EQL, session low).
- Price wicks below the SSL.
- The same candle (or within 1–3 bars) closes back above the SSL.
- Subsequent displacement upward confirms the failed breakout.

For bearish: symmetric (failed bullish breakout).

**Weekly-scale variant (`ICT-2017-STT-MM-TEMPLATES`).** In the March-2017 short-term module the turtle soup is the named entry for one specific weekly profile — *consolidation Thursday reversal*. The level swept is the **intraweek** low or high built Monday–Wednesday, and the sweep is news-driven: "when that happens, generally it's going to be like an FOMC or an employment release. The FOMC release generally happens around the 2 o'clock hour in Eastern Standard Time" (23:31–23:40). "This false break becomes a **turtle soup long** and you're looking for the market to trade up into where the weekly buy stops are" (23:55); the bearish mirror is stated at 26:02. Two constraints ICT attaches only to this variant:

- **Entry is a resting limit below the Monday/Tuesday low** placed after the first move: "wait for the initial knee jerk reaction, put your limit order down below the low that's formed on Monday and Tuesday" (24:47).
- **Size is capped, not normal.** "Don't put a lot of money on this type of trade because if it's FOMC, you can get really crushed if it's a lot of whipsaw on it" (24:33).

## Formula / Math

```
bullish_turtle_soup := low(n) < known_SSL_level
                       AND close(n+k) > known_SSL_level   for k in [0, 3]
                       AND post-event displacement is up

bearish_turtle_soup := high(n) > known_BSL_level
                       AND close(n+k) < known_BSL_level   for k in [0, 3]
                       AND post-event displacement is down
```

## Machine-Readable

```json
{
  "id": "turtle-soup",
  "category": "20-turtle-soup",
  "aliases": ["TS", "false-breakout", "failed-breakout", "breakout-fade", "fakeout", "swing-failure"],
  "criteria": [
    {"id": "c1", "expr": "wick_through_known_level == true"},
    {"id": "c2", "expr": "close_back_inside_within_few_bars == true"},
    {"id": "c3", "expr": "post-event displacement opposite to break direction"},
    {"id": "c4", "expr": "weekly variant: level swept == intraweek Mon..Wed extreme, sweep driven by FOMC (~14:00 NY) or employment release"},
    {"id": "c5", "expr": "weekly variant: entry == resting limit beyond the Mon/Tue extreme, placed after the initial knee-jerk"},
    {"id": "c6", "expr": "weekly variant: position size explicitly reduced below normal"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-turtle-soup","bearish-turtle-soup","stop-hunt-pattern","liquidity-sweep","liquidity-run","stop-run-definition","rejection-block","weekly-range-profiles","market-maker-manipulation-template"],
  "sources": ["ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-TIMEFRAME-SELECTION","ICT-2017-STT-MM-TEMPLATES","ICT-2017-INTRADAY-TOP-DOWN"]
}
```

## Visual Pattern

```
   bullish Turtle Soup:                 bearish Turtle Soup:

   resistance level                     ▲   ← wick above resistance
   ─────────                            █   ← close back inside
        │                            ───────
        │  (price respecting)
   support level                        support level
   ─────────                            ─────────
   ──╲   ←  wick below                          (price respecting)
     ╲╱   ← close back above            ▼  resistance level
        ──→ rally up                    ─────────
                                        ──╲  wick above
                                          ╲╱  close back inside
                                              ──→ sell-off
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — bullish Turtle Soup at PWL:**
- PWL at 1.0850 (known SSL).
- M15 wicks 1.0846 (4 pips below PWL), closes 1.0855.
- Next M15 candle: 18-pip green displacement, FVG forms.
- → bullish Turtle Soup. Long entry on FVG retest at CE.

## Common Mistakes

- **Calling every wick a Turtle Soup.** The level must be **known** liquidity (swing high/low, EQH/EQL, session extreme); random wicks don't qualify.
- **No bias filter.** Counter-bias Turtle Soup setups fail more often than bias-aligned ones.
- **No answer to "why does the sweep stop here?"** ICT's own validity condition is the [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md), not the candle pattern: "everyone used to ask, how do you know it's going to stop when it goes above that old high? **Because you have to know the PD array matrix for that time frame you're looking at.** Where are the PD arrays? What's the higher time frame?" (`ICT-2017-INTRADAY-TOP-DOWN`, 43:41–43:53). A Turtle Soup identified without a named higher-timeframe array for the sweep to terminate into is unfalsifiable — ICT is explicit that "without understanding the PD array matrix… you will never be consistent with my concepts" (46:53).
- **Holding through the close-back-inside.** A wick that doesn't close back inside within 3 bars is a continuation, not a Turtle Soup.

## Related Concepts

- [bullish-turtle-soup](bullish-turtle-soup.md), [bearish-turtle-soup](bearish-turtle-soup.md), [stop-hunt-pattern](stop-hunt-pattern.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [liquidity-run](../02-liquidity/liquidity-run.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md), [rejection-block](../19-rejection-blocks/rejection-block.md).
- [weekly-range-profiles](../25-htf-bias/weekly-range-profiles.md) — the *consolidation Thursday reversal* profile, whose entry is the weekly-scale turtle soup.
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the entry and sizing rules attached to that variant.

## Citations

- `ICT-2016-EQUILIBRIUM-DISCOUNT` (32:28–32:33) "So that should be a turtle soup. Turtle soup is a false breakout pattern"; (40:18–40:23) "if you ever see the conditions that's bullish, and a low is swept out, that's when you anticipate a turtle soup"; (52:55–52:57) "that this is a turtle soup — it's a run on stops."
- `ICT-2016-TIMEFRAME-SELECTION` (40:00) "there's stop runs, which we classically call the turtle soup, which is a false breakout" — one of the three setups ICT trades; (43:46) "a turtle soup or a false break or run above equal highs, taking out the buy stops."
- `ICT-2017-STT-MM-TEMPLATES` (23:10–23:40) the consolidation-Thursday-reversal profile and its FOMC / employment-release driver, "around the 2 o'clock hour in Eastern Standard Time"; (23:55–24:07) "This false break becomes a turtle soup long and you're looking for the market to trade up into where the weekly buy stops are… It's going to trade up into that level as your weekly objective"; (24:26–24:56) the reduced position size and the resting limit below the Monday/Tuesday low placed after the knee-jerk; (26:02–26:10) "This is a turtle soup short", targeting the sell stops below the intraweek low.
- `ICT-2017-INTRADAY-TOP-DOWN` (43:41–43:53) the PD-array-matrix validity condition — why the sweep terminates where it does; (46:37–46:53) the whole method reduced to two patterns, "internal range liquidity, optimal trade entry… or external range liquidity, turtle soup, running out stops, and fading that move"; (30:12–30:19) "smart money uses offset accumulation to pair long entries with sell-stop raid discount entry — ICT version of turtle soup"; (30:19) *Street Smarts* named as the source of the idea; (32:46–33:03) "this is Turtle Soup, this is when Turtle Soup works… Linda Rashkin, where she teaches this pattern in her book with Larry Connors."


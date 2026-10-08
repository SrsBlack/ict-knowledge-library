# Stop Hunt Pattern

**Category:** 20-turtle-soup
**Aliases:** stop hunt, stop run pattern
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-TIMEFRAME-SELECTION, ICT-2016-LIQUIDITY-POOLS, ICT-2022-MENTORSHIP-EP02, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP38, ICT-2022-MENTORSHIP-EP40
**Tags:** stop-hunt, turtle-soup-related, foundational

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2017`,
which matched neither cited source (`ICT-2016-LIQUIDITY`, 2016, and
`ICT-2022-MENTORSHIP-OVERVIEW`, 2022 — both build-time placeholders). The **Month 1**
(September 2016) lecture *Equilibrium Vs. Discount* teaches the mechanic and its price
target: "markets move in intraday price action in grades of 10 — 10 and 20 pip ranges above
a high; that's how far they'll reach for a stop. Boom. There you go. **There's your stop run
on equal highs**" (`ICT-2016-EQUILIBRIUM-DISCOUNT`, 51:02–51:21), and poses the
reversal-vs-continuation question this page is built on: "how do I know if the market's
going to keep going lower, or if it's going to just go below an old low, and then rally up?"
(40:26–40:32). Re-dated to **2016**.

⚠ **Terminology, re-scoped 2026-10-08 — ERA-SPLIT.** "Stop hunt" is **not** ICT's phrase in
the 2016-17 mentorship: across all 153 2016-17/2020-21 corpus packets the string *stop hunt* /
*stop-hunt* occurs **0 times**; ICT there says **stop run** (55×) and **run on / out the
stops** (56×), with *raid* (10×) from 2017 onward. But in the **2022 mentorship ICT does say
"stop hunt" in his own voice, roughly 10 times**: "always anticipate some measure of a stop
hunt on buy stops or a short-term high being taken out" (`ICT-2022-MENTORSHIP-EP02`, 22:30);
"that's running for stops — that's a stop hunt — then you're looking for that signature for
the market structure shift" (`ICT-2022-MENTORSHIP-EP03`, 35:55); "what would be the catalyst
for a stop hunt?" (`ICT-2022-MENTORSHIP-EP05`, 13:32); "this is just a stop hunt below that
short-term low" (`ICT-2022-MENTORSHIP-EP38`, 42:28); "shift in market structure after the stop
hunt" (`ICT-2022-MENTORSHIP-EP40`, 41:48). State both eras when citing this: `stop run` for
2016-17, `stop hunt` is genuinely ICT's own 2022 usage — do not call it library coinage
without qualification.

## Definition

The **stop hunt pattern** is the broader umbrella for any price action that **deliberately targets resting stops** — a superset that includes Turtle Soup, liquidity sweeps, and Judas swings. The stop hunt emphasizes the **intent**: the algorithm is going for the stops, not pursuing fair-value delivery. ICT teaches the stop hunt as the dominant explanation for sudden, fast wicks against a recent trend — they're not "random spikes," they're engineered moves to fill institutional orders. The deeper file at [stop-run-definition](../29-stop-runs/stop-run-definition.md) covers the same phenomenon from the stop-runs directory.

## Formal Criteria

- Price approaches a known stop cluster (above swing high for buy stops; below swing low for sell stops).
- A fast move takes the level — "the break in the market going higher and lower above old highs or lower below an old low that's running for stops — that's a stop hunt" (`ICT-2022-MENTORSHIP-EP03`, 35:55).
- One of two outcomes, in ICT's own vocabulary (see [liquidity-sweep](../02-liquidity/liquidity-sweep.md) / [liquidity-run](../02-liquidity/liquidity-run.md)):
  - **Sweep** = Turtle Soup outcome (price reverses back inside).
  - **Run** = price "runs right over top of it and it just doesn't look back" — continuation, stops were fuel.
- Bias direction post-hunt determines which outcome occurred. ICT gives **no bar-count window** for how quickly a reversal must show up — see Formula.

## Formula / Math

```
stop_hunt_pattern(level):
  approach_phase: price moves toward level
  hunt_event: high(n) > level (for BSL) OR low(n) < level (for SSL)
  resolution:
    sweep (reverses) OR run (continues) — ICT gives no close-based or bar-count formula
```

ICT's own quantification is penetration **depth**, not a bar-count close rule, and it is scoped to a lower-timeframe FX chart: "on a lower timeframe chart like a 15 or 30 minute chart… you can expect a 10 to 20 pip sweep below the old low" (`ICT-2016-LIQUIDITY-POOLS`, 10:28–10:46); beyond ~25 pips, "I think is a fair assessment," "it's probably not just a stop run" (11:30–11:39) — a hedged figure, with no equivalent given for HTF or non-FX instruments. The library's prior "if close returns inside within 3 bars" formula is **not in either corpus** — see `liquidity-sweep` and `turtle-soup` for the same correction.

## Machine-Readable

```json
{
  "id": "stop-hunt-pattern",
  "category": "20-turtle-soup",
  "aliases": ["stop-hunt", "stop-run-pattern"],
  "criteria": [
    {"id": "c1", "expr": "approach_to_known_stop_cluster"},
    {"id": "c2", "expr": "fast_move_takes_level"},
    {"id": "c3", "expr": "outcome: sweep (reverses, turtle_soup) OR run (continues) — ICT gives no close/bar-count formula; quantification is depth, scoped to a 15-30 min FX chart (10-20 pips typical, >~25 pips not a stop run, hedged, no figure for HTF/non-FX)"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["turtle-soup","bullish-turtle-soup","bearish-turtle-soup","liquidity-sweep","liquidity-run","stop-run-definition","judas-swing"],
  "sources": ["ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-TIMEFRAME-SELECTION","ICT-2016-LIQUIDITY-POOLS","ICT-2022-MENTORSHIP-EP02","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP38","ICT-2022-MENTORSHIP-EP40"]
}
```

## Visual Pattern

```
   stop hunt outcomes:

   Sweep (Turtle Soup, reverses):       Run (continues):

        █  ← spike + reverses back       █  ← spike
        █                                █
   ─────█── stop level                ───█── stop level
                                         █
        ▲▲▲ rally up                     █  ← "doesn't look back" —
                                         █  continues with displacement
```

## Timeframes

All TFs.

## Examples

**Example 1 — stop hunt with Turtle Soup outcome:**
- M15 PWL at 1.0850 has known sell stops below.
- 02:55 NY: M15 wicks 1.0843, closes 1.0858.
- → stop hunt + Turtle Soup. Long bias for the rest of London.

**Example 2 — stop hunt with run (continuation) outcome:**
- M15 PWL at 1.0850, HTF bearish.
- 02:55 NY: M15 wicks 1.0843; next M15 closes 1.0838 (continuation through).
- → stop hunt was fuel for the bearish move, not a reversal trigger.

## Common Mistakes

- **Treating every stop hunt as a Turtle Soup.** The continuation case (a *run*, in ICT's vocabulary) is real and frequent; don't assume reversal.
- **Inventing a bar-count close rule.** "If close returns inside within 3 bars" is not in either corpus — see Formula / Math.
- **Single-direction reading.** Stop hunts happen on both sides; check both BSL and SSL relative to current price.
- **Calling "stop hunt" library coinage without an era label.** It is 0 hits in 2016-17 but genuinely ICT's own phrase ~10× in 2022 — see the Terminology note above.

## Related Concepts

- [turtle-soup](turtle-soup.md), [bullish-turtle-soup](bullish-turtle-soup.md), [bearish-turtle-soup](bearish-turtle-soup.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [liquidity-run](../02-liquidity/liquidity-run.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md), [judas-swing](../13-judas-swing/judas-swing.md).

## Citations

- `ICT-2016-EQUILIBRIUM-DISCOUNT` (51:02–51:21) the 10-and-20-pip reach above a high, "there's your stop run on equal highs… mark out areas where there's equal highs, they're too clean, the market's going to want to run there"; (40:26–40:37) the reversal-vs-continuation question stated as the central one; (52:55–53:03) "this is a turtle soup, it's a run on stops… why? because it already took the stops out."
- `ICT-2016-TIMEFRAME-SELECTION` (42:22–42:39) "if you are looking to trade only stop runs, you first have to know why the stop run would be necessary… and you get that from the higher time frame"; (46:50) "you'll clearly see where the stop runs are and you'll be able to trade turtle soups."
- `ICT-2016-LIQUIDITY-POOLS` (10:28–10:46) "on a lower timeframe chart like a 15 or 30 minute chart… you can expect a 10 to 20 pip sweep below the old low"; (11:30–11:39) "if it starts moving beyond 25 pips, I think is a fair assessment… it's probably not just a stop run."
- `ICT-2022-MENTORSHIP-EP02` (22:30) "always anticipate some measure of a stop hunt on buy stops or a short-term high being taken out."
- `ICT-2022-MENTORSHIP-EP03` (35:55) "that's running for stops — that's a stop hunt — then you're looking for that signature for the market structure shift."
- `ICT-2022-MENTORSHIP-EP05` (13:32) "what would be the catalyst for a stop hunt?"
- `ICT-2022-MENTORSHIP-EP38` (42:28) "this is just a stop hunt below that short-term low."
- `ICT-2022-MENTORSHIP-EP40` (41:48) "shift in market structure after the stop hunt."

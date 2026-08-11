# London Close Judas Swing

**Category:** 13-judas-swing
**Aliases:** London close protraction, post-10:00 Judas, London close reversal swing, second swipe
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-MARKET-REVERSALS, ICT-2017-BREAD-BUTTER-BUY, ICT-2017-BREAD-BUTTER-SELL
**Tags:** judas, london-close, protraction, reversal, adr, session-open

## Definition

The London Close Judas swing is the fourth session Judas ICT enumerates, and the one that behaves differently from the other three. Where the London-open, New York and Asia Judas swings are counter-directional moves that *precede* their session's delivery, the London Close Judas is a move that **extends the day's established direction one last time after 10:00 NY, prints the day's extreme, and is then faded**. On a bullish day it is a rally, not a decline: "the rally that takes place post 10 a.m., that's the Judas swing or protraction — a state where it creates the high of the day, and then you'll be looking to sell that if you're going to be a London close trader" (`ICT-2017-BREAD-BUTTER-BUY` [21:32]).

It is explicitly **conditional**, not daily. `ICT-2017-MARKET-REVERSALS` qualifies the enumeration itself — "you have it also in London close **on days that create London close reversals**" [28:07] — and gates it on the day having already over-delivered its five-day average daily range.

Its second, distinct role is the **"second swipe"**: when a New York session reversal has already occurred, London close comes back once more to run the stops of the traders who were correctly positioned for that reversal [33:45–34:07].

## Formal Criteria

- **Time: after 10:00 New York.** Three windows appear in the corpus and they do not agree; all three are recorded rather than reconciled:
  - anticipation window "10 o'clock and 11 o'clock in the morning New York time" (`ICT-2017-MARKET-REVERSALS` [11:35]);
  - retracement window "10 o'clock in the morning to noon New York time" (`ICT-2017-MARKET-REVERSALS` [32:27]);
  - entry window "between 10.30 a.m. and 1 p.m. New York time" (`ICT-2017-BREAD-BUTTER-SELL` [09:42]).
- **Range gate: the five-day ADR must already be exceeded by ~1.25×–1.33×.** "If it's a hundred pips ADR, I want to see 125 pips or 130 pips like that or more" (`ICT-2017-MARKET-REVERSALS` [12:15]). ICT states the trade is not to be taken "when the range is smaller than the last five days average daily range or if it wasn't really explosive" [12:45].
- **Direction: with the day, against the coming reversal.** Bullish day → a rally post-10:00 that makes the high of the day, sold. Bearish day → the mirror; `ICT-2017-BREAD-BUTTER-SELL` requires that New York and London "have moved in tandem" and "the 5 day average daily range low has been reached" before expecting the retracement off the daily low [09:29–09:40].
- **Retracement magnitude: about 20 % of the total daily range.** "The large range day that exceeds its five day average daily range tend to retrace about 20 % of its total daily range at 10 o'clock in the morning to noon New York time" (`ICT-2017-MARKET-REVERSALS` [32:27]).
- **Entry trigger (sell-side mirror):** "a 5 minute failure swing at the low and a bullish order block to enter on" (`ICT-2017-BREAD-BUTTER-SELL` [09:54]).
- **Second-swipe variant:** after a New York reversal, "London closed can many times go up there one more time or down there below to knock out those stops for those people that were right anticipating the New York session reversal … step right in there again and buy it below the New York low" (`ICT-2017-MARKET-REVERSALS` [33:58–34:07]).
- **Frequency: roughly one setup per session across a basket of four or five pairs**, not one per pair (`ICT-2017-BREAD-BUTTER-BUY` [04:33–04:50]).

## Formula / Math

```
ADR5        := mean(daily_range) over last 5 days
today_range := high_of_day - low_of_day

gate        := today_range >= 1.25 * ADR5        # ICT: 1.25x to 1.33x, "or more"

london_close_judas := gate
                       AND t >= 10:00 NY
                       AND direction(move) == sign(day_direction)   # extends, not counters
                       AND makes(day_extreme)

expected_retrace := 0.20 * today_range            # 10:00 -> 12:00 NY

# bearish-day mirror (ICT-2017-BREAD-BUTTER-SELL 09:29):
precondition := london_and_ny_moved_in_tandem AND ADR5_low_reached AND t >= 10:30 NY
entry        := M5_failure_swing(at day_low) AND bullish_order_block
window       := [10:30, 13:00] NY
```

## Machine-Readable

```json
{
  "id": "london-close-judas-swing",
  "category": "13-judas-swing",
  "aliases": ["london-close-protraction", "post-1000-judas", "second-swipe"],
  "criteria": [
    {"id": "c1", "expr": "t >= 10:00 NY"},
    {"id": "c2", "expr": "today_range >= 1.25 * ADR5"},
    {"id": "c3", "expr": "direction == sign(day_direction) AND makes(day_extreme)"},
    {"id": "c4", "expr": "expected_retrace == 0.20 * today_range"},
    {"id": "c5", "expr": "entry == M5_failure_swing AND order_block", "scope": "sell-side mirror"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["judas-swing","london-judas-swing","ny-judas-swing","asia-judas-swing","market-protraction","london-close-killzone","london-close","ny-lunch"],
  "sources": ["ICT-2017-MARKET-REVERSALS","ICT-2017-BREAD-BUTTER-BUY","ICT-2017-BREAD-BUTTER-SELL"]
}
```

## Visual Pattern

```
   BULLISH DAY — the Judas EXTENDS the move, then is sold
                                       ↑ 10:00+ NY
                                       ↑  post-10 rally
   ADR5 high  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─↑─── HIGH OF DAY  ← the Judas
                                  ↗    │
                          ↗            │  ~20% of the daily
                  ↗                    ↓  range retraces
          ↗   (London + NY delivery)   ↓  10:00 -> 12:00 NY
   open ↗                              ↓
        └───── today_range >= 1.25 x ADR5 (the gate) ─────┘


   SECOND SWIPE — after a NY reversal has already happened
        NY reversal low ──┬───────────────
                          │        ↓ London close pushes BELOW it
                          │        ↓  (runs the stops of traders
                          │        ↓   who were right about NY)
                          ↑        ↑
                          ↑  re-enter long below the NY low
```

## Timeframes

M1 / M5 / M15 for execution; the ADR gate is measured on the daily. The five-minute chart is the stated chart for the whole scalping module (`ICT-2017-BREAD-BUTTER-BUY` [04:14]), and the failure-swing trigger is explicitly a five-minute pattern.

## Examples

**Example 1 — bullish-day fade, as taught (`ICT-2017-BREAD-BUTTER-BUY` [21:19–21:43]):**
- Higher-timeframe order flow bullish; London and New York deliver the up-move.
- Price "goes up a little bit after 10 o'clock in the morning"; a vertical line is drawn at 10:00 NY.
- That post-10:00 rally "creates the high of the day" — this is the Judas.
- The London-close trade is to **sell** it.

**Example 2 — bearish-day mirror (`ICT-2017-BREAD-BUTTER-SELL` [09:25–09:59]):**
- New York and London have moved lower in tandem; the five-day ADR low is reached; clock is at least 10:30 NY.
- Price ideally has *exceeded* the five-day ADR.
- Entry: a five-minute failure swing at the low plus a bullish order block, taken between 10:30 and 13:00 NY.

**Example 3 — second swipe (`ICT-2017-MARKET-REVERSALS` [33:45–34:36]):**
- A New York session reversal is anticipated and occurs at a higher-timeframe discount array.
- London close pushes back below the New York low, stopping out the traders who bought the reversal.
- "If it comes down again in London, I'll step right back in there again and buy it again … many times you'll get really wicked low pricing and it quickly moves away the other way."
- ICT's worked case: "the reversal occurred on the Wednesday at London closed."

## Common Mistakes

- **Trading it on an ordinary-range day.** The ADR gate is the whole filter. "I don't like to do that type of trade when the range is smaller than the last five days average daily range or if it wasn't really explosive" ([12:45]).
- **Expecting the same shape as the other three Judas swings.** London close is described as "the opposite" ([21:19]) — it extends the day's direction and tops or bottoms it, rather than faking against the coming delivery.
- **Treating the enumeration as a daily occurrence.** It is qualified in the source: "on days that create London close reversals" ([28:07]).
- **Over-sizing it.** ICT groups it with Asia as one of "the two smallest tiny little windows of opportunity" that "doesn't pay out enough in my opinion to take on the risk" (`ICT-2017-BREAD-BUTTER-BUY` [28:21]), and says of his own practice: "how many times do you see me trade in London close? You don't see it a lot … unless it's a reversal time of day; if it's going to be a reversal market profile, then I'm all over London close" ([29:39–29:48]).
- **Assuming reversals belong to London open.** "London, like New York, can reverse the market. It's not just London Open that creates the reversals" (`ICT-2017-MARKET-REVERSALS` [34:44]).

## Related Concepts

- [judas-swing](judas-swing.md) — the parent concept; this is its London-close instance and the least typical of the four.
- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md), [asia-judas-swing](asia-judas-swing.md) — the other three sessions.
- [market-protraction](market-protraction.md) — ICT uses "Judas swing or protraction" interchangeably here.
- [london-close-killzone](../10-killzones/london-close-killzone.md) — the 10:00–12:00 NY window.
- [london-close](../15-sessions/london-close.md) — the session.
- [ny-lunch](../15-sessions/ny-lunch.md) — the 11:00–13:00 NY period the entry window overlaps.

## Citations

- `ICT-2017-MARKET-REVERSALS` (28:07) — "you have it also in **London close on days that create London close reversals**"; (11:20–12:15) the ADR gate, "if it's a hundred pips ADR I want to see 125 pips or 130 pips like that or more", anticipation at "10 o'clock and 11 o'clock in the morning New York time"; (12:45) do not take it on a small-range day; (32:27) "the large range day that exceeds its five day average daily range tend to retrace about 20 % of its total daily range at 10 o'clock in the morning to noon New York time"; (32:38) "in longer term conditions, the London closed can time a market reversal that can lead to a series of days of one sided direction"; (33:45–34:07) the second-swipe doctrine; (34:44) "London, like New York, can reverse the market. It's not just London Open that creates the reversals."
- `ICT-2017-BREAD-BUTTER-BUY` (21:19–21:43) — "at London close it can happen but it's the opposite … for a bullish day … the rally that takes place post 10 a.m., **that's the Judas swing or protraction, a state where it creates the high of the day**, and then you'll be looking to sell that if you're going to be a London close trader"; (04:33–04:50) one setup per session across a basket of pairs; (28:21) one of "the two smallest tiny little windows of opportunity"; (29:39–29:48) ICT trades it only on reversal profiles.
- `ICT-2017-BREAD-BUTTER-SELL` (09:25–09:59) — "when the New York and London sessions have moved in tandem and the 5 day average daily range low has been reached and it is at least 10.30 a.m. New York time, expect a retracement off the daily low … between 10.30 a.m. and 1 p.m. New York time … ideally price should exceed the 5 day average daily range … we look for a 5 minute failure swing at the low and a bullish order block to enter on."

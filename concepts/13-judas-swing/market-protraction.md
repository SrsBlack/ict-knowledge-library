# Market Protraction

**Category:** 13-judas-swing
**Aliases:** protraction, protractionary phase, protractionary state, time-sensitive impulse swing
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-PROTRACTION
**Tags:** judas, manipulation, time-of-day, impulse-swing, protraction, session-open

## Definition

Market protraction is **a small, counter-directional impulse price swing anchored to a
specific time of day**, whose purpose is manipulation: "it's designed and intended for
manipulation only… it's to get traders to think that the market's making a low"
(`ICT-2016-PROTRACTION`, 05:03–05:13).

The concept is defined against a plainer primitive taught in the same lecture. An **impulse
price swing** is simply a directional leg from a swing high to a swing low or back; the chart
is read as a sequence of them. Protraction is the subset that carries a clock: "**the
difference in determining impulse price swings and market protraction is the fact that there
is a time element applied** to the small impulse swing" (11:20–11:38).

This is the **parent concept of the [judas-swing](judas-swing.md)** — ICT applies the Judas
label to the London instance within this same lecture (06:40, 09:50).

## Formal Criteria

- **It is a small impulse swing, not a major leg.** "A small little impulse price swing, but
  its design is to manipulate the sentiment and/or the thoughts of traders wanting to be
  participants" (07:56–08:06).
- **It is counter to the direction that follows.** "It's counter direction — if this move
  occurs at this time of day, if it goes higher, we think the opposite direction; if it goes
  lower, we think the opposite direction" (05:53–06:05).
- **It occurs at one of three windows per 24 hours** (11:38–11:53). All times New York:

  | Window | NY time | Equivalent | Session |
  |---|---|---|---|
  | 1 | **20:00** | ≈ 0 GMT (the day divider / true day open) | Asian open |
  | 2 | **00:00** | ≈ 4 GMT | London |
  | 3 | **07:00** | — | New York |

  ⚠ The GMT equivalences are **DST-dependent** and ICT quotes both clocks in the same lecture
  (0 GMT and 20:00 NY for window 1; "after 4 GMT" and midnight NY for window 2). Per
  [dst-handling](../04-time-cycles/dst-handling.md), anchor to the **New York** column.
- **Its function is liquidity.** "The market's going to seek to draw in participants on the
  wrong side of the marketplace or reach for liquidity" (06:13).
- **The Asian window is the least influential** — "I don't believe Asian is that influential
  initially" (03:58).
- **It resolves into the real move.** The protraction runs stops or attracts the wrong-side
  crowd, then price expands in the direction the higher timeframe called for.
- **Blend it with the PD array read.** The lecture's worked sequence measures an impulse swing,
  takes the retracement into a premium at the 62 % level, and sells there for a run to the
  sell stops below — protraction supplies the *timing*, the array supplies the *level*
  (08:34–09:32).

## Formula / Math

```
impulse_price_swing := any directional leg (swing_high -> swing_low, or reverse)
                       # no time element; the chart is a sequence of these

market_protraction(t) := impulse_price_swing
                         AND small_relative_to_the_following_move
                         AND t in { 20:00 NY, 00:00 NY, 07:00 NY }
                         AND direction(swing) == NOT direction(subsequent_delivery)

# reading it:
if protraction_direction == UP   -> expect delivery DOWN
if protraction_direction == DOWN -> expect delivery UP

# combined with the array read:
entry := PD_array reached BY the protraction        # e.g. 62% retracement into a premium
target := liquidity opposite the protraction        # old lows / equal lows
```

## Machine-Readable

```json
{
  "id": "market-protraction",
  "category": "13-judas-swing",
  "aliases": ["protraction", "protractionary-phase", "time-sensitive-impulse-swing"],
  "criteria": [
    {"id": "c1", "expr": "impulse_price_swing := directional leg with NO time element"},
    {"id": "c2", "expr": "market_protraction := impulse_price_swing WITH a time-of-day anchor"},
    {"id": "c3", "expr": "windows_NY == {20:00, 00:00, 07:00}"},
    {"id": "c4", "expr": "direction(protraction) == opposite(direction(subsequent_delivery))"},
    {"id": "c5", "expr": "magnitude small relative to the delivery leg"},
    {"id": "c6", "expr": "purpose == manipulation / reach for liquidity"},
    {"id": "c7", "expr": "asian_window least influential per ICT"},
    {"id": "c8", "expr": "timing from protraction; level from the PD array"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["judas-swing", "london-judas-swing", "ny-judas-swing", "manipulation-phase", "true-day-open", "dst-handling", "time-of-day-pivots", "liquidity-sweep", "sentiment-effect"],
  "sources": ["ICT-2016-PROTRACTION"]
}
```

## Visual Pattern

```
   THREE PROTRACTION WINDOWS IN 24 HOURS (New York time)

   20:00        00:00                    07:00
   Asian open   London                   New York
     │            │                        │
     │  ╱╲        │   ╱╲                   │   ╱╲
   ──┼─╱──╲───────┼──╱──╲──────────────────┼──╱──╲──────────────
     │      ╲     │       ╲                │       ╲
     │       ╲    │        ╲___            │        ╲____
     ▲            ▲                        ▲              ▼
   small        small                    small        THE REAL MOVE
   counter-     counter-                 counter-     (opposite the
   move         move                     move          protraction)

   Read: protraction UP  -> expect delivery DOWN
         protraction DOWN -> expect delivery UP

   An impulse swing without a clock is just a leg.
   An impulse swing AT one of these times is a protraction.
```

## Timeframes

Observed on M5–H1. The windows are fixed clock times, so the concept has no higher-timeframe
form — a daily candle contains all three.

## Examples

All from `ICT-2016-PROTRACTION`, read across successive days on one intraday chart.

**Example 1 — London protraction up, delivery down (04:22–04:44):**
- Just after midnight NY, price moves **higher**.
- "Its design is to fake out the individuals that chase that initial move after midnight."
- Delivery: price trades down for the rest of the session.

**Example 2 — the 07:00 NY window (04:50–05:17, 07:50–08:13):**
- London has moved lower; after 07:00 NY, a small rally forms.
- Retail reads the rally as a low being made and buys into the New York session.
- Delivery: the market reverses and trades lower.

**Example 3 — protraction blended with a premium array (08:34–09:32):**
- An impulse swing down is measured; price retraces **above equilibrium into a premium** at
  the **62 % retracement**.
- The protractionary phase follows the impulse swing, so the 62 % level is sold.
- Target: the sell stops below the swing low, plus an older low identified on previous days.

**Example 4 — protraction down, then delivery up (07:09–07:31):**
- Price drops from the midnight candle, clearing lows below the market.
- The downside move *is* the protraction — it "seeks liquidity below the market… clearing out
  lows, and then rallies."

## Common Mistakes

- **Treating every impulse swing as a protraction.** Without one of the three time anchors it
  is just a leg; the time element is the whole definition.
- **Trading in the protraction's direction.** It is counter-directional by construction — that
  is what makes it a manipulation.
- **Expecting it to be large.** It is explicitly a *small* swing relative to the delivery.
- **Anchoring to GMT instead of New York.** ICT quotes both clocks; the GMT figures drift with
  DST while the NY windows do not.
- **Over-weighting the Asian window.** ICT states outright that he does not consider it very
  influential.
- **Using it without a level.** Protraction supplies timing; the entry still comes from a PD
  array or a liquidity pool.
- **Assuming a protraction must occur in all three windows every day.** They are the windows to
  watch, not a guarantee of three moves.

## Related Concepts

- [judas-swing](judas-swing.md) — the named session-open instance; ICT uses the label for the London protraction in this lecture.
- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md) — the 00:00 and 07:00 windows respectively.
- [manipulation-phase](../12-power-of-three/manipulation-phase.md) — the AMD phase protraction implements.
- [true-day-open](../22-quarterly-theory/true-day-open.md) — the 0 GMT reference the first window sits on.
- [dst-handling](../04-time-cycles/dst-handling.md) — why the NY column governs.
- [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md) — the wider set of clock-anchored references.
- [sentiment-effect](../31-models/sentiment-effect.md) — the May-2017 lecture that turns the same idea into entry conditions.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — where the protraction is priced with a 10–20-pip limit at the 0 GMT open.

## Citations

- `ICT-2016-PROTRACTION` (01:00–01:52) the chart read as a sequence of impulse price swings high to low and back; (01:52–02:19) "inside the impulse price swings, it's going to give you a lot of detail… there are smaller, more specific impulse price swings that have a lot more influence… in the form of a manipulative move"; (02:41–02:56) adding the 0 GMT vertical day dividers to see "time sensitive impulse price swings, which is market protraction"; (03:12–03:20) "market protraction is time sensitive — it's an impulse price swing that is highly sensitive to a time of day"; (03:20–03:31) "there are three primary protractionary market moves every 24 hours; the first one is right at zero GMT"; (03:58–04:04) "I don't believe Asian is that influential initially"; (04:04–04:44) the London window at midnight New York and the fake-out of those who chase the initial move; (04:50–05:17) the New York window delineated at 07:00; (05:03–05:13) "it's designed and intended for manipulation only… it's to get traders to think that the market's making a low"; (05:53–06:19) "it's counter direction… the market's going to seek to draw in participants on the wrong side of the marketplace or reach for liquidity"; (06:32–06:49) the London window "after 4 GMT" — "if we see a movement higher and we're bearish, we see that as market protraction or a Judas swing; it's a false rally to sell into"; (07:09–07:31) protraction down, clearing lows, then rallying; (07:50–08:13) the 07:00 NY rally that "would look like a low" and entices buyers before the reversal; (08:34–09:32) blending the impulse swing with a 62 % retracement into a premium; (09:50) "in the next London session, it's in Judas swing lower or market protractionary phase"; (11:20–11:53) "the difference in determining impulse price swings and market protraction is the fact that there is a time element applied to the small impulse swing — after midnight New York time, after 7 a.m. New York time, and 8 p.m. New York time"; (11:53–12:09) the protraction "is counter the major direction that you're going to see after that specific time of day", useful for session drills and anticipatory skill.

# Index AM & PM Trend

**Category:** 15-sessions
**Aliases:** AM trend, morning swing, PM trend, afternoon swing, index session trends, spooz AM trend
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-INDEX-SMT-AM-TREND, ICT-2017-INDEX-PM-TREND, ICT-2017-INDEX-OPENING-RANGE
**Tags:** sessions, index-futures, ny-am, ny-pm, ny-lunch, trend, time-of-day

## Definition

The AM trend and the PM trend are ICT's **two daily price swings of the index-futures cash
session**, separated by the New York lunch hour. Each is a distinct, tradeable swing with its own
clock, its own expected extreme and its own confirmation: "between the open at 9:30 a.m. and noon
New York time, there is typically a **trend or price swing daily** — this is referred to as the
**AM trend or morning swing**" (`ICT-2017-INDEX-SMT-AM-TREND`, 01:06); "between 1 p.m. and 4 p.m.
New York time there's typically a trend or a price swing that's seen daily, and this is going to
be referred to… as the **PM trend or the afternoon swing**" (`ICT-2017-INDEX-PM-TREND`, 01:28).

Together they bracket the **true day**, 09:30 → 16:00 NY. The AM trend tends to build one end of
the daily range and the PM trend the other.

## Formal Criteria

**The clock (New York time)**

| Block | Window | Where its extreme forms |
|---|---|---|
| **Opening range** | 09:30 → 10:30 | see [futures-opening-range](futures-opening-range.md) |
| **AM trend / morning swing** | **09:30 → 12:00** | **true-day high or low forms 09:30 → 10:30** |
| **New York lunch** | nominally **12:00 → 13:00**, elastic **11:00 → 14:00** | consolidation / retracement |
| **PM trend / afternoon swing** | **13:00 → 16:00** | **the opposite extreme forms 15:00 → 16:00** |

- The AM trend "can end at **10:30 a.m. to 11 a.m.** but anticipate it continuing up to noon or
  the New York lunch hour" (`ICT-2017-INDEX-SMT-AM-TREND`, 01:32).
- Lunch is elastic and driven by the morning's pace: "if there's a **fast market in the morning**,
  traders are going to want to probably work through lunch, so **short lunch periods**… when the
  session in the morning was rather **lethargic**, the full lunch hour could… be seen"
  (`ICT-2017-INDEX-PM-TREND`, 02:50–03:24).
- The PM move "typically **2 p.m. New York time sees the move begin**. Now it can start as early
  as 1 p.m." (01:52–02:12).

**Direction rules**

- The AM trend "can be a **continuation of overnight direction or an outright reversal** of
  direction right from the opening at 9:30 a.m." (01:21).
- The PM trend "can be a **continuation of the AM trend direction or an intraday reversal** going
  into the close" (01:41).
- **Measured moves in the afternoon are faster than the morning's** (01:52).

**The bookend rule** (`ICT-2017-INDEX-PM-TREND`, 11:35–12:24)

- If the opening hour makes the day's **low**, the **15:00 → 16:00** hour will generally make the
  day's **high**, and vice versa: "if the AM session creates the low of the day… the **last hour,
  3 p.m. to 4 p.m.** New York time will create the high of the day."
- The pivot named is the **bond close**: "as soon as the **bond market closes at 3 p.m.** New York
  time, that's usually when the market makes its high or low in respective terms to what was seen
  in the AM session."

**Confirmation — index SMT, two windows**

The trigger for both swings is a divergence across the three indices (NASDAQ, Dow, e-mini S&P):

| Swing | Comparison window (NY) | Bullish | Bearish |
|---|---|---|---|
| AM trend | **05:00 → 09:30** | one index **fails to make the lower low** | one index **fails to make the higher high** |
| PM trend | **12:00 → 15:00** | one index **fails to make the lower low** | one index **fails to make the higher high** |

- The 05:00 anchor has a stated reason: London traders take lunch around then and return at an
  unknown time, so "we start waiting for that **buildup of orders** that come by way of the UK and
  European traders" (13:48–14:21).
- The window is a span, not a pair of goalposts: "don't think that it's exactly at 5 a.m. and 9:30
  a.m.… **don't think like they're goalposts**" (12:52–12:59). Compare **relative** highs and lows
  anywhere inside it.
- Frequency: "typically, there will be an index SMT divergence to qualify the AM trend setups **a
  few times a week**" (17:00).
- **Obviousness gate:** "**when it's not obvious, assume it's not there**" (17:38).

**Two entry techniques off the divergence** (16:35–16:46)

- **Buying on a stop / buying strength** — a buy stop above an old high, anticipating the breakout
  through what will later become bullish order blocks.
- **Buying weakness** — the index that *does* make the lower low is the **turtle soup**; buy below
  the old low. "Your eye should go right to that one that's making a lower low and identify that
  as turtle soup" (16:22).
- Neither is preferred: "there's not one over the other in terms of advantage" (16:49).
- The diverging index and the stop-running index both move; **speed is generally seen in the one
  that ran the stops**, though "it doesn't always equate to magnitude" (18:46–19:08).

**Contract basics** (`ICT-2017-INDEX-OPENING-RANGE`)

- **ES = e-mini S&P 500**; delivery months March (H), June (M), September (U), December (Z);
  1 tick = **$12.50**, 4 ticks = 1 point = **$50**; notional ≈ $50 × index.
- The other two indices ICT follows are **NQ (NASDAQ)** and the **Dow mini**; true day is
  09:30 → 16:00 for all three.

## Formula / Math

```
# --- clock (New York time) ---
true_day      := [09:30, 16:00]
opening_range := [09:30, 10:30]
AM_trend      := [09:30, 12:00]          # may terminate 10:30-11:00
lunch         := [12:00, 13:00]          # elastic [11:00, 14:00]
PM_trend      := [13:00, 16:00]          # move typically begins ~14:00

true_day_extreme_1 forms in [09:30, 10:30]
true_day_extreme_2 forms in [15:00, 16:00]

# --- bookend rule ---
if extreme_in(AM) == LOW:   expect HIGH in [15:00, 16:00]
if extreme_in(AM) == HIGH:  expect LOW  in [15:00, 16:00]
pivot := bond close 15:00

# --- index SMT trigger ---
idx := {NQ, YM, ES}
smt_window(AM) := [05:00, 09:30]
smt_window(PM) := [12:00, 15:00]

bullish_smt := IOF is bullish
               AND >=2 of idx make a lower low in window
               AND >=1 of idx FAILS to make that lower low
bearish_smt := IOF is bearish
               AND >=2 of idx make a higher high in window
               AND >=1 of idx FAILS to make that higher high

gate := divergence must be OBVIOUS; else treat as absent

# --- entries ---
entry_A := buy stop above an old high            # buying strength
entry_B := buy below the old low of the index that DID make it   # turtle soup
# speed usually in the stop-running index; magnitude not guaranteed
```

## Machine-Readable

```json
{
  "id": "index-am-pm-trend",
  "category": "15-sessions",
  "aliases": ["am-trend", "morning-swing", "pm-trend", "afternoon-swing", "index-session-trends"],
  "criteria": [
    {"id": "c1", "expr": "AM_trend == [09:30,12:00] NY; may end 10:30-11:00"},
    {"id": "c2", "expr": "true-day high or low forms in [09:30,10:30] NY"},
    {"id": "c3", "expr": "lunch == [12:00,13:00] NY nominal, elastic [11:00,14:00]; pace-dependent"},
    {"id": "c4", "expr": "PM_trend == [13:00,16:00] NY; move typically begins ~14:00"},
    {"id": "c5", "expr": "opposite true-day extreme forms in [15:00,16:00] NY, pivoting on the 15:00 bond close"},
    {"id": "c6", "expr": "AM trend := continuation of overnight OR reversal at 09:30"},
    {"id": "c7", "expr": "PM trend := continuation of AM OR intraday reversal into the close"},
    {"id": "c8", "expr": "PM measured moves complete faster than AM measured moves"},
    {"id": "c9", "expr": "trigger := index SMT across {NQ,YM,ES} in [05:00,09:30] for AM and [12:00,15:00] for PM"},
    {"id": "c10", "expr": "divergence must be obvious; if not obvious, treat as absent"},
    {"id": "c11", "expr": "entry := buy-stop above old high OR turtle soup below the diverging index's old low; neither preferred"}
  ],
  "timeframes": ["M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["futures-opening-range", "bond-split-session-rules", "ny-am-session", "ny-pm-session", "ny-lunch", "index-smt", "turtle-soup", "projected-range-objectives", "institutional-order-flow", "bullish-order-block"],
  "sources": ["ICT-2017-INDEX-SMT-AM-TREND", "ICT-2017-INDEX-PM-TREND", "ICT-2017-INDEX-OPENING-RANGE"]
}
```

## Visual Pattern

```
   THE INDEX-FUTURES TRUE DAY (New York time)

   05:00 ─────────── 09:30 ── 10:30 ── 12:00 ── 13:00 ──────── 15:00 ── 16:00
   ├── SMT window (AM) ──────┤ │        │        │              │        │
                        ┌────┴─────────┐│  ▪▪▪▪  ┌──────────────┴────────┐
                        │  AM TREND    ││ lunch  │      PM TREND         │
                        │ morning swing││ elastic│    afternoon swing    │
                        │              ││11:00-  │  move begins ~14:00   │
                        └──────────────┘│ 14:00  └───────────────────────┘
                        ███ opening      ├── SMT window (PM) ────┤
                            range        12:00               15:00
                        ▲                                          ▲
                 true-day extreme #1                    true-day extreme #2
                    forms 09:30-10:30                      forms 15:00-16:00
                                                    ▲ pivot = 15:00 bond close

   ─────────────────────────────────────────────────────────────────────
   THE BOOKEND RULE

     AM makes the LOW  ─────────────────────►  last hour makes the HIGH
     AM makes the HIGH ─────────────────────►  last hour makes the LOW

   ─────────────────────────────────────────────────────────────────────
   INDEX SMT (bullish form)

     NQ   ╲___╲   LOWER low   ✗  <- turtle soup: buy BELOW this
     YM   ╲___╱   higher low  ✓     (speed usually here)
     ES   ╲___╱   higher low  ✓  <- accumulation
                                    (or: buy stop above an old high)
```

## Timeframes

**15-minute** for the AM/PM swing framing and the index-SMT comparison; **5-minute** for the
interior arrays. This is an intraday construct — there is no higher-timeframe form.

## Examples

**Example 1 — bullish index SMT into the AM trend (`ICT-2017-INDEX-SMT-AM-TREND`, 08:33–09:45):**
- Window: 05:00 → 09:30 NY, 15-minute charts of NQ, YM and ES.
- NQ made a **lower low** right at the start of the NY AM session; YM made a **higher low**; ES
  made a **higher low**.
- Read: "massive accumulation under the Dow futures and on the S&P 500" — the NQ low was a stop
  run, and "quickly we reprice the NASDAQ futures higher after that low has been violated from
  the 5 a.m." (14:54–15:09).
- Outcome: all three moved up together off the divergence.

**Example 2 — AM trend off a bullish order block (03:39–04:07):**
- London session established the overnight leg.
- At the 09:30 open price traded down into a **previous down-closed candle** (bullish order block)
  and expanded higher, with the highs forming at **10:30 a.m. NY**.

**Example 3 — AM trend off a London bullish breaker, YM (06:07–07:04):**
- During London, price traded down and cleared a level of stops, leaving a **bullish breaker** —
  the last two up-closed candles of the London session.
- The expansion fired at the **09:30 equities open**: "that expansion move… is actually a
  precursor by looking at the London session run out on the lows."

**Example 4 — PM trend off an AM order block (`ICT-2017-INDEX-PM-TREND`, 03:48–04:07):**
- Setup: ES, afternoon session dropped into an **order block formed during the AM session**.
- Outcome: rallied off it into the **high of the day, made in the last trading hour**.

**Example 5 — bearish PM index SMT (08:48–10:16):**
- Window: noon → 15:00 NY. ES made a **higher low**, YM made a **higher low**, NQ made a **lower
  low** — "a break in what will be expected".
- Read: accumulation in the Dow and S&P not present in the NASDAQ; NQ was "the lethargic sister".
- Use: "if I see that crack among all three, my trade's going to be taken **in the S&P**" — the
  divergence signals the S&P, it is not a signal to trade the diverging index (09:55–10:34).

## Common Mistakes

- **Using the FX session clock.** The index AM trend starts at **09:30**, not 08:00, and the PM
  trend at **13:00**, not 13:30. The bond day is different again — see
  [bond-split-session-rules](bond-split-session-rules.md).
- **Treating lunch as a fixed hour.** It runs 11:00–14:00 at the extremes and shrinks on fast
  mornings.
- **Reading 05:00 and 09:30 as the exact swing points.** They bracket a **four-and-a-half-hour**
  comparison span; relative highs and lows anywhere inside it count.
- **Hunting for a divergence that is not there.** "When it's not obvious, assume it's not there."
  A daily divergence exists on many days without being a low-risk opportunity.
- **Trading the diverging index.** ICT takes the trade in the S&P regardless of which index
  produced the crack.
- **Assuming the stop-running index gives the bigger move.** It gives the **speed**; magnitude is
  not implied.
- **Expecting the PM to always reverse.** It is continuation *or* reversal, and on a clean
  trending day the last hour simply completes the range.

## Related Concepts

- [futures-opening-range](futures-opening-range.md) — the 09:30–10:30 block at the front of the AM trend.
- [bond-split-session-rules](bond-split-session-rules.md) — the bond-market analogue on a different clock; its 15:00 close is this page's PM pivot.
- [index-smt](../16-smt-divergence/index-smt.md) — the divergence that triggers both swings.
- [projected-range-objectives](../31-models/projected-range-objectives.md) — the six day-profiles built on top of these three blocks.
- [ny-am-session](ny-am-session.md), [ny-lunch](ny-lunch.md), [ny-pm-session](ny-pm-session.md) — the FX-side session definitions.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the entry taken on the index that *did* run the stops.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md) — the array most of the worked examples turn on.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the input that decides whether lows or highs are compared.

## Citations

- `ICT-2017-INDEX-SMT-AM-TREND` (00:23) "**June 2017, ICT Mentorship, ICT Index Trading, Lesson 2, The AM Trend**" — self-dates the lecture; (00:49–00:56) "the **New York AM session is defined by 9:30 a.m. to noon** New York time"; (00:56–01:06) "the **true day high or low will tend to form in between the hours of 9:30 a.m. and 10:30 a.m.** New York time"; (01:06–01:21) "between the open at 9:30 a.m. and noon New York time, there is typically a trend or price swing daily. This is referred to as the **AM trend or morning swing**"; (01:21–01:31) "the AM trend can be a **continuation of overnight direction or an outright reversal** of direction right from the opening at 9:30 a.m."; (01:32–01:50) "the AM trend can **end at 10:30 a.m. to 11 a.m.** but anticipate it continuing up to noon or the New York lunch hour"; (03:39–04:13) the bullish order block at the AM open with the highs forming at 10:30; (04:24–05:04) the fair value gap example — "only wicks were being shown here. **We like to see bodies. The bodies has to cross. That's efficiently traded**"; (06:07–07:04) the London bullish breaker as the precursor to the 09:30 expansion; (07:57–08:05) "**between 5 a.m. and 9:30 a.m. New York time, relative highs and lows should be compared**"; (08:05–08:33) "when institutional order flow is bullish… we have to be comparing relative lows across the three indices. **One index will fail to confirm a lower low**… when that occurs, that's your **bullish confirmation for trading the AM trend**"; (08:33–09:45) the worked NQ/YM/ES divergence; (10:08–10:33) the bearish mirror — comparable highs, one index failing to confirm a higher high; (11:11–12:59) "there may be a low seen at, for instance, 7 o'clock in the morning… **don't think like they're goalposts**"; (13:13–13:24) "**that crack in correlation** where otherwise the indices should be moving in tandem"; (13:48–14:21) why 05:00 — London traders take lunch and return at an unknown time, so orders build; (14:54–15:09) "that run under the **5 a.m. low on NASDAQ, that's a stop run**"; (15:36–16:11) buying on a stop above an old high, anticipating the breakout above down-closed candles that later become bullish order blocks; (16:11–16:49) "your eye should go right to that one that's making a lower low and identify that as **turtle soup**… buy it below the old low… **there's not one over the other in terms of advantage**"; (17:00–17:23) "typically, there will be an index SMT divergence to qualify the AM trend setups **a few times a week**… it does not equate to a large opportunity with low risk"; (17:32–17:42) "**when it's not obvious, assume it's not there**"; (18:46–19:08) "the **speed** will be seen at the one that makes the lower low… it doesn't always equate to **magnitude**".
- `ICT-2017-INDEX-PM-TREND` (00:24) "**June 2017 ICT mentorship, ICT index trading, lesson three, the PM trend**" — self-dates the lecture; (01:15–01:28) "the true day high or low will tend to form in between the hours of **3 p.m. and 4 p.m.** New York time — so typically it's the **last hour**"; (01:28–01:41) "between **1 p.m. and 4 p.m.** New York time there's typically a trend or a price swing that's seen daily and this is going to be referred to… as the **PM trend or the afternoon swing**"; (01:41–01:52) "the PM trend can be a **continuation of the AM trend direction or an intraday reversal** going into the close"; (01:52–02:12) "**measured moves in the afternoon tend to be faster** than that which was seen in the AM session, and typically **2 p.m.** New York time sees the move begin. Now it can start as early as 1 p.m."; (02:41–03:24) "while I say the New York lunch hour it's basically implying that lunch is **noon to 1 p.m.**, it can actually be **as early as 11 a.m. to as late as 2 p.m.**… if there's a fast market in the morning traders are going to want to probably work through lunch"; (03:48–04:07) the PM drop into an AM-session order block and the high of the day in the last trading hour; (04:21–04:47) the second example into a rejection block — "it's not a lot of movement, that's generally the nature of indices"; (05:23–06:00) the ES example where the PM violated the AM rejection block, "an accumulation phase… and the market rallies about **18 handles**"; (06:44–07:12) the NQ example — an order block formed **during the lunch hour** sending price into a morning-session rejection block, "about **nine full handles**"; (07:26–08:48) "as we've shown with the index SMT for the AM session, the same thing applies for the PM session, but we're going to be looking for the highs and the lows **between noon and 3 p.m. New York time**"; (08:48–10:16) the worked bearish-form example — ES and YM higher lows against an NQ lower low, "**the lethargic sister**"; (09:55–10:34) "if I see that crack among all three, **my trade's going to be taken in the S&P** — I'm not trying to trade the Dow or trading the NASDAQ futures"; (11:20–12:24) "it begins around **1 p.m.** New York time and extends all the way to **4 p.m.** at the close… **as soon as the bond market closes at 3 p.m.**… if the AM session creates the low of the day… the **last hour, 3 p.m. to 4 p.m.**, will create the high of the day". ⚠ The whisper transcript garbles the PM window at 00:41 as "1 p.m. to 1 p.m."; the window is stated correctly at 01:28 and 11:20 and is taken from there.
- `ICT-2017-INDEX-OPENING-RANGE` (00:57–01:53) ES contract basics — symbol, delivery months March (H) / June (M) / September (U) / December (Z), **$12.50 per tick**, four ticks to a point, $50 per point, notional $50 × index; (02:45–02:57) "**true day** for SPOOs… **9:30 a.m. to 4 p.m.** New York time"; (11:23–11:50) "there's a very specific relationship to the first hour's range high and low and the first 30 minutes high and low, as you'll see in the next teaching, **trading the AM trend**".

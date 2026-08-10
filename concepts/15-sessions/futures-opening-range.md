# Futures Opening Range

**Category:** 15-sessions
**Aliases:** opening range, bond opening range, spooz opening range, index opening range, 8-9 opening range, 930-1030 opening range
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-BOND-OPENING-RANGE, ICT-2017-INDEX-OPENING-RANGE, ICT-2017-BOND-CONSOLIDATION-DAYS, ICT-2017-BOND-SPLIT-SESSION
**Tags:** sessions, futures, bonds, index-futures, opening-range, volume, liquidity-pool

## Definition

The opening range is the **high and low of a fixed clock window at the start of a futures
market's cash session**, taken as the day's primary reference block. ICT teaches it twice in
the June 2017 mentorship — once for the 30-year Treasury bond (ZB) and once for the index
futures (ES/NQ/YM) — with the same logic and two different clocks, each anchored to that
market's own highest-volume window.

The claim is narrow and testable: the opening range "tends to create the bond market high or
low of the day" (`ICT-2017-BOND-OPENING-RANGE`, 03:47) / "tends to create the SPOOs market
high or low of the day" (`ICT-2017-INDEX-OPENING-RANGE`, 03:23). What happens at its bounds is
one of two things — "it can be a **run on stops** or a **fair value setup**" — and its interior
supplies the order blocks and rejection blocks used as entries for the rest of the day.

## Formal Criteria

**The two windows**

| Market | Symbol | Opening range | Highest-volume sub-window | Cash session |
|---|---|---|---|---|
| **30-year Treasury bond** | ZB | **08:00 → 09:00 NY** | 08:00 → 09:30 NY | 08:20 → 15:00 NY |
| **E-mini S&P / NASDAQ / Dow** | ES / NQ / YM | **09:30 → 10:30 NY** | 09:30 → 10:00 NY | 09:30 → 16:00 NY ("true day") |

- The opening range **is a high and a low** — nothing else (`ICT-2017-BOND-OPENING-RANGE`, 04:13).
- The index range is explicitly **one hour**, "a 60-minute opening range from 9:30 in the morning
  to 10:30 in the morning New York time", with the **first 30 minutes** carrying the volume spike
  (11:09, 02:35). The same 09:30–10:30 window is stated for **all three indices** (07:17, 08:29).

**How the range is drawn** (`ICT-2017-BOND-OPENING-RANGE`, 10:38–11:12)

- Same method as the Asian range: "I look for the **bodies**, but also **incorporate wicks**."
- Additionally **incorporate levels immediately to the left** of the window: an equal-high cluster
  formed just before 08:00 is folded into the range if a wick inside 08:00–09:00 reaches it.

**Range size as a filter**

- **Small opening range → expect expansion.** "If the opening range is **12 ticks or less**,
  generally you'll have an expansion move of some kind" — often just a run of the overnight high
  or low (`ICT-2017-BOND-CONSOLIDATION-DAYS`, 09:37–10:07).
- **Large / extended opening range → expect a return into it.** "When there's a large opening
  range, we want to start looking for **retracement ideas or fair value ideas** — bullish order
  blocks, fair value gaps to be a buyer or seller in" (`ICT-2017-BOND-SPLIT-SESSION`, 13:32). The
  index lesson states the same from the other side: with an extended range "we'll look for the
  high or the low to be **violated later in the day**" — the upper bound if bullish, the lower
  bound if bearish (`ICT-2017-INDEX-OPENING-RANGE`, 06:11–06:39).

**What the bounds are**

- Liquidity pools. The bond range "is also the location for **liquidity pools to build around for
  the stock market opening** to be raided" (04:06).
- A trade below the opening-range low, or above its high, is read as a **turtle soup / stop run**
  — "so a turtle soup right here below the opening range later in the morning" (06:51), and in the
  bond case a run of the low "is a stop run and a potential reversal" (05:07).
- On bonds the same event is named **three ways at once**: "it trades down, **creates the Judas
  swing, and it creates a turtle soup**, which is a move below the 154.02 level **in the opening
  range**… that **down-closed candle creates a bullish order block** at that 154.02 level"
  (`ICT-2017-BOND-SPLIT-SESSION`, 14:02–14:22). The opening-range violation, the session Judas,
  the turtle soup and the resulting order block are one price event under four labels.
- The bounds stay live **into the evening**: a bond opening-range high was run during the Asian
  session that night (11:17–11:26, and `ICT-2017-BOND-SPLIT-SESSION`, 16:20).

**What the interior is**

- The **last down-closed candle inside the range** is a bullish order block; the last up-closed
  candle is bearish (`ICT-2017-BOND-OPENING-RANGE`, 06:57–07:05, 08:44–09:04). Multiple test
  points on the same block are acceptable — "either one would fit the bill" (09:00).
- On the indices the same interior yields **rejection blocks** as well as order blocks
  (`ICT-2017-INDEX-OPENING-RANGE`, 07:49, 09:02).

**Volume precedes price** (the confirmation layer, futures only)

- "Volume precedes price" (`ICT-2017-BOND-OPENING-RANGE`, 08:03; restated
  `ICT-2017-INDEX-OPENING-RANGE`, 09:43).
- A new low or new high made **on lower volume than the opening-range extreme** is a **volume
  divergence**: "that lower low should have been met with a higher bar on volume… this is a sign
  of impending weakness for the down move" (06:00–06:12). The move is read as a stop run, not
  fresh participation.

**Signal timing (bonds)**

- "I like to see signals form at **8:20 or after**. They can occur as early as 8 a.m.… but I
  generally prefer to see it occur between 8 a.m. and 8:30. So basically the **target time is
  8:20, or CME opening**" (11:45–12:04).

## Formula / Math

```
# --- windows (New York time) ---
OR_window(ZB)          := [08:00, 09:00]
OR_window(ES|NQ|YM)    := [09:30, 10:30]
volume_peak(ZB)        := [08:00, 09:30]
volume_peak(ES|NQ|YM)  := [09:30, 10:00]

OR_high := max(high) over OR_window          # bodies first, wicks included,
OR_low  := min(low)  over OR_window          # plus adjacent levels just left of the window

OR_size := OR_high - OR_low

# --- size filter (bonds, ticks; 1 tick = $31.25) ---
if OR_size <= 12 ticks:  expect EXPANSION (often a run of the overnight high/low)
else:                    expect RETRACEMENT into the range -> OB / FVG entry
                         and a later violation of the opposite bound

# --- interior arrays ---
bullish_OB := last down-closed candle inside OR_window
bearish_OB := last up-closed candle inside OR_window

# --- bound events ---
trade_below(OR_low)  := turtle soup / stop run  (potential reversal)
trade_above(OR_high) := turtle soup / stop run  (potential reversal)

# --- volume divergence (futures only) ---
divergence := new_extreme(t) is made AND volume(t) < volume(OR_extreme)
              => move is a stop run, not participation      # "volume precedes price"

# --- tick values ---
ZB : 1 tick = $31.25 ; 32 ticks = 1 handle = $1,000/contract
ES : 1 tick = $12.50 ; 4 ticks = 1 point = $50/contract
```

## Machine-Readable

```json
{
  "id": "futures-opening-range",
  "category": "15-sessions",
  "aliases": ["opening-range", "bond-opening-range", "index-opening-range", "spooz-opening-range"],
  "criteria": [
    {"id": "c1", "expr": "OR_window(ZB) == [08:00,09:00] NY; OR_window(ES|NQ|YM) == [09:30,10:30] NY"},
    {"id": "c2", "expr": "OR := {max(high), min(low)} over window; bodies first, wicks included, plus adjacent left-of-window levels"},
    {"id": "c3", "expr": "OR tends to contain the day's high or low"},
    {"id": "c4", "expr": "bound event is either a stop run or a fair-value (PD array) setup"},
    {"id": "c5", "expr": "OR_size <= 12 ticks (ZB) => expect expansion"},
    {"id": "c6", "expr": "large/extended OR => expect retracement into OR and later violation of the opposite bound"},
    {"id": "c7", "expr": "interior last down-closed candle == bullish OB; last up-closed candle == bearish OB"},
    {"id": "c8", "expr": "OR bounds act as liquidity pools, live into the Asian session"},
    {"id": "c9", "expr": "new extreme on lower volume than the OR extreme == volume divergence => stop run"},
    {"id": "c10", "expr": "bond signal target time == 08:20 NY (CME open), acceptable 08:00-08:30"},
    {"id": "c11", "expr": "an OR-low violation is simultaneously the session Judas swing, a turtle soup, and the origin of a bullish order block"}
  ],
  "timeframes": ["M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["bond-split-session-rules", "index-am-pm-trend", "asia-session", "ny-am-session", "ny-am-open-range-model", "turtle-soup", "bullish-order-block", "rejection-block", "liquidity-pool", "smart-money-footprint"],
  "sources": ["ICT-2017-BOND-OPENING-RANGE", "ICT-2017-INDEX-OPENING-RANGE", "ICT-2017-BOND-CONSOLIDATION-DAYS", "ICT-2017-BOND-SPLIT-SESSION"]
}
```

## Visual Pattern

```
   BONDS (ZB)                          INDICES (ES / NQ / YM)
   08:00 ──────── 09:00                09:30 ──────── 10:30
   ┌───────────────┐                   ┌───────────────┐
   │  OPENING      │ OR_high ══════    │  OPENING      │ OR_high ══════
   │  RANGE        │                   │  RANGE        │
   │   ▪ last down-closed candle       │   ▪ last up-closed candle
   │     = bullish OB                  │     = bearish OB / rejection block
   └───────────────┘ OR_low  ══════    └───────────────┘ OR_low  ══════
   ███ highest volume 08:00-09:30      ███ highest volume 09:30-10:00

   ─────────────────────────────────────────────────────────────
   THE TWO OUTCOMES AT A BOUND

     RUN ON STOPS                      FAIR VALUE SETUP
     ══════ OR_low                     ══════ OR_low
        ╲                                 ╲__ ▪ OB / FVG inside the range
         ╲__╱‾‾‾  reversal                     ╲__╱‾‾‾  rally
     volume LOWER than the OR         entry taken at the array
     extreme  ->  divergence

   ─────────────────────────────────────────────────────────────
   SIZE FILTER (bonds)
     OR <= 12 ticks  ->  coiled; expect expansion
     OR large        ->  expect retracement INTO the range,
                         then the opposite bound violated later
```

## Timeframes

Both lessons are worked on **15-minute** charts; the index lesson also uses **5-minute** for the
interior arrays. The opening range is a single-day construct — there is no higher-timeframe form.

## Examples

**Example 1 — ZB September 2017, 15-minute (`ICT-2017-BOND-OPENING-RANGE`, 04:19–06:33):**
- Setup: 08:00–09:00 opening range delineated; highest volume of the day inside it.
- Trigger: price traded **below** the opening-range low after 09:00 — a stop run.
- Confirmation: the lower low printed on **lower volume** than the 08:00–09:00 bars — a volume
  divergence, "a sign of impending weakness for the down move".
- Outcome: price reversed, found support back at the opening range, and traded higher into the
  latter part of the day.

**Example 2 — ZB, order block inside the range (07:01–07:24):**
- Setup: last two down-closed candles inside the 08:00–09:00 range marked as a bullish order block.
- Trigger: price traded down into the block.
- Outcome: rallied away; the subsequent higher high at **154.21** came on **declining** volume, and
  price fell back into the opening range and consolidated.

**Example 3 — ZB, both bounds worked (08:32–10:10):**
- Price ran **above** the opening-range high into **154.26** on light volume with a volume
  divergence, failed to extend, and traded back down to close a fair value gap at **154.10**.

**Example 4 — ES September 2017, 5-minute (`ICT-2017-INDEX-OPENING-RANGE`, 05:59–07:00):**
- Setup: an **extended** 09:30–10:30 opening range, not a small one.
- Trigger: a **turtle soup below the opening-range low** later in the morning.
- Outcome: rally all the way back to the **opening-range high** to run the stops resting there.

**Example 5 — YM (Dow mini), rejection block (08:29–10:42):**
- Setup: the low of the day formed inside the opening range on the highest green volume bar.
- Trigger: a second attempt below **21,265** printed on a **red, lower** volume bar.
- Outcome: insufficient volume; the rejection block held and price closed higher on the day.

## Common Mistakes

- **Using one clock for both markets.** Bonds are 08:00–09:00; indices are 09:30–10:30. The clock
  is set by each market's own volume peak, not by a shared "NY open".
- **Reading the bounds as breakout levels.** A trade through a bound is treated as a **stop run**
  first; the reversal is the expectation, not the continuation.
- **Bodies only.** ICT includes wicks *and* pulls in equal highs/lows immediately left of the
  window — the range is deliberately not a pure body range.
- **Skipping volume.** The divergence check is what separates a genuine extension from a raid, and
  it only exists because these are **futures with real volume** — it does not transfer to spot FX.
- **Ignoring a 12-tick bond range.** A small opening range is the coiled-spring condition, not a
  reason to stand down.
- **Assuming the range dies at the close.** Its bounds were still being run in the Asian session
  that night.

## Related Concepts

- [bond-split-session-rules](bond-split-session-rules.md) — the AM/PM structure the bond opening range sits at the front of.
- [index-am-pm-trend](index-am-pm-trend.md) — the index AM trend that begins at the same 09:30 open.
- [asia-session](asia-session.md) — the Asian range, whose bodies-plus-wicks drawing method ICT explicitly reuses here.
- [ny-am-session](ny-am-session.md) — the FX-side session this overlaps.
- [ny-am-open-range-model](../31-models/ny-am-open-range-model.md) — the 2022 FX-side opening-range model; same idea, different instrument.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — what a trade through a bound is called.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [rejection-block](../19-rejection-blocks/rejection-block.md) — the interior arrays.
- [liquidity-pool](../02-liquidity/liquidity-pool.md) — what the bounds are.
- [smart-money-footprint](../03-order-flow/smart-money-footprint.md) — volume divergence as a footprint.

## Citations

- `ICT-2017-BOND-OPENING-RANGE` (00:23) "June 2017 ICT Mentorship, **ICT Bond Trading Lesson 1, Basics and Opening Range Concept**" — self-dates the lecture; (00:46–01:01) the 30-year Treasury bond futures contract, symbol **ZB**; (01:01–01:16) "the trading session… begins at **8:20 a.m. to 3 p.m. New York time**"; (02:41–03:01) "the amount per tick minimum fluctuation is **$31.25 per contract**… a full handle or full figure move equals **32 ticks**… **$1,000 per contract**"; (03:16–03:29) "the highest volume is going to be seen between **8 a.m. and 9:30 a.m.** New York time"; (03:29–03:46) "the opening range begins at **8 a.m.** New York time and ends **9 a.m.** New York time"; (03:47–04:13) "the opening range between 8 a.m. and 9 a.m. **tends to create the bond market high or low of the day. It can be a run on stops or a fair value setup**… it is also the location for **liquidity pools to build around for the stock market opening** to be raided. The opening range is a high and low"; (05:07–05:19) "price trades down below the low that was formed between 8 a.m. and 9 a.m. This is a **stop run and a potential reversal**"; (06:00–06:12) "this is a **volume divergence**. Price making a lower low. That lower low should have been met with a higher bar on volume. This is a sign of impending weakness for the down move"; (06:57–07:24) the last two down-closed candles inside the opening range as a bullish order block; (07:30–08:12) the higher high at 154.21 on declining volume — "**therefore, volume precedes price**"; (08:44–09:04) "inside the opening range, the last down closed candle is a bullish order block… **either one would fit the bill**"; (09:52–10:10) the run above the opening-range high at 154.26 on a volume divergence, then the trade back into the fair value gap at 154.10; (10:38–11:12) "I like to define the opening range… much like I did the **Asian range**. I look for the **bodies**, but also **incorporate wicks**, and then I also incorporate those that are just **to the left** of 8 to 9 a.m. New York time"; (11:17–11:26) the same reference point "becomes an issue for stop raiding later on in the evening during the Asian session time period"; (11:45–12:04) "I like to see signals form at **8:20 or after**… generally I prefer to see it occur between 8 a.m. and 8:30. So basically the **target time is 8:20, or CME opening**"; (12:37–12:40) "one of the wonderful things about the bond market — **it's the least manipulated of all markets**"; (15:13–15:25) "if you can capture anywhere between **five to eight ticks** as the intraday day trade, there's certainly nothing wrong with that".
- `ICT-2017-INDEX-OPENING-RANGE` (00:25) "**June 2017, ICT mentorship, ICT index trading, concepts lesson one, basics and opening range concept**" — self-dates the lecture; (00:57–01:14) the e-mini S&P, symbol **ES**, "keying in on the **9:30 a.m. to 4 p.m.** New York time"; (01:41–01:53) "the amount per tick is **$12.50**. One quarter of one point equals one tick… four ticks makes one point or **$50 per one point**"; (02:35–02:45) "the highest volume for S&P trading is going to be seen between **9:30 a.m. and 10 a.m.** New York time… only a 30-minute span"; (02:45–02:57) "**true day** for SPOOs is going to be viewed as **9:30 a.m. to 4 p.m.** New York time"; (03:07–03:26) "opening range is going to be seen with **9:30 a.m.** and ends at **10:30 a.m.**… so you have an opening range of **one hour**… which tends to create the SPOOs market high or low of the day. **It can be a run on stops or a fair value setup**"; (04:33–05:03) reference points inside the opening range used for a later short; (05:29–05:48) "inside the opening range, there is a return back to a **bullish order block, the last down-closed candle**"; (06:11–06:39) "notice it's an **extended range**… generally we'll look for the high or the low to be **violated later in the day**. If it's going to be a bullish day, we'll look for that upper end of the opening range to be violated"; (06:51–07:00) "so a **turtle soup** right here below the opening range later in the morning"; (07:17–07:31) the NASDAQ (NQ) — "the opening range is the same for this, it's **9:30 to 10:30** New York time"; (07:49–07:58) the rejection block formed by the last up-closed candle inside the range; (08:29–08:51) the Dow mini — same 09:30–10:30 opening range, "the first 30 minutes, 9:30 to 10 o'clock, has the largest volume of the day"; (09:02–10:42) the rejection-block example: the low of the day on the highest green volume bar, then a second attempt below 21,265 on a lower red volume bar — "**volume precedes price**… if we're going to be making a lower low or retesting an old low or old high, it should be seen with **higher volume**"; (11:09–11:23) "the full spectrum is a **60-minute opening range** from 9:30 to 10:30 New York time, but the **first 30 minutes** we're also going to build on".
- `ICT-2017-BOND-CONSOLIDATION-DAYS` (09:37–10:07) "if you look at an opening range of **12 ticks or less**… generally you'll have an **expansion move** of some kind, and it may just blow out a previous overnight high or low… that little bit of a squeeze, that **volatility squeeze**".
- `ICT-2017-BOND-SPLIT-SESSION` (14:02–14:22) "it trades down, **creates the Judas swing, and it creates a turtle soup**, which is a move below the 154.02 level **in the opening range**, 8 o'clock to 9 o'clock in the morning New York time. **That down-closed candle creates a bullish order block** at that 154.02 level"; (14:39–14:53) "so you have a bullish order block during the a.m. session **or** a turtle soup, **either or**"; (13:32–13:47) "during the a.m. session, price has a **large opening range**. So when there's a large opening range, we want to start looking for **retracement ideas or fair value ideas** — bullish order blocks, fair value gaps to be a buyer or seller in"; (16:20–16:30) a runner held to "run out the **opening range high at 154.21** later on in the evening during the Asian session".

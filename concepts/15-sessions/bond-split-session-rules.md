# Bond Split Session Rules

**Category:** 15-sessions
**Aliases:** T-bond split session, bond AM session, bond PM session, ZB session rules, treasury split session
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-BOND-SPLIT-SESSION, ICT-2017-BOND-OPENING-RANGE, ICT-2017-BOND-CONSOLIDATION-DAYS
**Tags:** sessions, bonds, futures, ny-am, ny-pm, london, time-of-day

## Definition

Split session rules are ICT's **time-of-day map for the 30-year Treasury bond (ZB)**: the
trading day is divided into an overnight reference window, an AM session and a PM session, each
carrying its own expectation. It is the bond-market counterpart to the FX session model, and ICT
states plainly that it deviates: "there's some similarities, but there's some **slight
deviations**… there's a small overlap, but then there's a small deviation from what we would
normally expect for time of day" (`ICT-2017-BOND-SPLIT-SESSION`, 01:21–01:41).

The purpose is **not** a bond trading system. The stated use is that the bond day, read this
way, tells a currency trader what the rest of the market is permitted to do — "you'll start to
see there's a **synergy** that takes place between the asset classes and how bonds influence
other markets" (16:56).

## Formal Criteria

**The three windows (New York time)**

| Window | Clock | Status | Expectation |
|---|---|---|---|
| **London reference** | **02:00 → 05:00** | **observe only, do not trade** | supplies overnight stops, liquidity voids, fair value gaps and any PD array |
| **AM session / morning trend** | **08:00 → 12:00** | primary | largest volume of the day; forms the session (and usually the day's) high or low |
| **PM session / afternoon trend** | **12:00 → 15:00** | secondary | continuation, reversal **or** consolidation |

- The **opening range** sits at the front of the AM session — see
  [futures-opening-range](futures-opening-range.md) for the 08:00–09:00 window.
- ICT's own working window inside the AM session was **08:20 → 11:00**: "that was like my
  **kill zone** if you want to call it that" (04:34–04:57).
- The AM session **can end early, around 11:00**, when London and European traders square up;
  volume drops but the day is not over (07:20–08:11).
- **New York lunch for bonds is 11:00 → 13:00** — wider than the FX-side definition (07:54).

**The London reference rule** (03:03–07:12)

- ZB *can* be traded overnight, but ICT counsels against it: "I would counsel you to **use the
  information** that is seen by overnight trading during the London session to look for stops,
  liquidity voids, fair value gaps… and **focus primarily on trading the New York session**."
- The reference is bracketed strictly: "we refer to it **always between these two reference
  points, 2 o'clock in the morning and 5 a.m.**"

**Why the AM session is privileged** (04:00–04:18)

- "The AM session has a **built-in advantage** because it generally will see the **largest volume
  of the day**. That means it's generally going to form the high or low of the New York session
  or… total range of the true day for treasury bonds."

**Day shapes** (05:11–06:20)

- **Trending day:** one-sided through **both** sessions — e.g. the 08:00–08:20 open makes the low
  of the day and price runs to 15:00. "Those sessions together create the full daily range."
- **Trending day starting late:** the AM consolidates and the PM trends (e.g. an afternoon FOMC),
  producing a **runner** that carries into the next session or the one after.
- **Consolidation day:** the two sessions run in **opposing directions**, or one produces a swing
  and the other is quiet.

**The PM abbreviation rule** (08:47–09:24)

- "Whatever usually happens in the morning session generally is seen in **quicker terms or in less
  time** in the PM session."
- "If there's a large degree of the average daily range seen in the AM session, that means the PM
  session will be rather **abbreviated**."
- Consequent: if the AM has delivered the day's range and you are flat before lunch, **skip the PM
  session** — "don't come back for the second portion."

**Contract and tick arithmetic** (`ICT-2017-BOND-OPENING-RANGE`, 00:46–03:01)

- Symbol format **ZB + month code + two-digit year** (e.g. `ZBU17`); delivery months **March (H),
  June (M), September (U), December (Z)**; Chicago Board of Trade.
- **1 tick = $31.25.** **32 ticks = 1 handle = $1,000 per contract.**
- Realistic intraday expectation: **5–8 ticks**; **16 ticks = $500** is "a good day"; a full
  32-tick handle is a large-range day and "not the normal" (15:13–15:45).

## Formula / Math

```
# --- windows (New York time) ---
london_reference := [02:00, 05:00]     # observe only; source of overnight PD arrays
bond_AM          := [08:00, 12:00]     # may terminate early at 11:00
bond_PM          := [12:00, 15:00]
bond_lunch       := [11:00, 13:00]
ict_working_hours:= [08:20, 11:00]

# --- day classification ---
trending_day     := sign(AM_move) == sign(PM_move)          # full daily range spans both
late_trending_day:= AM == consolidation AND PM == trend      # produces a runner
consolidation_day:= sign(AM_move) != sign(PM_move)
                    OR exactly one session produces a swing

# --- PM participation gate ---
adr_consumed_AM := (AM_range / average_daily_range) is large
if adr_consumed_AM and flat_before_lunch:  skip PM

# --- tick arithmetic (ZB) ---
tick        = $31.25
handle      = 32 ticks = $1,000 / contract
typical_day = 5..8 ticks
good_day    = 16 ticks = $500 / contract
```

## Machine-Readable

```json
{
  "id": "bond-split-session-rules",
  "category": "15-sessions",
  "aliases": ["t-bond-split-session", "bond-am-session", "bond-pm-session", "zb-session-rules"],
  "criteria": [
    {"id": "c1", "expr": "london_reference == [02:00,05:00] NY, observe only"},
    {"id": "c2", "expr": "bond_AM == [08:00,12:00] NY, may end early at 11:00"},
    {"id": "c3", "expr": "bond_PM == [12:00,15:00] NY"},
    {"id": "c4", "expr": "bond_lunch == [11:00,13:00] NY"},
    {"id": "c5", "expr": "AM session carries the largest volume and usually forms the day's high or low"},
    {"id": "c6", "expr": "PM session := continuation OR reversal OR consolidation"},
    {"id": "c7", "expr": "trending_day := both sessions one-sided; consolidation_day := opposing sessions"},
    {"id": "c8", "expr": "PM move completes in less time than the AM move"},
    {"id": "c9", "expr": "large AM share of ADR => abbreviated PM => skip PM if already flat"},
    {"id": "c10", "expr": "ZB tick == $31.25; 32 ticks == 1 handle == $1000/contract"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["futures-opening-range", "index-am-pm-trend", "bond-trending-and-consolidation-days", "london-session", "ny-am-session", "ny-pm-session", "ny-lunch", "power-of-three", "interest-rate-triad", "multi-asset-analysis"],
  "sources": ["ICT-2017-BOND-SPLIT-SESSION", "ICT-2017-BOND-OPENING-RANGE", "ICT-2017-BOND-CONSOLIDATION-DAYS"]
}
```

## Visual Pattern

```
   THE BOND TRADING DAY (New York time)

   02:00 ── 05:00        08:00 ──────── 12:00 ──────── 15:00
   ┌──────────┐          ┌──────────────┬──────────────┐
   │ LONDON   │          │  AM SESSION  │  PM SESSION  │
   │ REFERENCE│          │ morning trend│ afternoon    │
   │ observe  │          │              │ trend        │
   │ only     │          │ ███ 08:00-09:00 opening range
   └──────────┘          └──────────────┴──────────────┘
   stops · voids · FVGs   largest volume    continuation /
                          forms HOD/LOD     reversal /
                                            consolidation
                          ▲ 08:20 CME open
                          └── ICT's working window 08:20-11:00
                                   ▲ AM may end here (11:00, London close)
                                   └── bond lunch 11:00-13:00

   ─────────────────────────────────────────────────────────
   DAY SHAPES

   TRENDING          ╱‾‾‾‾‾‾‾‾‾‾‾‾   AM and PM one-sided
                     └ full daily range spans both sessions

   LATE TRENDING     ▪▪▪▪▪╱‾‾‾‾‾    AM consolidates, PM trends
                              └ runner into the next session

   CONSOLIDATION     ╱‾‾╲__          AM up, PM down (or one quiet)
```

## Timeframes

Worked on **15-minute** charts. The split-session map is a single-day construct; the higher
timeframe input (which premium or discount array the day is starting from) comes from the daily,
four-hour and two-hour charts.

## Examples

**Example 1 — trending bullish day, power of three (`ICT-2017-BOND-SPLIT-SESSION`, 09:38–11:19):**
- London reference 02:00–05:00: a London-open move, a fair value gap closed, then a sell-off.
- AM session: price ran the **opening-range low** at the equities open — the Judas swing — then
  rallied into the 11:00 hour where European traders squared and price retraced into noon.
- PM session: rallied again, made the **high of the day ahead of 14:00**, then retraced and went
  into consolidation at 15:00.
- ICT's label: "traditional **power three** just defined in terms of the split session rules for
  bonds."

**Example 2 — AM up, PM down (11:24–12:32):**
- AM: price took out the London-session low, formed a **failure swing**, moved into a bullish
  order block at **153.29** and expanded higher through the whole morning trend.
- Noon: a market reversal profile formed.
- PM: reversed lower — "both offering opportunities, one for a buy and one for a sell."
- After 15:00 price consolidated, matching the FX "true day" shape.

**Example 3 — both sessions paid, with numbers (12:40–16:30):**
- 07:00 NY: price rallied and cleared equal highs around **154.19**; then swept the London high
  and blew out the London low between 08:00 and 09:00, making the low of the day at 09:00.
- The move below **154.02** inside the opening range is named as three things at once:
  "it trades down, **creates the Judas swing, and it creates a turtle soup**, which is a move
  below the 154.02 level **in the opening range**… that **down-closed candle creates a bullish
  order block** at that 154.02 level" (14:02–14:22). This is the corpus's clearest single
  sentence tying the opening range, the Judas swing, the turtle soup and the order block to one
  event — and it is stated on **bonds**, not FX.
- The two entries are offered as **alternatives, not a sequence**: "you have a bullish order block
  during the a.m. session **or** a turtle soup, **either or**" (14:39–14:53).
- AM trade: fill of the fair value gap 154.03 → 154.02 ahead of the 10:00 hour, rally to
  **154.10** — "an **8 tick move**, 8 times $31.25 per contract."
- PM trade: 154.02 → **154.13** (the fair value gap close) — "an **11 tick move** for the PM
  session"; a runner could then reach the opening-range high at **154.21** in the Asian session.

## Common Mistakes

- **Importing the FX clock.** The FX day-trade window and the bond day are not the same. Bonds:
  AM 08:00–12:00, PM 12:00–15:00, lunch 11:00–13:00. ICT flags the deviation explicitly.
- **Trading the London session in bonds.** It is a **reference** window (02:00–05:00), used for
  locating stops and PD arrays — not an execution window.
- **Treating noon as a hard AM boundary.** The AM session frequently finishes at 11:00 with the
  London close.
- **Trading the PM after a full AM range.** The PM is abbreviated in proportion to how much of the
  daily range the AM already delivered.
- **Expecting FX-sized moves.** 5–8 ticks is the stated intraday expectation; 32 ticks is a
  large-range day, "not the normal".
- **Reading this as a bond trading system.** ICT's stated purpose is intermarket context for FX —
  see [multi-asset-analysis](../03-order-flow/multi-asset-analysis.md).

## Related Concepts

- [futures-opening-range](futures-opening-range.md) — the 08:00–09:00 block at the front of the AM session.
- [index-am-pm-trend](index-am-pm-trend.md) — the same split applied to index futures, on a different clock.
- [bond-trending-and-consolidation-days](../31-models/bond-trending-and-consolidation-days.md) — how to tell in advance which day shape is coming.
- [london-session](london-session.md) — the session the 02:00–05:00 reference window sits inside.
- [ny-am-session](ny-am-session.md), [ny-pm-session](ny-pm-session.md), [ny-lunch](ny-lunch.md) — the FX-side definitions this deviates from.
- [power-of-three](../12-power-of-three/power-of-three.md) — the shape ICT names on the trending example.
- [interest-rate-triad](../03-order-flow/interest-rate-triad.md) — what to compare the ZB read against.
- [multi-asset-analysis](../03-order-flow/multi-asset-analysis.md) — why a currency trader watches this at all.

## Citations

- `ICT-2017-BOND-SPLIT-SESSION` (00:23) "**June 2017, ICT mentorship, ICT bond trading, lesson number two, split session rules**" — self-dates the lecture; (01:13–01:41) "I'm going to teach you the way I interpret price action for my analysis for the bond market. There's some similarities, but there's some **slight deviations**"; (01:53–02:08) "**New York AM session is defined by 8 a.m. New York time to noon** New York time. **New York PM session is defined by noon New York time to 3 p.m.** New York time"; (03:03–03:36) "you **can** trade overnight or during a London session the ZB… I would counsel you to **use the information** that is seen by overnight trading during the London session to look for stops, liquidity voids, fair value gaps… and **focus primarily on trading the New York session**"; (03:36–04:00) "the largest volume is seen between 8 o'clock and 9 o'clock in the morning or generally **before the equities open**"; (04:00–04:18) "the AM session has a **built-in advantage** because it generally will see the **largest volume of the day**… it's generally going to form the high or low of the New York session or… total range of the true day for treasury bonds"; (04:18–04:28) "the **PM session generally will have a continuation or reversal**… and then the other thing is a **consolidation**"; (04:34–04:57) "I tried to focus… primarily on **8:20 in the morning to 11 o'clock in the morning**. That was like my **kill zone** if you want to call it that"; (05:05–05:11) "for the PM session for the treasury bond market, it's seen here as **noon to 3 p.m.**"; (05:11–05:35) "**trending days can see the complete trading day be one-sided in both the AM and PM sessions**… those sessions together create the full daily range"; (05:36–06:10) trending days can also begin with the PM session (an afternoon FOMC), "that carries over in what we call a **runner**"; (06:07–06:20) "**consolidation days can see opposing directions in the AM and PM sessions**, or it can see one session produce a swing and the other be quiet or consolidate"; (06:29–07:12) "when we look at **2 o'clock in the morning to 5 a.m.**, we understand that is the traditional London session… any measure of PD array that we would normally use in the foreign exchange market, we would look for that to be found in this specific reference point in time… we refer to it **always between these two reference points, 2 o'clock in the morning and 5 a.m.**"; (07:12–07:29) "the AM session, or **morning trend**, is defined by **8 a.m. to noon**. Now, sometimes the 8 a.m. to noon session can **end early, around 11 a.m.**, which is the traditional London closed time period"; (07:54–08:11) "we're also encountering what is referred to as **New York lunch, around 11 o'clock to 1 o'clock in the afternoon**… just know that it can end earlier around 11 o'clock"; (08:15–08:34) "the next portion of the daily range for bond trading is the **New York PM session**… delineating **12 noon New York time to 3 p.m.** New York time"; (08:34–08:57) "if you have a **runner**… you can see follow-through, equal distant measured moves… whatever usually happens in the morning session generally is seen in **quicker terms or in less time** in the PM session"; (08:57–09:24) "if there's a large degree of the average daily range seen in the AM session, that means the PM session will be rather **abbreviated**… we could **avoid trading the PM session altogether**. Don't come back for the second portion"; (09:38–11:19) the trending-day worked example ending "**traditional power three** just defined in terms of the split session rules for bonds"; (11:24–12:32) the AM-up/PM-down reversal example with the bullish order block at 153.29; (12:40–16:30) the 154.02 turtle-soup/order-block example, the "**8 tick move, 8 times $31.25 per contract**" AM trade and the "**11 tick move for the PM session**"; (16:43–17:12) "we're also including everything we've learned in terms of PD arrays, institutional order flow, and other time of day studies as it overlaps with Forex… you'll start to see there's a **synergy** that takes place between the asset classes and how bonds influence other markets".
- `ICT-2017-BOND-OPENING-RANGE` (00:46–02:10) the ZB contract, delivery months **March (H), June (M), September (U), December (Z)**, the `ZB + month code + year` symbol format, Chicago Board of Trade; (01:01–01:16) "the trading session… begins at **8:20 a.m. to 3 p.m. New York time**"; (02:41–03:01) "**$31.25 per contract**… a full handle or full figure move equals **32 ticks**… **$1,000 per contract**"; (15:13–15:45) "if you can capture anywhere between **five to eight ticks** as the intraday day trade, there's certainly nothing wrong with that. If you can get **16** … that's **five hundred dollars per contract**… a large range day is when you get a **full handle or 32 ticks or one thousand dollars per contract**. They don't happen all the time… that's **not the normal**".
- `ICT-2017-BOND-CONSOLIDATION-DAYS` (10:55–11:12) "when we're consolidating or we're anticipating small ranges, **do your trading in the AM session before noon**"; (16:31–17:21) "unless PM session news drivers are due out, consolidation days typically offer setups in the AM session most of the time… all of your trading has to be done, **preferably before 11 o'clock a.m. New York time**".

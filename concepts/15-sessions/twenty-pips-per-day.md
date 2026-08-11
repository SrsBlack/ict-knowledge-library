# 20 Pips Per Day

**Category:** 15-sessions
**Aliases:** 20 pips a day, ICT 20-pip scalp, Asian session stop raid, New York expansion scalp
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-20-PIPS
**Tags:** sessions, scalping, asian-session, ny-session, turtle-soup, fixed-target, adr

## Definition

"20 Pips Per Day" is a pair of **fixed-risk, fixed-target scalps** from the May-2017 scalping
month — one anchored to the Asian session, one to the New York session. Both are
[turtle-soup](../20-turtle-soup/turtle-soup.md) raids on a short-term level; both are timed off
a **five-minute chart**; both use **20 pips stop and 20 pips target**, and neither is allowed to
run: "we are **not graduating it** … it's straight 20 for 20 — 20 stops, 20 target, that's it"
(04:48–05:03).

ICT opens by disclaiming the title: "**you will not make 20 pips every day, period** — I can't
promise you that, no one can promise you that" (00:33–00:45), and the working claim is weaker
still: "there are a few techniques one can use to ferret out a 20-pip scalp **almost** every day
— again, the emphasis there is **almost**" (01:43–01:54).

## Formal Criteria

### Pattern A — Asian session stop raid (20:00 → 00:00 NY)

- **Instruments:** "this pattern is good for **yen, Aussie and Kiwi crosses**" (02:39–02:47).
- **Window:** the Asian session **up to 00:00 New York**; "all we're doing is looking for an
  opportunity to trade between **8 o'clock and midnight** New York time" (11:17–11:33).
- **The level:** a short-term high or low formed in the **late New York session**, just before
  Asia begins — "that short-term high is going to have a **very small pocket of stops** resting
  above it, and it's delineated here by **late New York stops**" (05:03–05:28).
- **Sell setup:** Asia probes **above** that short-term high → sell. **Buy setup:** Asia probes
  **below** the short-term low → buy (02:47–04:48).
- **Entry offset:** "how many pips above it, Michael? I don't know. **Five. Five is a good
  number** … preferably I like **five pips above** the short-term highs. If I can get that, then
  great; if I can't get it, then I miss it, it's fine" (09:04–09:17).
- **Why it works, in ICT's reading:** the probe is "a very, very **low-volume liquidity run**"
  that is *itself* the Asian range extreme being priced in — "we're **interpreting the Asian
  range high forming** when we take a move above that short-term high … once that's taken out
  they fade that and take it the other way down, making the **Asian range low**" (05:35–06:59).
- **Compatible with a bullish day:** selling the Asian-range high is not a counter-trend trade,
  it *is* the setup for the day's protraction — "if we're bullish we can see the selling above a
  short-term high like this. Many times they actually work out better, because what you're doing
  is you're **pricing in the Asian range high** — and what do we look for for upside movement?
  **That Judas swing down**" (10:15–10:40).
- Scope: "many times the Asian range is a lot larger than 20, 30, 40 pips, but many times it's
  at least enough to get 20 pips out of it" (06:59–07:09).

### Pattern B — New York expansion (up to 10:00 NY)

- **Instruments:** all of them — "this is a pattern that's good for **all pairs** … it's a
  **universal application**" (11:41–11:52). Also named for **ES, Dow futures, the Qs** and
  stocks (17:35–17:56).
- **Window:** the New York session **up to 10:00 New York** (11:52–12:01).
- **Two preconditions, both required:**
  1. **London already posted the day's extreme** — the low, for the buy setup; the high, for
     the sell setup (12:01–12:16).
  2. **The five-day average daily range is still pending** — "the five-day average daily range
     has **not been filled** for the day" (12:01–12:09), restated for the sell side as "average
     daily range for the last five days … **has not been met yet** — that's the condition we're
     looking to trade in" (13:20–13:31).
- **Trigger:** the New York retracement takes out a **five-minute short-term low** (buys) or
  **high** (sells) — "we buy long below that short-term low **in the mindset that it's a turtle
  soup**; it's coming back for short-term sell stops, and we're going to be looking for
  expansion going towards the five-day average daily range" (12:24–12:39).
- **What the raid is for:** "they're trying to **entice short sellers and breakout artists**,
  and also knock out those individuals that are already long that would stand to profit by the
  next leg up" (17:02–17:25).
- **Multiple setups per day are allowed** on this pattern, because the trigger is a five-minute
  level: "you can get **multiple setups** … there's a lot of potential for it to come back down
  below short-term lows if it's going to be a rather choppy day with an expansion later in the
  afternoon" (15:32–16:05).

### Shared

- **Timing chart: M5.** Target **20 pips**, stop **20 pips**, both fixed, on both patterns.
- **Confluence is optional but named:** the Aussie example lands on "a five-minute **fair value
  gap** back down into an **order block** as well" (14:02–14:11).
- **The 20 pips is a floor, not a ceiling, on the move** — the examples "go sometimes many pips
  beyond 20 pips", and the blue boxes in the lesson only mark what 20 looks like (06:10–06:17).
  The *trade* still exits at 20.

## Formula / Math

```
# ---- Pattern A: Asian session stop raid (yen / AUD / NZD crosses) ----
window_A   := [20:00, 24:00] New York
level_hi   := short-term high formed in LATE New York, before 20:00
level_lo   := short-term low  formed in LATE New York, before 20:00

sell_A := price trades above level_hi within window_A
          entry  := level_hi + ~5 pips
          stop   := entry + 20 pips
          target := entry - 20 pips
buy_A  := mirrored on level_lo

# ---- Pattern B: New York expansion (all pairs, ES/YM/NQ, stocks) ----
window_B := New York session up to 10:00 New York
ADR5     := mean(range(D-1 .. D-5))

buy_B  requires  london_posted_day_low  AND  range_so_far(D) < ADR5
         trigger := break below a M5 short-term low during the NY retracement
         entry   := below that low
         stop    := entry - 20 pips
         target  := entry + 20 pips        # the expansion itself aims at ADR5
sell_B requires  london_posted_day_high AND  range_so_far(D) < ADR5
         # mirrored

# both patterns: timing chart == M5; risk:reward == 1:1, fixed, never trailed
```

## Machine-Readable

```json
{
  "id": "twenty-pips-per-day",
  "category": "15-sessions",
  "aliases": ["20-pips-a-day", "asian-session-stop-raid", "new-york-expansion-scalp"],
  "criteria": [
    {"id": "c1", "expr": "timing_chart == M5 for both patterns"},
    {"id": "c2", "expr": "target == 20 pips AND stop == 20 pips, fixed, never trailed"},
    {"id": "c3", "expr": "A: window == [20:00, 24:00] America/New_York"},
    {"id": "c4", "expr": "A: instruments == JPY, AUD, NZD crosses"},
    {"id": "c5", "expr": "A: level == short-term high/low formed in LATE New York before Asia"},
    {"id": "c6", "expr": "A: entry offset ~5 pips beyond the level"},
    {"id": "c7", "expr": "A: the probe IS the asian range extreme being priced in"},
    {"id": "c8", "expr": "B: window == New York session up to 10:00 America/New_York"},
    {"id": "c9", "expr": "B: requires london already posted the day extreme"},
    {"id": "c10", "expr": "B: requires range_so_far(D) < ADR5 (five-day ADR still pending)"},
    {"id": "c11", "expr": "B: trigger == M5 short-term low/high taken out on the NY retracement"},
    {"id": "c12", "expr": "B: universal across pairs, ES, YM, NQ and stocks"},
    {"id": "c13", "expr": "both patterns are turtle soup raids"},
    {"id": "c14", "expr": "NOT a daily income claim; 'almost every day', across 10-15 pairs"}
  ],
  "timeframes": ["M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["asian-range", "asian-range-high", "asian-range-low", "asia-session", "ny-am-session", "turtle-soup", "bullish-turtle-soup", "bearish-turtle-soup", "stop-hunt-pattern", "judas-swing", "ict-day-trading-model", "order-flow-subordination", "day-trade-routine"],
  "sources": ["ICT-2017-20-PIPS"]
}
```

## Visual Pattern

```
  PATTERN A — Asian session stop raid (sell side shown)

     late NY          |            ASIAN SESSION 20:00 - 00:00 NY
                      |
        ╱╲  ◄ short-term high, small pocket of stops above
       ╱  ╲           |        ╱▲╲  ◄ probe +5 pips = ENTRY (sell)
      ╱    ╲__________|_______╱   ╲
                      |            ╲___     ── 20 pips ──► TARGET
                      |                ╲___     (and this becomes
                    20:00                        the Asian range low)

  PATTERN B — New York expansion (buy side shown)

    LONDON            |  NY OPEN ── up to 10:00 NY
      ╲               |     ╱╲
       ╲             ╱|    ╱  ╲   ◄ retracement
        ╲__●________╱ |   ╱    ╲
        LOW OF DAY    |  ╱      ╲__●  ◄ M5 short-term low taken out = ENTRY
        (London made  |               ── 20 pips ──►
         it, and ADR5 |               expansion aims at the ADR5 bound
         is unfilled) |
```

## Timeframes

**M5** for both triggers; the short-term levels themselves are read off the same chart. Neither
pattern uses anything above M15 except the ADR5 gate on Pattern B.

## Examples

**Example 1 — USDJPY, Pattern A (07:09–07:57):**
- Setup: a short-term high from late New York, with stops above it.
- Trigger: during the Asian session price trades above that high — "between 8 o'clock at night
  New York time we see a small little rally up, **they fade that**, and price trades down".
- Outcome: 20 pips banked before midnight. ICT notes a **fair value gap** far to the left "is
  what ultimately price was reaching down for", so the move continued well past the target —
  which is the point of the fixed exit, not an argument against it.

**Example 2 — AUDUSD, Pattern B, live-session call (13:41–14:33):**
- Setup: London made the day's low; price expanded, then retraced into New York; ADR5 unfilled.
- Trigger: a five-minute short-term low violated, landing in "a five-minute **fair value gap**
  back down into an **order block** as well".
- Outcome: "price expands 20 pips — well beyond 20 pips actually". ICT ties it to a prior call:
  "this is actually the reason why I expected that Aussie dollar to trade up and make a **higher
  high** during the live session on New York this past Friday … **this was the actual pattern I
  saw**."

**Example 3 — USDCAD, two setups in one day (15:32–16:51):**
- Setup: London low formed after an early-Frankfurt high was taken; price rallied, was violated
  at the New York open, then traded back below a five-minute short-term low.
- Trigger: the first raid pays 20 pips; a **second** five-minute low is violated later the same
  day and pays again.
- Outcome: "there's **two opportunities** in this particular currency, and it's a dollar CAD of
  all pairs — it's a really low-volatility pair generally."

## Common Mistakes

- **Reading the title as a daily income target.** Disclaimed in the first minute; the honest
  claim is "almost every day", and it depends on watching many instruments: "if you look at a
  great number of pairs — you need **10 or 15 pairs** — you'll find something like this panning
  out every single trading day" (18:37–18:49).
- **Letting a winner run.** Both patterns are 20-for-20 by construction. The examples exceeding
  20 pips are shown to demonstrate the cushion, not to license trailing.
- **Trading Pattern A on majors.** It is specified for **yen, Aussie and Kiwi crosses**.
- **Trading Pattern B without both preconditions.** London must already have posted the extreme,
  **and** the five-day ADR must still be unfilled. Without the second, there is no expansion
  left to aim at.
- **Chasing the probe.** Pattern A's entry is roughly **five pips** beyond the level; a missed
  fill is a missed trade, not a reason to chase — "if I can't get it, then I miss it, it's fine".
- **Reading the Asian-range probe as trend information.** It is a low-volume liquidity run and,
  on a bullish day, is the *precondition* for the Judas swing rather than a bearish signal.
- **Treating it as a system to run live immediately.** "Notice I said **practice** — because I
  don't want you thinking you can go in every single day trading and trying to get 20 pips"
  (18:24–18:42).
- **Day-trading stocks with it.** ICT names stocks as compatible and then advises against them:
  "I **don't advocate** day trading stocks, because the volume usually isn't enough to push it
  around" (17:56–18:06).

## Related Concepts

- [asian-range](../14-asian-range/asian-range.md), [asian-range-high](../14-asian-range/asian-range-high.md), [asian-range-low](../14-asian-range/asian-range-low.md) — Pattern A's probe is these levels forming.
- [asia-session](asia-session.md), [ny-am-session](ny-am-session.md) — the two windows.
- [turtle-soup](../20-turtle-soup/turtle-soup.md), [bullish-turtle-soup](../20-turtle-soup/bullish-turtle-soup.md), [bearish-turtle-soup](../20-turtle-soup/bearish-turtle-soup.md), [stop-hunt-pattern](../20-turtle-soup/stop-hunt-pattern.md) — the raid both patterns are.
- [judas-swing](../13-judas-swing/judas-swing.md) — what Pattern A's sell is a precursor to on a bullish day.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the five-day ADR that gates Pattern B.
- [order-flow-subordination](../25-htf-bias/order-flow-subordination.md), [day-trade-routine](../25-htf-bias/day-trade-routine.md) — the sibling May-2017 lessons.

## Citations

- `ICT-2017-20-PIPS` (00:16–00:33) "welcome back folks, this is **lesson three of the [May] 2017 ICT mentorship**, ICT amplified day trading and scalping — this lesson's teaching **20 pips per day**" — dates the source. ⚠ Whisper renders the month as "**mason** 2017"; the month is fixed by the series title ("ICT amplified day trading and scalping" = Month 09 = May 2017) and by the sibling packets `ICT-2017-CONSOLIDATION-TRADING` [00:15] and `ICT-2017-DAYTRADE-ROUTINE` [00:14], which both say "May 2017" cleanly. The **ordinal — lesson three — is quoted verbatim and is not in doubt**; (00:33–00:45) "**you will not make 20 pips every day, period** — I can't promise you that, no one can promise you that"; (01:18–01:31) "ideally you will want to **bank 20 pips in any day trade** that you take"; (01:43–01:54) "there are a few techniques one can use to ferret out a 20-pip scalp **almost** every day — again, the emphasis there is **almost**"; (02:05–02:15) "this lesson I'm going to teach you **two methods** that I like to scalp with and aim for 20 pips"; (02:15–02:25) "I get a lot of questions about how can I trade the Asian session — I **don't like to trade that that much**"; (02:32–02:47) "what we're doing is trading the **15-minute New York session stops** — this pattern is good for **yen, Aussie and Kiwi crosses**"; (02:47–02:58) "the **buy setup** is during Asian session **up to 12 a.m. New York time** — you're going to scout **short-term lows formed in New York session**"; (03:56–04:15) "I think all the volume should be done in London and New York, but for completeness' sake, for those that are **desk jockeys in the North American continent**"; (04:22–04:34) "trading long after **Asia probes the low** … basically what we're looking for is a **turtle soup long**"; (04:34–04:48) the mirrored sell setup, "trading short after Asia probes the highs"; (04:48–05:03) "we're timing off of a **five-minute chart**, we're targeting **20 pips**, and it's a **fixed target** — we are **not graduating it** … it's straight **20 for 20 — 20 stops, 20 target**, that's it"; (05:03–05:28) "there is a short-term high formed **prior to the Asian session start**, and that short-term high is going to have a **very small pocket of stops** resting above it — delineated here by **late New York stops**"; (05:35–05:55) "I interpret this as a very, very **low-volume liquidity run** … we're **interpreting the Asian range high forming** when we take a move above that short-term high"; (06:10–06:17) "the **blue ranges** you're going to see in this video are all delineating what 20 pips looks like"; (06:29–06:59) "the setup usually occurs **before New York midnight** … by expecting the Asian range to be what it typically is, a **consolidation** … once that's taken out they **fade that** and take it the other way down, making the **Asian range low**"; (06:59–07:09) "many times the Asian range is a lot larger than 20, 30, 40 pips, but many times it's **at least enough to get 20 pips** out of it"; (07:30–07:57) the USDJPY example, "between **8 o'clock at night** New York time we see a small little rally up, they fade that and price trades down" plus the far-left **fair value gap** "that's what ultimately price was reaching down for"; (08:48–09:17) "your **stop loss is fixed at 20 pips** … how many pips above it, Michael? I don't know. **Five. Five is a good number** … preferably I like **five pips above** the short-term highs — if I can't get it, then **I miss it, it's fine**"; (10:15–10:40) "if we're bullish we can see the selling above a short-term high like this — many times they actually **work out better**, because what you're doing is you're **pricing in the Asian range high**, and what do we look for for upside movement? **That Judas swing down**"; (11:17–11:33) "all we're doing is looking for an opportunity to trade **between 8 o'clock and midnight** New York time"; (11:33–11:52) "our second way of scalping 20 pips — we're going to be trading the **New York expansion** … this is a pattern that's good for **all pairs** … a **universal application**"; (11:52–12:16) "the buy setup is during the New York session **up to 10 a.m. New York time** … trading long after New York probes the lows **while London session posted the daily low** and the **five-day average daily range is still pending**"; (12:24–12:39) "we buy long below that short-term low **in the mindset that it's a turtle soup** — it's coming back for short-term sell stops, and we're going to be looking for **expansion going towards the five-day average daily range**"; (12:39–13:00) the mirrored sell setup; (13:20–13:41) "average daily range for the last five days … has **not been met yet** — that's the condition we're looking to trade in … again we're **targeting 20 pips**, fixed, with a **stop loss at 20 pips**"; (13:41–14:33) the AUDUSD example — "a five-minute **fair value gap** back down into an **order block** as well … this is actually the reason why I expected that Aussie dollar to trade up and make a **higher high** during the live session … **this was the actual pattern I saw**"; (15:32–16:51) the USDCAD example with **two** setups in one day, "and it's a dollar CAD of all pairs — it's a really **low-volatility pair** generally"; (17:02–17:25) "they're trying to **entice short sellers and breakout artists**, and also knock out those individuals that are already long"; (17:35–18:06) "it's actually a really good pattern for **S&P** trading too — if you're an **ES** trader you can do this same pattern … it's good for **Dow futures and triple Qs**, it's good for stock trading too … [but] I **don't advocate** day trading stocks, because the volume usually isn't enough to push it around"; (18:24–18:49) "notice I said **practice**, because I don't want you thinking you can go in every single day trading and trying to get 20 pips — but if you look at a great number of pairs, you need **10 or 15 pairs**, you'll find something like this panning out every single trading day".

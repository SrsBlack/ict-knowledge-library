# London Open Killzone

**Category:** 10-killzones
**Aliases:** London Open KZ, LDN open KZ, LO killzone
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2017-DEFINING-DAILY-RANGE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, london, manipulation, open

## Definition

The London Open killzone is the 02:00 → 05:00 NY sub-window of the London session and ICT's prime morning manipulation window. The classic delivery: sweep one side of the [asian-range](../14-asian-range/asian-range.md) (Judas swing) inside the first 60 minutes, then displace in the opposite direction toward HTF DOL. This is one of the highest-volume killzones of the day — second only to London Close × NY AM overlap.

⚠ **The start time is disputed between ICT's own sources, and he says so.** In the April-2017
mentorship the window is **01:00 → 05:00**, and that lesson rejects the 02:00 reading by name:
"folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4
o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**, it
ends at 5 a.m." (`ICT-2017-DEFINING-DAILY-RANGE`, 08:16), framed as "the **definitive
teaching** … if you've seen anything different in the past, **this is the real one**"
(02:13–02:27). The 02:00 start below is the public 2016/2022 formulation and is what the rest
of this page is built on. **The end time, 05:00, is identical in both.** The companion
April-2017 lesson `ICT-2017-DAYTRADE-ESSENTIALS` reconciles them by treating 01:00–05:00 as
the envelope with a **02:00–04:00 hotspot** — see
[ict-day-trading-model](../31-models/ict-day-trading-model.md). Full 2017 set:
[ipda-true-day](../04-time-cycles/ipda-true-day.md).

## Formal Criteria

- Time window: 02:00 → 05:00 NY (public 2016/2022 anchor); **01:00 → 05:00 NY** in the
  April-2017 mentorship.
- Sits inside the London session (02:00 → 11:00 NY).
- Behavioral profile: opening manipulation move (Judas swing) → CHoCH/MSS → expansion.
- Contains the 02:50–03:10 macro time window.
- Often defines the day's HOD or LOD via the post-Judas displacement.

## Formula / Math

```
london_open_kz      = [02:00, 05:00] NY   # public 2016/2022 formulation
london_open_kz_2017 = [01:00, 05:00] NY   # April-2017 mentorship
contains_macro      = [02:50, 03:10] NY
```

## Machine-Readable

```json
{
  "id": "london-open-killzone",
  "category": "10-killzones",
  "aliases": ["london-open-kz", "ldn-open-kz"],
  "criteria": [
    {"id": "c1", "expr": "time_in [02:00, 05:00] NY (public 2016/2022)"},
    {"id": "c2", "expr": "opening_manipulation_then_expansion == true"},
    {"id": "c3", "expr": "time_in [01:00, 05:00] NY (April-2017 mentorship; 02:00-04:00 hotspot)"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","london-session","asian-range","judas-swing","silver-bullet-london","macro-time-0250-0310","manipulation-phase","ipda-true-day","ict-day-trading-model"],
  "sources": ["ICT-2016-KILLZONES","ICT-2017-DEFINING-DAILY-RANGE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   00:00 ─── 02:00 ─── 03:00 ─── 05:00 NY
              |          █          |
              ──── London Open KZ ──
                         ↑
              02:50–03:10 macro window
              (Judas swing typical here)
```

## Timeframes

M1 / M5 / M15. The first 30–60 minutes of the killzone (02:00–03:00) typically produce the manipulation; the next 60–90 minutes (03:00–04:30) deliver the expansion.

## Examples

**Example 1 — Judas-swing-down → bullish expansion:**
- HTF bias bullish; Asian range 1.0850–1.0880; PDH BSL at 1.0925.
- 02:30 NY: M5 wicks 1.0846 (Asian SSL swept), closes 1.0854.
- 02:55 NY: M5 displaces 18 pips up, FVG at 1.0860.
- 03:30 NY: returns to FVG, continues upward.
- 04:30 NY: takes 1.0925 PDH BSL.
- → London Open KZ delivers a textbook Judas + expansion.

## Common Mistakes

- **Entering on the manipulation move.** The first 30 minutes of LO-KZ is typically the *fake-out direction*; entering on it gets stopped before the real move.
- **Skipping the macro check.** The 02:50–03:10 macro window inside LO-KZ is the highest-density delivery moment; setups that align with the macro have higher confluence.
- **Holding past 05:00.** Post-killzone London (05:00–10:00) is mostly drift; setups that don't trigger inside the killzone usually don't deliver outside it.
- **Quoting 02:00 as the start while working through 2017 mentorship material.** In that
  material the window opens at **01:00**, and the 02:00 reading is the one ICT is correcting.
  State which formulation is in use.

## Related Concepts

- [ipda-true-day](../04-time-cycles/ipda-true-day.md) — the April-2017 time set, where this window is 01:00–05:00.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — records the 01:00–05:00 envelope with a 02:00–04:00 hotspot.
- [killzone-overview](killzone-overview.md), [london-session](../15-sessions/london-session.md), [asian-range](../14-asian-range/asian-range.md), [judas-swing](../13-judas-swing/judas-swing.md), [silver-bullet-london](../11-silver-bullet/silver-bullet-london.md), [macro-time-0250-0310](../04-time-cycles/macro-time-0250-0310.md), [manipulation-phase](../12-power-of-three/manipulation-phase.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW` — the 02:00–05:00 public formulation.
- `ICT-2017-DEFINING-DAILY-RANGE` (00:14) "**lesson two of the April 2017 ICT mentorship**"; (03:06–03:24) "the ICT London killzone — every day at **1 a.m.** Eastern Standard Time New York begins the London killzone; every day at **5 a.m.** … ends the London killzone"; (08:16) "folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4 o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**, it ends at 5 a.m."; (02:13–02:27) "this is the **definitive teaching** … if you've seen anything different in the past, **this is the real one**".

# Asia Judas Swing

**Category:** 13-judas-swing
**Aliases:** Asian Judas, zero-GMT Judas, 0 GMT Judas, Asia-open protraction
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-MARKET-REVERSALS, ICT-2017-BREAD-BUTTER-BUY
**Tags:** judas, asia, protraction, zero-gmt, session-open

## Definition

The Asia Judas swing is the session-open protraction at the **Asian open — 20:00 New York / 00:00 GMT**. It is the fourth and smallest of the four session Judas swings ICT enumerates: London open, CME open (New York), Asia, and London close. Mechanically it is identical to the others — a short counter-directional move off the session open before delivery in the HTF-bias direction — but ICT qualifies it twice: the displacement is small ("it doesn't go down very much that time of day"), and the sweep target is not a fixed range bound but "a previous late session swing".

ICT teaches it for completeness of the daily-range model rather than as a setup he takes. He calls Asia's open and London close "the two smallest tiny little windows of opportunity" and says it "doesn't pay out enough in my opinion to take on the risk" (`ICT-2017-BREAD-BUTTER-BUY` [28:21]).

⚠ **This page is deliberately thin.** The corpus names the Asia Judas, times it, gives its direction, its magnitude qualifier and its sweep target, but contains **no worked example, no failure mode, no macro-window overlap and no target ladder** for it. Everything below is quoted; nothing is extrapolated from the London or NY pages.

## Formal Criteria

- **Time anchor: the 00:00 GMT open, which ICT states as 20:00 New York** — "in Asia it's your GMT eight o'clock in the evening in my time right now" (`ICT-2017-BREAD-BUTTER-BUY` [20:52]). ICT tracks two daily opens and this is one of them: "we look at both zero GMT open at Asia's open and we're looking at midnight in New York" [08:00].
- **Direction: counter to the day's expected delivery.** On a bullish day, "you want to see it trade down right after your GMT" [20:58].
- **Magnitude: small.** "It doesn't go down very much that time of day though" [21:06].
- **Sweep target: a prior late-session swing**, not the Asian range (which has not formed yet at the open) — "it can go down just below a previous late session swing" [21:06].
- **Frequency: about one per session across a basket of pairs**, not one per pair — "per session you generally get about one per session, that means one in London, one in New York, one in London close and one in Asia … if you look across a handful of pairs and get a basket of four or five" [04:33–04:50].
- Associated scalp, when taken: enter at or just under the 0 GMT opening price and **expect 15–20 pips** of expansion as the Asian range establishes [27:29–27:34].

## Formula / Math

```
asia_judas := t0 == 00:00 GMT (20:00 NY)
               AND direction(move) == -sign(HTF_bias)
               AND sweeps(prior_late_session_swing)
               AND magnitude(move) is SMALL          # ICT: "doesn't go down very much"

# associated scalp, bullish day (ICT-2017-BREAD-BUTTER-BUY 27:29):
entry   := open_0GMT  or slightly below
target  := entry + 15..20 pips
```

No further quantification is given in the corpus. In particular the sweep depth, the stop
distance and the reversal-confirmation criterion are **not stated** for this session.

## Machine-Readable

```json
{
  "id": "asia-judas-swing",
  "category": "13-judas-swing",
  "aliases": ["asian-judas", "zero-gmt-judas"],
  "criteria": [
    {"id": "c1", "expr": "session_open == 00:00 GMT == 20:00 NY"},
    {"id": "c2", "expr": "direction == opposite(HTF_bias)"},
    {"id": "c3", "expr": "sweep_target == prior_late_session_swing"},
    {"id": "c4", "expr": "expansion_target == 15..20 pips"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["judas-swing","london-judas-swing","ny-judas-swing","london-close-judas-swing","market-protraction","asia-killzone","asian-range","asia-session"],
  "sources": ["ICT-2017-MARKET-REVERSALS","ICT-2017-BREAD-BUTTER-BUY"]
}
```

## Visual Pattern

```
   20:00 NY  ──────────────────────────────  00:00 NY
   (00:00 GMT)
   Asia open
       │
   ────┼──── opening price
       ↓  small decline right after the open
       ↓  (ICT: "doesn't go down very much")
       ↓
   ────┴──── just below a PREVIOUS LATE SESSION SWING
       ↑
       ↑  delivery in HTF-bias direction
       ↑  15-20 pips as the Asian range establishes
       ↑
```

Bearish day is the mirror: a small rally above the 0 GMT open, just above a prior late-session
swing, then delivery lower.

## Timeframes

M1 / M5 / M15. `ICT-2017-BREAD-BUTTER-BUY` specifies the five-minute chart for the whole scalping module [04:14].

## Examples

The corpus contains **no worked Asia-Judas example**. `ICT-2017-BREAD-BUTTER-BUY` shows worked examples for the London-open, New York and London-close scalps, and describes the Asian-open scalp in slides only. This page records that absence rather than fabricating an illustration.

The one conditional ICT gives for actually taking it: "same way with Asia — if I think it's going to be trading down to a level that would be a higher-timeframe discount array but it didn't quite get down there in New York and it's just hovering above" [29:48].

## Common Mistakes

- **Demanding size from a session designed to be narrow.** ICT names this contradiction himself: "what you're actually trying to do is demand that the Asian range pays you when you really hope that it's going to be a small range — so it is a confliction between the rules" [29:00–29:11]. A trader who wants a wide Asian expansion is betting against the Asian-range premise the rest of the model depends on.
- **Expecting the Asian range as the sweep target.** At 20:00 NY the Asian range does not exist yet — it is being *built*. The stated target is a **prior late-session swing**. Sweeping the Asian range bound is the London Judas ([london-judas-swing](london-judas-swing.md)), a different pattern.
- **Trading it as a primary setup.** "Asia's opening and London close are the two smallest tiny little windows of opportunity and it doesn't pay out enough in my opinion to take on the risk … if you're looking for more bang for your buck in your study time and seeing movement in price, you want to be focusing on the New York and the London sessions" [28:21–28:43].
- **Assuming it fires daily.** "You can have a really tight Asian range and it doesn't do anything" [14:58].

## Related Concepts

- [judas-swing](judas-swing.md) — the parent concept; this is its Asia-session instance.
- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md), [london-close-judas-swing](london-close-judas-swing.md) — the other three of the four sessions ICT enumerates.
- [market-protraction](market-protraction.md) — the mechanism ("every session has a protractionary market stage").
- [asia-killzone](../10-killzones/asia-killzone.md) — the 20:00–00:00 NY window this Judas opens.
- [asian-range](../14-asian-range/asian-range.md) — the range built *after* this Judas, and the London Judas's target.
- [asia-session](../15-sessions/asia-session.md) — the broader session.

## Citations

- `ICT-2017-MARKET-REVERSALS` (28:07) — "we can reduce it to the London open for Judas, the CME open for the New York Judas, and **Asia it has its Judas at eight o'clock and then New York time or … zero GMT**, and then you have it also in London close on days that create London close reversals." The enumeration that establishes Asia as one of four.
- `ICT-2017-BREAD-BUTTER-BUY` (20:52–21:19) — "in Asia it's your GMT eight o'clock in the evening in my time right now … you want to see it trade down right after your GMT. It doesn't go down very much that time of day though, but it can go down just below a previous late session swing … **that is the Judas swing at zero GMT or Asia's open**"; (04:33) one setup per session across a basket of pairs; (08:00) "we look at both zero GMT open at Asia's open and we're looking at midnight in New York"; (27:29–27:42) enter at or just under the 0 GMT open, expect 15–20 pips; (28:21–28:43) smallest window, does not pay enough for the risk; (29:00–29:11) the "confliction between the rules"; (29:48) the one condition under which he takes it.

# Institutional Swing Points

**Category:** 01-market-structure
**Aliases:** breaker swing point, failure swing, two swing point theories, stop run vs failure swing
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-INSTITUTIONAL-SWING-POINTS
**Tags:** structure, swing, breaker, failure-swing, reversal, taxonomy, entry

## Definition

Institutional swing points are ICT's **exhaustive two-item taxonomy of how a market turns**. Not
a shape library — a claim that there are exactly two mechanisms and nothing else. "There's really
only two forms of swing points in the marketplace as it relates to institutional trading. It's in
the form of a stop run or a failure swing. That's it. There's nothing else"
(`ICT-2017-INSTITUTIONAL-SWING-POINTS`, 01:37–01:51).

1. **Breaker swing point** — price runs *through* the prior extreme (a stop run), rejects, then
   breaks the intervening short-term pivot. The preferred one.
2. **Failure swing** — price *falls short* of the prior extreme and turns without running it.

The taxonomy is stated as closed: "I challenge you to go in and show me something where it
doesn't do this because I can tell you it's either a breaker or it's a failure swing every single
time. It's never anything else" (31:14–31:23).

⚠ This is the **swing-point** sense of "breaker", i.e. the turn pattern. The traded zone it leaves
behind is the [breaker-block](../08-breaker-blocks/breaker-block.md).

## Formal Criteria

**Breaker swing point (bearish form)**

1. Price rallies toward a known institutional reference — bearish order block, breaker,
   mitigation block, old high, old low — and **falls short**, printing a short-term high.
2. It pulls back, printing a short-term low.
3. It drives back up, **exceeds** the short-term high, and reaches the reference. Buy stops are
   run.
4. It rejects and **takes out the short-term low made in step 2**. That break is the trigger.
5. Entry: sell on any retrace back to the step-4 break level. Stop: above the run high.

The bullish form is the mirror. ICT's rationale for the stop placement: "if my buy stop is here
now, they're not going to come back up and give these opportunity to get off. They're not going
to let them out" (24:56–25:01) — the stops in that zone were already cleared, so there is no
remaining reason to revisit it.

**Failure swing**

1. Price approaches the reference level and **does not reach or exceed it**.
2. It turns and takes out the most recent counter-directional short-term pivot: "if it takes out
   this short-term high or on the sell side takes out this short-term low, we have another
   opportunity" (21:37).
3. Entry: on the retrace back to that broken pivot. Stop: beyond the swing that failed.

**The relationship between the two.** The breaker is what you aim for; the failure swing is the
fallback when you do not get it. "We don't ever know with great deal of conviction if we're going
to get the breaker set up" (18:08). And: "if you can't get the breaker, don't fear or be upset
about missing that move because it still gives you the opportunity to get in there because
they're only going to turn the market one of these ways" (31:00–31:12).

**Time limit on the run:** none, for the old-high/old-low variant. "If it's an old low, there is
no limit to time between this low and the new low that forms… it could be six months and then
finally it trades down below that low and then it runs. That's still the same pattern" (13:24–13:41).

**Prerequisite:** the reference levels must already be drawn. "If you don't have the levels on
your chart, you're going to be surprised by these things" (09:24).

## Formula / Math

```
# bearish breaker swing point, on any timeframe
STH_1 := short-term high formed short of reference level R
STL   := short-term low after STH_1
STH_2 := new high with STH_2 > STH_1 and STH_2 reaches/exceeds R   # the stop run
trigger := close below STL
entry   := retrace up to STL level
stop    := above STH_2

# bearish failure swing
STH_2 does NOT exceed STH_1        # the failure
trigger := break of the most recent STL
entry   := retrace up to that broken STL
stop    := above STH_1

# exhaustive
turn_type(any reversal) in {breaker_swing_point, failure_swing}
```

## Machine-Readable

```json
{
  "id": "institutional-swing-points",
  "category": "01-market-structure",
  "aliases": ["breaker-swing-point", "failure-swing", "two-swing-point-theories"],
  "criteria": [
    {"id": "c1", "expr": "turn_type in {breaker_swing_point, failure_swing} and nothing else"},
    {"id": "c2", "expr": "breaker := run of prior extreme THEN break of intervening pivot"},
    {"id": "c3", "expr": "failure_swing := prior extreme NOT reached THEN break of counter pivot"},
    {"id": "c4", "expr": "entry == retrace to the broken pivot; stop == beyond the run extreme"},
    {"id": "c5", "expr": "time_between_old_extreme_and_run is unbounded"},
    {"id": "c6", "expr": "requires pre-marked institutional reference level"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["swing-high","swing-low","mss","choch-bearish","choch-bullish","breaker-block","turtle-soup","stop-run-definition","ote-overview","mitigation-block"],
  "sources": ["ICT-2017-INSTITUTIONAL-SWING-POINTS"]
}
```

## Visual Pattern

```
   BREAKER SWING POINT (bearish)        FAILURE SWING (bearish)

   ····· reference level R ·····        ····· reference level R ·····
                    /\  <- stop run                    (never reached)
       /\          /  \                     /\        /\
      /  \        /    \                   /  \      /  \   <- falls short
     /    \      /      \                 /    \    /    \
    /      \    /        \               /      \  /      \
   /        \__/          \             /        \/        \
      STH_1  STL           \               STH_1  STL       \
             ^                                    ^
             break here = trigger                 break here = trigger
             sell the retrace back up             sell the retrace back up
             stop above the run high              stop above STH_1
```

## Timeframes

Every timeframe. "You want to be looking for that scenario all the time on any time frame, not
just the daily chart" (30:54). ICT recommends intraday charts for practice volume precisely
because the pattern "materializes every single day… and in every single pair" (06:44–06:47).

On the daily chart the run leg often becomes the candle's wick: "this many times will become the
wick. The market will trade down, make that low here and then wick away from that low… what many
people get excited about as a hammer or some kind of a doji" (15:11–15:24). ICT's point is that
the institutional entry happens while the candle is still a full body, before the wick exists.

## Examples

**Example 1 — bearish breaker swing point (`ICT-2017-INSTITUTIONAL-SWING-POINTS`, 09:57–11:04):**
- Short-term high prints just under a bearish order block; price falls short of the block.
- Pullback prints a short-term low.
- Second leg exceeds the short-term high, closes the residual gap into the order block, rejects.
- The short-term low is taken out → "that market structure shift breaking point, that becomes
  your trigger. If price ever comes back up to that level, you can be a seller."

**Example 2 — bullish failure swing (`ICT-2017-INSTITUTIONAL-SWING-POINTS`, 20:52–21:50, 25:08–25:40):**
- Price trades into a support level, turns, retraces, comes back down and **fails to make a new
  low**.
- It then breaks the intervening short-term high.
- Entry on the retrace back down to that broken high; "my stop loss can be placed just below this
  low because it's going to be in an area where they had already ran the sell stops."

## Common Mistakes

- **Demanding the breaker.** "We may have even second guessed this entry as a short, but we are
  demanding a breaker to occur… But it doesn't give it to you here. That would be a missed
  opportunity. But it doesn't mean there's no trading opportunity" (18:36–18:50).
- **Trading it without reference levels.** The pattern only has meaning at a pre-marked PD array
  or old high/low; without one it is just noise.
- **Waiting for candlestick confirmation.** "If you're demanding confirmation, you're not going
  to get this entry down here" (15:55).
- **Substituting classical patterns.** "Don't think in terms of classical chart patterns like
  head and shoulders or… bear flags and bull flags" (30:28–30:37).
- **Assuming the retrace entry always arrives.** "It may just keep on screaming higher. And
  that's sometimes going to happen. And that's going to be a missed opportunity" (17:21–17:25).
  The retrace may also stop at a nearer order block instead of reaching the break level (16:56–17:09).

## Related Concepts

- [swing-high](swing-high.md), [swing-low](swing-low.md) — the 3-bar primitive ICT builds on ("that's what I learned from my mentor Larry Williams", 00:56).
- [mss](mss.md), [choch-bearish](choch-bearish.md), [choch-bullish](choch-bullish.md) — the structural break at step 4.
- [breaker-block](../08-breaker-blocks/breaker-block.md) — the zone the breaker swing point leaves behind.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the stop-run leg of the breaker form; ICT names it directly at 17:44.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — the raid mechanic.
- [mitigation-block](../08-breaker-blocks/mitigation-block.md) — one of the reference levels the pattern forms against.

## Citations

- `ICT-2017-INSTITUTIONAL-SWING-POINTS` (00:00) — "Welcome back folks this is lesson 1.5 defining institutional swing points"; (00:32–00:56) the 3-bar swing high/low from Larry Williams; (01:37–01:51) "there's really only two forms of swing points… a stop run or a failure swing. That's it"; (02:58–03:08) "this pattern in my opinion is the most powerful, the most dynamic, the most significant price pattern"; (05:29–05:52) why the intervening short-term low defines the breaker; (09:24) the levels must already be on the chart; (09:57–11:04) the bearish breaker trigger and entry; (13:24–13:41) no time limit between the old extreme and the run; (15:11–15:24) the run leg becoming the daily wick; (17:21–17:25) the retrace may never come; (18:08–18:50) the failure swing as the fallback; (20:52–21:50) failure-swing criteria; (24:56–25:01) why the stop zone will not be revisited; (29:07–29:22) the breaker as "the deepest discount buy and the absolute most premium to sell"; (30:28–31:23) the taxonomy stated as closed.

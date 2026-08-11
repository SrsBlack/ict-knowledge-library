# OTE Failure

**Category:** 17-optimal-trade-entry
**Aliases:** failed OTE, broken OTE, OTE invalidation
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2017-OTE-FAILED-FOMC, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, failure, invalidation, risk

## Definition

An OTE failure is when an entered OTE setup invalidates — ultimately by price **taking out the leg-origin extreme** (fib 1.0), which is where the taught stop sits. A close beyond **0.79** is the earlier warning: once price closes past the deepest acceptable entry, the leg's structural premise is in doubt and the algorithm may be shifting bias.

> ⚠ **Corrected 2026-08-05: two distinct events, previously conflated.** This page treated a close below 0.79 as *the* invalidation because it assumed the stop sat beyond 0.79. The dedicated OTE material places the stop at the **leg-origin extreme, exactly** (`ICT-2017-OTE`), so a close past 0.79 **warns**; the leg extreme **invalidates**. Traders using the community 0.79-buffer stop experience the two as the same event — that is a property of their stop choice, not of the setup. See [ote-79](ote-79.md), [ote-overview](ote-overview.md).

## Formal Criteria

For a long OTE failure:

- Entry was taken inside [0.62, 0.79] of a measured bullish leg.
- **Warning:** price closes **below 0.79** — out of the zone, premise weakening.
- **Invalidation:** price takes out **leg_start** (fib 1.0) — the structural low that defined the leg is gone; the stop is hit and the leg is void.
- *(Invalidation semantics — whether a body close beyond the level is required, and on which timeframe — are NOT specified in the primary material. Any mechanical implementation must pin its own convention and say so.)*
- Optional confirmation: bearish FVG / displacement forms after the close-below.

For a short OTE failure: symmetric.

When failure occurs:

- **Don't fight it.** Don't add to a *still-open* losing OTE expecting a deeper reversal.
- **Reassess HTF bias.** A close below 0.79 often signals HTF bias is flipping or the dealing range is being broken.
- **Look for counter-bias setups.** If HTF bias appears to be flipping, the next setups belong in the new direction.

### Re-entry after a stop-out — added 2026-08-11

⚠ **A stop-out is not, by itself, an invalidation of the analysis, and ICT re-enters the same pattern on the same bias when it isn't.** `ICT-2017-OTE-FAILED-FOMC` is a recorded worked example of exactly this: he takes a long OTE on cable, is stopped out, and re-enters the same setup the same day.

- The failure cause is named and it is **stop distance against a known pool**, not a bad read: "my stop loss was a little … tight in the sense that … better setups it would have never been hit. But because I felt that we hit this high of two days ago — we hit it one time, two times, three times — I didn't think we'd see it again, but **they ran it one more time and then stopped me out**" [06:36–07:07].
- The re-entry is explicit and pre-empts the objection: "so after the run through I said, okay, I'm going back in … I'm entering **right at optimal trade entry again, between the 62 and 79 % retracement level**. Now you're probably thinking, wait a minute Michael, this is a break in that pattern isn't it? **Yes, but it has not changed my analysis. I've still believed that we're going above previous day's high**" [07:07–07:30].
- The fill improves on the second attempt: "you can see the re-entry at optimal trade entry, so I'm using the same entry pattern — **got a better fill than I did on the initial entry**" [05:49–05:59].
- Outcome: "my loss down here that I took in this trade was completely mitigated, almost with the first scaling out, and certainly with the last two portions, so it allowed me to go to a **new equity high**" [08:13–08:31].

The distinction the page must hold: **adding to an open loser is refused; re-entering after the loss is closed, when the draw-on-liquidity thesis is intact, is taught.** The test is whether the *bias* was invalidated, not whether the *stop* was hit. A stop run through a repeatedly-tested pool is a liquidity event, and the leg's premise can survive it.

## Formula / Math

```
long_ote_failure  := close < (leg_end - 0.79 * leg_size)
short_ote_failure := close > (leg_end - 0.79 * leg_size)     # leg_size negative for bearish leg
```

## Machine-Readable

```json
{
  "id": "ote-failure",
  "category": "17-optimal-trade-entry",
  "aliases": ["failed-OTE", "OTE-invalidation"],
  "criteria": [
    {"id": "c1", "expr": "close beyond 0.79 of measured leg in invalidation direction", "role": "warning"},
    {"id": "c2", "expr": "leg_origin_extreme (fib 1.0) taken out", "role": "invalidation"},
    {"id": "c3", "expr": "stop_hit AND bias_intact -> re_entry_permitted_at_same_OTE_zone"},
    {"id": "c4", "expr": "add_to_open_loser == false"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ote-overview","ote-79","ote-rules","fib-79","htf-bias-framework"],
  "sources": ["ICT-2017-OTE","ICT-2017-OTE-FAILED-FOMC","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   OTE failure (bullish setup invalidated):

   leg_end ──────── 0.0
   ─────────────── 0.50 EQ
   ─── 0.62 ────── (entry zone)
   ─── 0.705 ────  (entry tried here)
   ─── 0.79 ────── ← invalidation trigger
   ─── close ────── ← bearish close BELOW 0.79
                     → setup invalidated; leg structure broken
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example 1 — failed bullish OTE:**
- Leg 1.0800 → 1.0900.
- 0.79 = 1.0821; entry at 1.0830 (0.705).
- Price extends down, closes M15 candle at 1.0815 (below 0.79) — **warning: out of the zone**, premise weakening, but the stop at 1.0800 is still intact.
- Price continues and takes out 1.0800, the leg-origin low → **SL hit; setup invalidated.** HTF bias reassessed: D1 just printed CHoCH down. The bullish leg is being violated; bias is flipping.
- Action: stand aside; wait for new structure to define the next setup direction.

## Common Mistakes

- ⚠ **Treating a stop-out as a refuted thesis.** ICT re-enters the identical OTE on the identical bias after being stopped out, and says so on tape (`ICT-2017-OTE-FAILED-FOMC`, 07:18). The question to ask is whether the *draw on liquidity* changed, not whether the stop was hit.
- ⚠ **Assuming a repeatedly-tested level will not be run again.** The named cause of the loss in that recording is exactly that assumption: "we hit this high of two days ago, we hit it one time, two times, three times — I didn't think we'd see it again, but **they ran it one more time and then stopped me out**" [06:46–07:00]. The count of prior tests is not evidence of exhaustion. *(The transcript does not make the side of the pool unambiguous; quoted rather than reconstructed.)*
- **"It'll come back."** Adding to an invalidated OTE based on hope/anchoring loses bigger.
- **No HTF reassessment.** OTE failures often herald HTF bias change. Failing to re-read HTF after a failure leads to repeated same-direction failures.
- **Over-tight SL leading to false failures.** A 1-pip overshoot of 0.79 is not a real failure on FX; require a closing print.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [fib-79](../28-fibonacci-levels/fib-79.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2017-OTE-FAILED-FOMC` — "Pattern Recognition, Failed OTE & FOMC Mitigation Example", 2017-10-11. A recorded loss and same-day re-entry on cable. (05:29–05:59) "there's my loss earlier in a day … entered here on optimal trade entry and stopped me out, and then you can see the **re-entry at optimal trade entry** — so I'm using the same entry pattern, got a better fill than I did on the initial entry"; (06:36–07:07) the stop-run cause; (07:07–07:30) "I'm entering right at optimal trade entry again, between the 62 and 79 % retracement level … **it has not changed my analysis**"; (08:13–08:31) the loss "completely mitigated" to a new equity high; (09:22–09:29) "I always want to exit before my target … it's much higher probability … to exit before a known target in your trading plan than it is to just be greedy."

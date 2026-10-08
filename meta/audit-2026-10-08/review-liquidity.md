# Review — cluster LIQUIDITY (2026-10-08)

Reviewer: read-only gate. Inputs: `liquidity.md` audit, `FIX-BRIEF.md`, `git diff` of the 13 pages, `raw/*/report.md`, `m22-captions/ep*.txt`. Every quote on the 13 pages was re-grepped (normalised, punctuation-insensitive) against its cited packet/episode; `tools/lint.py` → `problems: 0`. The mechanical quote-miss list contains no page from this cluster.

Verification summary: 150 quote fragments checked. All 2022-caption quotes resolve to the cited episode within ±30 s. All raw-packet quotes resolve to the cited packet; one timestamp is >2 min off (liquidity-run "hot knife"). Both "extra scrutiny" items verify: ep38 [04:29]–[05:26] names "chris laurie" [= Chris Lori], "he teaches how the market wants to come back down and fill all that area in as you probably noticed i don't teach that … i'm not trying to insist that these imbalances completely rebalance that's one of the main differentiations between me and chris laurie"; MMT-TRENDLINE [07:58] "when that third touch of that uptrend line is seen in price action many times i get dialed in expecting the high that forms between the low at the second time it hits the trend line and the third time" + [08:48] "the high in between there is going to be a sell scenario that i'm aiming for".

| page | PASS / FIX | issue count |
|---|---|---|
| liquidity-sweep | FIX | 3 FIX, 1 NOTE |
| liquidity-run | FIX | 2 FIX |
| liquidity-pool | PASS | 0 FIX, 1 NOTE |
| equal-highs | FIX | 1 FIX, 1 NOTE |
| equal-lows | PASS | 0 FIX, 1 NOTE |
| relative-equal-highs-lows | PASS | 0 FIX, 1 NOTE |
| buy-side-liquidity | PASS | 0 |
| sell-side-liquidity | PASS | 0 |
| external-range-liquidity | PASS | 0 |
| internal-range-liquidity | PASS | 0 |
| liquidity-void | PASS | 0 FIX, 2 NOTE |
| turtle-soup | FIX | 1 FIX, 1 NOTE |
| stop-hunt-pattern | FIX | 3 FIX |

Totals: 5 FIX pages / 8 PASS pages; 10 FIX items.

## liquidity-sweep

- [FIX] The 10–20-pip / 25-pip depth rule is generalised beyond ICT's stated scope. Formula block and JSON c3 present `typical_sweep_depth := 10 to 20 pips beyond the swept level` as a general sweep criterion on timeframes M1…W, all instruments. ICT scopes it to a lower-timeframe FX chart and hedges the 25 — evidence: "on a lower timeframe chart like a 15 or 30 minute chart. you can expect a 10 to 20 pip sweep below the old low. a 30 to 50 pip stop is ideal" (`ICT-2016-LIQUIDITY-POOLS` [10:46]); "if it starts moving beyond 25 pips i think is a fair assessment below the low it's probably not just a stop run" ([11:30]); the companion "grades of 10 … 10 and 20 pit [pip] ranges above a high" is "intraday price action" (`ICT-2016-EQUILIBRIUM-DISCOUNT` [51:07]) — required change: in Formula / Math and JSON c3 add the scope verbatim: "on a lower timeframe chart like a 15 or 30 minute chart" (FX pips, intraday), and quote the hedge "i think is a fair assessment"; state that ICT gives no depth figure for H4/D/W or for non-FX instruments.
- [FIX] Example 1 arithmetic contradicts the page's own rule: "M5 wicks to 1.0879 (4 pips beyond — within the 10-20 pip typical range)". 4 pips is not within 10–20 — evidence: page line 85 vs Formula block line 31 — required change: either make the wick 10–20 pips (e.g. 1.0888, 13 pips) or delete the parenthetical; do not claim 4 pips is "within the 10-20 pip typical range".
- [FIX] Body cites `ICT-2016-MMT-FALSE-BREAKOUT` (Visual Pattern, "$109.40 is swept, moving just above the bodies of the candles", 09:50) but it is absent from `**Source IDs:**`, JSON `sources[]` and `## Citations`; the attribution text "`ICT-2016-LIQUIDITY-POOLS` folder's sibling … lecture" is also wrong — it is the Month 02 *Market Maker Trap* lecture (`raw/…MONTH-02-MARKET-MAKER-TRAP-pv2-R-STviA`), not a sibling of the Month 04 folder — evidence: "as you can see $109.40 is swept moving just above the bodies of the candles" (MONTH-02-MARKET-MAKER-TRAP-pv2 [09:50]) — required change: add `ICT-2016-MMT-FALSE-BREAKOUT` to header, JSON `sources[]` and Citations (quote + 09:50), and replace "`ICT-2016-LIQUIDITY-POOLS` folder's sibling … lecture" with "`ICT-2016-MMT-FALSE-BREAKOUT`".
- [NOTE] Definition quotes the auto-caption as-is: "if we're going to sweep by side" — the caption's "by side" is ASR for "buy side"; per FIX-BRIEF clarify in brackets: "sweep by [buy] side" (ep23 [05:16]).

## liquidity-run

- [FIX] Definition: "ICT's own **1916-origin taxonomy**" — typo for 2016 — evidence: the lecture is `ICT-2016-LIQUIDITY-RUNS` (Sep 2016); page's own Formal Criteria says "September 2016" — required change: "2016-origin taxonomy".
- [FIX] Timestamp wrong by 2 min: "it's like a hot knife through butter" cited (`ICT-2016-LIQUIDITY-RUNS`, 17:31) in Formal Criteria and Citations — evidence: "[19:33] It's like a hot knife through butter. [19:35] Very little resistance." (MONTH-1-LIQUIDITY-RUNS) — required change: 17:31 → 19:33 in both places.
- Verified OK (no change): 07:33 / 07:58 / 11:25 / 17:42 quotes; "(08:31, 10:20) only a sharp catalyst or black-swan event" — [08:31] "a very sharp economic market release … like non-farm payroll or FOMC", [10:26] "a black swan event … generally the only type of thing you see that will cut through"; "(20:15) duals" — [20:15] "having a high resistance liquidity run here, it turns into a low resistance liquidity run"; REINFORCING-LIQUIDITY [12:35]–[12:41] "So every time. A run above. An old high. Is expected. That's going to be framed. As a low resistance. Liquidity run." (whisper split across lines, verbatim); ep35 [11:44]; ep02 [42:53].

## liquidity-pool

- PASS. All seven sources verified at the cited timestamps (LP 00:50/04:26/17:19/17:59; ETS 16:13; MMT-TRENDLINE 07:35/07:58; USDCAD 10:09; NYO 00:33; ep02 21:32; ep18 19:08). Option-strike removal, third-touch trigger, alias purge all applied as the audit required.
- [NOTE] The third-touch quote is ICT's trigger for his *sell* at the high between the 2nd and 3rd touch ([08:48]), i.e. the trendline's liquidity is harvested on the third touch; the page's "ICT's own trigger is specifically the third touch" is faithful, but "A retail trendline has 2+ touches" in the same bullet is the library's wording, not ICT's — consider "a retail trendline that retail has drawn (ICT acts on the third touch)".

## equal-highs

- [FIX] Formula / Math cites `ICT-2022-MENTORSHIP-EP16` (04:13) "relatively equal, not exactly — that's why I named them relatively equal lows" as evidence, but EP16 is not in `**Source IDs:**`, JSON `sources[]` or `## Citations` — evidence: ep16 [04:13] "they're relatively equal not exactly that's why i named them relatively equal lows" (quote itself is verbatim) — required change: add `ICT-2022-MENTORSHIP-EP16` to header + JSON + Citations, or drop the EP16 sentence and rely on EP05 [15:31].
- [NOTE] Formal Criteria bullet 1 splices two packets inside one quotation: "areas where it's too clean, equal highs and equal lows in close proximity to one another… the market's going to want to run there" with cite "(18:31; `ICT-2016-EQUILIBRIUM-DISCOUNT`, 51:27–51:29)". The first half is WHAT-TO-FOCUS-ON [18:31], the second is EQUILIBRIUM-DISCOUNT [51:27]. Both verbatim; split into two quotes so each carries its own packet.

## equal-lows

- PASS. New quote WHAT-TO-FOCUS-ON [16:04] verified verbatim ("when a low is formed and another low is equally formed in close proximity to the initial one that's a big area for sell stops to pull or build up underneath those lows"); LV [13:15], LP [17:59], DTB [12:12]–[12:25], ep09 [14:47], ep16 [04:13] all verified.
- [NOTE] Formal Criteria bullet 2 / Formula `AND exists(SH between SL_1 and SL_2)` is kept without a label. The audit found "intervening" 0/0 — it is a library convention (trivially true of two swing lows), not an ICT rule; label it "(library convention — not stated by ICT)" as `equal-highs` effectively does by moving it to Common Mistakes.

## relative-equal-highs-lows

- PASS. DTB 00:52 / 02:06 / 04:27–04:37 / 12:12, LP 17:59, OTE-VOL09 01:50 (folder `…SERIES-09`), ep05 15:31, ep16 04:13 all verified; `0 < |Δ|` removed; tolerance table removed; "near-equal" aliases removed.
- [NOTE] Same unlabelled "intervening opposite pivot must exist" criterion as equal-lows — label as library convention.

## buy-side-liquidity

- PASS. LR 03:29; MMT-FALSE-BREAKOUT 03:25; LP 03:52 / 04:11 / 08:44–08:49 / 09:33; ep02 22:01; ep25 50:00 — all verified. "continuation BOS" replaced by sweep/run alternatives as the audit required.

## sell-side-liquidity

- PASS. LR 03:36; MMT-FALSE-BREAKOUT 03:34; LP 09:13–09:33; QUARTERLY-SHIFTS 34:00; ep16 04:13 — all verified. The "few pips / few ticks" number and the "close below SSL = bearish BOS" rule are removed and explicitly disclaimed.

## external-range-liquidity

- PASS. Year 2022 → 2016 with evidence; REINFORCING-LIQUIDITY 00:54–01:02 / 06:04 / 10:30–10:40 / 12:05 ("that is a run. on external. range. liquidity. on this time frame. being the daily. but on the monthly chart. it's still. internal range liquidity." — whisper-split, verbatim); ORDERBLOCKS 08:16–08:41; INTRADAY-TOP-DOWN 46:40–46:46; ep06 45:41; ep12 25:56 — all verified. "ERL take = external BOS = bias change" removed and labelled not-in-corpus with the searched terms. Range-relative classification added as the audit asked.

## internal-range-liquidity

- PASS. REINFORCING-LIQUIDITY 01:34–02:31 / 10:30–10:40; ORDERBLOCKS 08:16 / 09:15 ("entering long inside of a known range at a bullish order block at internal range liquidity"); INTRADAY-TOP-DOWN 36:56 (new, verified: "it's either going to be an internal range liquidity optimal trade entry fair value plays what that is or it's going to be external range liquidity run or basically it's turtle soup"); ep03 00:17 / 35:03; ep06 45:41 — all verified. Entry-side framing restored; bias-flip and trendline claims removed and labelled.

## liquidity-void

- PASS. LV 00:57 / 01:09 / 01:54 / 02:19–02:43 / 03:08 / 03:23; FVG-REINFORCED 05:26 / 09:43; FAIR-VALUATION 24:40; TIMEFRAME-SELECTION 46:57; ep38 04:56–05:26 — all verified. 80 % / 0.3 / FVG-containment thresholds removed; M1 contradiction applied; year 2017 → 2016.
- [NOTE] The ERA-SPLIT on refill is stated correctly with both quotes, but only under Common Mistakes; the Definition no longer mentions refill at all. Consider one sentence in Definition: "2016: 'price typically will want to revisit this porous range' (LV 01:09); 2022: 'I don't teach that … not trying to insist that these imbalances completely rebalance' (ep38 04:56–05:26)."
- [NOTE] The auto-caption spells the name "chris laurie" (ep38 [04:29], [05:26]); the prose says "Chris Lori". Fine, but per FIX-BRIEF a bracket on first mention — "chris laurie [Chris Lori]" — would make it grep-findable.

## turtle-soup

- [FIX] JSON c2 and the Formula block replicate the depth rule without its scope: "his quantification is depth: 10-20 pips typical, >~25 pips probably not a stop run" on `timeframes: M5…W` — evidence: the figure is given for "a lower timeframe chart like a 15 or 30 minute chart" and hedged "i think is a fair assessment" (`ICT-2016-LIQUIDITY-POOLS` [10:46], [11:30]) — required change: same scope wording as liquidity-sweep FIX 1 (lower-timeframe FX chart, intraday; no figure for HTF/non-FX).
- [NOTE] Visual Pattern still annotates "close back inside" / "close back above" while Formal Criteria, Formula and Common Mistakes say ICT gives no close-based rule. Change the two labels to "reverses back inside" for internal consistency.
- Verified OK: ED 32:28–32:33 / 40:20 / 52:57–53:03; TFS 40:00 / 43:46; STT 23:31–23:35 / 23:55 / 24:41 ("don't put a lot of money", page says 24:33 — within tolerance) / 24:47 / 26:02; ITD 30:06–30:19 ("sell stop raid discount entry ict version of turtle soup … street smarts book where i got the inspiration"), 30:30 ("myopic"), 32:51–32:53, 43:41–43:47, 46:40–46:53; INSTITUTIONAL-SWING-POINTS 01:37–01:52; ep05 16:03; ep07 24:56–25:34. "swing failure" alias removed from header and JSON; `Year Refined: 2022` caveat resolved with real quotes.

## stop-hunt-pattern

- [FIX] Example 2 heading "stop hunt with run-and-continue" keeps the vocabulary the page's own Formal Criteria, the audit (cross-page issue 1) and `liquidity-run` declare non-ICT ("run-and-continue" 0/0 in both corpora) — evidence: ep23 [05:39] "if i'm saying we're going to run an old high … that means we're going to run through it and continue" is the only ICT wording, and it is *run* — required change: rename to "stop hunt with run (continuation) outcome" and in the bullet "→ stop hunt was fuel" leave as is.
- [FIX] Header `**Aliases:** stop hunt, stop run pattern, liquidity grab pattern` vs JSON `"aliases": ["stop-hunt", "stop-run-pattern"]` — the writer removed "liquidity grab pattern" from JSON but not the header; and "liquidity grab" is 0/0 in both corpora (audit cross-page issue 9) and unlabelled — evidence: audit term counts "liquidity grab 0/0" — required change: either delete "liquidity grab pattern" from the header, or keep it in both places as "liquidity grab pattern (SMC)" with "not ICT's term — 0 hits in either corpus" in the Terminology box.
- [FIX] JSON c3 and Formula / Math replicate the unscoped depth rule ("quantification is depth (10-20 pips typical, >~25 pips not a stop run)") on `timeframes: M1…D` — evidence: as liquidity-sweep FIX 1 — required change: add the "15 or 30 minute chart" / FX-pip / "i think is a fair assessment" scope.
- Verified OK: ED 51:07–51:27 (ASR "pit" = pip, already bracketed on page), 40:20–40:27, 52:57–53:03; TFS 42:22, 46:50; ep02 22:30; ep03 35:55; ep05 13:32; ep38 42:28; ep40 41:48. The ERA-SPLIT terminology box is correct: raw "stop hunt" 0, 2022 ≥ 6 distinct own-voice uses verified. The "(56×)" count for "run on / out the stops" is pre-existing text, not a writer addition.

## Cross-page / scope

- No page references the owner's engines, studies or projects; the one "engine" word (`liquidity-run` Common Mistakes, "A library or engine that labels…") is generic. No CHoCH/BOS presented as ICT's; remaining BOS mentions are explicit "not in the corpus" disclaimers or link targets.
- The unscoped 10–20 / 25-pip rule now appears identically on three pages (sweep, turtle-soup, stop-hunt) and in their JSON criteria — fix once in `liquidity-sweep` and mirror the scope sentence on the other two.
- Years: all five 2017→2016 and both 2022→2016 corrections applied; header == JSON on all 13 (lint 0).

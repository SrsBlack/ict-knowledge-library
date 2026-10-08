# Review — cluster ote-risk (2026-10-08)

Reviewer re-grepped every quote below against `raw/*/report.md` and `m22-captions/ep*.txt`. Lint: `problems: 0`.
Packet shorthand as in `ote-risk.md` (PRIMER = `ICT-2017-OTE`, VOLnn = 2020 series, SCALPING, PAL, M1-EQ-DISC, GSA, NO-FEAR, MITIGATE, MM, REDUCE-RISK, HP-DAYTRADE, OB).

| page | PASS / FIX | issue count |
|---|---|---|
| ote-overview | FIX | 4 |
| ote-rules | FIX | 5 |
| ote-62 | FIX | 3 |
| ote-705 | FIX | 2 |
| ote-79 | PASS | 0 |
| fib-anchoring | FIX | 1 |
| fib-62 | FIX | 1 |
| r-multiple | FIX | 2 |
| risk-per-trade | FIX | 2 |
| position-sizing | PASS | 0 |
| stop-placement-by-pd-array | FIX | 4 |

**Totals:** 2 PASS, 9 FIX, 24 FIX items.

## Extra-scrutiny verdict: ote-rules item 6 (2020-series stop = leg-origin extreme)

Checked every stop line in VOL01/02/04/05/09/10/14/15/16/18/19/20 + EURUSD-EX. The reversal of the Aug-2026 "fixed-pip branch" is **justified — no 2020-series stop contradicts a leg-origin derivation**, but the page overstates how many cases *state* it:

- **Explicit derivation (3):** VOL01 [37:04–37:14] "this low is where your stop would have to be below that. Okay, so the lowest candle, what we're anchoring the fib on, the low is 64, 34, and 7-fifetz. So you can do a stop at 64, 30"; VOL14 [05:38] "using a 20 pip stop loss. That would take us above this high"; EURUSD-EX [02:50–03:09] "using a 20 pip stop loss that would put your stop just about in this high here."
- **Deictic referent that reads as the leg extreme (4):** VOL05 [01:54] "Stop would be above the high here" (after "here's the high. We trade down to this low"); VOL09 [02:46] "our entry stop would have to be at this high" (after "This high to this low price retraces"); VOL15 [01:40] "a 10 pip stop loss below this low here"; VOL20 [01:09] "You do 30 pip stop loss at the old price. It's high" [ASR; = old price high].
- **Indeterminate from the transcript (1):** VOL04 [05:44–05:46] "79% retracement level lays right on top of that level here. Your stop will be above here"; [06:48] "Stop would be above here." No textual referent — frame-dependent.
- **Pip/tick count only, no anchor stated (5):** VOL02 [04:09], VOL10 [02:12], VOL16 [07:58], VOL18 [02:42], VOL19 [02:13].

Nuance the page flattens: VOL01's stop is ~5 pips *below* the anchor candle's **wick** low (6434.7 → 6430), and SCALPING is +5 pips; "the same stop as the Primer" ("exactly at this low") is the same *reference*, not the same *price*.

## ote-overview
- [FIX] Paraphrase passed off as a quote — page: `ICT-2020-OTE-EURUSD-EXAMPLE`'s 20-pip stop is "chosen "to reach the leg high" (02:50)". — evidence: "using a 20 pip stop loss that would put your stop just about in this high here" (ICT-2020-OTE-EURUSD-EXAMPLE [02:50–03:09]) — required change: replace the quoted phrase with the verbatim line and cite 02:50–03:09.
- [FIX] Altered quote — page prints "the low is 64, 34, and 7-fifths"; the transcript says "7-fifetz" (Whisper for "pipettes"). "Fifths" is a different, wrong word. — evidence: "the low is 64, 34, and 7-fifetz" (ICT-2020-OTE-VOL01 [37:10]) — required change: quote as-is, "7-fifetz [pipettes]".
- [FIX] Stale era-fork in Visual Pattern: "SL: leg-origin low (Primer) OR a fixed pip stop (2020 series) — era-fork." contradicts the rewritten Formal Criteria, Formula comment and JSON c4 on the same page. — evidence: VOL01 [37:04–37:14] (above) — required change: "SL: leg-origin extreme (fib 1.0); the 2020 series reports the same stop as a pip/tick distance."
- [FIX] Non-verbatim Primer quote in the rewritten stop bullet: "my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that". — evidence: "my stop will be exactly at this low low not 10 pips or five pips below that it's gonna be rated that low" (ICT-2017-OTE [12:32–12:39]) — required change: "my stop will be exactly at this low… not 10 pips or five pips below that" (12:32–12:39). Same string also sits on ote-rules, ote-79, fib-62, stop-placement — fix all five identically.
- [NOTE] 40:30 quote silently drops "when we have that anticipate some measure of buying" (needs an ellipsis); 26:39 quote drops "you" ("I'm not teaching you ICT kill zones"). Trivial but not verbatim.
- [NOTE] Pre-existing unsourced items left in Common Mistakes: "Use a buffer ±0.5–1 pip on FX" (no ICT number; also on ote-705) and "HTF reversal context (CHoCH/MSS)" — CHoCH is an SMC term, should carry "(SMC)".
- [NOTE] "The 2020 applied material states the same stop" is loose: VOL01's 6430 is ~5 pips below the anchor candle's wick low, not "exactly at" it (see verdict above). Say "same reference (leg-origin extreme), rounded below it".

## ote-rules
- [FIX] Item 6 overstates the evidence. (a) Banner: "every located 2020-series stop is derived from the leg-origin extreme and reported as the resulting pip/tick distance" — five volumes state only a count (VOL02/10/16/18/19) and VOL04 has no textual referent. (b) "The same anchor-to-origin pattern recurs with its own distance stated: VOL04 (05:46) 'your stop will be above here'; VOL05 (01:54) …; VOL09 (02:46) …" — none of those three states a distance. — evidence: "79% retracement level lays right on top of that level here. Your stop will be above here." (ICT-2020-OTE-VOL04 [05:44–05:46]); "Stop would be above the high here." (VOL05 [01:54]); "as our entry stop would have to be at this high." (VOL09 [02:46]) — required change: banner → "no located 2020-series stop contradicts the leg-origin reading; it is stated explicitly in VOL01, VOL14 and the EURUSD example, by deictic reference in VOL05/09/15/20, and VOL04's 'above here' is frame-dependent"; delete "with its own distance stated" for VOL04/05/09.
- [FIX] "7-fifths" — as ote-overview. — evidence: ICT-2020-OTE-VOL01 [37:10] "7-fifetz" — required change: "7-fifetz [pipettes]".
- [FIX] JSON c2 still reads "stop_placed (leg_origin OR fixed_pip)" — contradicts item 6, Formula block and c4. — required change: "stop_placed (leg_origin_extreme; 2020 series reports it as a pip/tick distance)".
- [FIX] Citations line "2020-series stop distances, derived from the leg-origin extreme (item 6): `ICT-2020-OTE-VOL02`, `ICT-2020-OTE-VOL10`, `ICT-2020-OTE-VOL19` (10 pips); `ICT-2020-OTE-VOL20` (30 pips)" contradicts item 6's own text, which files VOL02/10/19 as "counts with no re-stated anchor". — evidence: "Our stop will be at 106.215. So it's a 10 pip stop." (VOL02 [04:09]); "using a 10 pip stop" (VOL10 [02:12]); "10 pip stop loss which takes us at 108.60" (VOL19 [02:13]) — required change: "2020-series stop distances with no stated anchor (item 6): VOL02/10/19 (10 pips)"; keep VOL20 under "stated at the old high".
- [FIX] Non-verbatim Primer quote "[or] 5 to 10 pips" in the rewritten Primer bullet — see ote-overview item 4 for the verbatim line.
- [NOTE] VOL20 quote repaired to "a 30 pip stop loss at the old price[-action] high"; transcript is "You do 30 pip stop loss at the old price. It's high" — quote as-is with "[= old price high]".
- [NOTE] Mechanical-checker miss: "wherever 62 percent retracement level is, that's your entry, that's your old high, and you add five pips to that" omits "price" ("that's your entry price") — ASR-trivial, add the word. VOL03 "static time" is at 03:44, page cites 03:38 — within tolerance.

## ote-62
- [FIX] Example 2 heading "0.62 entry with a fixed stop (`ICT-2020-OTE-VOL14`…)" restates the branch the page's own Formula block says was mis-read. — evidence: "using a 20 pip stop loss. That would take us above this high" (VOL14 [05:38]) — required change: heading → "0.62 entry, leg-origin stop reported as 20 pips".
- [FIX] Visual Pattern: "leg_start ── 1.0 ← SL (Primer branch); the 2020 branch uses a fixed stop" — stale. — required change: "← SL (fib 1.0); the 2020 series reports the same stop as a pip count".
- [FIX] Common Mistakes "Unrealistic R:R expectations… or use the stop rule the same source pairs with the entry" — implies VOL14 pairs 0.62 with a different stop rule; the page's Formula block now says the opposite ("ICT does not pair 0.62 with a different, tighter stop"). — required change: delete the clause after "calibrate position size".
- [NOTE] Definition quote "at or very close to the 62%… I'm not going to demand 79%" is spliced from [12:18–12:26] and [18:52] (audit flagged on ote-overview; same splice here and on ote-79) — add both timestamps.
- [NOTE] ANTICIPATING [20:01] reads "62% of tracing level"; page silently normalises to "62 % retracement level" — fine as [bracketed] clarification, not as a silent repair.

## ote-705
- [FIX] JSON c3 `"SL == leg_start (fib 1.0) OR fixed_pip", "strength": "era-fork; see ote-rules item 6"` — ote-rules item 6 now says there is no fork. — required change: `"SL == leg_start (fib 1.0); 2020 series reports it as a pip/tick distance"`, drop "era-fork".
- [FIX] Visual Pattern "← SL (Primer branch); the 2020 branch uses a fixed stop" — stale, as ote-62. — required change: as ote-62.
- [NOTE] Definition says ICT "names it the 'sweet spot' twice" while the page now cites four instances (PRIMER [11:11], VOL03 [04:28], DRILL-USDJPY [02:37], M1-EQ-DISC [24:02]) — say "repeatedly" or list them.
- [NOTE] "they differ by ~9%" — 8.7 percentage points absolute, 14 % relative (audit nit); write "8.7 points".
- [NOTE] "Use buffer of ±0.5–1 pip" — no ICT number; label as reader convention.

## ote-79
PASS. Audit's one MINOR-FIX (0.79→0.80 tolerance, [12:26–12:32] and LONDON-DEMO [04:11–04:17]) applied verbatim; Year Introduced 2016 = JSON; M1-EQ-DISC [37:37] verified; header == JSON == Citations.
- [NOTE] Carries the pre-existing non-verbatim "[or] 5 to 10 pips" Primer quote and the 12:18/18:52 splice — apply the same wording fix as ote-overview when that page is touched.

## fib-anchoring
- [FIX] New claim not supported by the source: Definition point 3 heading "A volatility-conditioned exception on the retracement fib itself", JSON c8 "retracement_fib_anchor MAY switch to wick around a scheduled high-volatility event", and Formula "volatility_exception := wick anchors replace body anchors" all file ep23 as a retracement-fib rule. The fib ICT draws on wicks in that passage is a **target projection**, not a retracement — the page then contradicts its own Common Mistakes bullet ("no source … states a wick anchor for a retracement fib"). — evidence: "now i'm going to use the wix … i'm going to draw it from the low up to the high i'm looking for upside objectives okay so low up to high here's one objective" (ep23 [12:34–13:03]) — required change: re-title point 3 "A volatility-conditioned anchoring statement, demonstrated on a projection fib"; c8 → "fib_anchor MAY switch to wick around a scheduled high-volatility event (stated generally; shown on a projection fib, ep23)"; same wording in the Formula comment and the Formal Criteria bullet ("a volatility-event exception on the retracement fib itself" → drop "on the retracement fib itself").
- [NOTE] ep23 quote silently repairs the caption's "lowest opener close" to "lowest open or close" — quote as-is with "[open or close]" per the fix brief.
- [NOTE] Formal Criteria "the separate dealing-range/premium-discount fib, which is wick-anchored throughout" — "throughout" rests on one clause (ep22 [49:13]); say "per ep22".
- [NOTE] Audit's era note not carried: in 2022 the swing projection is body-anchored too — "you take your fibonacci and you anchor it to the highest body it could be open or closed … notice i'm not putting on the high here" (ep16 [08:47–09:15]); worth a line beside point 1's 2017 "sometimes wicks" carve-out.

## fib-62
- [FIX] Newly added non-verbatim Primer quote in the Example correction: "my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that" (`ICT-2017-OTE`, 12:32). — evidence: "my stop will be exactly at this low low not 10 pips or five pips below that" (ICT-2017-OTE [12:32–12:39]) — required change: "…not 10 pips or five pips below that".
- All other 2026-10-08 additions verified verbatim: M1-EQ-DISC [29:25], [41:36–41:48]; PRIMER [18:46–18:52]; VOL09 [02:41]; SCALPING [13:32–13:40]; PAL [04:07–04:15]. Era-split stated both ways; sibling ote-62 now agrees.

## r-multiple
- [FIX] Internal contradiction: Common Mistakes "Targeting 1R or less. Setups with TP ≤ 1R have no edge after slippage and commission" vs the rewritten Definition and Citations, which record ICT accepting 1:1. — evidence: "if it's one to one, it's still good" (ICT-2020-OTE-VOL01 [41:51–41:52]); "it only requires 1.5% risk and it only requires 1 to 1 ratio to do it" (GSA [15:39–15:45]) — required change: delete the bullet or rewrite as "ICT's own floor is the breakeven curve (1:1 at 50 % accuracy), not a fixed R minimum".
- [FIX] `ICT-2017-OTE` ([17:17], [18:18]) and `ICT-2020-OTE-VOL01` ([41:51]) are quoted in the Definition but appear in neither the Source IDs header, the JSON `sources[]`, nor `## Citations`. — required change: add both IDs to header + JSON and a Citations line for each (AGENTS.md ingest step 3: append the Source ID and a citation).
- Verified: "$750 or 15% return" is verbatim at NO-FEAR [09:57–10:04]; the page's arithmetic note is correct ($1,500 − $700 = $800 = 16 % of $5,000; ICT's $750 = 15 % is internally consistent with his own $50 slip). ep18 [13:20] quote and the "student's question about a low win rate" framing are verbatim ("What if your win rate is really, really low? Can you still double an account?"). ep09 [22:07], ep17 [23:20], ep25 [41:10] verified.
- [NOTE] Definition cites "better than two to one…" to 18:18; the clause starts at 17:17 — cite 17:17–18:18.

## risk-per-trade
- [FIX] "There is no single number; the figure varies by year, **account purpose**, and the trader's stated experience level" reintroduces the account-type axis the same page (and JSON c2: "not account purpose") just removed. The real second axis in the evidence is trading horizon (1.5 % for swing setups, REDUCE-RISK [17:13]; 1 % of a 30 % base for position trading, MM [06:30–06:36]). — required change: "varies by year, trading horizon (swing/position vs intraday), and stated experience level".
- [FIX] `ICT-2017-OTE` is quoted in the Definition ("we'll say it's a half a percent", [16:01]), the table and `## Citations`, but is missing from the Source IDs header and the JSON `sources[]`. — required change: add `ICT-2017-OTE` to both.
- Every percentage verified verbatim at the cited stamp: GSA [03:45] 2 %; NO-FEAR [14:33–14:38] 1 %, [15:43] 0.5 %; PRIMER [16:01] 0.5 %; MM [06:30–06:36] 1 % of 30 %; REDUCE-RISK [17:13], [18:54] 1.5 %; ep07 [04:44] "less than 1% about a half percent or a quarter percent" and "I like 3 and a half%"; ep03 [48:47] 4.5 %; ep41 [22:18] 1 %, [28:50] 2 %, [31:37–32:04] 50 %-recovery gate, [32:04] 0.25 % floor; MITIGATE [05:26–05:33] 2→1→0.5 %. "Prop firms cap daily loss" removed. Year 2016 = JSON.
- [NOTE] 1.5 % is also a 2016 figure — "it only requires 1.5% risk" (GSA [15:39]); "your risk per trade is going to be 1.5% or $15" (GSA [17:04]) — table row "1.5 % | swing setups, REDUCE-RISK" should add GSA (6 %/month model).
- [NOTE] Example 1 "$50,000 funded account" is harmless but echoes the removed account-type framing; "a initial loss" is rendered "an initial loss" (trivial).

## position-sizing
PASS. ep41 [22:18–23:52] walkthrough verified line by line (37.54¾ / 45¾ / 9 points / 11 / $50 / micros $5 / "how many fives can you go into 11 with it two"); ep01 [24:14] $12.50/tick; ep40 [14:50]; GSA [17:04]. Non-ICT pip values clearly labelled; "never sized retroactively" removed; Year 2016 = JSON; header == JSON == Citations.
- [NOTE] Example 1 labels the setup "NY AM SB" — the Silver Bullet name that sibling r-multiple says post-dates the corpus; rename to a generic "H1 bullish OB" so the cluster is consistent.
- [NOTE] 22:18 quote drops "that's one hundred dollars" between "figure of one hundred" and "that's what one percent…" without an ellipsis.
- [NOTE] "round DOWN … never up" — "never up" is the writer's inference; ICT says "you can't" trade a mini at that risk.

## stop-placement-by-pd-array
- [FIX] Mis-applied quote: ep06 [35:31] "just go one tick above that and removes all the doubt" is about where to place the **entry** limit, not the stop; the page uses it twice as a stop-buffer figure (Definition buffer list "2022, tightest: …"; FVG paragraph "the easiest form is 'just go one tick above that'"). — evidence: "so if it trades back this candle's high plus i don't know one handle or one tick maybe two ticks whatever whatever you believe is an ideal entry for you the easiest one to is just go one tick above that and removes all the doubt" (ep06 [35:31]) — required change: remove the 35:31 quote from both places; the stop-side buffer evidence is ep25 [43:39] "one tick two ticks above that that's sufficient enough" and ep07 [16:04] "just below that maybe one one tick".
- [FIX] FVG example and Visual Pattern mislabel the reference candle. Example 2 and the diagram take "candle 1's low" and caption it "the DISPLACEMENT candle's own extreme". Candle 1 is the swing-extreme candle; the candle that *creates* the gap is candle 2. ICT offers both, as the page's own table row says, but the example/diagram collapse them into one wrong label. — evidence: "where's your stop loss going to be above the high of candle number two or you can use above candle number one which creates a swing high okay whichever one you can afford" (ep06 [36:06]); "place your stop right above can[dle] number one or you can put it above candle number two" (ep06 [17:09–17:38]) — required change: in Example 2 and the diagram, label candle 2's extreme "the creating/displacement candle (tighter option)" and candle 1's extreme "the swing extreme (wider option)"; keep candle 1 as the worked choice if desired but drop "DISPLACEMENT" from its caption.
- [FIX] Newly added non-verbatim Primer quote "not 10 pips [or] 5 to 10 pips below that" (OTE row correction). — evidence: ICT-2017-OTE [12:32–12:39] "not 10 pips or five pips below that" — required change: as fib-62.
- [FIX] `ICT-2020-OTE-VOL01` is quoted in Common Mistakes ("not jamming it up too tight…", [53:14–53:19]) but is absent from the Source IDs header, JSON `sources[]` and `## Citations`. — required change: add to all three.
- Verified verbatim: ep12 [42:53]; ep13 [25:05]; OB [01:53], [10:44]; MITIGATE [04:49]; HP-DAYTRADE [15:15], [15:19], [15:49], [15:58], [24:37], [25:06] and the 40-pip rules [14:49], [24:26]; MM [15:45]; REDUCE-RISK [23:36]; M1-EQ-PREM [20:49]; ep22 [17:30], [18:00]; ep25 [41:46], [43:39]; ep07 [16:04]; ep38 [42:52]; ep06 [17:09–17:38]. "2–5 pips" removed; breaker row marked NOT IN CORPUS; Year 2016 = JSON.
- [NOTE] Definition calls the 2017 day-trade rules "fixed-pip BY SETUP TYPE, not structural at all", yet they reference structure ("10 pips under the lowest low of the day", "30 pips below that low") with a flat buffer — and the page's own buffer list treats them as buffers. Soften to "structural reference + flat setup-keyed buffer".
- [NOTE] Formula/Example 1 use "1 pip" for the "2022 tight convention" whose stated unit is "one tick, two ticks"; on FX a tick is a pipette. Say "1–2 ticks (1–2 pipettes on FX)".
- [NOTE] M1-EQ-PREM quote adds "[to take you out]" in brackets; the transcript already says "for spread to take you out" — drop the brackets.

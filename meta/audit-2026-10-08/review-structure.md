# Review — cluster STRUCTURE (rewrites of 2026-10-08)

Reviewer: structure review gate (read-only). Every quote below was re-grepped in `raw/*/report.md` or
`meta/audit-2026-10-08/m22-captions/ep*.txt`; timestamps are the matching paragraph's own. `python tools/lint.py`
(read-only) reports `problems: 0`; header `Source IDs` == JSON `sources[]`, header years == JSON years, all 10
sections present and all relative links resolve on all 12 pages.

Quote-miss file verdicts for this cluster (all ASR/punctuation-trivial, none fabricated, none paraphrase-as-quote):
swing-high ep12 [41:23] (em-dashes added; "rebalance and imbalance" → "an imbalance" normalised without brackets);
swing-low ep12 [16:58]/[14:15] ("a imbalance", "immed term" normalised without brackets); displacement-definition and
displacement-strength-criteria ep24 [23:30] (caption word "oh" dropped — it is "oh[ld] low", see below);
equilibrium-definition FILLING-NUMBERS [11:53]–[11:59] (two segments joined, "flouts" → "flout's") and ep41 [18:21]
("tracement" → "retracement"); mean-threshold ORDERBLOCKS [10:08]+[10:13] (two adjacent segments joined).

| page | PASS / FIX | issue count |
|---|---|---|
| 01-market-structure/mss.md | PASS | 0 FIX, 2 NOTE |
| 01-market-structure/mss-vs-choch.md | FIX | 3 FIX, 1 NOTE |
| 01-market-structure/swing-high.md | FIX | 2 FIX, 2 NOTE |
| 01-market-structure/swing-low.md | FIX | 2 FIX, 1 NOTE |
| 01-market-structure/bos-bullish.md | FIX | 1 FIX, 2 NOTE |
| 01-market-structure/bos-bearish.md | PASS | 0 FIX, 2 NOTE |
| 01-market-structure/range-expansion.md | FIX | 1 FIX, 2 NOTE |
| 09-displacement/displacement-definition.md | FIX | 1 FIX, 1 NOTE |
| 09-displacement/displacement-strength-criteria.md | FIX | 1 FIX, 2 NOTE |
| 05-pd-arrays/dealing-range.md | FIX | 1 FIX, 2 NOTE |
| 27-equilibrium/equilibrium-definition.md | PASS | 0 FIX, 1 NOTE |
| 27-equilibrium/mean-threshold.md | FIX | 1 FIX, 2 NOTE |

Totals: 3 PASS · 9 FIX · 13 FIX items.

## mss.md

All audit findings applied (CHoCH nesting removed, FVG requirement removed, close rule era-split, Year 2016, continuation/reversal
both covered). All 14 quotes verified verbatim at the cited packet/episode and timestamp (ep03 [02:20] [02:51]; ep06 [19:05] [19:37]
[20:29]; ep10 [37:43]; ep12 [31:09]; BREAKER-BLOCK [06:56]; OPEN-FLOAT-L12 [07:38] [07:45]; SECRETS-SELECTING-HIGH [42:03];
ICT-2017-OTE [28:02] [28:04] [40:30]–[40:56]). `ICT-2017-HIGH-REWARD-SETUPS` misdating note confirmed in SOURCES.md line 50.

- [NOTE] Formal Criteria bullet 5 and Common Mistakes point to "[swing-high] Common Mistakes" for the higher-order-break claim — that
  content lives on bos-bullish.md (ICT-2017-OTE [34:35]–[35:30]), not swing-high. — required change: point the two cross-refs at
  bos-bullish Common Mistakes.
- [NOTE] `ICT-2017-QUARTERLY-SHIFTS` is cited with no timestamp or quote. — evidence: "i teach that there is a market structure shift
  that takes place every three to four months." (MONTH-05-QUARTERLY-SHIFTS-IPDA [05:01]) — required change: add `[05:01]` + quote to
  the Citations line.

## mss-vs-choch.md

Extra-scrutiny item (break MORE significant than shift) — VERIFIED on ep03: "it's not necessarily a break in market structure that
leads to prolonged multi-day movement" (ep03 [02:20]); "when i'm gonna lean on that term market structure break it means a little
bit more in context versus an intraday shift in market" (ep03 [02:51]). ep12 [31:09] is supporting but not terminological (see NOTE).

- [FIX] Definition: "used interchangeably by careless teaching of his material" misreads the quote — ICT is announcing HIS OWN usage,
  not criticising others. — evidence: "i see a lot of people try to teach my concepts it'll talk about market structure breaks or
  shifts and we'll use that term interchangeably but for intraday i want you to think about intraday market structure shifts"
  (ep03 [02:20]) — required change: replace "used interchangeably by careless teaching of his material" with "and says he will use
  them interchangeably himself".
- [FIX] Example B over-corrects: "Same M15 event, 5-pip body, no FVG … ICT's own words: still a valid shift — no displacement or FVG
  gate exists in either corpus". The 2022 corpus DOES state a displacement preference, and a thin wick-through is exactly what ICT
  calls unconvincing; this also contradicts mss.md's own 2022 bullet. — evidence: "whereas if we just go through this low a little
  bit like a wick and come back up um that to me is not all that convincing i want to see that it has absolutely displaced and then
  the candle closed" (ep06 [19:37]); "it's got to be energetic it can't be a little lethargic little move" (ep06 [19:05]) — required
  change: rewrite Example B as "2016-17: valid shift on the trade-through; 2022: ICT would call a lethargic 5-pip wick-through
  'not all that convincing' (ep06 [19:37]) — a strength preference, still not an FVG gate (ep10 [37:43])"; delete "no displacement
  or FVG gate exists in either corpus".
- [FIX] Year Introduced 2016 (header + JSON) but no 2016 source is on the page — earliest cited is QUARTERLY-SHIFTS (Month 05 =
  Jan 2017). — evidence: "so we look at the market with a quarterly perspective and allow the next shift in market structure to
  unfold." (MONTH-02-SECRETS-SELECTING-HIGH [42:03], Oct 2016 = `ICT-2017-HIGH-REWARD-SETUPS`, misdated ID per SOURCES.md) —
  required change: add `ICT-2017-HIGH-REWARD-SETUPS` [42:03] to Source IDs, JSON sources and Citations with the Oct-2016 note.
- [NOTE] Formal Criteria bullet 2 presents ep12 [31:09] as a shift-vs-break distinction; the passage contrasts "a significant break
  in market structure" (break below a return low) with "it took out a short-term low" and never uses the word "shift". — required
  change: label it "scope evidence (significant break vs. short-term-low take-out)", keep ep03 as the terminology source.

## swing-high.md

3-bar rule, wick basis, n+1 confirmation, Williams-fractal rejection, 4th-candle wrinkle, Larry Williams line and ep12 two-class ITH
all verified verbatim. Year 2016/2022 consistent.

- [FIX] Mis-citation: the ITH route-1 quote "a head and shoulders top formation" is attributed to `ICT-2017-INSTITUTIONAL-SWING-POINTS`
  "via `ICT-2017-OTE` [34:20]–[34:35]"; it is in neither — it is in `ICT-2017-OPEN-FLOAT-L12`, which is not on the page. The OTE
  Citations line also claims the "head and shoulders" framing. — evidence: "term high is any high that has a short-term high to the
  left of it and to / the right of it think of it like a head and shoulders top formation every time you / see a intermediate term
  high that has a lower intermediate term high to the left of / it and intermediate term high to the right of it that's actually a
  long-term high" (MONTH-05-OPEN-FLOAT [20:15]–[20:31]); ICT-2017-OTE [34:20]–[34:27] actually says "a high that has two lower highs
  on / either side of it it makes that high in the middle a significant high and as it nests out" — required change: cite
  `ICT-2017-OPEN-FLOAT-L12` [20:15]–[20:31] for route 1 and the LTH tier (add to Source IDs, JSON, Citations); reword the OTE
  Citations line to the "two lower highs on either side … nests out" wording; drop "via".
- [FIX] Example 3 and the Visual Pattern sentence invert ICT's route 2. The page says an existing STH "later trades back up and
  rebalances the imbalance left at that high". ICT's rule is that the high PRINTED BY the move that trades up into (rebalances) an
  imbalance is immediately an ITH — the imbalance is elsewhere, not "at that high"; swing-low.md Example 2 states the mirror
  correctly. — evidence: "or and this is the main one here it trades back up to rebalance and imbalance that immediately becomes an
  interm term high" (ep12 [41:23]); mirror: "anytime a imbalance like this big candle up is rebalanced that becomes an intermediate
  term low" (ep12 [16:58]) — required change: Example 3 → "Price rallies up into a prior imbalance (e.g. a bearish FVG) and turns
  down; the high printed by that rebalancing move is immediately an ITH, whether or not it has lower STHs beside it (ep12 [41:23])";
  Visual Pattern sentence → "An ITH can also be the high formed when price trades up to rebalance an imbalance".
- [NOTE] ep12 [41:23] quote is normalised ("rebalance an imbalance", "intermediate term high"); caption reads "rebalance and
  imbalance … interm term high" — put the corrections in brackets per the fix brief.
- [NOTE] Related Concepts describes external-structure as "the LTH/LTL swings that define the larger range itself" while
  dealing-range.md now rejects LTH/LTL bounding; align the one-liner (e.g. "higher-order swings; see dealing-range for ICT's actual
  range anchors").

## swing-low.md

3-bar rule, wick basis, close confirmation, Larry Williams line, ep12 rebalance quotes verified.

- [FIX] ITL route 1 (geometric) is evidenced with ep10 [18:04], which is a plain 3-candle SWING-LOW definition, not an
  intermediate-term-low definition. — evidence: "it creates a swing low that means a low with a higher low to the right of it and a
  higher low to the left of it so it's three candles that make up a swing" (ep10 [18:04]); the real ITL sources: "now invert that
  and / you'll have the same thing that would be said for an intermediate term low or a long-term low" (MONTH-05-OPEN-FLOAT
  [20:36]–[20:42]); "intermediate term low has a higher short-term low to the right of it and a higher short-term low to the left of
  it" (ep12 [14:15]) — required change: cite `ICT-2017-OPEN-FLOAT-L12` [20:36]–[20:42] and/or ep12 [14:15] for route 1; add
  OPEN-FLOAT-L12 to Source IDs/JSON/Citations; keep ep10 [18:04] only under the 3-bar definition bullet.
- [FIX] Year Introduced 2016 (header + JSON) but every source on the page is Jan 2017 (INSTITUTIONAL-SWING-POINTS, Month 05) or 2022.
  — evidence: "this is why i do not use the williams fractal that requires five candles." / "i only need three candles."
  (MONTH-1-EQUILIBRIUM-VS-PREMIUM [11:53]–[11:58], Sep 2016) — required change: add `ICT-2016-EQUILIBRIUM-PREMIUM` [11:53]–[11:58]
  to Source IDs/JSON/Citations (or change Year Introduced to 2017 in both places).
- [NOTE] ep12 [14:15] and [16:58] quotes normalised without brackets ("this intermediate term low" for "this immed term low";
  "an imbalance" for "a imbalance").

## bos-bullish.md

BOS/term-absence, continuation+reversal, higher-order-break-more-significant, internal/external = liquidity, Year 2016 all applied
and verified (FAIR-VALUATION [08:29]; LIQUIDITY-RUNS [16:32]; OTE [28:02] [28:23] [34:35]–[35:30] [40:37]–[40:56]; FIBER-OTE-NYO
[02:46]; REINFORCING-LIQUIDITY [02:42]).

- [FIX] Formal Criteria bullet 2 files ep02 [27:37] under "2016-17: called on the trade-through" with the invented gloss
  "re-teaching 2016-17 material". ep02 is the Jan-2022 episode; nothing in it says it is re-teaching 2016-17. — evidence: "the market
  creates a short-term low here here and then it breaks below that this is key this is called a break in market structure"
  (ep02 [27:37]) — required change: delete "re-teaching 2016-17 material"; move the quote to a 2022 bullet ("even in 2022 ICT names
  the plain trade-through a break …"); leave FAIR-VALUATION [08:29] and LIQUIDITY-RUNS [16:32] as the 2016 evidence (they name the
  event but state no close/trade-through rule — say so).
- [NOTE] `ICT-2016-REINFORCING-LIQUIDITY` [02:42] is quoted in Common Mistakes but is not in Source IDs / JSON / Citations — add it.
- [NOTE] Tags still carry `continuation` although the page's thesis is "no continuation-only restriction" — drop the tag.

## bos-bearish.md

Mirror findings applied. OPEN-FLOAT-L12 [07:38]–[07:45], ep12 [31:09], USDX-SMT (= MONTH-03-INSTITUTIONAL-MARKET-STRUCTURE)
[04:59]–[05:05], OTE [34:35]–[35:30] verified verbatim; Year 2016 consistent.

- [NOTE] Common Mistakes "Stale swing low. Always use the most recent confirmed swing low — but note breaking an older, higher-order
  low is the MORE significant event" contradicts itself in one bullet — required change: reword to "the most recent swing low is the
  default reference; a break of an older, higher-order low is a more significant event, not a disqualified one".
- [NOTE] Tag `continuation` — same as bos-bullish.

## range-expansion.md

Year 2016, four-condition framework, equilibrium-leaving definition, order-block coupling, K/70 % removal, contraction-as-volatility-
filter all applied; all ELEMENTS-TRADE-SETUP, ESSENTIALS-DAYTRADING [30:17], HOW-MARKET-MAKERS [15:28], KEYS-SELECTING-MARKETS
[21:27]/[21:37] quotes verified.

- [FIX] Year Refined 2022 (header + JSON) with no 2022 source anywhere on the page — all four sources are Sep 2016–Apr 2017. —
  evidence: latest cited material is "range expansion on a weekly chart is a gold mine" (MONTH-08-ESSENTIALS-DAYTRADING [30:17],
  Month 08 = Apr 2017) — required change: set Year Refined 2017 in header AND JSON, or add a real 2022 citation.
- [NOTE] JSON `timeframes` is a prose string `["any — ICT applies it from weekly down to intraday"]`, not TF tokens — use a list such as
  `["M5","M15","H1","H4","D","W"]` and keep the prose in the Timeframes section.
- [NOTE] The MARKET-EFFICIENCY-PARADIGM quote "after the high or low is formed, the range will start expanding" sits at [15:28], not
  [15:25] (within tolerance; the Citations range [15:24]–[15:28] is right).

## displacement-definition.md

2016-17 "price imbalance"/HTF sense era-split stated; all numeric thresholds removed; FVG-after-displacement direction corrected;
Year 2016. All 2016 and 2022 quotes verified (LIQUIDITY-VOIDS [01:54]; INSTITUTIONAL-SPONSORSHIP [12:10]–[12:13]; ORDERBLOCKS
[04:45]–[04:49]; ep05 [20:14] [20:40]; ep06 [19:05] [20:58] [21:29] [23:55] [24:25]; ep10 [37:15]–[37:43]; ep19 [15:16]; ep24
[23:30]; ep40 [08:56]).

- [FIX] Timeframes: "the 2022 usage is taught mostly on lower, entry timeframes (M1–M5 in the worked examples)" is a writer addition
  not in the audit and not quote-backed; the ep06 worked example is a 15-minute chart (caption mentions "15 minute" 8×, "one
  minute" 5×, "five minute" 3×) and ep05 works from a daily chart to 15-minute. — required change: replace with "taught on intraday
  charts (15-minute with 1–5-minute drill-downs in the ep05/ep06/ep10 examples)" or delete the parenthetical.
- [NOTE] ep24 [23:30] quote drops the caption word "oh": caption reads "melted didn't do anything above that oh low there was no
  displacement no energetic move"; the preceding paragraph shows "oh low" = "old low" ("it's got to trade back above this old low
  it's got to have displacement above that did it happen here no", ep24 [22:52]) — write "above that oh[ld] low".

## displacement-strength-criteria.md

5-factor score, bands, "Year Refined 2024" and "weak/moderate/strong" removed; binary energetic-vs-anemic test stated with verified
quotes (ep05 [20:40]; ep06 [19:05]; ep24 [23:30]; ep40 [08:56] incl. "meaningful displacement").

- [FIX] Example 1: "Price approaches an old high, breaks it, but 'melted…'" — the ep24 passage is the opposite geometry: sell stops
  are run below a low and price fails to displace back ABOVE AN OLD LOW. — evidence: "they go down run out the sell stops traders
  are caught in then what what's the next logic we got to look for displacement it's got to trade back above this old low it's got
  to have displacement above that did it happen here no" (ep24 [22:52]) → "melted didn't do anything above that oh low there was
  no displacement no energetic move" (ep24 [23:30]) — required change: rewrite Example 1 as "sell-side stops run; price returns to
  the old low but 'melted…' — no displacement above it, so no long idea".
- [NOTE] `ICT Confidence: disputed` — under the fix brief "disputed" means the corpus contradicts the page's claims; after the rewrite
  every definitional claim is quote-backed and the contradicted material is gone. Either set `high` (keeping the history sentence)
  or state on-page what is still disputed.
- [NOTE] Definition and ICT-vs-Community carry page-history commentary ("A prior version of this page presented…", "This version
  corrects the attribution"); that belongs in log.md — keep at most one sentence.

## dealing-range.md

Extra-scrutiny item (2016→2017, "Nov 2017") — VERIFIED: `dealing range` has 0 hits in all 110 MONTH-* packets; raw hits are
ICT-2017-USDCAD-MARKET-REVIEW-DEMO-EXAMPLE [08:46] ("it's being held in a rather tight dealing range."), ICT-2020-OTE-VOL09 [03:14],
and the two 2021 packets; SOURCES.md line 23 dates `ICT-2017-OTE-USDCAD-REVIEW` **2017-11-07** (the video itself references
"Monday, October 23rd, 2017" [01:35]). 2017 is sound for the TERM. All ep11/19/32/33/34/35/38 quotes verified verbatim.

- [FIX] Alias "trading range (2016 name for the same reference band)" is asserted with no quote, and the audit reported 0
  dealing-range-sense hits for "trading range"; the Definition then says the 2016-17 equivalent is only "impulse price swing"/"price
  move". The alias is in fact supportable, but it must be cited. — evidence: "The total range you're trading in, the equilibrium
  price point relative to the most recent trading range, high and low." (MONTH-1-FAIR-VALUATION [22:34], Sep 2016); "the most
  recent trading range that the market has moved from an old high to an old low." (MONTH-05-DEFINING-HTF-PD [17:46], Jan 2017);
  "sell off back to some equilibrium price point of the most recent trading range" (MONTH-05-TRADE-CONDITIONS-SETUP [04:31]) —
  required change: add `ICT-2016-FAIR-VALUATION` [22:34] (and/or `ICT-2017-HTF-PD-ARRAYS` [17:46]) to Source IDs/JSON/Citations and
  cite it beside the alias; amend the Definition sentence to "called the 'most recent trading range' / 'impulse price swing' in
  2016-17".
- [NOTE] The Nov-2017 hit is the loose "held in a tight dealing range" (consolidation) sense; the measurement sense the page defines
  first appears at ICT-2020-OTE-VOL09 [03:14] ("standard deviation of the dealing range used for the fib"). Say so in the Definition
  so Year Introduced 2017 is read as the term's first appearance.
- [NOTE] `ICT-2016-EQUILIBRIUM-DISCOUNT` [10:26] is quoted in the Definition but is not in Source IDs / JSON / Citations — add it or
  drop the quote and keep only the cross-link.

## equilibrium-definition.md

SOUND page; the two small audit notes (drop "consequent encroachment" alias; remove ±ε) applied. All 2016/2017/2022 quotes verified,
including the ones not in the audit: "ultimately reaches down into our mean threshold of the liquidity void" (MITIGATION-BLOCKS
[14:40]); "that range divided in half would give you a new equilibrium / price point" (MILLION-DOLLAR-SWING [26:41]–[26:46]);
"shorting above the / flouts equilibrium or 50% of the range" (FILLING-NUMBERS [11:53]–[11:59]); ep41 [18:21] confluence list.

- [NOTE] FILLING-NUMBERS quote spans [11:53]–[11:59] (cited as [11:59]) and ep41 "tracement" is normalised to "retracement" — bracket
  the correction; no content change.

## mean-threshold.md

Body-only MT, full-range variant deleted, MT-as-validity-line primary role, entry at the open, Year 2016 all applied; ORDERBLOCKS
[09:43]–[10:44], MITIGATE-LOSING [01:33] [01:42], PROPULSION-BLOCK [01:24] [01:28] [01:41], INSTITUTIONAL-ORDER-FLOW [05:01],
REDUCING-RISK [22:21], ep19 [78:54] [80:56], ep35 [00:36] verified.

- [FIX] The closing-basis rule is attributed to the wrong packet: "In other words, we don't want to see that violated on a closing
  basis." is cited to `ICT-2016-MITIGATE-LOSING-TRADES` ("via its own worked example", no timestamp) in Formal Criteria and in the
  Citations line "[01:05]–[03:33] — MT as the closing-basis invalidation line". That packet contains no "closing basis"; the line is
  in `ICT-2016-NO-FEAR-LOSING`, which is not on the page. — evidence: "the middle of that candle, we're going to be using that as a
  mean threshold." / "in other words, we don't want to see that violated on a closing basis." (MONTH-02-NO-FEAR-LOSING
  [03:29]–[03:34], Oct 2016); MITIGATE-LOSING has only the stop-below-MT example ("want to have a stop loss just a little bit below
  this mean threshold." [01:42]) — required change: cite `ICT-2016-NO-FEAR-LOSING` [03:29]–[03:34] for the closing-basis rule (add to
  Source IDs/JSON/Citations); change the MITIGATE-LOSING Citations line to "[01:33]–[03:33] — MT must not be violated; stop placed
  just below MT (worked losing-trade example)".
- [NOTE] Timeframes "M1 OBs are noisy" is an uncited legacy claim — delete or label as library guidance.
- [NOTE] Common Mistakes "Dating this to 2017" cites MITIGATE-LOSING [01:33] as Oct 2016 — correct (Month 02), but NO-FEAR-LOSING
  [03:29] is the earlier and more explicit MT statement; cite it here once the FIX above adds it.

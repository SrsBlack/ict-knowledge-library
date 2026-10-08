# Review — cluster GAPS (rewritten pages)

Reviewer: rev-gaps (read-only). Checked every quoted string on the 10 pages against `raw/*/report.md` and
`m22-captions/ep*.txt` with a fragment matcher (brackets stripped, `...` split), then by hand for every flagged
string; checked each cited Source ID against `SOURCES.md` and the packet map; ran `python tools/lint.py`
(read-only) → `287 concept pages, 232 source ids, problems: 0`. `quote_misses.txt` lists nothing for this cluster.

| page | PASS / FIX | issue count |
|---|---|---|
| fair-value-gap | PASS | 0 FIX, 3 NOTE |
| bullish-fvg | PASS | 0 FIX, 0 NOTE |
| bearish-fvg | PASS | 0 FIX, 1 NOTE |
| inversion-fvg | FIX | 1 FIX, 1 NOTE |
| consequent-encroachment | FIX | 1 FIX, 2 NOTE |
| balanced-price-range | FIX | 1 FIX, 2 NOTE |
| volume-imbalance | FIX | 2 FIX, 2 NOTE |
| fvg-mitigation | PASS | 0 FIX, 3 NOTE |
| nwog | FIX | 1 FIX, 2 NOTE |
| ndog | FIX | 2 FIX, 2 NOTE |

Totals: 4 PASS, 6 FIX pages, 8 FIX items.

## fair-value-gap

All audit findings applied: displacement criterion c3 removed; Sep-2016 "I define it by the body" and the
Oct–Nov-2016 order-block-candle usage recorded as an era split inside 2016; BISI/SIBI marked 2023+; ATR filter
removed with the 2-pip quote; "most-cited PD array" removed with the Jan-2017 hierarchy quote; re-sourced to the
evidenced packets + ep02/03/06/16/18/20; Year Refined 2025 → 2022, header == JSON. All 14 quotes verified
verbatim at the cited timestamps (ep06 [16:41]/[17:09]/[20:58]/[22:35], ep16 [37:50], ep18 [34:37], ep20 [13:52],
FVG-REINFORCED [04:28]/[06:15]/[12:37], REINFORCING-LIQUIDITY [07:03], FAIR-VALUATION [04:49], HTF-PD [25:17]).

- [NOTE] The bracket in the ep06 definition quote substitutes ICT's words instead of clarifying them: the page has
  "the number three candle gives you the [other end — t]he upper end of the fair value gap" — evidence: "the
  number three candle gives you the lower end the upper end of the fair value gap is going to be the low of candle
  number one" (ep06 [16:41]). ICT's "lower end" is correct for the bearish case he is drawing. Suggested: quote
  as-is — "gives you the lower end[;] the upper end of the fair value gap is going to be…".
- [NOTE] "the high of the cand[le] to the right of the down candle" — the transcript word is "count", not "cand":
  "the high of the count to the right of the down candle" (`MONTH-04-FAIR-VALUE-GAPS` [04:28]). Per the
  quote-as-is rule write "count [candle]". Same string on bearish-fvg.
- [NOTE] Related Concepts still describes [inversion-fvg] as "flipped FVG after rebalance + reversal" and
  [balanced-price-range] as "overlapping bullish + bearish FVG" as if settled, while both target pages are now
  labelled unverified. Add "(unverified)" to the two one-liners.

## bullish-fvg

All findings applied: body/wick-ratio displacement criterion removed; CE-entry + 2-pip-buffer example replaced
with ICT's near-edge entry and stop-beyond-candle-1/2 (ep06 [17:09]–[17:38], mirrored per [22:35]); BISI kept
only as `(SMC)` alias with the 0-hit statement; ATR filter removed; re-sourced. Quotes verified: ep06 [22:35]–
[23:00] ("it's three candles formation … candle number one's high that is the low of the fair value gap candle
number three's low is the high of the fair value gap"), ep18 [16:01], ep06 [17:09], MONTH-12 [34:58] ("a lower
time frame discount array like a fair value gap"). `ICT-2017-INTRADAY-TOP-DOWN` is the correct SOURCES.md ID for
video `Oec_0NM_OeY` (SOURCES.md line 127); the scratchpad packet map's row for that folder (`ICT-2017-TOPDOWN-
SHORT-TERM`) is the one that is wrong — see cross-page notes. No issues.

## bearish-fvg

All findings applied (displacement test removed, CE example replaced, SIBI → SMC alias, "holds at CE" removed,
re-sourced to MMT-TRENDLINE [13:11], FVG-REINFORCED [04:28], ep06 [16:41]/[14:42]/[17:09], STT-LRLR [08:26],
INTRAWEEK [17:59]). All quotes verified at the cited timestamps.

- [NOTE] "cand[le]" — transcript says "count" (`MONTH-04-FAIR-VALUE-GAPS` [04:28]); see fair-value-gap.

## inversion-fvg

Term, 2018/2024 dates and rules correctly labelled UNVERIFIABLE with the searched population on-page;
confidence medium; ep23 [03:09] precursor, ep09 [25:24] non-invalidation and ep18 [01:53]–[02:29] breaker
distinction all verified verbatim ("Many of you would see that as my bearish breaker. Mhm, it's not, okay? …
the discount low of the fair value gap? In other words, this candle's high.").

- [FIX] JSON criterion c2 keeps the rule the audit marked EMBELLISHED, and it contradicts the page's own Formal
  Criteria: JSON has `"UNVERIFIED: close_breaks_far_edge_with_displacement == true"` while Formal Criteria says
  only "A later candle trades through the original FVG's far edge" (no displacement) — evidence: audit
  inversion-fvg claim 3 "Inversion requires a CLOSE beyond the FVG's far edge with displacement … → EMBELLISHED
  (no such rule in corpus)"; the only corpus statement is "does this invalidate the fair value Gap no it does
  not … look at the body of this candle here isn't that respecting that" (ep09 [25:24]). Required change: set c2
  to `"UNVERIFIED: later_candle_trades_through_far_edge == true"` (drop "close" and "with_displacement") so JSON,
  Formal Criteria and the Formula block agree.
- [NOTE] Header `**Year Introduced:** 2018 (unverified in this library's corpus)` — lint passes (its regex takes
  the first four digits), but 282/287 vault pages use a bare year; see cross-page note 1.

## consequent-encroachment

Term correctly marked 0-hit with population; "most-frequent stopping point", "median rebalance depth", "CE
rebalance event" removed; era split stated (2016 void midpoint under "equilibrium / mean threshold",
MITIGATION-BLOCKS [10:13]/[12:58]; 2022 near-edge entry ep06 [17:09], midpoint declined ep18 [08:49], halfway
ep19 [06:55]/[103:45], mean threshold ep19 [78:54]) — all nine quotes verified verbatim.

- [FIX] Visual Pattern puts ICT's entry on the wrong edge. The diagram labels `H_{n-1} (FVG low / near edge) ←
  ICT's 2022 stated entry sits here instead` for a bullish FVG. For a bullish FVG price retraces DOWN into the
  gap, so the near edge is `L_{n+1}` (candle 3's low = FVG high), not `H_{n-1}` — evidence: "the easiest entry
  would be trading just above candle number three's high" (ep06 [17:09], bearish case; "everything i teach
  obviously is reversed the same way" [22:35]), which mirrors to just below candle three's LOW for the bullish
  case. The page's own Example 1 already says the near edge is 1.0866 = the FVG high, so the diagram contradicts
  the example. Required change: swap the two labels — top line `L_{n+1} (FVG high / near edge) ← ICT's 2022
  stated entry`, bottom line `H_{n-1} (FVG low / far edge)`; keep CE in the middle.
- [NOTE] Example 1 line "enters at the near edge (1.0866, the FVG's own low/high boundary per side)" is
  muddled; write "(1.0866 = candle n+1's low, the FVG high)".
- [NOTE] Year Introduced 2018 is kept for the *term* while the midpoint concept is corpus-dated Dec 2016
  (MITIGATION-BLOCKS [10:13]); acceptable as labelled, but the header-year format deviates — cross-page note 1.

## balanced-price-range

The 2017 mis-attribution is fixed correctly: sense 2 "price balanced range" quoted verbatim (INTRAWEEK [18:33]–
[18:42], [18:06]–[18:12]) and separated from the FVG-overlap sense; "unmitigated", "contraction", "M5 too
noisy", "decision zone" all removed; 0-hit population stated; confidence medium.

- [FIX] `Year Introduced: 2023` / `Year Refined: 2023` (header and JSON) is not evidenced anywhere. The audit's
  only basis is its hedge "may well be ICT 2022-23 YouTube material not in these 41 episodes … flag as 2023+";
  `balanced price range|bpr` has 0 hits in both corpora and no 2023 source exists in SOURCES.md for BPR (the
  only 2023 registry stub, `ICT-2023-NDOG-NWOG`, is for a different concept). The page also keeps
  `ICT-2017-CHARTER-OVERVIEW` "as the claimed-origin pointer for sense 1" — a 2017 stub cited as the origin of
  a concept the same page dates to 2023, which is self-contradictory. Answer to the lead's question: no 2023
  date is evidenced; it should be unknown. Lint forbids a non-numeric year (`re.search(r"\*\*Year
  Introduced:\*\* (\d{4})").group(1)` would raise on "unknown"), so a four-digit placeholder is unavoidable.
  Required change: keep a four-digit placeholder but (i) state in the banner and in the Citations that the
  year is a placeholder with no evidence behind it ("no dated source located; placeholder only"), (ii) add
  `"dating": "placeholder, not evidenced"` to the JSON so machine readers do not take 2023 as a fact, and
  (iii) drop `ICT-2017-CHARTER-OVERVIEW` from Source IDs, JSON `sources[]` and Citations (it supports nothing on
  the page; Source IDs then = `ICT-2017-STT-INTRAWEEK-REVERSALS` only). If the lead prefers an evidenced year
  over a placeholder, the only corpus-dated use of the phrase is 2017 (sense 2, INTRAWEEK [18:33]) and the
  banner would have to say sense 1 is undated — but that re-creates the 2017 reading the audit called WRONG,
  so the placeholder-with-label is the better of the two.
- [NOTE] Timeframes: "'price balanced range' (sense 2) is discussed on weekly/daily charts" — the passage
  [18:06]–[18:44] talks about Tuesday/Wednesday inside a weekly profile but never names a chart timeframe; say
  "inside a weekly market-maker profile; chart timeframe not stated".
- [NOTE] Header-year format — cross-page note 1.

## volume-imbalance

Body-gap geometry quotes verified (FVG-REINFORCED [12:26]–[12:41], [13:19]–[13:25]; LIQUIDITY-VOIDS [10:34],
[12:23]–[12:37], [12:45], [13:03]); ATR criterion c3 replaced with the 2-pip statement; "conviction stacks"
removed; the "name originates in 2022" claim retracted with the 0-hit statement.

- [FIX] `Year Refined: 2022` is still justified by a claim the audit found false: the banner says Year Refined
  "stays 2022 on the strength of the geometry being re-taught that year" and the Citations keep
  `ICT-2022-MENTORSHIP-OVERVIEW` "because the body-gap geometry is re-taught across the 2022 season". Evidence:
  audit volume-imbalance claim 2 — "Searched also `body gap|gap between the bodies|opening … close … gap` in m22:
  no body-gap discussion at all in 2022"; re-checked here: every 2022 "bodies" hit near "gap" is about candle
  bodies respecting a 3-candle FVG (ep03, ep09, ep19), none is a close-to-open body gap; `volume imbalance` 0
  hits. Required change: set `Year Refined` to 2016 (header and JSON `year_refined`), remove
  `ICT-2022-MENTORSHIP-OVERVIEW` from Source IDs / JSON `sources[]` / Citations (it supports nothing), and
  reword the banner's last sentence to "no 2022 corpus passage teaches the body gap; the label's date is
  unverified".
- [FIX] Timeframes section still carries an invented size/timeframe filter: "M5+. M1 VIs are micro-noise." This
  contradicts the page's own c3 ("no minimum size: ICT trades a 2-pip body gap directly") and the audit's
  finding against size filters — evidence: "it's only two pips difference, but that creates a what? A gap. So we
  can be a seller at a more refined price level" (`MONTH-04-FAIR-VALUE-GAPS` [12:37]–[12:42]); no corpus
  statement about M1 gaps. Required change: Timeframes → "All TFs. ICT gives no timeframe or size floor." and
  add "M1" to JSON `timeframes`.
- [NOTE] Example 1 is titled "bullish VI inside displacement" — displacement is no longer part of any FVG-family
  definition on these pages; retitle "bullish VI (M15)".
- [NOTE] "VIs often nest near or inside an FVG" — "often" is an unsourced frequency word; "can nest".

## fvg-mitigation

All findings applied: "mitigation" retracted as ICT's word for an FVG state (rebalance / closed in / fill, with
FAIR-VALUATION [22:23], FVG-REINFORCED [07:18]–[07:24], ep16 [13:10] verified); CE-mitigation rule and
fresh/partial/mitigated state machine removed; "structurally consumed" replaced by ep12 [16:58] and the second
visit at FVG-REINFORCED [11:51]–[11:57] (verified: "Here's the first time it trades up into that 104.75 level.
Closing that fair value gap. And then here's the second time it trades up into it."); Year 2017 → 2016 header ==
JSON. The two claims the writer added beyond the audit are both quote-backed: "There's no specific time limit on
how long it's going to take for these voids to close in" (`MONTH-04-LIQUIDITY-VOIDS` [02:19]) and "implication
of order block theory" (`MONTH-04-MITIGATION-BLOCKS` [00:28]).

- [NOTE] The H1 was retitled "FVG Rebalance / Fill (sometimes called "FVG Mitigation")". File id unchanged
  (lint OK), but INDEX.md line 116 still reads "fvg-mitigation — fresh/partial/mitigated state", which the page
  now says is not in the corpus. Replacement one-liner: "FVG rebalance / close-in; 'mitigation' is not ICT's
  word for it".
- [NOTE] `ICT Confidence: medium` although every definitional claim is now quote-backed; under the fix brief's
  rule it qualifies for `high`. Writer's call; not an error.
- [NOTE] Formula `rebalanced(fvg) := … price(k) fully closes in the gap` is the library's formalisation of
  "closes the fair value gap in", fine, but the comment "# The corpus-supported state is binary" slightly
  overstates: ICT describes partial fills too ([06:55]); "binary completion rule" would be exact.

## nwog

Term correctly marked 0-hit; fill statistics removed; 2022 index-futures precursor quoted verbatim (ep34
[00:06], [09:31], [10:00], [10:25] — "sometimes the week will just run away from it and won't really come back
to it but in weeks where there's consolidation like fomc we have that uh to deal with"; ep14 [00:01] "i'm
looking for a gap fill from friday's close so i'm going to go long here 12 micros of the mini nasdaq or i'm
sorry micro nasdaq futures contract"); 2017 era split quoted verbatim (DAY-TRADE-ROUTINE [11:31]–[12:01]);
VACUUM-BLOCK [10:15] boundary analogy labelled as analogy. The ep34 gap is confirmed to be the Sunday reopen
("we traded down into the sunday gap" [04:57]; "the opening gap on sunday" [09:31]).

- [FIX] Era-split date is internally inconsistent: Definition says "in Mar-2017 ICT instead downplayed Sunday
  gaps" and Common Mistakes says "ICT's Mar-2017 statement", but Citations says `ICT-2017-DAYTRADE-ROUTINE` is
  "(May 2017)". SOURCES.md line 101: "Month 09 — ICT Day Trade Routine … self-dates 'welcome back to lesson 8
  of the May 2017 ICT mentorship'". Required change: "Mar-2017" → "May-2017" in Definition and Common Mistakes
  (Mar 2017 is Month 07, the BPR/INTRAWEEK packet, not Month 09).
- [NOTE] The "~18:00 NY" anchor: ep34 [00:06] says "last night my local time about six o'clock" — NY time is
  inferred there; the explicit statement "resumes around six o'clock in the afternoon new york time" is ep11
  [04:01], which this page does not cite. Either cite ep11 [04:01] for the NY-time clock or write "six o'clock
  his local time (ep34)". The anchor itself is right: the ES/NQ Sunday session reopen ICT describes is 18:00 NY
  and ep11 states it in NY time.
- [NOTE] Year 2023 rests only on the registry stub `ICT-2023-NDOG-NWOG`; labelled as such on-page, fine.
  Header-year format — cross-page note 1.

## ndog

The 17:00→00:00 midnight-gap anchor is correctly retracted; "midnight is only ever an opening price" is backed
by ep19 [103:45] (verified); "~70% same day" removed; term 0-hit stated; VACUUM-BLOCK [10:15]/[12:48]/[12:58]
verified. The "six o'clock … new york time" reopen clock IS in the corpus (ep11 [04:01], verbatim) and the
ep11 [19:59] gap passage is verbatim ("it opened up six o'clock in new york time opened up and slammed down
accelerating lower … you have a big gap here it's likely to come back and rebalance that and fill it in and it
does"). Two problems with how that evidence is presented:

- [FIX] Mis-cited timestamp / stitched quote. The Definition quote "trading stops at one o'clock in the
  afternoon on holidays generally and resumes around six o'clock in the afternoon[,] New York time... it opened
  up six o'clock…" is cited as (`ICT-2022-MENTORSHIP-EP11` [19:04]–[19:59]); the first sentence is at [04:01]
  ("now on monday it was a bank holiday and trading stops at one o'clock in the afternoon on holidays generally
  and resumes around six o'clock in the afternoon new york time"), fifteen minutes before the second ([19:59]).
  The audit carried the same wrong range; the writer copied it without grepping. Required change: split into two
  quotes cited (`ICT-2022-MENTORSHIP-EP11` [04:01]) and (`ICT-2022-MENTORSHIP-EP11` [19:59]); fix the Citations
  line to "[04:01], [19:30]–[19:59]".
- [FIX] Neither corpus instance is an ordinary DAILY opening gap, but the page presents them as "the futures
  session reopen after the daily halt" (Definition, Formal Criteria bullet 1, JSON c1, Example 1 "Futures
  session halts, then reopens around 18:00 NY", Citations "Session-reopen gap restated [00:06]"). Evidence:
  ep11 is a Monday bank-holiday abbreviated session — "now on monday it was a bank holiday and trading stops at
  one o'clock" (ep11 [04:01]); "monday again was a holiday so i knew i had abbreviated session hours so it's
  going to close at one o'clock" (ep11 [19:04]); ep34 [00:06] "a gap when the session started again last night
  … about six o'clock" is the Sunday weekly reopen — "we traded down into the sunday gap" (ep34 [04:57]), "the
  opening gap on sunday" (ep34 [09:31]). The audit's sentence "the daily opening gap ICT trades is the 18:00 NY
  futures session reopen" over-generalised from these two special sessions and the writer carried it over.
  Required change: in Definition, Formal Criteria bullet 1, JSON c1, Example 1 and Citations, label ep11 as a
  holiday-session reopen gap and ep34 as the Sunday (weekly) reopen gap, and add one sentence: "No ordinary
  Monday–Thursday daily reopen gap is described in either corpus; the six-o'clock NY reopen is the stated clock
  for both special sessions." Keep the midnight finding and the "not on FX" caveat unchanged.
- [NOTE] Formula comment "session_close … ~17:00 NY (stated only as 'one o'clock... on holidays')" — the 17:00
  figure is a real-world CME fact, not corpus; it is labelled, fine, but ep11's actual halt that day was 13:00.
- [NOTE] "New York time" is capitalised in the quote; transcript has "new york time". Trivial.

## Cross-page notes (for the lead, not page FIX items)

1. Header-year format. Five pages (balanced-price-range, consequent-encroachment, inversion-fvg, nwog, ndog)
   write `**Year Introduced:** 2023 (unverified in this library's corpus)`. Lint passes because its regex
   `(\d{4})` takes the first four digits and the JSON holds the bare year, so nothing breaks; but 282 of 287
   vault pages use a bare year and no page outside this cluster uses a suffix. Recommend: bare year in the
   header (as the JSON already is) and the caveat in the ⚠ banner, which every one of these pages already
   carries. This is a convention nit, not an error.
2. INDEX.md one-liners now stale: line 116 fvg-mitigation "fresh/partial/mitigated state" (wrong — see
   fvg-mitigation NOTE); line 342 ndog "New Day Opening Gap (midnight NY)" (wrong — midnight retracted);
   line 110 balanced-price-range "overlapping bull+bear FVGs" and line 343 nwog "(Sunday/Monday)" are fine but
   could add "(unverified)".
3. Scratchpad `packet_map.tsv` maps folder `…MONTH-12-INTRADAY-TOP-DOWN-Oec_0NM_OeY` to
   `ICT-2017-TOPDOWN-SHORT-TERM`, but SOURCES.md line 127 registers `Oec_0NM_OeY` as
   `ICT-2017-INTRADAY-TOP-DOWN` and line 125 registers `ICT-2017-TOPDOWN-SHORT-TERM` as video `3B7Reg2Yiqs`.
   The bullish-fvg writer followed SOURCES.md (correct); other clusters using the map for Month 12 may cite the
   wrong ID.
4. Audit-report errata found while verifying (so the auditor's own text is not re-used as-is): ndog claim 2's
   range "ep11 [19:04]–[19:59]" for the holiday-hours sentence should be [04:01]; both ep11 and ep34 are special
   sessions, not a daily gap (see ndog FIX 2); the ep18 [01:53]–[02:29] breaker quote is verbatim (ep18 is a
   punctuated transcript, unlike the other episodes).
5. The CE Visual Pattern error (wrong edge labelled as the entry) is the one item here that, if copied by a
   reader or an engine, reproduces exactly the midpoint/near-edge confusion the audit set out to remove.

# Verify-A — final gate for clusters STRUCTURE, LIQUIDITY, GAPS (2026-10-08)

Verifier: read-only final gate. For every FIX item in `review-structure.md`, `review-liquidity.md`,
`review-gaps.md` the page was opened as it is now on disk; every replacement quote was re-grepped in
`raw/*/report.md` or `meta/audit-2026-10-08/m22-captions/ep*.txt`; every newly added Source ID was
checked against `SOURCES.md`. `python tools/lint.py` (read-only): `287 concept pages, 232 source ids,
problems: 0` (header years == JSON, Source IDs == JSON `sources[]`, all sections present).
Scope grep (`the owner|our engine|owner's|trading-wiki|MT5|PT-0x|SE-xx|FOB-|prereg|alert_m15`) over
all 35 pages: 0 hits. All remaining SMC vocabulary on the 35 pages (CHoCH, BOS, BISI, SIBI,
liquidity grab, swing failure, run-and-*) is labelled not-ICT / 0-hit / SMC.

**Totals: 31 FIX items — 31 RESOLVED, 0 NOT RESOLVED. New errors: 1 (minor, nwog). Notes: 6.**

## FIX item table

| # | cluster / page | FIX item (abridged) | status | evidence checked |
|---|---|---|---|---|
| S1 | structure / mss-vs-choch | "careless teaching" → ICT announcing his own usage | RESOLVED | line 19: "says he will use them interchangeably himself … this is ICT announcing his own usage"; ep03 [02:20] verbatim |
| S2 | structure / mss-vs-choch | Example B over-correction (no displacement gate in either corpus) | RESOLVED | line 90: 2016-17 trade-through / 2022 "not all that convincing" (ep06 [19:37] verbatim) / "still not a hard FVG gate" (ep10 [37:43]); offending sentence gone |
| S3 | structure / mss-vs-choch | Year 2016 with no 2016 source | RESOLVED | `ICT-2017-HIGH-REWARD-SETUPS` in header, JSON, Citations with Oct-2016 note; "So we look at the market with a quarterly perspective and allow the next shift in market structure to unfold." = MONTH-02-SECRETS-SELECTING-HIGH [42:03]; SOURCES.md line 50 maps the ID to Month 02 |
| S4 | structure / swing-high | "head and shoulders" mis-cited to INSTITUTIONAL-SWING-POINTS via OTE | RESOLVED | line 27 cites `ICT-2017-OPEN-FLOAT-L12` [20:15]–[20:21]; line 29 LTH tier [20:27]–[20:31]; OTE line 140 reworded to "two lower highs on either side … nests out" (OTE [34:20] verbatim); "via" dropped; OPEN-FLOAT-L12 in header/JSON/Citations (SOURCES.md line 108 = Month 05 Open Float, packet …MONTH-05-OPEN-FLOAT-BkmZgjuYREU lines [20:15]–[20:42]) |
| S5 | structure / swing-high | Example 3 + Visual Pattern inverted route 2 | RESOLVED | line 92 "An ITH can also be the high formed when price trades up to rebalance an imbalance"; lines 110–111 "the high printed by that rebalancing move is immediately an ITH … the imbalance being rebalanced is the earlier gap it rallied into"; ep12 [41:23] verbatim with ASR brackets |
| S6 | structure / swing-low | ITL route 1 evidenced with the plain 3-bar ep10 [18:04] | RESOLVED | line 26 keeps ep10 [18:04] under the STL bullet only; line 27 cites OPEN-FLOAT-L12 [20:36]–[20:42] ("now invert that and you'll have the same thing…", verbatim) and ep12 [14:15] ("intermediate term low has a higher short-term low to the right of it and a higher short-term low to the left of it", verbatim); OPEN-FLOAT-L12 in header/JSON/Citations |
| S7 | structure / swing-low | Year 2016 with no 2016 source | RESOLVED | `ICT-2016-EQUILIBRIUM-PREMIUM` [11:53]–[11:58] in header/JSON/Citations; "This is why I do not use the Williams fractal that requires five candles." = MONTH-1-EQUILIBRIUM-VS-PREMIUM [11:53] |
| S8 | structure / bos-bullish | ep02 [27:37] filed as 2016-17 with invented "re-teaching" gloss | RESOLVED | "re-teaching" gone; line 19 is a 2022 bullet ("even here, ICT names the plain trade-through itself a break"); line 18 says FAIR-VALUATION [08:29] / LIQUIDITY-RUNS [16:32] name the event but state no close/trade-through rule; ep02 [27:37] verbatim |
| S9 | structure / range-expansion | Year Refined 2022 with no 2022 source | RESOLVED | header + JSON `year_refined` = 2017; latest source DAYTRADE-ESSENTIALS (Month 08) |
| S10 | structure / displacement-definition | Timeframes "M1–M5 in the worked examples" invented | RESOLVED | line 75 now "taught on intraday charts (15-minute, with 1–5-minute drill-downs in the ep05/ep06/ep10 examples; ep24's worked example is itself on a 5-minute chart)"; ep24 [22:23] "this is a 15 minute chart", [22:52] "here is a five minute chart" confirm the added clause |
| S11 | structure / displacement-strength-criteria | Example 1 had opposite geometry (break of old high) | RESOLVED | lines 78–80: sell stops run, "it's got to trade back above this old low … did it happen here no" (ep24 [22:52] verbatim), "melted … no displacement" (ep24 [23:30]), "no long idea" |
| S12 | structure / dealing-range | "trading range" alias uncited | RESOLVED | line 13 quotes FAIR-VALUATION [22:34] ("The total range you're trading in, the equilibrium price point relative to the most recent trading range, high and low." verbatim) and HTF-PD-ARRAYS [17:46] (verbatim); both + EQUILIBRIUM-DISCOUNT in header/JSON/Citations; Definition now "most recent trading range / impulse price swing / price move"; 2020 measurement-sense note added (OTE-SERIES-09 [03:14] "standard deviation of the dealing range used for the fib" verbatim) |
| S13 | structure / mean-threshold | "closing basis" mis-cited to MITIGATE-LOSING | RESOLVED | line 23 cites `ICT-2016-NO-FEAR-LOSING` [03:29]–[03:34] ("The middle of that candle, we're going to be using that as a mean threshold." / "In other words, we don't want to see that violated on a closing basis." verbatim, MONTH-02-NO-FEAR-LOSING lines 39–40); ID in header/JSON/Citations (SOURCES.md line 170); MITIGATE-LOSING Citations line reworded to "MT must not be violated; stop placed just below MT" |
| L1 | liquidity / liquidity-sweep | 10–20 / 25-pip depth rule unscoped | RESOLVED | Formula block lines 31–42 and JSON c3 carry "on a lower timeframe chart like a 15 or 30 minute chart" (LP [10:28] verbatim), "I think is a fair assessment" (LP [11:30] verbatim), "no depth figure for H4/D/W or for non-FX" |
| L2 | liquidity / liquidity-sweep | Example 1 "4 pips … within 10-20" | RESOLVED | line 91: 1.0875 → 1.0888 = 13 pips, "within ICT's stated 10-20 pip range for a 15-30 min FX chart" (arithmetic correct) |
| L3 | liquidity / liquidity-sweep | MMT-FALSE-BREAKOUT quoted but absent from header/JSON/Citations; "folder's sibling" wording | RESOLVED | ID in header, JSON `sources[]`, Citations (09:50 quote verbatim at MONTH-02-MARKET-MAKER-TRAP-pv2 line 115); "sibling" wording gone (0 hits) |
| L4 | liquidity / liquidity-run | "1916-origin taxonomy" | RESOLVED | line 15 "2016-origin taxonomy" |
| L5 | liquidity / liquidity-run | "hot knife" at 17:31 | RESOLVED | 19:33 in Formal Criteria (line 22) and Citations (line 98) |
| L6 | liquidity / equal-highs | EP16 quoted but not in header/JSON/Citations | RESOLVED | `ICT-2022-MENTORSHIP-EP16` in header, JSON, Citations; ep16 [04:13] verbatim; NOTE also applied (WHAT-TO-FOCUS-ON [18:31] and EQUILIBRIUM-DISCOUNT [51:27] now separate quotes) |
| L7 | liquidity / turtle-soup | depth rule unscoped in Formula + JSON c2 | RESOLVED | Formula lines 63–69 and JSON c2 carry the 15-30-min FX scope, the "fair assessment" hedge, and "no figure for HTF/non-FX"; NOTE applied (Visual Pattern now "reverses back") |
| L8 | liquidity / stop-hunt-pattern | Example 2 heading "run-and-continue" | RESOLVED | line 108 "stop hunt with run (continuation) outcome"; `run-and-` only survives on liquidity-run inside the 0-hit disclaimer |
| L9 | liquidity / stop-hunt-pattern | header aliases ≠ JSON ("liquidity grab pattern") | RESOLVED | header `stop hunt, stop run pattern` == JSON `["stop-hunt","stop-run-pattern"]` |
| L10 | liquidity / stop-hunt-pattern | depth rule unscoped in Formula + JSON c3 | RESOLVED | Formula line 59 and JSON c3 carry the scope wording |
| G1 | gaps / inversion-fvg | JSON c2 kept "close … with_displacement" | RESOLVED | c2 = `"UNVERIFIED: later_candle_trades_through_far_edge == true"`; matches Formal Criteria bullet 2 and the Formula comment |
| G2 | gaps / consequent-encroachment | Visual Pattern entry on the wrong edge | RESOLVED | lines 89–95: top `L_{n+1} (FVG high / near edge) ← ICT's 2022 stated entry sits here (candle 3's low)`, bottom `H_{n-1} (FVG low / far edge)`, CE in the middle; agrees with Example 1 (1.0866 = candle n+1's low) |
| G3 | gaps / balanced-price-range | 2023 presented as a finding; CHARTER-OVERVIEW kept | RESOLVED | banner and Citations state the year is a lint-format placeholder, not evidenced; JSON has `"dating": "placeholder, not evidenced …"`; Source IDs/JSON/Citations = `ICT-2017-STT-INTRAWEEK-REVERSALS` only; Timeframes NOTE applied |
| G4 | gaps / volume-imbalance | Year Refined 2022 on a false "re-taught in 2022" claim | RESOLVED | header + JSON `year_refined` = 2016; `ICT-2022-MENTORSHIP-OVERVIEW` removed from header/JSON/Citations; banner now "no 2022 corpus passage teaches this body-gap pattern" |
| G5 | gaps / volume-imbalance | Timeframes "M5+. M1 VIs are micro-noise." | RESOLVED | line 97 "All TFs. ICT gives no timeframe or size floor"; JSON `timeframes` starts with "M1" |
| G6 | gaps / nwog | "Mar-2017" for Month 09 | RESOLVED | "May-2017" in Definition (line 33) and Common Mistakes (line 122); Citations "(May 2017)"; SOURCES.md line 101 = Month 09 |
| G7 | gaps / ndog | stitched ep11 quote cited [19:04]–[19:59] | RESOLVED | holiday-hours sentence cited [04:01] (verbatim at ep11 line 11), reopen gap cited [19:59] (verbatim at ep11 line 44); Citations "[04:01]; … [19:30]–[19:59]" |
| G8 | gaps / ndog | special sessions presented as the ordinary daily reopen | RESOLVED | Definition, Formal Criteria bullet 1, JSON c1, Example 1, Visual Pattern and Citations all label ep11 as the Monday bank-holiday abbreviated-session reopen and ep34 as the Sunday weekly reopen ("we traded down into the sunday gap" ep34 [04:57]; "the opening gap on sunday" [09:31]); the required "No ordinary … daily reopen gap is described in either corpus" sentence is present (line 33); midnight finding and FX caveat unchanged |

## New errors (found in the second skim)

- [NEW ERROR — minor] `concepts/31-models/nwog.md` Common Mistakes, lines 120–121: "ICT's own 2022
  examples give the reopen as 'six o'clock,' i.e. the session restarting **after the daily halt**."
  This contradicts the page's own Definition (the ep34 gap is "between Friday's last trade and the
  Sunday-evening session reopen") and the ndog correction just applied (G8): the ep34 gap is the
  weekend/Sunday reopen, not a daily halt. Evidence: "we traded down into the sunday gap" (ep34
  [04:57]); "the opening gap on sunday" (ep34 [09:31]); the only "daily"-looking reopen in the corpus
  is the ep11 bank-holiday session ("trading stops at one o'clock in the afternoon on holidays
  generally and resumes around six o'clock", ep11 [04:01]). Required change: "the session restarting
  after the **weekend (Sunday) halt**, or after the ep11 holiday halt" — do not say "daily".

No other new errors. Every quote on the 35 pages that the three reviews or the writers added was
re-grepped and found at the cited packet/episode; no unquoted "ICT says" claim was added by the
writers beyond the ones the reviewers already passed.

## Notes (not errors; for the lead's discretion)

1. `turtle-soup.md` Example 1 ends "Long entry on FVG retest **at CE**" (library example, not
   attributed to ICT). After the gaps-cluster rewrite, `consequent-encroachment.md` and
   `fair-value-gap.md` state ICT's 2022 entry is the near edge and the midpoint is explicitly
   declined (ep06 [17:09], ep18 [08:49]). Suggest "at the FVG's near edge" to keep the clusters
   consistent.
2. `swing-low.md` Visual Pattern line 88: "An ITL can also be a plain STL that later forms by
   rebalancing an imbalance" is garbled (an STL cannot "later form"). The swing-high mirror was
   reworded correctly; suggest "An ITL can also be the low formed when price trades down to
   rebalance an imbalance".
3. `bos-bullish.md` Common Mistakes line 93 ("2016-17 material calls the break on the trade-through")
   cites nothing, while Formal Criteria bullet 2 says the two 2016 packets state no rule either way.
   Not a contradiction — `ICT-2017-OTE` [27:45]–[28:02] ("it trades through it once it does that …
   this break above that short term high") is the 2017 support and is on the page; cite it there.
4. `fair-value-gap.md` Related Concepts still describes [inversion-fvg] as "flipped FVG after
   rebalance + reversal" and [balanced-price-range] as "overlapping bullish + bearish FVG" without
   "(unverified)" (review-gaps NOTE, not applied). INDEX.md one-liners for fvg-mitigation / ndog /
   nwog / balanced-price-range WERE updated.
5. `swing-low.md` line 28 still normalises ep12 [14:15] "this immed term low forms by rebalancing"
   to "this intermediate term low forms by rebalancing" without a bracket (review NOTE, not
   applied); content unaffected.
6. `ndog.md` header keeps the `2023 (term unverified in this library's corpus)` suffix while
   inversion-fvg, consequent-encroachment, balanced-price-range and nwog now use a bare year. Lint
   passes either way; convention nit only.

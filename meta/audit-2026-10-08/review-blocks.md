# Review — cluster BLOCKS (rewrites of 2026-10-08)

Reviewer: rev-blocks (read-only). Checked every quote on all 10 pages against `raw/*/report.md` and
`m22-captions/ep*.txt` with a normalising grep (case/punctuation/bracket-insertions ignored, ellipsis segments
checked separately); checked header == JSON (Year Introduced/Refined, confidence, Source IDs == `sources[]`),
every Source ID present in `## Citations`, 10 sections, `id` == filename, and `python tools/lint.py`
(`287 concept pages, 232 source ids / problems: 0`, no file written). Packet short-names as in `blocks.md`
(OB-LECT = `ICT-2016-ORDERBLOCKS`, BRK-LECT = `ICT-2016-BREAKER-BLOCK`, MIT-LECT = `ICT-2016-MITIGATION-BLOCKS`,
PROP-LECT = `ICT-2016-PROPULSION-BLOCK`, HTF-PD = `ICT-2017-HTF-PD-ARRAYS`, BEAR-SWING = `ICT-2017-SWING-BEAR-SETUPS`,
TRADE-COND = `ICT-2017-TRADE-CONDITIONS`, CLASSIC-SWING = `ICT-2017-PD-ARRAY-MATRIX`, QTR = `ICT-2017-QUARTERLY-SHIFTS`).

Structural checks: all 10 pages pass (header == JSON on every field, sources == JSON, all IDs cited, 10 sections, id ok).
No page references the owner's engine/projects. Era splits on the three OB pages are stated as two eras with
their own quotes, not collapsed. Breaker dating 2017 → 2016 and the dropped 2023/2024 "refined" years are consistent
with the corpus.

| page | PASS / FIX | issue count |
|---|---|---|
| 07-order-blocks/bullish-order-block | FIX | 2 FIX, 2 NOTE |
| 07-order-blocks/bearish-order-block | PASS | 0 FIX, 1 NOTE |
| 07-order-blocks/order-block-criteria | FIX | 2 FIX, 1 NOTE |
| 07-order-blocks/propulsion-block | PASS | 0 FIX, 3 NOTE |
| 08-breaker-blocks/breaker-block | FIX | 4 FIX, 2 NOTE |
| 08-breaker-blocks/bullish-breaker | FIX | 1 FIX, 0 NOTE |
| 08-breaker-blocks/bearish-breaker | FIX | 1 FIX, 1 NOTE |
| 08-breaker-blocks/mitigation-block | FIX | 3 FIX, 2 NOTE |
| 08-breaker-blocks/breaker-vs-mitigation | FIX | 1 FIX, 1 NOTE |
| 19-rejection-blocks/rejection-block | FIX | 2 FIX, 3 NOTE |

Totals: 3 PASS / 7 FIX pages; 16 FIX items.

Mechanical-checker misses, adjudicated: `bullish-order-block` "key off your demo entries on the down candle's body,
the high or the opening" = **trimmed quote** (words "of the candle" dropped, see FIX below); `rejection-block`
"just above the candle's body, not the wicks" = **ASR/punctuation-trivial** (transcript: "not the wick's.", HTF-PD
[18:49]) — verbatim apart from the apostrophe; no change required beyond an optional `[sic]`.

## 07-order-blocks/bullish-order-block

- [FIX] The EP13 [17:52] quote is glossed backwards. Page: "There is no engulfing candle, does this [not have one] —
  forget all that" applies "to invalid candidates without an imbalance". — evidence: "it's that's it there is no
  engulfing candle does this forget all that you don't need that okay it's the gap plus the down closed candle plus the
  idea that's likely to go for my side liquidity that's it" (ep13 [17:52]). "does this" is auto-caption for "dojis";
  ICT is saying there is NO candlestick-pattern requirement (engulfing/doji) — only gap + down-close candle + narrative.
  — required change: rewrite the Common-Mistakes bullet as "Requiring an engulfing/doji candle" with the verbatim quote
  and the bracket `[dojis — auto-caption renders 'does this']`; drop the "[not have one]" gloss.
- [FIX] Quote not verbatim (silent trim). Page: "key off your demo entries on the down candle's body, the high or the
  opening" [07:54–08:01]. — evidence: "I want you to try to key off your demo entries on the down candles body of the
  candle, the high or the opening in this instance." (OB-LECT [07:54–08:01]). — required change: quote verbatim
  ("…on the down candles body of the candle, the high or the opening in this instance") or mark the trim with an ellipsis.
- [NOTE] "0 hits for 'demand' as ICT's own label in either corpus" is not a greppable claim (ICT says "supply and
  demand" repeatedly, e.g. ep18 [40:41]); rephrase as "ICT never labels his order block a demand zone and explicitly
  rejects the framing".
- [NOTE] Formula `argmin(low) … tie-broken by max(open - close)` is the writer's formalisation; ICT's definition is
  conjunctive ("the lowest candle … that has the most range … and is near a support level" [00:59–01:08]). Say so.

## 07-order-blocks/bearish-order-block

- PASS. All eight quotes verbatim at the cited timestamps in the cited sources (OB-LECT [00:54], [25:40], [34:58];
  ep18 [38:26], [40:41], [42:22]; ep19 [20:46], [80:56]). Mirror statements are labelled as mirrors of [00:54].
- [NOTE] The Definition leans on EP12 quotes via the bullish page; fine, but if the lead wants each page
  self-contained, add `ICT-2022-MENTORSHIP-EP12` [44:09] here too (header + JSON + Citations).

## 07-order-blocks/order-block-criteria

- [FIX] Quote altered inside the quotation marks (the same defect the page just corrected at [05:53]). Page:
  "…so we don't look at that as an order block. We used a big beefier body candle" [19:05–19:26]. — evidence: "So we
  don't look at that as a bullish order block. We used a big beefier body candle." (BEAR-SWING [19:19–19:21]).
  — required change: quote verbatim ("as a bullish order block") and keep the existing ⚠ note explaining the
  transcript's "bullish".
- [FIX] Silent elision inside a quote. Page: "…there's a market structure shift — there's your high probability
  bearish order block" (EP03 [23:40]). — evidence: "there's a market structure shift there's your height frequency
  high power high probability bearish order block" (ep03 [23:40]). — required change: insert an ellipsis
  ("there's your … high probability bearish order block").
- [NOTE] Citations line gives "(13:56–14:20)" for a quote the body cites as [13:56–14:09]; transcript hit is [14:03].
  Harmless; align the two.

## 07-order-blocks/propulsion-block

- PASS. All PROP-LECT and IOF quotes verbatim at the cited timestamps; audit nit on `invalidated := close < pb_mt`
  applied; stub IDs dropped with the search population recorded on-page; Year Refined 2024 → 2016 header == JSON.
- [NOTE] [01:02–01:11] transcript reads "owner block" (ASR); the page silently normalises to "order block". Add
  `[order block — ASR 'owner block']` to match the page's own bracket convention.
- [NOTE] Timeframes "M15–D is the practical range" and JSON `["M15","H1","H4","D"]` are the writer's; ICT names only
  the 15-minute chart and a 45-minute preference [04:46–04:54]. Label as unsourced or drop the range.
- [NOTE] Formal Criteria "the last down-close candle (or a run …)" reuses the "last candle" wording the sibling OB
  pages now mark as rejected in 2022; qualify it as the Dec-2016 lecture's framing.

## 08-breaker-blocks/breaker-block

- [FIX] Geometry of the breaker candle is wrong in Definition, Formula and Visual. Page: "taking out the short-term
  high (or low) **between the run and the current price**"; formula `intervening_swing := the short-term high …
  BETWEEN the run and now`; the diagram draws the swing-high candle AFTER the low is run. — evidence: "focusing on
  the high in between the two lower lows one low has to be traded below and that is going to run out to sell stops."
  (BRK-LECT [02:11]); "We focus our attention on the short term high that is in between the two lows." [02:24]; "a
  bullish range or up close candle in the most recent swing high **prior to** an old low being violated" [05:08];
  "a bullish breaker is a up candle between two swing lows" (HTF-PD [27:48]). The breaker candle forms BEFORE the
  stop run — it is the swing high between the old low and the lower low that runs it; the structure break is the
  later rally back through that same swing high. — required change: Definition → "the short-term high (bullish) /
  low (bearish) that sits between the old low/high and the lower low/higher high that ran it"; Formula →
  `intervening_swing := the swing high BETWEEN the two lows (formed before the run)`; redraw the Visual with the
  breaker candle preceding the run (the sibling pages' "between the two lows/highs" wording is already correct).
- [FIX] EP39 "if you leave that out it's not a breaker — it's a gamble" is used (Definition ⚠ and Common Mistakes) as
  proof that the **liquidity run** is mandatory; in context "that" is knowing the draw/narrative. — evidence: "if it
  trades back up to that and the narrative is bearish notice that it's not just simply we have this pattern here and
  that's all it is no you must know what the market's likely to be reaching for if you leave that out it's not a
  breaker it's a gamble" (ep39 [20:25–20:50]). — required change: keep the run as definitional using ep39's own
  definition sentence ("a breaker is a pattern where price runs out a pool of liquidity") plus BRK-LECT [02:11–02:24]
  / [05:41]; move the "gamble" clause to a separate narrative requirement ("you must know what the market's likely to
  be reaching for … if you leave that out it's not a breaker it's a gamble") and stop presenting it as the run clause.
- [FIX] TRADE-COND [10:11] quoted twice, neither verbatim. Page: "we have this range up here, we also have this down
  candle which is a breaker." (Citations) and "we have this down candle which is a breaker" (Timeframes). — evidence:
  "we have a range up here we also have this down candle which is a breaker" (TRADE-COND [10:11]). — required change:
  "a range", and keep "also" (or ellipsise).
- [FIX] Timeframes "use the full range from M15 to monthly" re-introduces an unsourced floor on a page that says "No
  floor is stated", and ICT trades an hourly breaker. — evidence: "here's trading up into that area I outlined on the
  hourly chart where we can see that breaker." (`ICT-2020-OTE-VOL04` [04:57]). — required change: drop "from M15";
  state "no floor; shown monthly/weekly/hourly" (JSON timeframes may list what ICT shows, not a floor).
- [NOTE] Example 1 "The up-close (or down-close — see Formal Criteria) candle at that swing high" is muddled; for the
  bullish case ICT says "a bullish range or up close candle" [05:08]. Delete the parenthetical.
- [NOTE] 2022 adds stop guidance the page could carry: "I'm going to use the breaker's candle and just above that for
  my stop … the Market's going to mostly stay in the lower half of the breaker candle which is the down … Clos[e]
  candle" (ep10 [40:30–41:00]) — optional, would need `ICT-2022-MENTORSHIP-EP10` added to header/JSON/Citations.

## 08-breaker-blocks/bullish-breaker

- [FIX] Common Mistakes: "the antecedent low run is what makes the pattern a breaker at all (see breaker-block, EP39
  [20:25–20:50])" — same EP39 misreading as above; the "gamble" clause is about the narrative. — evidence: ep39
  [20:50] "you must know what the market's likely to be reaching for if you leave that out it's not a breaker".
  — required change: cite BRK-LECT [02:11–02:24] ("one low has to be traded below") and [05:08] ("prior to an old low
  being violated") for the run; cite EP39 only for the narrative requirement.
- Otherwise PASS: [05:08], [05:41], [06:56], HTF-PD [27:48–28:02], `ICT-2017-OTE-DRILL-AUSUSD` [00:42] all verbatim;
  "between the two lows" geometry is correct here.

## 08-breaker-blocks/bearish-breaker

- [FIX] Formal Criteria: "An old high is run first (the liquidity event) — not optional (EP39 [20:25–20:50])" — same
  EP39 misreading. — evidence: as above. — required change: cite BRK-LECT [04:20] ("what we are looking for is an old
  high to be ran out, or a false break above an old high") and [03:13] for the run; EP39 for the narrative only.
- [NOTE] "ICT ties the label to the underlying narrative, not geometry alone: 'many of you would see that as my
  bearish breaker — mhm, it's not, okay?' (EP18 [02:29])". The ep18 reason that follows is not narrative — "So, look
  at this here. Which is lower? Is it this low here or the discount low of the fair value gap? In other words, this
  candle's high." (ep18 [02:29]). Keep the quote as "a textbook high/low/higher-high that ICT says is not his
  breaker"; hang the narrative requirement on ep39 only. Timestamp [02:29] is correct (caption chunk starts there).

## 08-breaker-blocks/mitigation-block

- [FIX] The mitigation candle's colour is stated three different ways and two are wrong. Formal Criteria: "the last
  candle of the **prior-direction colour**"; Formula: "the last candle of the **ORIGINAL-direction colour**"; Visual
  Pattern: "last down... no: **LAST UP-colour candle** before the failure swing's low is the mitigation candle" (the
  writer's self-correction is left in the diagram, and it corrects the wrong way). Definition and Example 1 say "last
  down candle" / "last down-close candle". — evidence: "Inside that low, what we're going to be focusing on is the
  last down candle. Because the last down candle is where the buying took place right before that little short-term
  rally up." (MIT-LECT [04:14–04:23]); "that last down candle will give us a bearish level to sell into." [05:02];
  "Trades back up into the last down candle." [12:29]; "Last down candle. Wait for the up move. Price hits it. Sell it
  right there. This is a mitigation block." [13:29–13:34]. — required change: bearish mitigation block = the last
  DOWN-close candle at the failure-swing low (the candle that was a bullish reference and now sells); bullish mirror =
  last UP-close candle at the failure-swing high. Fix Formal Criteria, Formula and redraw the Visual (remove the
  "last down... no:" text).
- [FIX] Formula `mitigation_zone := [low(candle), high(candle)]  # entire body/range` is the wick range; the text,
  c3 and ICT say body. — evidence: "it's inside the body of the candle, which is what a mitigation block represents"
  (MIT-LECT [12:32]); "The bodies, the whole entire candle is used, not just the bottom" [13:51]; stop "above the down
  candle … that high on this candle comes in at 112.89" [14:01–14:09]. — required change:
  `mitigation_zone := [min(open,close), max(open,close)]` (whole body), `stop := above high(candle)`.
- [FIX] Timeframes "M15+ in the worked examples" — the lecture names only a 30-minute chart. — evidence: "Let's take a
  look at a 30 minute chart on the same price action." (MIT-LECT [13:13]); grep "minute|hour|daily|weekly" in MIT-LECT:
  that is the only hit. — required change: "worked example on a 30-minute chart [13:13]; no floor stated".
- [NOTE] "(or its mirror, a 'W')" — "W pattern" has 0 hits in MIT-LECT; label it as the inferred mirror, not ICT's term.
- [NOTE] Common Mistakes "the same structural break a CHoCH names, not a BOS" — tag CHoCH/BOS as SMC terms (0 hits in
  either corpus) per the fix brief.

## 08-breaker-blocks/breaker-vs-mitigation

- [FIX] Same candle-colour error as mitigation-block: Formal Criteria "the body of the last **original-direction**
  candle inside the low/high", Visual "last **up-colour** candle's BODY", Example B "The last **up-close** candle
  inside the low framed by that failure swing = mitigation candle". — evidence: MIT-LECT [04:14–04:23], [05:02],
  [13:29–13:34] (last DOWN candle at the failure-swing low). — required change: "last down-close candle at the
  failure-swing low (bearish case; mirror for bullish)" in all three places.
- [NOTE] "CHoCH-vs-BOS as the axis" — tag as SMC terms (0 corpus hits). Everything else verified: SWING-PTS
  [01:37–01:51], BRK-LECT [00:26], [00:42–00:56], MIT-LECT [02:44–03:08], [08:57], HTF-PD [07:46–07:51],
  [20:55–21:07] all verbatim at the cited timestamps.

## 19-rejection-blocks/rejection-block

- [FIX] New claim not in the audit and contradicted by the corpus: "the wick itself is expected to be the part later
  run through" (Definition), c2 "the wick is expected to be run through", Visual "(wick tip is NOT the level —
  expected to be run through)", Example "the wicks above are the part liquidity sits behind and gets run through",
  Common Mistakes "the wick is what gets run through". — evidence: "We look for a price to go just below the bodies of
  the candles, and we'll trade right below that like a turtle soup. It doesn't need to go through the wicks."
  (CLASSIC-SWING [22:13–22:17]); "When you see the long wicked candles and you're bearish, chances are it probably
  won't go above the wicks. Many times we'll just go above the bodies of the candles and then fail there. That's the
  rejection block." [36:12–36:20]. HTF-PD [23:07] "You would expect that to be ran out" refers to the rejection-block
  level just above the bodies, not the wick. — required change: state that price is expected to trade just past the
  body edge (into the wick zone) and fail there, and "doesn't need to go through the wicks"; remove every "wick gets run
  through" sentence (Definition, c2, Visual, Example, Common Mistakes).
- [FIX] Swapped attributions. Page: '"a lot of wicks" (ICT-2017-HTF-PD-ARRAYS [29:09]), "long wicks"
  (ICT-2017-QUARTERLY-SHIFTS [24:28])'. — evidence: "if it has wicks, long wicks below it" (HTF-PD [29:09]); "if those
  highs have a lot of wicks" (QTR [24:28]); "a lot of wicks" also at HTF-PD [22:59], "long wicks" also at QTR [24:37].
  — required change: swap the two timestamps (or cite [22:59]/[24:37]).
- [NOTE] Flagged quote adjudicated: "The rejection block would be just above the candle's body, not the wick's."
  (HTF-PD [18:49]) — the page's "not the wicks" differs by an apostrophe only (ASR-trivial); optionally add `[sic]`.
- [NOTE] "Less standardized than OBs and FVGs; ICT teaches RBs as secondary references" and the aliases "wick rejection
  block", "long-wick block" are unsourced editorial; label or drop.
- [NOTE] JSON timeframes start at M15 while the text says no floor; harmless but inconsistent with the audit's
  cross-page item 8.

## Cross-page items for the lead (outside this cluster's edit scope)

- `concepts/08-breaker-blocks/failed-breaker.md` still encodes "originally bearish OB → bullish breaker (after CHoCH up)"
  and "bearish CHoCH/BOS confirms" — the pre-audit breaker definition; it now contradicts the rewritten
  breaker-block/bullish-breaker pages.
- The audit's ep39 reading ("if you leave that out it's not a breaker") was itself the source of the EP39 misattribution
  on three pages; the correction above applies to the audit report's wording too.

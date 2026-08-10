# Log

Chronological, append-only record of activity on this wiki — ingests, queries, lint passes, structural changes. Each entry starts with `## [YYYY-MM-DD] <kind> | <short title>` so the log is parseable with `grep "^## \[" log.md | tail -10` for the last 10 entries.

Per the Karpathy LLM Wiki pattern, this file complements [`INDEX.md`](INDEX.md) (content-oriented, alphabetical-ish catalog) — `log.md` is **time-oriented**, the wiki's history.

---

## [2026-08-10] distill+redate | Months 05 and 07 read in full; the 17 TIMELINE mismatches resolved; IPDA splits into two dates

**21 packets read in full** — the January-2017 long-term-analysis module (13, including the
122-minute longest packet in the corpus) and the March-2017 short-term-trading module (8,
self-numbered lessons 1–8 assembling the one-shot-one-kill model). 12 new pages, 21 new Source IDs.
`SOURCES.md` now carries **155 IDs**; lint and TIMELINE placement are both at **zero**.

**The 17 pre-existing TIMELINE mismatches are closed** — pages whose `Year Introduced` disagreed
with the section listing them. Resolved by deciding which side was wrong, not by mechanical
reconciliation: 9 page-year corrections, 8 cases where the page was right and the placement lied.

⚠ **"array" appears in ZERO of the 35 Sep–Dec 2016 packets** (full enumeration, independently
reproduced). The **PD-array umbrella term is Jan-2017**; the premium/discount *market states* are
Sep 2016. Same shape as draw-on-liquidity — idea first, name later. `pd-array-definition`,
`pd-array-confluence` and `htf-pd-array-hierarchy` re-dated accordingly.

⚠ **IPDA is two dates, not one.** The **algorithm** is defined Sep 2016 — "the interbank price
delivery algorithm … is the actual, basically artificial intelligence. **It's a price engine** …
90 % done by electronic algorithms" (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [04:44–05:12]) — while
the **20/40/60 data ranges** are Jan 2017. Surfaced only because two concurrent passes disagreed.

⚠ **A previous note of ours was refuted.** The claim that `stop-run-into-breaker` "stays 2018
because breaker vocabulary does not exist until then" is false: the breaker is named Nov 2016
(`ICT-2016-TIMEFRAME-SELECTION` [36:20]) and has a dedicated Dec-2016 lecture. Breaker vocabulary
is **2016**; `breaker-vs-mitigation` and `mitigation-of-breaker` re-dated 2018 → 2016.

⚠ **`open-interest` now carries THREE independent gates, and the earliest is Jan 2017** — the same
~15 % threshold paired with three different second variables: price sideways at a major level
(Jan), the COT commercial line (Feb), higher-timeframe array location (Aug). The page's
"refinement" framing had the chronology backwards. Plus the hard discard rule it lacked: outside
all three, open interest is **not a weak signal, it is not a signal**.

⚠ **Fourth instance of the failure-page defect class.** `failed-breaker` joins `judas-swing-failure`
and `smt-failure`: a *failure/invalidation* concept the original build assigned a year and `high`
confidence on no located source. 37 "breaker" packets scanned, 15 failure-adjacent windows, none
naming a failed breaker. Downgraded to `medium` with the enumeration recorded. `nested-fvg` is a
fifth of the same shape — array-in-array nesting is Feb 2017, but the strict same-polarity
FVG-in-FVG construction is nowhere in the corpus.

**Two near-misses caught by cross-checking, both rejected on the evidence:** the open-float page's
"120 trading days" is correct (ICT states both "three months of data" and "120 trading days" thirty
seconds apart; the 120 is the precise definition), and the Month-07 cast-forward line is a rolling
lookback, not a daily re-anchored projection — both now recorded on-page so the wrong reading
cannot be re-derived.

⚠ **`ICT-2017-OPEN-FLOAT` and `ICT-2017-OPEN-FLOAT-L12` are different lectures** — lesson 1.4
"Defining Open Float Liquidity Pools" (`vqtA1S9JH34`) and lesson 1.2 "Open Float" (`BkmZgjuYREU`).
A tranche brief wrongly told an agent to reuse the first ID for the second; the agent refused.

**61 of 153 packets now cited.** Of the 92 remaining, ~39 are short OTE pattern-recognition drills.

## [2026-08-10] redate | The 2018 cohort was a build artifact — 21 pages re-dated to 2016–2017 against primary audio

An audit compared every page's `Year Introduced` against the years of the Source IDs it cites.
**23 pages claimed a year no cited source carried.** Twenty of them cited only the placeholder pair
`ICT-2017-CHARTER-OVERVIEW` + `ICT-2022-MENTORSHIP-OVERVIEW` while claiming 2018 — filler citations
from the 2026-05 single-session build, never provenance.

**21 pages re-dated, every change grounded in a transcript quote with a timestamp.** Turtle soup,
stop runs, SMT, relative equal highs/lows, volume imbalance, gap classification and symmetrical
projections are **2016**. The NY and failed Judas swings, Asian-range projections, index SMT,
draw-on-liquidity and the liquidity matrix are **2017**. `TIMELINE.md` rewritten to match; its 2018
section had listed eight concept groups that do not belong to 2018, and its 2021 section is now
empty of concept files.

**The 2026-08-09 pass got the NY Judas wrong.** It closed the question by reporting that all 16
corpus files mentioning "Judas" attach the label to the London protraction only. False — three
May-2017 lectures name the New York Judas outright, and ICT enumerates **four** session Judas swings:
"the London open for Judas, the CME open for the New York Judas, and Asia it has its Judas at eight
o'clock … and then you have it also in London close" (`ICT-2017-MARKET-REVERSALS` [28:07]). The
earlier pass enumerated the file population but never read the mentions inside it. ⚠ **The Asia and
London-close Judas swings remain undocumented in this library.**

**Two "failure" pages had no source at all.** `judas-swing-failure` and `smt-failure` were both
assigned `2018` + `high` confidence on nothing. Full-corpus enumeration finds ICT teaching each base
concept but never its named failure mode — what he actually teaches is the *delayed protraction* and
the openly accepted no-entry day. Both downgraded to `medium` with the searched population recorded
on-page. Same shape twice; flagged as a probable build-era defect class.

**Turtle soup is not ICT-original**, and the library had never said so. He credits it outright —
"Street Smarts book, where I got the inspiration for this pattern" [30:19]; "Linda Rashkin … in her
book with Larry Connors" [32:53] — and states his own extension: the raid must land in a
pre-identified HTF discount array, not merely below an old low.

**The corpus now self-dates.** Three lectures state their calendar month in their own audio —
*Liquidity Voids* [00:37], *Divergence Phantoms* [00:30], *Double Bottom Double Top* [00:30], all
"December 2016". The Month→calendar map is no longer an inference from lecture ordering.

⚠ **New registry rule, added after a near-miss:** lesson numbers are either a verbatim quote with a
timestamp or marked unknown — **never inferred from upload order.** A "teaching 6 of 8" was one
commit from freezing into the append-only registry for a lecture that states no lesson number at all.
Month 04 holds 13 packets, not 8, and upload order does not track lesson order: one lecture
self-states "third teaching of eight" while sitting 4th by upload, another "7 of 8" while sitting 12th.

18 new Source IDs registered. Three duplicate-ID collisions caught and consolidated before commit —
two agents had independently minted separate IDs for the same video, which an append-only registry
cannot undo.

## [2026-08-10] lint+refine | Closed the three open threads; added a lint check that catches silent header/JSON drift

The three items left open at the end of the distillation programme are resolved. None needed a
new page — two were answered by **enumerating the corpus** rather than by finding new material.

- **"Eight vs six" projected ranges — RESOLVED.** `projected-range-objectives` recorded that ICT
  says "eight" twice while enumerating six. Searching all **five** Month-10 index-futures
  lectures: only two mention profile names, and the follow-up lesson
  [`ICT-2017-INDEX-TRADE-SETUPS`] walks **the same six**, one by one. **Six is the taught set**;
  "eight" is a repeated misstatement, not a pointer to missing profiles.
- **That follow-up lesson was itself uncovered material**, so `projected-range-objectives` gained
  a **trigger layer**: index SMT across S&P/NASDAQ/Dow as the entry signal for every profile,
  time-of-day holds (10:30–11:00 AM minimum; PM toward the 15:00 bond close), the AM/PM extremes
  as M15/H1 arrays, and the rule that a reversal needs that array **nested** with an H4/daily one.
- **The 30 % vs 34 % accuracy discrepancy — RESOLVED.** Enumerating every accuracy figure in the
  corpus gives **three**: 30 % (recurring), 33 % once, 34 % once. **30 % is the convention**, and
  `ICT-2016-NO-FEAR-LOSING` builds it arithmetically — $5,000, 10 trades, 30 % accuracy → 2 %/month
  at 3:1 and 8 %/month at 5:1. `r-multiple` now carries the worked table instead of "he says both".
  ⚠ That lecture was correctly classified NOT-A-CONCEPT (psychology); it is cited only for the
  arithmetic. **A rejected lecture can still be a legitimate source for one fact.**
- **`ny-judas-swing` / `judas-swing-failure` dating — CONFIRMED at 2018, deliberately.** All 16
  corpus files mentioning "Judas" were checked. Both 2016 lectures and the 7 mentions in the
  Apr-2017 intraday-profiles lecture attach the label to the **London / after-midnight**
  protraction only. There is no NY-Judas naming anywhere earlier than the existing date, so the
  two pages stay at 2018. The absence is now **sourced against the enumerated population**, not
  assumed — per [[feedback-enumerate-before-asserting-absence]].

⚠ **A silent failure mode was found and closed.** Three pages had a `**Source IDs:**` header that
disagreed with their JSON `sources[]`: edits updated the header and missed the JSON because the
array's formatting differed from what the edit expected. Every existing check reads only **one**
of the two lists, so nothing noticed — the same shape as the `bad_lines` defect found in the
trading repo the same day: *a check that cannot fail because it never looks at the thing that
breaks.* Fixed on `trendline-liquidity`, `risk-per-trade` and `r-multiple`.

**New: `tools/lint.py`** — the lint is now a committed script rather than a re-typed one-liner,
with two checks added: **header↔JSON source agreement** and **header↔JSON year agreement**. Both
verified by mutation (drop a source, change a year → lint exits 1 naming the file).

Two new Source IDs. Lint clean: **252 concept pages**, **97 Source IDs**, exit 0.

**All distillation threads are now closed.**

## [2026-08-09] ingest | Distillation tranche 5 - market maker traps, protraction, anticipatory setups, sentiment, rate triad. BACKLOG CLOSED.

Backlog items A12-A15 plus both section-B merges. Nine transcripts read in full (~2.7 hrs).

- [market-maker-trap](concepts/31-models/market-maker-trap.md) - **one page, four sources.** The backlog listed a single Head & Shoulders lecture; the corpus holds a deliberate **four-lecture series** (False Flag, False Breakouts, Trendline Phantoms, Head & Shoulders - 90 min across two months). One mechanism: a classical retail pattern printed *against* HTF order flow, so the pattern's textbook trigger is the liquidity pool. Writing it from the one lecture the backlog named would have repeated the 2026-08-05 sampling error exactly.
- [market-protraction](concepts/13-judas-swing/market-protraction.md) - a small counter-directional impulse swing at **20:00 / 00:00 / 07:00 New York**. Backlog flagged a possible split with `impulse-price-swing`; reading settled it - ICT defines protraction *against* the untimed impulse swing ("the difference... is the fact that there is a **time element**"), so the primitive is defined inline and no second page was written.
- [anticipatory-setup-development](concepts/25-htf-bias/anticipatory-setup-development.md) - **two monthly candles define the range**: the most recent down candle and the nearest up candle whose low exceeds its high. Whichever has been violated becomes an order block; the other is the objective. Then refine W -> D -> H1.
- [sentiment-effect](concepts/31-models/sentiment-effect.md) - short-term sentiment is **maximally opposed at the entry**. Four buy/sell conditions on the Asian range and midnight-NY open, with an explicit odds-decay rule: the longer price hovers at the 15-minute array, "the odds drop off precipitously".
- [interest-rate-triad](concepts/03-order-flow/interest-rate-triad.md) - 30-year / 10-year / 5-year read against each other; **a failure swing in one validates a dollar-index PD array, and its absence is a pass rule**.

⚠ **Backlog item B1 was misclassified as a MERGE.** It was slated to append "smart-money framing" to `interest-rate-differentials`. The lecture's actual subject is the named **interest rate triad** with its own instruments, signal and pass rule - a distinct concept, not a paragraph. It also resolves a garbled quote already in the library: `bond-yield-analysis` cites "an intratrade triad", which is whisper mis-hearing **interest rate triad**.

⚠ **Two dating corrections, both forced by reading rather than by audit:**

- **[judas-swing](concepts/13-judas-swing/judas-swing.md) and [london-judas-swing](concepts/13-judas-swing/london-judas-swing.md): 2018 -> 2016.** The September-2016 protraction lecture uses the term outright - "we see that as market protraction **or a Judas swing**" - and describes the London instance in full. `ny-judas-swing` and `judas-swing-failure` were **left at 2018**: the same lecture describes the 07:00 NY window but does not attach the Judas label to it, so the evidence does not extend there. Flagged for a future pass rather than swept along.
- **[trendline-liquidity](concepts/02-liquidity/trendline-liquidity.md): 2017 -> 2016**, and materially extended. The page treated trendlines as unreliable; the 2016 lecture rejects the *premise* - "price has no awareness of your trendline" - and supplies the counter-entry rule (fade the swing point between touch 2 and touch 3; the stops rest at point 2, not point 3).

**Both merges completed.** B2 (*Reducing Risk & Maximizing Reward*) went into [risk-per-trade](concepts/32-risk-management/risk-per-trade.md) - leverage as a trap rather than a resource (**3:1, not 50:1**), H4 entries on monthly/weekly frames to compress the stop, one to two swing trades every four to six weeks - and [r-multiple](concepts/32-risk-management/r-multiple.md) - 200-500 pip ranges yielding up to 10R. ⚠ It also exposed a **discrepancy in ICT's own numbers**: this lecture says 3:1 needs **30 %** accuracy, `ICT-2017-SWING-ELEMENTS` says **34 %**, and the arithmetic breakeven is **25 %**. All three are recorded on `r-multiple`; none was quietly selected.

Nine new Source IDs. Lint clean: **252 concept pages**, **95 Source IDs**, 0 dead links, 0 dead `related[]`, INDEX-disk aligned, TIMELINE covers all five new pages, header/JSON years agree on every file.

**The distillation backlog is closed: 16 of 16 concepts written, 2 of 2 merges done** (one merge reclassified to a concept).

## [2026-08-09] ingest | Distillation tranche 4 — swing hallmarks, projected ranges, macro-to-micro, equity seasonals

Backlog items A8, A9, A10, A11. Five transcripts read in full (two were needed to settle A9).

- [swing-trading-hallmarks](concepts/31-models/swing-trading-hallmarks.md) — **seven cumulative** checks for whether a swing trade is valid; COT and seasonals flagged by ICT himself as optional enhancers. Also carries the static rule-filter doctrine — *"you don't side with ICT, you side with your rule-based ideas"* — and the risk/equity gate that can veto a valid setup.
- [projected-range-objectives](concepts/31-models/projected-range-objectives.md) — the taxonomy of index-futures daily profiles across AM / lunch / PM. The load-bearing rule is the **PM continuation filter**: whether the PM resumes the AM direction depends on the *timeframe rank* of the array the AM reversed at — H4-or-higher can be recapitalised, M15/H1 gets traded through.
- [macro-to-micro-framework](concepts/03-order-flow/macro-to-micro-framework.md) — a **3–6 month currency outlook from the debt market**, cascaded to a pair list and then to ordinary daily PD-array entries. Contains the **10Y-vs-30Y internal SMT divergence**, which appears nowhere else in the library, and the Nov-2016 election fake-move filter.
- [equity-seasonal-windows](concepts/04-time-cycles/equity-seasonal-windows.md) — three divisions of the stock year, the **May–October low-magnitude period**, and the month-by-month Dow tendency table.

⚠ **A9 was misclassified in the backlog.** It pointed at *Stock Trading — Valuation Stock Selection* for the Feb–May / May–Sep windows. Reading it showed the lecture is actually **long-call / long-put option mechanics** — out of scope for this library — with the seasonal windows stated in its first 60 seconds as context. The real source is *Stock Trading — Seasonals & Monthly Swings*, which was not on the A-list at all. The page is written from the seasonals lecture, with the options lecture cited only for the three program windows and its scope exclusion recorded on the page and in `SOURCES.md`.

⚠ **Count discrepancy recorded, not smoothed over.** ICT says "eight projected ranges" twice; the lesson enumerates and diagrams **six**. The page states both facts rather than inventing two profiles to reach eight.

⚠ **[macro-to-micro-framework](concepts/03-order-flow/macro-to-micro-framework.md) vs [bond-yield-analysis](concepts/03-order-flow/bond-yield-analysis.md)** — the closest near-duplicate this programme has produced. Both read debt against the dollar index. They differ on instrument (30Y vs 10Y), on whether seasonals are used, on output (a **direction** cascaded to pairs vs a **regime** classification), and on signature signal (10Y-vs-30Y internal divergence vs tandem-vs-inverse DXY movement). A comparison table sits on the macro page and both cross-link.

**One refinement:** [r-multiple](concepts/32-risk-management/r-multiple.md) gained the breakeven-accuracy arithmetic — `1/(1+R)`, with ICT's own quote that **3:1 permits as low as 34 % accuracy to be net profitable** and his preference for 5×. The page previously had target-R tables and no statement of why R is the lever.

Five new Source IDs. Lint clean: **247 concept pages**, **86 Source IDs**, 0 dead links, 0 dead `related[]`, INDEX↔disk aligned, TIMELINE covers all four.

**Remaining backlog: 4 concepts + 2 merges.**

## [2026-08-09] ingest | Distillation tranche 3 — day trading model, timeframe selection, bond yields, explosive market selection

Backlog items A2, A3, A5, A6 from [distillation-backlog-2026-08-09](meta/distillation-backlog-2026-08-09.md). 175 minutes of lecture across six transcripts, all read in full before writing.

- [ict-day-trading-model](concepts/31-models/ict-day-trading-model.md) — **one page, two lectures** (Month 08 lessons 1 and 8). Target **65–70 % of the daily range**, expected range = the **five-day ADR**, **two setups per day on average**, and the **Sunday-opening-price filter** projected on the hourly through Thursday. Lesson 8 folds in as the HTF-integration section: enter at the **0 GMT open** (or a 10–20-pip limit beyond it) with a five-day-ADR stop, no London session required.
- [timeframe-selection](concepts/25-htf-bias/timeframe-selection.md) — the timeframe→style map (monthly = position, weekly = swing, daily = short-term, H4-and-below = day trading), five trader models, and **ICT's reduction of his own repertoire to three setups**: return into an exposed range, order block, stop run. Distinct from [top-down-analysis](concepts/25-htf-bias/top-down-analysis.md), which is the descent sequence every trader performs; this page is which row you *trade* on.
- [bond-yield-analysis](concepts/03-order-flow/bond-yield-analysis.md) — **one page, two lectures.** The 10-year note read against the dollar index. Its primary output is a **regime test**, not a direction: notes and DXY moving **in tandem** = large consolidation across bonds, dollar and FX (day trades only); moving **inversely** with the seasonal = trending (position trades). Qualified by a **"crack in correlation"** — broken mirror symmetry, which ICT himself names as an SMT divergence.
- [explosive-market-selection](concepts/31-models/explosive-market-selection.md) — the **eight hallmarks** of an explosive swing trade: ≥2 of 4 asset classes trending (one from {commodities, stocks} *and* one from {currencies, interest rates}), intermarket confluence, COT alignment, open interest, seasonal tendency, volatility contraction, contrarian headlines, and a 15-period Williams %R. Adjacent to [mega-trade](concepts/31-models/mega-trade.md) — ICT names it as the precursor — but swing-scale, not position-scale.

⚠ **Two existing pages were refined, not duplicated.** Both refinements came out of the explosive-markets lecture and would have been silently forked into the new page if the sibling check had been skipped:

- [commitment-of-traders](concepts/03-order-flow/commitment-of-traders.md) — **recentred zero line.** When qualifying a trade ICT discards the printed zero line and uses the **midpoint of the commercial line's 12-month high/low range**. A market whose commercials sat below absolute zero all year can still be buying by this measure.
- [open-interest](concepts/03-order-flow/open-interest.md) — **10–15 % qualifying gate.** The page previously stated "no numeric threshold for *rising* is taught". That was true of the trend-sponsorship read and **wrong** for the qualifying read: a decline of 10–15 %+ paired with a rising commercial net line is short covering (bullish); the mirror is bearish. The claim is now scoped to the read it actually describes.

Six new Source IDs (five 2017 Core Content, one 2016). Lint clean: **243 concept pages** (+1 directory README = 244 files under `concepts/`; earlier entries counted the README, which is where "240" came from), **81 Source IDs**, 0 dead links, 0 dead `related[]`, INDEX↔disk aligned, TIMELINE covers all four new pages. `meta/hot.md` refreshed — it had been stale since 2026-05-21.

**Remaining backlog: 8 concepts + 2 merges.**

## [2026-08-09] ingest | Distillation tranche 2 — mega-trade, filling the numbers, reclaimed OB, efficiency paradigm

Backlog items A1, A4, A7, A16 from [distillation-backlog-2026-08-09](meta/distillation-backlog-2026-08-09.md).

- [mega-trade](concepts/31-models/mega-trade.md) — **one page, four sources.** The four Mega-Trades lectures (stock/bond/commodity/forex, 161 min) teach one concept across four markets: the single prolonged annual move, six-to-nine months in equities, driven by seasonal tendency (quarterly shifts in FX), qualified by institutional sponsorship. Writing four near-identical pages would have been the obvious mistake.
- [filling-the-numbers](concepts/04-time-cycles/filling-the-numbers.md) — the daily range fills **~four reference levels per day**: prior-day high/low plus the **zero-GMT** pivot ladder. Levels attract because staged orders rest there; *which* four fill is selected by order flow + the PD array matrix. Includes the retail inversion — S1/S2 below the central pivot as a short area, not a buy area.
- [reclaimed-order-block](concepts/07-order-blocks/reclaimed-order-block.md) — a block formed on the **opposing leg** of a market maker curve, re-used in the opposite role. Distinct from mitigation: a mitigated block is spent, a reclaimed block is deliberately re-entered. `07-order-blocks` had ten files and none covered it.
- [market-efficiency-paradigm](concepts/03-order-flow/market-efficiency-paradigm.md) — "they're not efficient for the speculators, they're efficient for the smart money"; smart money is the liquidity provider, "everyone else's liquidity". The premise beneath treating levels as destinations rather than barriers.

⚠ The efficiency paradigm is recorded with an explicit confidence note: ICT asserts it as fact about market structure; the library records the assertion and its lineage and takes no position on whether it is empirically true, per `CONTRIBUTING.md`.

Seven new Source IDs (four mega-trade lectures + three). Lint clean: 240 concept files, 75 source ids.

**Remaining backlog: 12 concepts + 2 merges (~6 hrs).**

## [2026-08-09] ingest | Distillation tranche 1 — four concepts from dedicated Core Content lectures

Continuing the market-context backlog. Method: a **curriculum map** — a lecture *titled* after a concept is far stronger evidence than a frequent phrase — which ranked 36 lectures (14.2 hrs) whose subject the library did not cover. Tranche 1 took the four with the strongest dedicated teaching behind them.

- [commitment-of-traders](concepts/03-order-flow/commitment-of-traders.md) — weekly CFTC report, **futures positions only**, commercial net = long − short; above the zero line is a buy program, below a sell program; judged against that market's **own 12-to-6-month band**, not an absolute count. (`ICT-2017-COT`, 35 min)
- [open-float-liquidity-pool](concepts/02-liquidity/open-float-liquidity-pool.md) — **60 trading days back + 60 cast forward = 120 days**; highest high / lowest low mark the *large-fund* pools, which stay live until the forward horizon expires. (`ICT-2017-OPEN-FLOAT`, 28 min)
- [interest-rate-differentials](concepts/03-order-flow/interest-rate-differentials.md) — central-bank policy-rate table as the start of the macro read; capital flows to yield; output is HTF bias only. (`ICT-2017-RATE-DIFFERENTIALS`, 19 min)
- [premium-vs-carrying-charge-market](concepts/03-order-flow/premium-vs-carrying-charge-market.md) — nearby vs next month out; no premium = carrying charge (normal), nearby above later months = premium = demand high / supply short. (`ICT-2017-CARRYING-CHARGE`, 19 min)

⚠ **Open float is NOT the IPDA 60-day lookback.** IPDA windows are *trailing only*; open float is symmetric and carries an expiry horizon. The lookback halves coincide, the concepts do not — disambiguated on both pages so the pair cannot be silently conflated later.

⚠ **"Carrying charge" means two different things.** In commodities it is the delivery-month curve; in FX it is a rate-differential carry. Same phrase, different mechanism — cross-noted on both pages.

Four new Source IDs. Full-library lint clean.

**Backlog:** 32 candidate lectures remain (~11 hrs), including the Mega-Trades series (161 min, four markets, zero coverage), *How Market Makers Condition The Market*, and *Market Maker Trap Head & Shoulders*. Several curriculum-map hits are psychology or admin rather than concepts (*No Fear Of Losing*, *Growing Small Accounts*) — the method has false positives by design and they are filtered by reading, not by score.

## [2026-08-09] ingest | Core Content mined: the library was missing ICT's entire market-context layer

Ingested the 114-video *Mentorship Core Content* curriculum (113 usable) bringing the corpus to 153 packets / 59 hrs. Ran a coverage scan — recurring 2–4 word phrases across all 148 usable transcripts, minus every term the library already names — and the gap was structural, not incidental.

**The library documented ICT's price-structure half (228 files: FVG, order blocks, MSS, PD arrays, killzones) and had essentially nothing on his market-context half.** Verified absent by direct search, with corpus frequency / source-spread:

| concept | mentions | sources | library hits before today |
|---|---|---|---|
| seasonal tendency | 398 | 51 | 0 |
| dollar index | 334 | 33 | 0 |
| interest rates / central bank | 272 | 32 | 0 |
| bank dealers range | 228 | 10 | 0 |
| open interest / COT | 175 | 16 | 0 |
| average daily range | 123 | 15 | 0 |

New concept files, each written from the dedicated lecture rather than from inference:
[seasonal-tendency](concepts/04-time-cycles/seasonal-tendency.md),
[central-bank-dealers-range](concepts/15-sessions/central-bank-dealers-range.md),
[open-interest](concepts/03-order-flow/open-interest.md),
[dollar-index](concepts/03-order-flow/dollar-index.md).
Five new Source IDs.

⚠ **Dating correction:** the Core Content lectures are the **2017 mentorship** re-uploaded in 2022 — each names its own 2017 lesson number ("lesson 4.3 of the January 2017 ICT mentorship"). Cited as 2017; the 2022 upload date is publication, not authorship. Anyone citing them as 2022 material is mis-dating the curriculum.

**Not filed as new concepts:** `old high` / `old low` (541 mentions, 72 sources) are ICT's plain phrasing for prior swing levels used as liquidity targets, already covered by [swing-high](concepts/01-market-structure/swing-high.md), [swing-low](concepts/01-market-structure/swing-low.md), [buy-side-liquidity](concepts/02-liquidity/buy-side-liquidity.md) and [sell-side-liquidity](concepts/02-liquidity/sell-side-liquidity.md). Added as **aliases** — a new page would have duplicated four existing concepts. Coverage scans surface vocabulary, not concepts; every candidate still needs the source read before it earns a file.

**Still open:** interest-rate differentials / carrying-charge markets and average-daily-range have corpus evidence but no dedicated lecture read yet. Commodity-specific material (Month 10) is largely unmined.

## [2026-08-09] correction | Channel enumerated: 43 OTE videos, not 3 — the 08-05 pass is PARTLY REVERSED

Enumerated the official channel (715 videos) instead of sampling. **43 carry OTE in the title; the library cited 3.** Among them a 20-part *OTE Pattern Recognition Series* of which only Vol. 01 had ever been read. Ingested 40 as transcripts (~7 h) via `tools/ingest_video.py`; 15 new Source IDs added for the volumes actually cited.

Two claims from the 2026-08-05 correction do not survive the fuller corpus:

1. **Standard-deviation targets are dedicated OTE material.** 08-05 removed them saying "none … is what the dedicated OTE material teaches". The series teaches them across ≥9 volumes; `ICT-2020-OTE-VOL10` (01:39–02:00) walks the fib preset's own levels — half / full / 1.5 / 2 SD. Restored in `ote-rules` item 7 as an era-fork. ⚠ Note the *set* differs from the library's: the OTE series uses **−0.5/−1.0/−1.5/−2.0**, `standard-deviation-projections` documents −1.5/−2.0/−2.5/−4.0. Both recorded.
2. **The stop rule is a fork, not a single rule.** 08-05 asserted a tighter stop had "no primary-source quote behind it". Falsified by **two of the three videos that pass itself used**: `ICT-2020-OTE-VOL01` (41:33) "so it's a 20 pip stop"; `ICT-2020-OTE-EURUSD-EXAMPLE` (02:50) a 20-pip stop placed to survive expansion "beyond the 79% retracement level" — explicitly not leg-origin. Fixed-pip stops recur in Vols 02/10/15/19/20.

The reversal-framing correction (OTE ≠ 2022 model) **stands unchanged** — the fuller corpus supports it.

Root cause: sample size, not method. Confident negatives ("none of the three", "no primary-source quote") are unsupportable from 3 of 43 sources. Lesson banked: enumerate the source population before asserting an absence.

Updated: `ote-rules.md` (items 6, 7, banner, formula, JSON), `ote-overview.md` (criteria, formula, JSON, ASCII), `standard-deviation-projections.md` (two-set note), `SOURCES.md` (+15 IDs), `fib-anchoring.md` (+3 corroborating sources).

## [2026-08-09] ingest | Three dedicated OTE sources re-read with frames — fib anchoring documented for the first time

Re-ingested `ICT-2017-OTE` (OTE Primer, 44m), `ICT-2020-OTE-VOL01` (57m) and `ICT-2020-OTE-EURUSD-EXAMPLE` (5m) as transcript + scene frames via `tools/ingest_video.py`. No new Source IDs — all three were already cited; the existing entries were re-read, not renumbered.

**New concept: [fib-anchoring](concepts/28-fibonacci-levels/fib-anchoring.md).** ICT anchors the fib to **candle bodies, not wicks**, and states the reason: wicks are the part of a candle that differs most between brokers. Primer 36:28 — "we're going to put on the bodies of candles up here, this is the highest body right there… we're going to look at that as the open, so the open is 1.1799, so that's where our fib will be dropped". Restated in the EURUSD example at 01:37. The rule was absent from all 226 prior files despite being load-bearing: it sets `leg_size`, hence the OTE band, the stop at fib 1.0, and every target. Also recorded the contrasting PD-array convention — "the order block is starting at the wick" (`ICT-2020-OTE-VOL01`, 13:56).

Updated: `ote-overview.md` (criterion + formula + mistake + related), `ote-rules.md` (checklist item 2b), `ict-fib-overview.md` (anchor note + formula + mistake), `INDEX.md`, `TIMELINE.md` (2017).

⚠ The 2026-08-05 pass below ran on caption tracks and did not surface this. The rule is spoken plainly in the Primer, so the gap was one of search, not of source access — the frames corroborated the 1.1799 anchor but did not originate the finding.

## [2026-08-05] correction | OTE category re-verified against primary sources — stop placement, continuation framing, target ladder

First substantive content correction since the build. Seven files in `concepts/17-optimal-trade-entry/` and `concepts/28-fibonacci-levels/` carried claims that a primary-source verification pass (official-channel caption tracks, upload dates verified by `yt-dlp`) does not support. Two new Source IDs added: `ICT-2020-OTE-VOL01` (`E9F_aT9f038`, 2020-05-08 — ⚠ frequently mis-dated to 2017 in secondary write-ups) and `ICT-2020-OTE-EURUSD-EXAMPLE` (`2mtzC7ajUew`, 2020-08-10). `ICT-2017-OTE` annotated as the definitional "OTE Primer" (`Cg0-CFJOJvg`, 2017-09-30) which ICT himself defers to from the 2022 mentorship.

**Corrected:**
- **Stop placement.** The library said "SL beyond 0.79 + buffer" across `ote-overview`, `ote-rules`, `ote-62`, `ote-705`, `ote-79`. The Primer states the opposite in as many words: *"my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that."* Vol.01's worked example placed its initial stop at the fib origin likewise. **0.79 is the deepest ENTRY; the stop is the leg-origin extreme (fib 1.0).** The 0.79-buffer stop is retained as an explicitly labelled community variant with no primary quote behind it.
- **Continuation vs reversal.** `ote-rules` #5 described a lower-TF MSS/CHoCH "confirming the reversal". OTE is a **with-trend continuation** entry; a counter-directional sweep is not a precondition, and *sweep/raid/stop-hunt/inducement* appear nowhere as entry conditions in any dedicated OTE teaching. The sweep-reversal sequence is the separately-filed `ict-2022-model`. Cross-links added in both directions so the two are hard to confuse.
- **Missing criterion.** The impulse leg must **break a prior swing level in the trade direction** (short-term / intermediate-term / PDH-PDL). This was absent from the criteria entirely; the Primer teaches intermediate-term breaks as "much much more reliable".
- **Target ladder.** "-1.5 SD / -2.0 SD" replaced with the Primer's own ladder: first partial at the prior extreme (fib 0.0), then **-0.27 / -0.62 / -1.0**. The worked examples' R:R arithmetic (previously ~14-46R) is corrected accordingly and now lands at 1.6-3.8R across the three entry depths.
- **Failure semantics.** `ote-failure` conflated the 0.79 close (a **warning** — out of zone) with invalidation (**leg-origin extreme taken out**). Separated, with a note that body-close-vs-wick semantics are unspecified in the primary material and must be pinned by any mechanical implementation.

**Disclosed, not resolved:** two intra-primary conflicts now stated rather than silently picked — R:R floor (Primer "better than two to one" vs Vol.01's explicit rejection of R:R plus a 15-pip first-scale floor) and time window (Primer is time-silent; Vol.01 teaches 08:30-11:00 NY as constitutive). Both are ICT-original from different eras. The Primer governs as the definitional video; the alternatives are labelled as tracked variants. Bias-gate and PD-array-presence downgraded from hard criteria to strong conventions, since neither is stated as a mandate in the dedicated material.

No other concept directories touched.

## [2026-05-21] structural | wiki-skill adoption + lint

Added `CLAUDE.md` at vault root mapping the existing layout to the `wiki` skill's operations vocabulary (`INDEX.md` ≡ `wiki/index.md`, `meta/hot.md` ≡ `wiki/hot.md`, etc.). Schema continues to live in `AGENTS.md`; the new file is a thin pointer + deviation note, not a duplicate.

Established `meta/` directory and wrote two artifacts:
- `meta/lint-report-2026-05-21.md` — full vault health check: 0 orphans, 0 dead links (1 intentional template placeholder), 0 frontmatter gaps, INDEX↔disk fully aligned. Vault publication-ready.
- `meta/hot.md` — hot cache per the Karpathy pattern, ~500 words, overwrite-on-update.

No concept files modified.

## [2026-05-05] structural | initial scaffold

Repo initialized. Created concept directory tree (33 directories), `TEMPLATE.md`, `README.md`, `INDEX.md` skeleton.

→ commit `e78acd4`

## [2026-05-05] structural | phase 0 meta scaffolding

Built out the 6 root cross-cutting files: `GLOSSARY.md`, `TIMELINE.md`, `READING-ORDER.md`, `SOURCES.md`, `CONTRIBUTING.md`, `CHANGELOG.md`. Refined `TEMPLATE.md` with required top-matter fields + machine-readable JSON block + ICT vs Community section.

→ commit `6086c0e` (+ review fixes `c930bd8`)

## [2026-05-05] ingest | phase 1 — foundations

Wrote 35 concept files: `01-market-structure/` (12) + `02-liquidity/` (14) + `15-sessions/` (9). All Phase 1 files validated: 10 sections, JSON parse, id-match. Updated INDEX, TIMELINE backfill 2016/2017/2018/2021/2022.

→ commit `bb22e31` (+ review fixes `c0a65ee`)

## [2026-05-05] ingest | phase 2 — time & sessions

Wrote 28 files: `04-time-cycles/` (10) + `10-killzones/` (8) + `14-asian-range/` (6) + `13-judas-swing/` (4). Cumulative: 63 files.

→ commit `f68c7a5` (+ review fixes `b4aa89d`)

## [2026-05-05] ingest | phase 3 — PD arrays core

Wrote 33 files across 6 dirs (PD arrays, imbalance, equilibrium, fib levels, OTE, IPDA foundation). Cumulative: 96 files.

→ commit `8a71931` (+ review fixes `2933468`)

## [2026-05-05] ingest | phase 4 — FVG / OB / breakers

Largest single phase: 40 files (FVG 14 + OB 10 + breakers 6 + mitigation 5 + rejection 3 + displacement foundation 2). Cumulative: 136 files.

→ commit `c25affa` (+ review fix `cd866cd`)

## [2026-05-05] ingest | phase 5 — models & strategies

Wrote 30 files (silver-bullet 7 + PO3 6 + AMD 4 + turtle-soup 4 + SMT 5 + stop-runs 4). Cumulative: 166 files.

→ commit `ffecbe4` (+ review fix `3df3b6d`)

## [2026-05-05] ingest | phase 6 — bias, named models, risk

Wrote 28 files (htf-bias 7 + 14 named models including Venom + Zircon + risk 7). Cumulative: 194 files.

→ commit `d9327be`

## [2026-05-05] ingest | phase 7 — final content

Wrote 32 files (CRT 4 + quarterly-theory 9 + news-driven 5 + order-flow 6 + displacement remainder 4 + IPDA lookbacks 4). Cumulative: 226 files. **Library content-complete.**

→ commit `b4bc7d7`

## [2026-05-05] lint | phase 8 — final audit

Verification-only pass. Closed 20 timeline gaps. Confirmed: 226 files validated (10 sections, JSON parse, id-match), 0 broken cross-links, 0 orphan source citations, INDEX↔disk fully aligned, TIMELINE 100% coverage. **Library declared ship-ready.**

→ commit `b543976`

## [2026-05-05] lint | final polish

Cleared 4 stale `(pending)` markers in TIMELINE (Phase 7 had left two on shipped 2025 entries; 2019/2020 sections clarified as no-additions years). Replaced `(Phase 8)` placeholder in INDEX 99-glossary section with explanatory note pointing to root `GLOSSARY.md`. All audit checks still pass.

→ commit `8622ceb`

## [2026-05-05] structural | adapt to Karpathy LLM Wiki pattern

Added `log.md` (this file) and `AGENTS.md` schema following the [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern. The library was already 90% aligned with the pattern — `INDEX.md` was already content-oriented per the design — so the adaptation was incremental: explicit log + explicit ingest/query/lint schema for future LLM sessions.

→ commit `abc69ea`

## [2026-05-05] lint | SMC alias coverage

Added Smart Money Concepts (SMC) vocabulary aliases to 4 existing concept files for grep-discoverability. SMC is a community rebrand of ICT material, not its own framework — adding aliases lets SMC users find the right ICT files without claiming ICT authored the SMC framework.

- `bullish-order-block.md` += `demand zone (SMC)`, `demand block (SMC)`
- `bearish-order-block.md` += `supply zone (SMC)`, `supply block (SMC)`
- `liquidity-sweep.md` += `liquidity grab (SMC)`
- `turtle-soup.md` += `fakeout (SMC)`, `swing failure (SMC)`

Both top-matter `**Aliases:**` fields and JSON `aliases[]` arrays updated.

Also extended `GLOSSARY.md` with an "SMC Vocabulary Cross-Reference" section — full mapping table of SMC terms ↔ ICT equivalents + flagged terms that are SMC-only (engulfing block, Wyckoff spring/upthrust) as out-of-scope.

→ this commit

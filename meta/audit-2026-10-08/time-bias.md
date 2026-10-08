# Cluster TIME / BIAS / MODELS — audit

Corpora searched: `raw/*/report.md` (153 packets, 2016-17 mentorship + 2017/2020/2021 OTE material) and `m22/ep*.txt`
(41 episodes, 2022 YouTube mentorship). Clock convention: every ICT time quoted below is New York local time unless the
quote itself says otherwise (he says so explicitly in `DEFINING-DAILY-RANGE` 03:35 "you have to have a New York time clock").
Packet names are abbreviated to the distinctive part of the folder name (e.g. `M08-DEFINING-DAILY-RANGE` =
`ICT-2022-MENTORSHIP-CORE-CONTENT-MONTH-08-DEFINING-DAILY-RANGE-_2nUKLAD9ig`). Stub IDs = IDs that exist in SOURCES.md
without a video (`ICT-2016-KILLZONES`, `ICT-2016-PO3`, `ICT-2016-LIQUIDITY`, `ICT-2017-CHARTER-OVERVIEW`,
`ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`).

## Summary table

| page | stub/partial/evidenced (from its Source IDs) | verdict | worst finding (one line) |
|---|---|---|---|
| 10-killzones/killzone-times-table | partial (2 stubs + 1 real) | WRONG | "Public / 2016 + 2022" NY AM 08:00–11:00 exists in neither corpus; 2022 says forex NY KZ 07:00–10:00, index AM 08:30–11:00; London close 10–11 in 2022; macros + silver bullets not in corpus |
| 14-asian-range/asian-range | stub (2 stubs) | WRONG | "18:00–03:00" alt window and "typically 25–60 pips" are not ICT; ICT: 20:00–00:00 only, "Asian range has to be 20 to 30 pips", >40 pips = delayed-protraction filter |
| 15-sessions/london-session | stub (2 stubs) | WRONG | "02:00–11:00 London session" appears nowhere; ICT's London manipulation is anchored at the MIDNIGHT open (2016+2017), not "first 15–30 min after 02:00" |
| 15-sessions/london-close | stub (2 stubs) | MINOR-FIXES | 10:00–12:00 is the 2017 KZ; 2022 says "10 o'clock until 11 o'clock in the morning is london closed profit taking hour"; "highest-volume window" / "European book unwinds" not in corpus |
| 15-sessions/central-bank-dealers-range | evidenced | MINOR-FIXES | Buy-day low "between the CBDR and one SD below" understates ICT ("down to the third standard deviation"); page omits the BODY-based range ICT says he prefers |
| 13-judas-swing/judas-swing | partial (2 real + 2 stubs) | MINOR-FIXES | "first 15–60 minutes of the killzone" is not ICT — Judas is measured from an OPENING PRICE (midnight / 08:20 CME / 08:30 / 09:30); FVG-reversal entry is 2022-only |
| 12-power-of-three/power-of-three | stub (2 stubs) | MINOR-FIXES | "MMBM/MMSM = PO3 to the upside/downside" conflates two concepts; "AMD doctrine", "4th phase X" not in corpus; PO3 is defined on the DAILY OHLC bar |
| 11-silver-bullet/silver-bullet-rules | stub (2 stubs) | UNVERIFIABLE | No Silver Bullet teaching in either corpus (10 hits, all idiomatic); only 2022 statement about 10–11 is "have about 80 percent of your trade off" |
| 25-htf-bias/weekly-bias | partial (1 real + 2 stubs) | SOUND | All 2017 quotes verified; "external BOS / EQ / DOL" criteria are SMC vocabulary, not ICT's (minor) |
| 25-htf-bias/daily-bias | partial (1 real + 2 stubs) | MINOR-FIXES | COT midpoint rule: lecture says "bullish if above halfway mark" at 10:22 then "if I'm below it … expand to the upside" at 10:30 — page records only the second; "TDO above prior range = bullish lean" is anti-ICT |
| 31-models/ict-2022-model | stub (1 stub) | WRONG | SL "beyond the swept extreme" and "entry at CE (per 2025 default)" contradict the 2022 episodes (stop above the FVG candle / swing high; limit at the FVG edge); killzone list wrong (model = NY session 07–10 forex / 08:30–11 + 13:30–16 indices); MSS trigger missing |
| 16-smt-divergence/smt-divergence | evidenced (2 real + 1 stub) | SOUND | "gold vs silver" pairing not in corpus (minor) |

## killzone-times-table

- claim: "two ICT killzone time sets … the table below is the public / 2016 + 2022 set" → CONTRADICTED for New York. Neither corpus
  contains a 2016 killzone clock at all (`grep -iE "kill ?zone"` over Months 1–7 packets: zero hits with clock times; first clocked
  killzones are April-2017 `M08-DEFINING-DAILY-RANGE`). The 2022 set for New York is 07:00–10:00 (forex) and 08:30–11:00 (indices), not
  08:00–11:00: "fx predominantly you're working with seven o'clock in the morning to ten o'clock in the morning that's your new york
  open kill zone" (ep17 [23:54]); "if you're looking at a model that works in index futures you're looking at that 8 30 to 11 o'clock
  window and if you're trying to apply this model to fx it's seven o'clock in the morning to 10 o'clock in the morning" (ep17 [25:38]);
  "this is new york index am session operating hours or killzone if you want to call it that and it's 8 30 in the morning to 11" (ep41
  [03:24]); "seven o'clock in the morning new york time that's the beginning of my ict new york kill zone it's extended to 10 o'clock in
  the morning when it's 4x" (ep40 [08:28]). No "8 a.m."/"8 o'clock … kill zone" hit in either corpus (searched `8 a.m|8 o'clock|eight
  o'clock|8:00` near `new york|kill`; raw hits are bond-market opening-range lines only).
- claim: "London Open 02:00–05:00" (public set) → CONFIRMED (2022) — "london open that's our kill zone that i teach here on the youtube
  channel it's two o'clock in the morning to five o'clock in the morning new york local time" (ep20 [08:09]); also 2021: "two o'clock
  in the morning to five o'clock in the morning london" (`ICT-2021-FOREX-INTERACTIVE-LEARNING-EXPERIENCE-SCALPING` [11:20]). ERA-SPLIT
  with 2017 (01:00–05:00) is correctly recorded on the page; 2017 quotes at 03:06/03:18/08:16 verified verbatim; "my normalized kill
  zone which encompasses one o'clock in the morning new york time to 5 a.m new york time" (`ICT-2017-LONDON-OTE-DEMO-SCALPING-EXAMPLE`
  [02:58]). Note the 2017 lecture also narrows the hot spot: "typically london the hot spot for the higher low the form of the day is
  usually between two o'clock in the morning and four o'clock in the morning new york time" (`M08-ESSENTIALS-DAYTRADING` [11:59]).
- claim: "NY AM 08:00–11:00; London Close 10:00–12:00 (public set)" → CONTRADICTED / ERA-SPLIT. 2017: "every day at 7 a.m. … begins the
  New York kill zone every day at 10 a.m. … ends" ([03:57]); London close 10:00–12:00 ([04:31]–[04:39]) — verified. 2022: "that time
  frame 10 to 11 that's london close … i've always taught that 10 o'clock until 11 o'clock in the morning is london closed profit taking
  hour" (ep40 [17:18], [18:14]); news days widen it "between 10 o'clock to noon" (ep40 [18:14]). So the 2022 London close is 10–11, not
  10–12, and NY AM never starts at 08:00 in either era.
- claim: "NY PM 13:30–16:00" → CONFIRMED (2022 indices only) — "the 1 30 to 4 new york local time that's the pm session new york index pm"
  (ep41 [05:53]); "between 1 30 and 4 o'clock in the afternoon new york local time" (ep40 [43:52]). Not a 2017 window (2017 true day
  ends 15:00: "every day at 3 p.m. New York time ends the IPTA true day" [05:29]).
- claim: "Asia 20:00–00:00" → CONFIRMED (2017) — "every day at 8 p.m. … begins the Asian range every day at midnight … ends the Asian
  range" (`M08-DEFINING-DAILY-RANGE` [02:27]–[02:41]). No Asian clock in the 2022 episodes.
- claim: "London lunch 05:00–07:00 (2017)" → CONFIRMED by inference — "this area here between the London and New York kill zones this is
  London lunch" ([07:47]); 2016 version: "Between 5 o'clock in the morning to 8 o'clock in the morning in that time window, the market
  will go back into consolidation" (`M1-HOW-MARKET-MAKERS` [16:15]) — 2016 lunch runs to 08:00, not 07:00 (ERA-SPLIT, unrecorded).
- claim: macros "00:50–01:10, 02:50–03:10, 09:50–10:10, 13:50–14:10, 14:50–15:10" → NOT IN CORPUS. Searched `macro` in both corpora: raw
  hits are "macro economic"; 2022 hits name only "there's an algorithm macro that starts running at 130" (ep05 [32:15]) and "three
  o'clock to four o'clock that market on closed macro" (ep39 [72:50]). No 20-minute windows anywhere. 2023+ material.
- claim: silver-bullet windows 03–04 / 10–11 / 14–15 → NOT IN CORPUS (see silver-bullet-rules below).
- claim: "Year Introduced 2016" → NOT IN CORPUS — no clocked killzone in any 2016 packet; earliest is April 2017.
- engine divergence: no engine convention covers clocks; but any engine using NY AM = 08:00–11:00 is on neither ICT era (07–10 forex,
  08:30–11 indices). ICT's own ruling on fills vs windows: "Kill zones are when you determine your entry, and you place your orders, and
  you walk away. You don't need to have your entry filled inside that kill zone window" (ep18 [48:30]).

## asian-range

- claim: "typically 18:00 prev → 03:00 NY … some references use the entire Asia session 18:00–03:00" → NOT IN CORPUS. Searched
  `(asia|asian).{0,80}(7 p|6 p|5 p|7 o'clock|6 o'clock|3 a.m|3 o'clock)` and the reverse in raw; `asian? (range|session)` in m22. Zero
  hits for a 18:00 or 03:00 bound. ICT frames 20:00–00:00 as the only definition: "this is the definitive teaching … if you've seen
  anything different in the past this is the real one okay every day at 8 p.m. … begins the Asian range every day at midnight … ends
  the Asian range" (`M08-DEFINING-DAILY-RANGE` [02:13]–[02:41]).
- claim: "20:00 → 00:00 NY" → CONFIRMED (above; also "between 8 p.m. New York time, midnight New York time, we're going to be looking for
  consolidation" `M08-INTRADAY-PROFILES` [05:28]; "at 8 p.m. starting the Asian range" `M08-CENTRAL-BANK-DEALERS` [11:27]).
- claim: "Range size: typically 25–60 pips on EURUSD" → CONTRADICTED. ICT's numbers are a filter, not a typical range: "Asian range has to be
  20 to 30 pips" (`M08-INTRADAY-PROFILES` [03:09]); "if the Asian range is greater than 40 pips I'm going to consider the delayed
  protraction profile" (`M08-WHEN-AVOID-LONDON` [09:26]); "Many times the Asian range is a lot larger than 20 30 40 pips but many times
  it's at least enough to get 20 pips out of it" (`M09-20-PIPS-PER` [06:59]). A 60-pip Asian range is a stand-aside condition.
- claim: "engineered liquidity setup for London … London's first killzone almost always sweeps one bound" → CONFIRMED in spirit (2016):
  "Every day starts with consolidation, Asian range. After midnight, there's a manipulation that takes place … It's coming in the form
  of a Judas swing" (`M1-HOW-MARKET-MAKERS` [13:56]–[14:05]); but ICT's sweep is of the opening price/CBDR deviations, not strictly the
  Asian bound: "protractionary stage for Judas swing will be one to two standard deviations of the central bank dealer's range"
  (`M08-INTRADAY-PROFILES` [03:29]).
- claim: scoped warning quotes (`ICT-2017-INTRADAY-TOP-DOWN` 11:14, 11:49) → CONFIRMED verbatim ("Now if I'm bullish I expect the Asian
  range high to be retested for entry as support" [11:14]).
- claim: "Year Refined 2022" → EMBELLISHED. The 2022 model drops the Asian range: "I wouldn't worry about doing anything with Asian range"
  (ep18 [06:22]). 2016 view: "I don't believe Asian is that influential initially" (`M1-IMPULSE-PRICE-SWINGS` [03:58]).
- engine divergence: none of the listed conventions; if any study filters on "Asian range 25–60 pips", it is filtering on a number ICT
  never gave.

## london-session

- claim: "London session runs from 02:00 NY to 11:00 NY (canonical)" → NOT IN CORPUS. Searched `london.{0,80}(2 a.m|2 o'clock|…)` and
  `11 (a.m|o'clock)` near `london` in raw; `london` + clock in m22. Nothing defines a 02:00–11:00 session. What exists: London KZ 01:00–05:00
  (2017, above), 02:00–05:00 (2021, 2022), "2 o'clock in the morning to 5 AM, we understand that is the traditional London session"
  (`M10-BOND-TRADING-SPLIT` [06:20]), London close 10–12 (2017) / 10–11 (2022).
- claim: "London almost always begins with a manipulation phase — a judas-swing that sweeps one side of the asian-range" → ERA-SPLIT /
  EMBELLISHED on the anchor. ICT anchors the London Judas at the midnight open, not at 02:00: "we're looking at 12 a.m. for a classic
  London protraction or Judas swing" (`M08-INTRADAY-PROFILES` [18:42]); "if we do not see an immediate decline from 12 a.m. New York down
  into 2 a.m. New York, this is not going to be a London normal protraction buy day" ([12:04]); delayed case "between 2 o'clock and 3
  a.m., that Judas swing should occur" ([21:25]). 2016: "right after midnight New York time, there's a drop down in price. That's the
  manipulation, making the false move for the low" (`M1-HOW-MARKET-MAKERS` [15:49]). 2022: "that opening price is useful for trading
  the london session that's two o'clock and five o'clock in the morning new york local time and it helps me frame the power 3 for the
  daily range if i'm bearish i'm looking for something to rally above that opening price in london" (ep21 [13:14]).
- claim: "The first 15–30 minutes are typically manipulation" → NOT IN CORPUS (searched `15 minutes|first hour|first 30|thirty minutes|60
  minutes` within 120 chars of `judas|protraction` in both corpora: zero hits).
- claim: "London frequently establishes the day's high or low" → CONFIRMED — "we're looking for the low of the day to form predominantly
  in the London session" (`M08-CENTRAL-BANK-DEALERS` [06:56]); 2016 expansion "into 5 o'clock in the morning New York time"
  (`M1-HOW-MARKET-MAKERS` [16:11]).
- claim: "London open killzone (~02:00–05:00): manipulation + initial expansion" → ERA-SPLIT (01:00–05:00 in the mentorship; page carries
  only the public set and does not reference the 2017 set the killzone table records).
- engine divergence: an engine that opens its London window at 02:00 misses ICT's 00:00–02:00 protraction window in both the 2016 and
  2017 teaching; a "sweep = wick through + close back inside" detector at 02:00+ will fire on the delayed profile only.

## london-close

- claim: "10:00 → 12:00 NY" → CONFIRMED (2017) — "every day at 10 a.m. … begins the London close kill zone every day at 12 p.m. noon New
  York time ends" (`M08-DEFINING-DAILY-RANGE` [04:31]–[04:39]); ERA-SPLIT with 2022: "10 to 11 that's london close" / "i've always taught
  that 10 o'clock until 11 o'clock in the morning is london closed profit taking hour" (ep40 [17:18], [18:14]). Page does not record the
  2022 window.
- claim: "one of the highest-volume windows of the trading day because both London and NY traders are active" → NOT IN CORPUS (searched
  `highest volume|volume` near `london close`; only volume statement is bonds: "the highest volume is going to be seen between 8 a.m. and
  9.30 a.m." `M10-BOND-TRADING-BASICS` [03:16]).
- claim: "European positions are squared … European institutional book unwinds" → NOT IN CORPUS (searched `unwind|square|book` near
  `london close`: no hits). ICT's framing is profit-taking + reversal: "london close is the time of day where we look to really bank our
  positions … london close is not always just simply close existing trades and move to the sidelines many times london close can be
  incorporated as a entry point for longer term one shot one kill" (`M08-ESSENTIALS-DAYTRADING` [14:52]–[15:21]).
- claim: "frequently producing reversals against the London-open direction" → CONFIRMED — "Then we go into London close, which is another
  reversal condition" (`M1-HOW-MARKET-MAKERS` [14:38]); "between 10 a.m. and noon in New York time we expect the high of the daily range
  to form" (`M09-BREAD-BUTTER-BUY` [11:38]); "usually that's when it creates the opposing end of the daily range" (ep40 [17:18]).
- claim: "Overlaps NY AM (08:00 → 12:00)" → CONTRADICTED on the NY AM bound (see killzone table: 07–10 / 08:30–11). The 08:00–12:00 figure
  appears once, for bonds: "New York AM session is defined by 8 AM New York time to noon New York time" (`M10-BOND-TRADING-SPLIT` [01:53]).
- claim: "10:00–11:00 is also the NY AM Silver Bullet" → NOT IN CORPUS (see silver-bullet-rules).
- engine divergence: none listed.

## central-bank-dealers-range

- claim: "2:00 p.m. → 8:00 p.m. NY" → CONFIRMED — "the time period that frames the central bank dealers range is 2 p.m. to 8 p.m. new york
  time" (`M08-CENTRAL-BANK-DEALERS` [04:32]).
- claim: "<40 pips, preferably 20–30" → CONFIRMED — [04:39] verbatim; rationale "if we have a hundred pips one third of that is around 33
  pips so that's why I give about 20 to 30 pips" ([12:42]–[12:48]). Page omits "larger than 30 pips can tend to be unfruitful for
  projections" ([05:53]).
- claim: "Range = high − low within that window" (wicks) → EMBELLISHED by omission. ICT gives two calibrations and prefers bodies: "we can use
  the range in pips by calibration from high to low or using the wicks or alternatively we can use the range in the highest body and the
  lowest body" ([06:03]–[06:11]); "I like to use the bodies predominantly because the wicks are always going to show erroneous price
  because of your dealing spread" ([09:03]–[09:14]); "we still have to look at the ranges with the wicks included" ([10:36]).
- claim: "SD 1, 2, 3 and 4 added/subtracted successively" → CONFIRMED ([01:57]–[02:57]).
- claim: "on buy days the low of the day tends to form between the CBDR and a standard deviation below it" → EMBELLISHED (understated). ICT:
  "most buy days will create the low of the day from the central bank dealers range down to the third standard deviation" ([03:18]–[03:23]);
  "ideal buy days will create the low the day no less than two standard deviations below … many times you'll see it just go one standard
  deviation below" ([03:37]–[03:52]); "four standard deviations above for a high the day is going to be on the heels of a very high impact
  news event" ([03:55]–[04:04]). The page's own citation at 03:09–03:23 drops the word "third".
- claim: "at 8 p.m. starting the Asian range" → CONFIRMED ([11:27]).
- claim: "Year Refined 2017" → CONFIRMED by omission in 2022: "I wouldn't worry about doing anything with like uh central bank dealer's
  range" (ep18 [06:22]).
- engine divergence: the owner's body-only convention for order blocks is echoed here by ICT's stated CBDR preference for bodies; the page's
  wick-only formula is the one ICT calls less reliable.

## judas-swing

- claim: definition "deceptive opening move … opposite direction of the session's true intended delivery" → CONFIRMED — "Judas swing is the
  false move typically in London and in New York session there are fake runs that start off a move" (ep09 [03:21]); "the market's going in
  the opposing direction that it's likely to go to later in the day" (ep16 [06:06]); 2016: "we see that as market protraction or a Judah
  swing. It's a false rally to sell into" (`M1-IMPULSE-PRICE-SWINGS` [06:40]–[06:46]).
- claim: dating 2016 → CONFIRMED (above, Sep-2016 lecture; also `M1-HOW-MARKET-MAKERS` [14:05]).
- claim: four session Judas swings, `MARKET-REVERSALS` 28:07 and `BREAD-BUTTER-BUY` 20:29 → CONFIRMED verbatim ("every session has a
  protractionary market stage" [20:29]); London-close "opposite" ([21:19]–[21:43]) CONFIRMED.
- claim: "Named for the New Testament betrayal" → NOT IN CORPUS (searched `betray|testament|bible` both corpora: zero).
- claim: "clear directional move in the first 15–60 minutes of the killzone" → NOT IN CORPUS / CONTRADICTED on the anchor. ICT measures the
  Judas from an opening price, not from the killzone start: London — midnight open ([18:42], [12:04] above) or "between 2 o'clock and 3
  a.m." for the delayed profile; New York — "if you're bullish in New York you're looking for 820 and the Judas swing dropping down after
  820" (`M09-BREAD-BUTTER-BUY` [20:35]); 2022 indices — "the opening price at 8 30 i use that for again power 3 for the new york session …
  i want to see a move above that's what i dub a judas swing" (ep21 [15:58]); "i'm waiting for that judas swing to happen where it drops
  down at 9 30" (ep24 [05:59]); Asia — "the Judas swing at zero GMT or Asia's open" ([21:11]).
- claim: "reversal usually displaces and leaves a fair value gap that becomes the entry zone" → ERA-SPLIT. 2022: "judas swing that fake rally
  up … then it creates the pattern that's in the mentorship fair value gap market structure shift then starts to show displacement" (ep25
  [32:46]–[33:13]). 2017: the entry is a PD-array retracement, with the Judas depth measured in CBDR deviations: "You're going to be
  looking for an intraday premium PDRA to short on inside that retracement" (`M08-INTRADAY-PROFILES` [09:29]); "reach down one to two
  standard deviations in the central bank dealer's range. And that will be your projected low" ([13:37]).
- engine divergence: Sweep = "wick through a prior high/low with close back inside" is a sweep test; ICT's Judas test is "price above/below
  the session opening price" — the two fire on different bars.

## power-of-three

- claim: "Accumulation → Manipulation → Distribution" → CONFIRMED both eras — "power three stands for accumulation distribution and
  manipulation" (`ICT-2017-USDCAD-MARKET-REVIEW-DEMO-EXAMPLE` [05:21]); "Power Three which is accumulation manipulation and distribution"
  (ep09 [00:05]).
- claim: "Year Introduced 2016" → CONFIRMED — "Daily range is the time and price theory that we use for engineering the daily range, the power
  three. The open, high, low, and close" (`M02-SECRETS-SELECTING-HIGH` [42:50]–[42:56], Oct 2016). Source `ICT-2016-PO3` is a stub; this
  is the real anchor.
- claim: "fractal pattern that repeats at every TF (yearly, monthly, weekly, daily, session, 90-minute)" → PARTLY CONFIRMED / EMBELLISHED.
  ICT defines it on the daily bar: "Power three is the concept I teach as it relates to the daily open high low and close bar"
  (`M03-INSTITUTIONAL-SPONSORSHIP` [35:21]); 2022 extends to sessions: "power 3 which is a fractal element of accumulation manipulation and
  distribution" (ep21 [24:11]), weekly: "Friday being closed for power three for the weekly range" (`M12-SHORT-TERM-TOP` [14:34]). "Yearly",
  "90-minute" NOT IN CORPUS.
- claim: "also called the AMD doctrine" → NOT IN CORPUS (searched `\bAMD\b|AMD doctrine` both corpora: zero; ICT says the three words).
- claim: "MMBM (Market Maker Buy Model) … PO3 cycle ending in upward distribution" → EMBELLISHED (conflation). ICT's market maker buy model is a
  separate price-curve construct: "consolidation here the runaway come back to the consolidation distribution smart money reversal low
  risk buy reaccumulation … what i just described to you is a market maker buy model" (`ICT-2017-OTE` [29:22]–[33:58]); "this market maker
  buy model, the curve is basically a price swing lower that trades higher" (`M04-RECLAIMED-ORDERBLOCK` [03:50]). No sentence equates it
  with PO3.
- claim: "4th phase X (continuation/reversal) … Quarterly Theory" → NOT IN CORPUS (searched `amd ?x|fourth phase|4th phase|accumulation.*
  (continuation|reversal) phase` both corpora: zero). Not ICT material.
- claim: "every named setup (Silver Bullet, Judas Swing, etc.) is an instance of PO3" → EMBELLISHED; ICT's operational PO3 statement is about
  the open: "when you're bullish, you want to be buying near or below the opening price" (`M03-INSTITUTIONAL-SPONSORSHIP` [35:51]); "if
  I'm bullish I'm expecting the opening price to be near the low of the day or the session" (ep09 [02:43]).
- engine divergence: none listed; but note ICT's PO3 is keyed to the midnight (and 08:30) opening price, a value the engine conventions do
  not mention.

## silver-bullet-rules

- claim: the whole page (three windows, 8-item checklist, Year Introduced 2022, Refined 2025) → NOT IN CORPUS. Searched `silver bullet` in
  both corpora: 6 episode hits (ep08, ep10, ep17, ep18, ep20, ep40 — on inspection ep10 [28:38] "not going to give you a silver bullet that
  removes losing trades"; the others are the same idiom) and 4 packet hits (`M09-BREAD-BUTTER-SELL` [19:18] "They're not a silver
  bullet"; `M11-BOND-MEGA-TRADES` [03:35] "interest rate SMT is going to be that little silver bullet"; `M11-STOCK-MEGA-TRADES` [25:15],
  [51:22] index SMT "is the silver bullet"). Window searches `(10|ten) (to|and) (11|eleven)`, `(3|three) (to|and) (4|four) a.m`, `(2|two)
  (to|and) (3|three) p.m` in m22: the only 10–11 statements are London-close profit-taking (ep40 [17:18]) and "I want to try to be
  positioned before 11:00" (ep05 [10:50]). The Silver Bullet is 2022-Q4/2023 YouTube material outside the 41-episode series.
- claim: "SL beyond the swept liquidity pool" and "entry at CE" → see ict-2022-model: the 2022 episodes place the stop above the FVG candle
  / swing high and enter at the FVG edge; if the SB inherits the 2022 model, items 6–7 are unsupported.
- Page verdict UNVERIFIABLE; `ICT-2022-SILVER-BULLET` and `ICT-2025-MACRO-PRECISION` are both stubs.

## weekly-bias

- claim: ICT's weekly routine (relative strength → COT → sentiment → structure/IOF → transpose to daily), with cited quotes → CONFIRMED.
  Verified verbatim in `M12-INTERMEDIATE-TERM-TOP`: [02:52] "not have a clear picture from the monthly"; [04:38] "there's a couple things
  missing here that we saw in the monthly that is not in the weekly portion" (the "three different things" clause is at [04:55]);
  [08:23] "I determine what markets lead in strength by failing to make lower lows and lead in weakness by failing to make higher highs";
  [08:50] "top 30 industry groups"; [09:23] "I look for leadership and laggards so I want to know what the strongest is and the weakest";
  [10:58] "six month extreme in net holdings I also like to sort markets that are at two year and four year extremes"; [12:52] "big
  descriptive adjectives"; [13:04] "I haunt forums"; [13:39]–[13:52] "percent R on a weekly chart in periods of 20, 14, period, and 10 …
  which one is the most accurately depicting or overlaps with the previous important highs and lows"; [19:12] "split that in half and above
  it would be buying and below it would be selling"; [40:01] "Ideal long entry, I have it set at 80 … it's 20"; [41:17] "14 periods in my
  opinion would have been optimal"; [46:44] "It's not required on these timeframes. Monthly and weekly."; [05:33] "diametrically opposed to
  that in an alignment with what smart money is doing"; [06:46] "down close candles supporting price and up close candles being broken";
  [08:02] "I come to a weekly bias … transpose that to the daily chart".
- timestamp slip: "this does look like form fitting" is at [40:28], not 13:34 (13:34 is "like diametrically opposed"). Cosmetic.
- claim: Formal Criteria "Most recent weekly external BOS was up; price below weekly EQ; weekly DOL upside" → NOT IN CORPUS as ICT's words
  (searched `break of structure|\bBOS\b|change of character|choch` both corpora: zero files). Closest 2022 statement: "the only thing
  you're looking for is a likely movement higher or lower based on on the weekly candle okay that's all you're doing that sets your
  initial bias for the week on the daily chart you're looking for swing highs and swing lows to get your liquidity" (ep02 [16:23]); "i'm
  trying to determine the likely weekly expansion" (ep40 [21:09]). Not contradicted; vocabulary is SMC-derived.
- claim: "PWL often gets swept early in the week (Mon/Tue) before … Wed-Thu distribution" → PARTLY CONFIRMED — "There could be a load that
  forms on Monday … take off going through the second portion of Tuesday, all of Wednesday and the first half of Thursday" (`M12-SHORT-
  TERM-TOP` [14:04]–[14:11]); "PWL" as the swept level is the page's addition.
- engine divergence: Engine "bias = direction of the last structure break on D1/W1/H4" is supported by neither corpus; ICT's weekly bias is
  the multi-input routine above (2017) or weekly-candle expansion read (2022). ICT's structural input is institutional order flow (down-
  close candles supporting), not a break-of-structure flag.

## daily-bias

- claim: ICT's daily routine with cited quotes → CONFIRMED verbatim in `M12-SHORT-TERM-TOP`: [01:07]–[01:14] "that is all the work I do I
  don't do anything additional to that"; [05:08]–[05:24] "all monthly and weekly analysis is carried over into the daily time frame …
  preferably the daily should confirm it"; [09:39] "if that range is very narrow or can't discern from looking at 12 months, I'll go down to
  six months"; [11:03]–[11:36] open-interest ±15 % gate and "it either has to meet one of these two criterias, or I'm not going to refer to
  it at all"; [12:06]–[12:15] "support at down-closed daily candles and breaking through up-closed daily candles … The daily order flow is
  the most important one to know"; [12:53] "you're playing with Russian roulette"; [13:58] "the weekly range typically forms between
  Tuesday and Thursday"; [14:19]–[14:27] "Tuesday, creating the high of the week, and Thursdays, New York open, creating the low of the
  week"; [18:19]–[18:42] "I've never been able to create a systematic approach for forecasting weekly profiles … about a 60% likelihood …
  goes into a 70% likelihood"; [19:06]–[21:26] Sunday open and "midnight opening price on Monday … that's the opening price I use for the
  weekly"; [22:03]–[22:08] "SMT divergence at this point from daily going into the four hour because I think that's where the heart of its
  effectiveness exists"; [22:19]–[22:43] breakers "It's the meat in the middle"; [26:02] "just because we're bullish doesn't mean we're
  buying every day"; [09:16] "transpose all these ideas and analysis and levels over to our four-hour chart".
- claim: "Below the midpoint → hunt discount arrays and expect upside expansion (10:22)" → CONTRADICTED by the adjacent line. The lecture states
  both polarities within eight seconds: "I consider the net position bullish if above halfway mark of the 12-month range and bearish if
  we're below the halfway mark" ([10:22]–[10:27]) and then "So if I'm below it, I'm going to be focusing on discounted raise and looking for
  scenarios where the market should expand to the upside" ([10:30]). The weekly lecture resolves it: "above it would be buying and below it
  would be selling" (`M12-INTERMEDIATE-TERM-TOP` [19:12]). The page records only the slip; an engine keyed to it has the COT sign inverted.
- claim: "True Day Open (00:00 NY) above prior day's range = mild bullish lean" → NOT IN CORPUS and against ICT's open-price logic: "if I'm
  bullish, preferably I want to see price go down below those prices and seek some kind of a discount array" ([20:41]–[20:48]); 2022 "if
  we're bullish we're gonna be looking for the opening price at midnight" to buy below (ep38 [17:44]). "true day" has zero hits in m22.
- claim: Formal Criteria "external BOS / CHoCH / daily EQ / DOL" → NOT IN CORPUS as ICT's words (same search as weekly); 2022 analogue: "the
  majority of your analysis should be framed on your daily chart where is it likely to go where is the expansion likely to take price"
  (ep16 [14:42]); equilibrium/discount logic for bias in ep10 [20:41] ("it's probably going to go below equilibrium to do what to offer the
  market a discount").
- claim: "A daily CHoCH on a thin-volume day" → NOT IN CORPUS (volume is not an ICT input).
- engine divergence: as weekly — "last structure break on D1" is not ICT's daily bias in either era; ICT's named structural test is daily
  institutional order flow (down-close candles hold / up-close candles break).

## ict-2022-model

- claim: "HTF bias clear (D/W align)" → CONFIRMED (2022) — "likely movement higher or lower based on on the weekly candle … sets your initial
  bias for the week on the daily chart you're looking for swing highs and swing lows to get your liquidity" (ep02 [16:23]); "Number one,
  the bias is bearish … you're looking at a daily chart, so you start your analysis there" (ep18 [07:49]–[08:18]).
- claim: "Killzone window active (London open / NY AM / London close)" → CONTRADICTED. The model is taught for the New York session: "what's the
  model teach? Trading when? The New York session. Okay? So, we're trading the New York session. In Forex, it's 7:00 in the morning to 10:00
  in the morning" (ep18 [31:28]); indices "8 30 to 11 o'clock window" (ep17 [25:38]) and PM "1 30 to 4" (ep41 [05:53]). Other sessions are
  optional extensions, not the model's windows: "the same model you can use it in Asian session … you can trade it in London clothes …
  the New York open like I'm teaching you and London open" (ep10 [26:23]); ep20 [03:09] "this is not an addition to the model".
- claim: "Liquidity sweep of a known pool" → CONFIRMED — "look for periods where price runs above an old high then it breaks down and then you
  look for this pattern" (ep06 [15:14]); "the run above a single high or multiple highs like a double top okay either one of those fits
  this criteria" (ep06 [15:40]).
- claim: step 4 "Displacement in the bias direction with an FVG inside or after" → CONFIRMED but INCOMPLETE: ICT's trigger is the market
  structure shift (a short-term low/high taken out with displacement) and the FVG must sit inside that displacement leg: "find the nearest
  short term low because that right there is going to be your trigger … you have to see it go below that and displacement with the
  energetic move take out a short term low" (ep24 [33:30]); "on the model I'm teaching you you have to look for what the short-term low
  being broken that's your Market structure shift then you see price go up into that imbalance" (ep12 [37:16]); "where does that reside
  between the displacement high and the displacement low … if there isn't one there you don't have a trade" (ep06 [23:55]–[24:25]). The
  page has no MSS step.
- claim: "Entry on FVG retest at CE (per 2025 default)" → CONTRADICTED for 2022 and out of corpus for 2025 (`consequent` has zero hits in m22).
  2022 entry is a limit at the FVG edge: "put your limit order in to sell short right at that price right there or plus one pip" (ep18
  [32:47]); "we're just going to use the actual candle high that would be your limit order entry" (ep20 [14:19]); "it doesn't have to
  completely close it if it trades up into it anywhere between here and here is good" (ep24 [36:15]).
- claim: "SL beyond the swept extreme" → CONTRADICTED — "where's your stop loss going to be above the high of candle number two or you can use
  above candle number one which creates a swing high okay whichever one you can afford" (ep06 [36:06]); "the rule is you want to use the
  candle that creates the fair value you got that high just above that okay one tick two ticks above that" (ep25 [43:39]); "your risk is
  going to be above this high" (the displacement-leg high, ep18 [32:47]).
- claim: "Targets via SD projections + HTF DOL" → PARTLY CONFIRMED — primary target is liquidity: "partials internal range external range your
  trade" (ep06 [45:41]), "run above fourteen …" (ep14 [00:01]); SD only as a how-far gauge: "the projection is -1 1/2 standard deviation
  and there's your low" (ep12 [32:47]).
- claim: "Pre-killzone or post-killzone setups don't qualify" → EMBELLISHED — "You don't need to have your entry filled inside that kill zone
  window. Your order idea and your order placement need to be considered at that time" (ep18 [48:30]).
- claim: "downstream named models (Silver Bullet, Bread-and-Butter, Unicorn) instantiate" it → NOT IN CORPUS (Bread & Butter is 2017 forex
  material predating it; Silver Bullet / Unicorn absent).
- engine divergence: Engine "FVG = wick-to-wick gap, no displacement filter" matches ICT's FVG geometry ("candle number one's high that is
  the low of the fair value gap candle number three's low is the high" ep06 [22:35]–[23:00]) but the MODEL requires the FVG to be inside an
  "energetic" displacement leg that broke structure — the engine's no-filter rule is a geometry choice, the model's is an admission test.
  Engine "sweep = wick through + close back inside" vs model "run above an old high then it breaks down" + MSS close below a short-term low
  — ICT's test is the later structural close, not the sweep candle's own close. Engine "OTE 0.62–0.79" is not part of the 2022 model (entry
  is the FVG). Engine "stop at the fib origin (leg extreme)" vs 2022 stop above the FVG candle / swing high: ICT's 2022 words support
  neither the page nor the engine's swept-extreme stop.

## smt-divergence

- claim: definition and 2016 dating, quotes at `M03-INSTITUTIONAL-MARKET-STRUCTURE` 02:21 / 05:28 / 08:28 → CONFIRMED verbatim ("stands for
  smart money tool or smart money technique and we're going to be looking for a divergence between closely correlated or inversely
  correlated assets" [02:21]). `M02-SECRETS-SELECTING-HIGH` [39:44]–[39:59] "that's a crack in correlation" CONFIRMED; correlated-pair SMT
  "euro dollar and the British pound dollar" [40:10] CONFIRMED.
- claim: bullish SMT = A new low, B higher low → CONFIRMED (2022) — "we have the lower low in nasdaq higher low in s p that sets the stage for
  that run higher" (ep38 [46:46]); 2016 inverse form "when the dollar index makes a lower low in the foreign currency fails to trade
  higher than a previous high this is us dollar index smt" ([05:19]–[05:28]).
- claim: "Smart Money Technique" alias → CONFIRMED with ICT's own hedge: "smt smart money tool or smart money technique i never really
  settled on what the t was going to be" (ep38 [41:34]).
- claim: pairings NQ vs ES → CONFIRMED (ep22 [43:05], ep35 [07:03]); EURUSD vs DXY inverse → CONFIRMED (2016); "gold vs silver" → NOT IN
  CORPUS (searched `gold.{0,40}silver` both corpora: only relative-strength lists; `M05-HOW-USE-INTERMARKET` [12:19] "it's not meant for
  metals like silver, palladium, platinum, gold" refers to a different tool).
- claim: "HTF SMT (D, W) most reliable" → compatible with 2017 "from daily going into the four hour" (`M12-SHORT-TERM-TOP` [22:04]); 2022 adds
  a time-of-day rule the page lacks: "smt usually will occur around a 9 30 time period when there has already been a nice early run before
  seven o'clock" (ep35 [13:49]) and a caution "if you don't know where it's going you're going to many times encounter what would look like
  smt divergence and then it disappears" (ep35 [07:39]).
- engine divergence: none listed.

## Cross-page issues (contradictions between pages, inconsistent numbers)

1. New York AM window: killzone table says 08:00–11:00; london-close says NY AM = 08:00–12:00; ICT says 07:00–10:00 (forex, 2017 and 2022)
   or 08:30–11:00 (indices, 2022). Three different numbers, none ICT's.
2. London close: killzone table / london-close / london-session all carry 10:00–12:00 only; 2022 ICT = 10:00–11:00 ("profit taking hour").
3. Asian range: asian-range offers an 18:00–03:00 alternative that overlaps the CBDR window (14:00–20:00) which the CBDR page says is
   "consecutive, not overlapping". The CBDR page is right.
4. Judas timing: judas-swing "first 15–60 minutes", london-session "first 15–30 minutes" — different numbers, neither in corpus; ICT anchors
   to opening prices.
5. Stop placement: silver-bullet-rules and ict-2022-model both say "SL beyond the swept pool/extreme"; the 2022 episodes say above the FVG
   candle or the swing high.
6. "Entry at CE (per 2025 default)" appears on ict-2022-model and silver-bullet-rules; 2022 entry is the FVG edge by limit order; no 2025
   source is in corpus.
7. Daily-bias COT rule: page's "below midpoint → bullish" vs weekly-bias page's "above it would be buying" — the two pages carry opposite
   polarities for the same recentred COT line; the weekly page matches ICT's rule statement at `M12-SHORT-TERM-TOP` [10:22].
8. power-of-three lists MMBM/MMSM as PO3 aliases; the 2017 OTE and Month-04 reclaimed-OB lectures define the market maker model as a
   distinct curve.
9. Killzone table labels the 02:00–05:00 / 10:00–12:00 set "2016 + 2022": no 2016 packet contains any killzone clock, and the 2022 London
   close is 10–11.

# ICT library audit brief (shared by all 6 reviewers)

Goal: verify that each assigned concept page in `C:/Users/User/ict-knowledge-library/concepts/` states what ICT
(Michael Huddleston) actually teaches. Our trading engines/studies use these definitions, so a wrong definition is
expensive. Prior audits found two definitions INVERTED (propulsion block, rejection block) on pages that cited
placeholder "stub" Source IDs with no real video — assume more such errors exist. Be adversarial.

## Primary sources (ONLY these count as evidence)
1. `C:/Users/User/ict-knowledge-library/raw/*/report.md` — 153 packets: Sep 2016–Aug 2017 mentorship ("Core Content",
   uploaded 2022 but authored 2016-17; Month 1 = Sep 2016 … Month 12 = Aug 2017), 2017 OTE drills, 2020 OTE
   pattern-recognition series, 3 2021 videos. Whisper transcripts — ASR errors exist (e.g. "not" rendered "now",
   inverting a sentence); read the surrounding clauses before trusting a single line.
2. `C:/Users/User/AppData/Local/Temp/claude/C--Users-User/013404bc-24f8-4bbb-8821-2ef6d66f5d15/scratchpad/m22/ep*.txt` — the 41
   episodes of the public 2022 ICT Mentorship (YouTube auto-captions, `[mm:ss]` paragraph timestamps; ep01 = intro).
   Auto-captions mangle terms ("fair value gap" may appear as "fair valley gap", "FBG", "imbalance"; "order block" as
   "orderblock"; "market structure shift" as "shift in market structure"). Search for variants.
Library `SOURCES.md` text and the page's own claims are NOT evidence. Community/SMC websites are NOT evidence.
Do not use the web.

## Method per page
1. Read the page. Extract its LOAD-BEARING claims: the Definition, every Formal Criteria bullet, the Formula/Math
   (which price — body/open/close/wick/high/low — defines each boundary), any time windows/numbers, and the Year
   Introduced.
2. Grep both corpora (Grep tool or rg, case-insensitive, several phrasings) for ICT's own words on each claim.
   Read the context around hits.
3. Verdict per claim:
   - CONFIRMED — quote (verbatim, short) + packet folder or episode + timestamp.
   - CONTRADICTED — ICT says otherwise; quote it. This is the important finding class.
   - ERA-SPLIT — ICT taught it differently in 2016-17 vs 2022; quote both. Do not collapse.
   - EMBELLISHED — the page adds a specific rule/number/threshold ICT never states (e.g. invented thresholds,
     "must", ratios). Say what was added.
   - NOT IN CORPUS — list the search terms you tried in BOTH corpora (absence must be enumerated, not assumed).
     Note if the concept is plausibly 2023+ material that neither corpus could hold.
4. Page verdict: SOUND / MINOR-FIXES / WRONG (a definitional claim is contradicted) / UNVERIFIABLE.
5. Where the page's definition differs from our ENGINE CONVENTIONS below, say whether ICT's words support the
   engine, the page, or neither. These conventions are owner choices; report divergence, don't "fix" them.

## Engine conventions (owner rulings, Sept 2026) — compare, do not change
- Order block zone = candle BODY only (open..close), wicks excluded.
- FVG = gap between candle 1's wick and candle 3's wick (bull: low[3] > high[1]); every geometric gap counts,
  NO displacement/size filter.
- Dealing range = depth-2 swing (intermediate-term high/low), current-leg rule.
- OTE fib anchored on the impulse that broke structure after a liquidity sweep; anchor at the sweep candle's
  BODY extreme, not its wick; OTE = 0.62–0.79; stop at the fib origin (leg extreme).
- Bias per TF = direction of the last structure break on D1/W1/H4.
- Sweep = wick through a prior high/low with close back inside.

## Hard rules
- READ-ONLY on everything except your one report file. Do NOT edit the repo, do NOT run git, do NOT run any
  trading/MT5/alert/Telegram script, do NOT kill processes, do NOT use the web.
- Write your report to the path given in your prompt. Format:

```
# Cluster <name> — audit
## Summary table
| page | stub/partial/evidenced (from its Source IDs) | verdict | worst finding (one line) |
## <page-stem>
- claim: "<page text, short>" → VERDICT — "<ICT quote>" (<packet|epNN> [mm:ss])
...
- engine divergence: ...
## Cross-page issues (contradictions between pages, inconsistent numbers)
```
- Quotes must be verbatim from the files and locatable by grep. A finding without a locatable quote is not a finding.
- End your final message with the report path and a 5-line summary (count of WRONG/MINOR/SOUND/UNVERIFIABLE + the
  single most consequential error for trading).

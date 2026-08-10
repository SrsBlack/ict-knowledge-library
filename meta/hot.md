---
type: meta
title: "Hot Cache"
updated: 2026-08-09
---

# Recent Context

## Last Updated

2026-08-09. **Video-corpus distillation programme, tranche 3.** The vault now sits on top
of a 153-packet / 59-hour transcript corpus in `raw/`, and concept pages are being written
from the lectures rather than from titles. Tranche 3 added four pages and **refined two
existing ones**. Lint clean.

## Key Recent Facts

- **243 concept pages** across 33 numbered domain folders (+1 directory README in
  `99-glossary/`, which is why earlier entries said "240 files" for 239 pages — the count
  now states both). **81 Source IDs.**
- **Two-layer state is intentional.** `raw/` holds 153 packets / 59 hrs / 148 usable;
  only a minority is distilled into concept pages. The rest is searchable but uncited.
- ⚠ **Core Content lectures are the 2016–2017 mentorship re-uploaded in 2022.** Each names
  its own lesson number in its opening seconds. **Cite as 2016/2017**; the 2022 upload date
  is publication, not authorship. Month → calendar map: Month 1 = Sep 2016 … Month 03 =
  Nov 2016, Month 05 = Jan 2017, Month 06 = Feb 2017, Month 08 = Apr 2017, Month 09 =
  May 2017, Month 10 = Jun 2017, Month 11 = Jul 2017.
- **Method (non-negotiable):** read the transcript before writing; grep for an existing
  sibling first. Near-misses already caught this way — `old high` (541 mentions) was an
  alias for four existing concepts, open float ≠ the IPDA 60-day lookback, and "carrying
  charge" means two different things in commodities vs FX.
- ⚠ A 2026-08-05 correction pass was **partly reversed**: it read 3 of the channel's 43 OTE
  videos and asserted absences from that 7 % sample. Do not repeat confident-absence claims
  without enumerating the source population.

## Recent Changes

- **Tranche 3** — [ict-day-trading-model](../concepts/31-models/ict-day-trading-model.md),
  [timeframe-selection](../concepts/25-htf-bias/timeframe-selection.md),
  [bond-yield-analysis](../concepts/03-order-flow/bond-yield-analysis.md),
  [explosive-market-selection](../concepts/31-models/explosive-market-selection.md).
- **Two refinements forced by the same reading** — `commitment-of-traders` gained the
  **recentred zero line** (12-month midpoint replaces the printed zero), and `open-interest`
  gained the **10–15 % qualifying gate**, which corrected a standing claim on that page that
  no numeric threshold was taught.
- Tranches 1–2 (same day) — COT, open-float, interest-rate-differentials, carrying-charge;
  then mega-trade, filling-the-numbers, reclaimed-order-block, market-efficiency-paradigm.
- New capability: `tools/ingest_video.py` produces a transcript packet in `raw/`. It
  automates AGENTS.md ingest steps 1–2 only; steps 3–9 are judgment and are printed, not
  performed. Run `--self-check` before trusting it.

## Active Threads

- **Backlog:** [distillation-backlog-2026-08-09](distillation-backlog-2026-08-09.md) —
  **8 concepts + 2 merges remain** after tranche 3. Next up: swing-trading-hallmarks,
  equity-seasonal-windows, macro-to-micro-framework, projected-range-objectives,
  market-maker-trap, anticipatory-setup-development, sentiment-effect, market-protraction.
- Merges pending: *Interest Rate Effects On Currency Trades* → `interest-rate-differentials`;
  *Reducing Risk & Maximizing Potential Reward In Swing Setups* → `32-risk-management`.
- Layout deviates from the canonical wiki-skill scaffold (kebab-case files, markdown
  relative links, bold-key headers, no `wiki/` wrapper). Deliberate; see `CLAUDE.md`.
- Decision still open: whether to point the `obsidian-vault` MCP server at this repo.

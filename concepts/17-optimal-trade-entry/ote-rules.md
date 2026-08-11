# OTE Rules

**Category:** 17-optimal-trade-entry
**Aliases:** OTE setup rules, OTE checklist
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2020-OTE-VOL01, ICT-2020-OTE-VOL02, ICT-2020-OTE-VOL03, ICT-2020-OTE-VOL10, ICT-2020-OTE-VOL13, ICT-2020-OTE-VOL14, ICT-2020-OTE-VOL15, ICT-2020-OTE-VOL16, ICT-2020-OTE-VOL18, ICT-2020-OTE-VOL19, ICT-2020-OTE-VOL20, ICT-2020-OTE-EURUSD-EXAMPLE, ICT-2017-OTE-DRILL-AUSUSD, ICT-2017-OTE-DRILL-USDCAD, ICT-2017-OTE-DRILL-USDCHF, ICT-2017-OTE-LONDON-CLOSE, ICT-2017-OTE-LONDON-DEMO, ICT-2017-OTE-USDCAD-REVIEW, ICT-2021-OTE-SCALPING-EXERCISE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, rules, checklist, continuation

## Definition

OTE rules are the operational checklist for taking an OTE entry — the discipline that distinguishes a high-probability OTE from a low-probability fib-level fade. ICT teaches OTE not as "buy at 0.705" but as a **multi-condition checklist**.

> ⚠ **Checklist corrected 2026-08-05.** Items 5–7 previously described a *reversal* entry (lower-TF MSS confirming "the reversal"), a stop beyond 0.79, and standard-deviation targets. The reversal framing belongs to the [ict-2022-model](../31-models/ict-2022-model.md) and that correction stands. Corrections are quoted to primary sources below; items 1–4 are unchanged.
>
> ⚠ **Partly reversed 2026-08-09 — the 08-05 pass over-corrected on two of the three.** It read 3 OTE videos; the official channel carries 43, including a 20-part *OTE Pattern Recognition Series* of which only Vol. 01 had been read. On the fuller corpus, **SD targets and non-leg-origin stops are both ICT-original** and are restored as disclosed era-forks in items 6 and 7. Only the reversal-framing correction survives unchanged. Root cause was sample size, not method — the confident negatives ("none of the three", "no primary-source quote") were unsupportable from 3 of 43.

## Formal Criteria — The OTE Checklist

A valid OTE entry requires ALL of:

1. **HTF bias direction confirmed.** Long OTEs only on bullish bias; shorts only on bearish. *(Majority convention; ICT-original teaches the raw pattern bias-agnostically — "many times you don't even need a bias", `ICT-2020-OTE-VOL01`.)*
2. **Clean measured leg** (leg_start and leg_end are confirmed swing pivots) that **breaks a prior swing level in the trade direction** — short-term, intermediate-term, or the previous day's high/low. Intermediate-term breaks are "much much more reliable" (`ICT-2017-OTE`). ⚠ This is a **with-trend continuation break, not a counter-directional sweep.**
2b. **Fib anchored to candle bodies, not wicks** — the highest/lowest *body* of the terminal and origin swings (`ICT-2017-OTE`, 36:28; restated `ICT-2020-OTE-EURUSD-EXAMPLE`, 01:37). Wick-anchoring changes `leg_size` and therefore items 3, 6 and 7 below. See [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md).
3. **Retracement enters [0.62, 0.79]** — the whole zone is tradable; no pixel precision.
4. **PD array at the entry level** (FVG / OB / breaker / mitigation). *(Shown in worked examples; not stated as a hard mandate in the dedicated material.)*
4b. **Time gate — a hard rule in the 2020 series, a killzone convention in the 2017 drills.** The Pattern Recognition Series makes it pass/fail: "it has to occur between 8:30 and 11 AM. **If it doesn't, we don't do anything.** We just wait for the next trading day or trade another pair or market" (`ICT-2020-OTE-VOL16`, 06:08–06:21). The window is stated as invariant — "always 8.30 to 11 a.m. New York time" (`ICT-2020-OTE-VOL14`, 00:38), "standard times never changing" (`ICT-2020-OTE-VOL13`, 01:45), "it's a static time, it doesn't change" (`ICT-2020-OTE-VOL03`, 03:38). The 2017 demos instead scope OTEs to whichever ICT killzone they occur in — a London-close OTE (`ICT-2017-OTE-LONDON-CLOSE`), a London-open OTE inside "my normalized kill zone which encompasses one o'clock in the morning New York time to 5 a.m. New York time" (`ICT-2017-OTE-LONDON-DEMO`, 02:58), a New York killzone OTE (`ICT-2017-OTE-DRILL-USDCAD`, 01:44). ⚠ The 01:00 London start in the 2017 demo does not match the **02:00–05:00 NY** London window ICT gives for the same purpose in `ICT-2021-OTE-SCALPING-EXERCISE` [11:20]; both are recorded, neither is reconciled here. A time-gated implementation must state which convention it uses — the 08:30–11:00 gate alone rejects every London and London-close OTE in the 2017 corpus.
5. **Entry executed in the impulse direction** — a limit at the chosen depth, or a lower-TF confirmation inside the zone if the trader wants one. ⚠ Any lower-TF trigger here confirms **continuation**, not a reversal; OTE does not wait for structure to break *against* the impulse.
6. **Stop placement — a disclosed intra-primary fork.** **0.79 is the deepest entry, not the stop** in either branch.
   - **Primer branch (2017, definitional):** SL at the leg-origin extreme (fib 1.0), exactly — "my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that" (`ICT-2017-OTE`).
   - **2020 applied branch:** a **fixed pip stop** sized to the setup, not to the leg. `ICT-2020-OTE-VOL01` (41:33) — "the stop would be 6430, so it's a 20 pip stop"; `ICT-2020-OTE-EURUSD-EXAMPLE` (02:50) — "using a 20 pip stop loss, that would put your stop just about in this high here, so you'd be able to withstand all of the expansion **beyond the 79% retracement level**". Recurs throughout the series: 10 pips (`ICT-2020-OTE-VOL02`, `ICT-2020-OTE-VOL10`, `ICT-2020-OTE-VOL15`, `ICT-2020-OTE-VOL19`), 30 pips (`ICT-2020-OTE-VOL20`).

   The Primer governs as the definitional video, but the fixed-pip branch is **ICT-original and explicitly not leg-origin** — the EURUSD quote places the stop past 0.79 by design. State which branch a backtest or implementation uses; they produce materially different R. *(Corrected 2026-08-09: this item previously asserted the tighter stop had "no primary-source quote behind it". That was wrong — two of the three videos the 2026-08-05 pass itself relied on contain fixed-pip stop quotes.)*

   **A third formulation, added 2026-08-11:** an **offset from the leg-origin extreme**, which is neither "exactly at the low" nor a market-fixed pip count. `ICT-2021-OTE-SCALPING-EXERCISE` specifies it for a bearish OTE study: "your stop has to be **five pips above the old high that you pulled your fib from** … wherever 62 percent retracement level is, that's your entry, that's your old high, and you add five pips to that" [14:03–14:27]. The 2017 drills state the plain leg-origin form — "your stop is going to be **at the low**" (`ICT-2017-OTE-DRILL-AUSUSD`, 01:28), "your risk is the high" (`ICT-2017-OTE-DRILL-USDCHF`, 01:17) — matching the Primer branch. Instrument-specific fixed stops recur outside FX too: 20 pips on cable (`ICT-2020-OTE-VOL14`, 05:38), **26 ticks** on crude (`ICT-2020-OTE-VOL16`, 07:58), **six ticks** on the 30-year bond (`ICT-2020-OTE-VOL18`, 02:42).
7. **Targets defined** — first partial at the prior extreme (fib 0.0), then an extension ladder; move the stop to 0.5 of the range after the first target (`ICT-2020-OTE-VOL01`). Optionally aligned with an HTF draw on liquidity. Two ladders are taught, and they are era-split:
   - **Primer ladder (2017):** −0.27 / −0.62 / −1.0 of the same leg (`ICT-2017-OTE`), the last being the symmetrical price swing.
   - **Standard-deviation ladder (2020 series):** half / full / one-and-a-half / two standard deviations of the fib range. `ICT-2020-OTE-VOL10` (01:39–02:00) walks the preset's own levels — "you can add a negative 1.5 level… so that way you have your half standard deviation, full standard deviation, one and a half standard deviation and two standard deviations". Used throughout `ICT-2020-OTE-VOL04`–`VOL09`, `VOL12`, `VOL15`. See [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md).

   *(Corrected 2026-08-09: the 2026-08-05 pass removed SD targets on the grounds that "none … is what the dedicated OTE material teaches". The OTE Pattern Recognition Series is dedicated OTE material and teaches them across at least nine volumes; the earlier pass had read only Vol. 01 of 20.)*

8. **Missed and late entries — two disclosed allowances (added 2026-08-11).**
   - **Retest re-entry.** "If you were to miss this setup, say you missed this ideal entry right in here — you could have gotten in on this **retest** of it right here … and the same parameters would have been used for scaling out" (`ICT-2017-OTE-DRILL-USDCHF`, 01:32–01:48). It is bounded: "if you missed your entry it might give you another opportunity, but if it doesn't, no problem, because you're going to take the next setup. **Don't try to force yourself into taking every single trade or chasing price**" [01:57–02:03]. `ICT-2020-OTE-VOL03` shows the same thing structurally — "the market comes back down and does give **multiple entries**", three candles all inside the zone and inside the time window [04:35–04:55].
   - **A price ceiling on a late fill.** When ICT missed a fill because the ideal entry printed before the killzone opened, he entered on the next candle and gave the filter as a price, not a time: "I asked you guys on Twitter today what would be the absolute latest time you can use for an entry — **it's where your first scalping profit-taking level is. It's got to be at or below that. Otherwise you can't take the trade**" (`ICT-2017-OTE-USDCAD-REVIEW`, 13:47–14:01). ⚠ The transcript says "latest time" but the answer given is a price level; quoted verbatim rather than repaired. The same passage supplies the swing-high reference for that check, and it is explicitly **the wick, not the body** — see item 2b's exception note and [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md).

Missing any of (1)–(6) significantly reduces conviction. (7) is for trade management; missing it doesn't invalidate the entry but does compromise execution. (8) governs what to do after the ideal fill is gone.

⚠ **Disclosed conflict on R:R:** the Primer requires "better than two to one"; Vol.01 rejects an R:R requirement outright ("if it's one to one it's still good") and imposes a ≥15-pip first-scale floor instead. The Primer governs as the definitional video.

## Formula / Math

```
ote_entry_valid := htf_bias_agree
                    AND clean_measured_leg
                    AND fib_anchored_to_candle_bodies
                    AND leg_breaks_prior_swing_in_trade_direction
                    AND retracement_in [0.62, 0.79]
                    AND pd_array_at_entry_level
                    AND entry_direction == impulse_direction
                    AND (sl_at_leg_origin_extreme
                         OR sl_fixed_pip
                         OR sl_at_leg_origin_extreme +/- 5 pips)     # three-way fork, item 6

# 2020-series time gate (item 4b) — hard pass/fail in that branch:
in_window := 08:30 <= t <= 11:00 NY
# 2017-drill convention instead scopes to the killzone the OTE forms in.

# late-fill filter (item 8), long side:
late_entry_ok := entry_price <= first_scaling_target
```

## Machine-Readable

```json
{
  "id": "ote-rules",
  "category": "17-optimal-trade-entry",
  "aliases": ["OTE-checklist", "OTE-rules"],
  "criteria": [
    {"id": "c1", "expr": "all six core checks pass"},
    {"id": "c2", "expr": "checks: htf_bias, clean_leg_with_structure_break, fib_anchored_to_bodies, retracement_zone, pd_array, entry_in_impulse_direction, stop_placed (leg_origin OR fixed_pip)"},
    {"id": "c3", "expr": "counter_directional_sweep_required == false"},
    {"id": "c4", "expr": "stop_rule in [leg_origin_extreme, fixed_pip, leg_origin_plus_5_pips]", "strength": "era-fork"},
    {"id": "c5", "expr": "target_ladder in [primer(-0.27,-0.62,-1.0), sd(-0.5,-1.0,-1.5,-2.0)]", "strength": "era-fork"},
    {"id": "c6", "expr": "08:30 <= t <= 11:00 NY", "strength": "hard in 2020 series; killzone-scoped in 2017 drills"},
    {"id": "c7", "expr": "late_entry_price <= first_scaling_target"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fib-anchoring","ote-overview","ote-62","ote-705","ote-79","ote-failure","ict-2022-model","htf-bias-framework","pd-array-definition"],
  "sources": ["ICT-2017-OTE","ICT-2020-OTE-VOL01","ICT-2020-OTE-VOL02","ICT-2020-OTE-VOL03","ICT-2020-OTE-VOL10","ICT-2020-OTE-VOL13","ICT-2020-OTE-VOL14","ICT-2020-OTE-VOL15","ICT-2020-OTE-VOL16","ICT-2020-OTE-VOL18","ICT-2020-OTE-VOL19","ICT-2020-OTE-VOL20","ICT-2020-OTE-EURUSD-EXAMPLE","ICT-2017-OTE-DRILL-AUSUSD","ICT-2017-OTE-DRILL-USDCAD","ICT-2017-OTE-DRILL-USDCHF","ICT-2017-OTE-LONDON-CLOSE","ICT-2017-OTE-LONDON-DEMO","ICT-2017-OTE-USDCAD-REVIEW","ICT-2021-OTE-SCALPING-EXERCISE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   OTE entry checklist (bullish example):

   ☐ HTF bias bullish?                           [check D / W]
   ☐ Clean leg (start = LTL, end = recent LTH)?  [structural confirmation]
   ☐ Leg TOOK OUT a prior high on the way up?    [with-trend structure break]
   ☐ Fib anchored on BODIES, not wicks?          [anchoring — sets every level below]
   ☐ Retracement entered [0.62, 0.79]?           [fib measurement]
   ☐ Inside the time window?                     [08:30-11:00 NY in the 2020 series;
                                                  killzone-scoped in the 2017 drills]
   ☐ FVG / OB / breaker at entry level?          [PD-array check]
   ☐ Entering LONG, with the impulse?            [NOT fading a sweep — that's the 2022 model]
   ☐ SL at the leg-origin low, exactly?          [risk control, fib 1.0]
   ☐ Targets 0.0 / -0.27 / -0.62 / -1.0, HTF DOL? [trade management]

   All checked → take the entry.
   Missing any of 1-6 → skip or reduce conviction.
```

## Timeframes

All TFs.

## Examples

**Example 1 — full checklist pass:**
- Daily bias bullish ✓.
- H1 leg 1.0800 → 1.0900, clean, and it **took out the prior short-term high** at 1.0885 on the way up ✓.
- Retracement reaches 1.0830 (0.705) ✓.
- M15 bullish FVG at 1.0828–1.0832 ✓.
- Entry long, with the impulse ✓ (no counter-sweep is being faded).
- **SL at 1.0800 — the leg-origin low, exactly** ✓. Risk = 30 pips.
- Targets: 1.0900 first partial (70 pips ≈ 2.3R), then 1.0927 / 1.0962 / 1.1000 ✓.
- → take the entry.

**Example 2 — checklist fails on PD array:**
- All conditions met EXCEPT no FVG/OB at the OTE level.
- → skip; entry has no algorithmic anchor. Wait for fresh structure.

## Common Mistakes

- **Skipping the leg-quality check.** Choppy "legs" produce unreliable retracement levels.
- **Skipping the entry trigger.** Pre-positioning at the fib level without a lower-TF confirmation candle invites SL hits on overshoots.
- **Force-fitting OTEs onto every chart.** Not every retracement is OTE-grade; some moves don't pull back into 0.62–0.79 at all (price runs without retest).
- ⚠ **Running the checklist on a counter-sweep setup.** If the trigger was a raid on the opposite side that you are now fading, you are trading the [ict-2022-model](../31-models/ict-2022-model.md), not OTE. Its criteria — and its FVG-at-CE entry — govern that trade.
- ⚠ **Stopping out at 0.79.** The taught invalidation is the leg origin. A 0.79 stop turns a ~2:1 setup into a much tighter one with a different failure profile; whatever its merits, it is not the rule ICT states.

## Related Concepts

- [ote-overview](ote-overview.md), [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-failure](ote-failure.md).
- [ict-2022-model](../31-models/ict-2022-model.md) — the sweep-reversal composite that OTE is most often confused with.
- [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md) — item 2b; bodies, not wicks.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [pd-array-definition](../05-pd-arrays/pd-array-definition.md).

## Citations

- `ICT-2017-OTE`, `ICT-2020-OTE-VOL01`, `ICT-2020-OTE-EURUSD-EXAMPLE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- Item 2b added 2026-08-09 from a frames+transcript pass over the three dedicated OTE sources; `ICT-2017-OTE` (36:28) states the body-anchoring rule and its broker-variance rationale.
- Fixed-pip stop branch (item 6): `ICT-2020-OTE-VOL02`, `ICT-2020-OTE-VOL10`, `ICT-2020-OTE-VOL15`, `ICT-2020-OTE-VOL19` (10 pips); `ICT-2020-OTE-VOL20` (30 pips).

Added 2026-08-11 from the 21 remaining non-Core OTE packets:

- `ICT-2020-OTE-VOL16` (06:08–06:21) — "it has to occur between 8:30 and 11 AM. If it doesn't, we don't do anything"; (07:58) 26-tick crude stop.
- `ICT-2020-OTE-VOL14` (00:38) "always 8.30 to 11 a.m. New York time"; (05:38) 20-pip stop, 7 pips drawdown.
- `ICT-2020-OTE-VOL13` (01:45) "standard times never changing, 8:30 a.m. New York time to 11 a.m."
- `ICT-2020-OTE-VOL03` (03:38) "it's a static time, it doesn't change"; (04:35–04:55) the zone "does give multiple entries".
- `ICT-2020-OTE-VOL18` (02:42) six-tick stop on the September 30-year bond contract.
- `ICT-2021-OTE-SCALPING-EXERCISE` (14:03–14:27) — "your stop has to be five pips above the old high that you pulled your fib from"; (11:20–11:31) London 02:00–05:00 NY and New York 08:30–11:00 NY as the two study windows; (14:58–15:11) the position must be closed before the session ends — 05:00 NY for London, 11:00 NY for New York.
- `ICT-2017-OTE-DRILL-AUSUSD` (01:25–01:33) — price "does wick through a little bit here but your stop is going to be at the low."
- `ICT-2017-OTE-DRILL-USDCHF` (01:17) "your risk is the high, and your first scaling is the old low"; (01:32–02:03) the retest re-entry and its bound.
- `ICT-2017-OTE-DRILL-USDCAD` (01:44) "during the New York kill zone."
- `ICT-2017-OTE-LONDON-DEMO` (02:58–03:05) — "my normalized kill zone, which encompasses one o'clock in the morning New York time to 5 a.m. New York time; that's my London kill zone, and it's all referenced to New York time."
- `ICT-2017-OTE-LONDON-CLOSE` (00:00–00:16) an OTE taken in the London-close killzone, outside the 08:30–11:00 gate.
- `ICT-2017-OTE-USDCAD-REVIEW` (13:47–14:01) the late-fill price ceiling.

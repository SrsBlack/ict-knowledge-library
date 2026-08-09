# Optimal Trade Entry — Overview

**Category:** 17-optimal-trade-entry
**Aliases:** OTE, optimal entry, OTE zone
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2020-OTE-VOL01, ICT-2020-OTE-VOL10, ICT-2020-OTE-EURUSD-EXAMPLE, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** ote, fibonacci, entry, foundational, continuation

## Definition

Optimal Trade Entry (OTE) is ICT's **canonical entry methodology** for taking a position on a measured pullback **in the direction of the preceding impulse**. An impulse leg **breaks a prior swing level in the trade direction**; price then **retraces into the 0.62–0.79 zone** of that leg, where the trader enters in the impulse's direction. The OTE zone is the 0.62–0.79 retracement of a clean swing leg, with **0.705 as the optimal mid-point**. OTE is one of the original ICT setups and remains a foundational entry tool taught in every mentorship cycle since.

> ⚠ **OTE is a CONTINUATION setup, not a reversal setup.** A counter-directional liquidity sweep is **not** a precondition. Across the dedicated OTE teachings — the 2017 Primer (`ICT-2017-OTE`, the definitional video, which ICT himself defers to from the 2022 mentorship), Pattern Recognition Vol.01 (`ICT-2020-OTE-VOL01`) and the worked EURUSD example (`ICT-2020-OTE-EURUSD-EXAMPLE`) — the words *sweep / raid / stop-hunt / inducement* **never appear as entry conditions**. Where "sweep" appears in an applied OTE example it is **after entry, on the way to the target**. The popular "counter-sweep → displacement → MSS → OTE-style entry" sequence is a **different, later, composite model** — the ICT 2022 Model, filed at [ict-2022-model](../31-models/ict-2022-model.md), whose canonical entry is an FVG at CE. Do not use this page's criteria to describe that model, or vice versa. *(Correction applied 2026-08-05 after a primary-source verification pass against official-channel caption tracks; the two setups have opposite geometry and conflating them is a documented, expensive failure mode.)*

## Formal Criteria

A canonical OTE setup requires:

- A clean **measured swing leg** — `leg_start` and `leg_end` are confirmed swing pivots (the three-bar fractal: "a high that has two lower highs on either side of it… makes that high in the middle a significant high", `ICT-2017-OTE`).
- The fib is anchored to **candle bodies, not wicks** — "we're going to put on the bodies of candles up here, this is the highest body right there… we're going to look at that as the open, so the open is 1.1799, so that's where our fib will be dropped" (`ICT-2017-OTE`, 36:28). Wick-anchoring shifts `leg_size` and therefore every level below, including the stop. See [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md).
- A **market-structure break in the trade direction** by the impulse leg — it takes out a short-term, intermediate-term, or previous-day high/low. Intermediate-term breaks are taught as "much much more reliable" (`ICT-2017-OTE`); PDH/PDL takes are the Vol.01 session pattern (`ICT-2020-OTE-VOL01`). *(No displacement-magnitude gate is taught; none should be inferred.)*
- A **retracement** of price back into the 0.62–0.79 zone of that leg. The whole zone is tradable — "at or very close to the 62%… I'm not going to demand 79%" (`ICT-2017-OTE`). No pixel precision.
- **Stop placement is a disclosed era-fork.** The 2017 Primer puts it at the leg-origin extreme (fib 1.0) — "my stop will be exactly at this low, not 10 pips [or] 5 to 10 pips below that" (`ICT-2017-OTE`). The 2020 applied material uses a **fixed pip stop** instead (`ICT-2020-OTE-VOL01` "a 20 pip stop"; `ICT-2020-OTE-EURUSD-EXAMPLE` places a 20-pip stop that deliberately sits *beyond* 0.79). **In both branches 0.79 is the deepest ENTRY, not the stop.** See [ote-rules](ote-rules.md) item 6.
- A **PD array** in the OTE zone (FVG, OB, breaker, mitigation) — the entry trigger. *(Confidence note: ICT shows order blocks in worked examples but does not state PD-array presence as a hard requirement in the dedicated OTE material. Treat as strong convention, not a quoted mandate.)*
- **HTF bias agreement** — long OTE entries on bullish bias, short on bearish. *(Confidence note: the community teaches this as mandatory and it is the majority convention, but ICT-original teaches the raw pattern bias-agnostically — "many times you don't even need a bias", `ICT-2020-OTE-VOL01`.)*

## Formula / Math

```
# leg_start / leg_end are BODY extremes — max(open,close) / min(open,close)
# of the terminal and origin swings. Not wick extremes. See fib-anchoring.
leg_size = leg_end - leg_start

OTE_upper = leg_end - 0.62 * leg_size      # shallowest OTE
OTE_optimal = leg_end - 0.705 * leg_size   # optimal mid-point
OTE_deep = leg_end - 0.79 * leg_size       # deepest OTE ENTRY (not the stop)

stop = leg_start          # Primer branch: leg-origin extreme, fib 1.0
# stop = entry -/+ fixed_pips   # 2020 branch: fixed pip stop (see ote-rules item 6)

# target ladder A — Primer, same leg (ICT-2017-OTE):
T0 = leg_end                                # fib 0.0 — prior extreme, first partial
T1 = leg_end + 0.27 * leg_size              # fib -0.27
T2 = leg_end + 0.62 * leg_size              # fib -0.62
T3 = leg_end + 1.00 * leg_size              # fib -1.0, symmetrical price swing

# target ladder B — standard deviations of the fib range (2020 series,
# ICT-2020-OTE-VOL10 enumerates the preset). Era-fork, not a replacement:
S1 = leg_end + 0.50 * leg_size              # half standard deviation
S2 = leg_end + 1.00 * leg_size              # full SD  (== T3)
S3 = leg_end + 1.50 * leg_size              # one and a half
S4 = leg_end + 2.00 * leg_size              # two

# Bullish leg 1.0800 → 1.0900:
OTE_zone = [1.0821, 1.0838]    # [0.79, 0.62]
OTE_optimal = 1.08295
stop       = 1.0800
T0..T3     = 1.0900 / 1.0927 / 1.0962 / 1.1000
```

## Machine-Readable

```json
{
  "id": "ote-overview",
  "category": "17-optimal-trade-entry",
  "aliases": ["OTE", "optimal-entry"],
  "criteria": [
    {"id": "c1", "expr": "impulse_leg_breaks_prior_swing_level_in_trade_direction == true"},
    {"id": "c1b", "expr": "fib_anchors == candle_body_extremes (not wicks)"},
    {"id": "c2", "expr": "retracement_in [0.62, 0.79] of measured leg"},
    {"id": "c3", "expr": "entry_direction == impulse_direction"},
    {"id": "c4", "expr": "stop in [leg_origin_extreme (fib 1.0), fixed_pip]", "strength": "era-fork"},
    {"id": "c5", "expr": "PD_array_present_in_zone == true", "strength": "convention"},
    {"id": "c6", "expr": "HTF_bias_agrees_with_entry_direction == true", "strength": "convention"},
    {"id": "c7", "expr": "counter_directional_sweep_required == false"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["fib-anchoring","ote-62","ote-705","ote-79","ote-rules","ote-failure","ict-2022-model","ict-fib-overview","fib-62","fib-705","fib-79","fib-vs-ote","standard-deviation-projections","pd-array-definition"],
  "sources": ["ICT-2017-OTE","ICT-2020-OTE-VOL01","ICT-2020-OTE-VOL10","ICT-2020-OTE-EURUSD-EXAMPLE","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OTE setup:

   leg_end ──────── 0.0  (recent swing high)
   ───────────────  0.50 (EQ)
   ─── 0.62 ────── ┐
                   │ OTE zone
   ─── 0.705 ────  │ ← optimal entry (with PD-array)
                   │
   ─── 0.79 ────── ┘ ← deepest ENTRY (not the stop)
   leg_start ──── 1.0  (recent swing low)  ← STOP sits here
                        ↑ the leg that got here broke a prior
                          swing high in the trade direction

   Long entry at 0.705 with FVG/OB at the level.
   SL: leg-origin low (Primer) OR a fixed pip stop (2020 series) — era-fork.
   Targets: 0.0 first partial, then -0.27/-0.62/-1.0 (Primer)
            or -0.5/-1.0/-1.5/-2.0 standard deviations (2020 series).
```

## Timeframes

Most actionable on M5–H4 entry TFs. Daily OTE setups exist but the swing leg sizes are larger and the SL distances scale up.

## Examples

**Example 1 — bullish H1 OTE entry:**
- HTF bias bullish.
- H1 leg: 1.0800 (LTL) → 1.0900 (recent LTH). 100-pip leg. **The leg took out the prior short-term high on its way up** — this is what makes it an OTE leg rather than any retracement.
- OTE zone = [1.0821, 1.0838], optimal at 1.08295.
- Price retraces; M15 prints bullish FVG at 1.0828–1.0832 (within OTE).
- Long entry at 1.0830 (≈ optimal), **SL at 1.0800 — the leg-origin low, exactly.** Risk = 30 pips.
- Targets: 1.0900 (fib 0.0, prior extreme — first partial, 70 pips), then 1.0927 / 1.0962 / 1.1000.
- R:R to the first target ≈ **2.3:1**, satisfying the Primer's "better than two to one".

> ⚠ **Disclosed intra-primary conflict on R:R.** The 2017 Primer requires "better than two to one" (`ICT-2017-OTE`). Vol.01 explicitly rejects an R:R requirement — "forget risk to reward, we're not teaching that… if it's one to one it's still good" — and imposes a ≥15-pip first-scale floor instead (`ICT-2020-OTE-VOL01`). The Primer is the definitional video and governs here; Vol.01's rule is the tracked alternative.

> **Time window (era-dependent, disclosed):** the definitional Primer is **time-silent** — it teaches no session window. Vol.01 teaches the **08:30–11:00 NY** window as constitutive ("time AND price"). Both are ICT-original; they belong to different teaching eras. Do not present either as *the* OTE time rule.

## Common Mistakes

- **OTE without PD array.** Pure fib-level entries with no FVG / OB at the level lack the algorithmic anchor; conviction is too low.
- **OTE against HTF bias.** Counter-trend OTE setups need explicit HTF reversal context (CHoCH/MSS). Without it, the trade fights the algorithm.
- ⚠ **Treating OTE as a reversal entry.** Waiting for a counter-directional sweep, then fading it into the "OTE zone", is the [ict-2022-model](../31-models/ict-2022-model.md) — a different setup with the opposite geometry and its own criteria. It is not OTE, no matter how the fib is drawn.
- ⚠ **Putting the stop below 0.79.** 0.79 is the deepest acceptable *entry*. The taught stop is at the leg-origin extreme; a 0.79-based stop is a much tighter, structurally different trade that ICT explicitly declines in the Primer.
- ⚠ **Anchoring the fib to wicks.** Charting tools snap to high/low by default; ICT anchors to candle bodies and says why (wicks are the broker-variable part of a candle). This moves the OTE band, the stop at fib 1.0, and every target. See [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md).
- **Demanding exact 0.705.** Use a buffer ±0.5–1 pip on FX. Pixel-precision misses fills.
- **Ignoring leg quality.** A choppy, overlapping "leg" produces unreliable retracement levels. Use clean swing legs only.

## Related Concepts

- [ote-62](ote-62.md), [ote-705](ote-705.md), [ote-79](ote-79.md), [ote-rules](ote-rules.md), [ote-failure](ote-failure.md) — per-level and rules deep-dives.
- [fib-anchoring](../28-fibonacci-levels/fib-anchoring.md) — where the fib attaches: bodies, not wicks.
- [ict-fib-overview](../28-fibonacci-levels/ict-fib-overview.md), [fib-62](../28-fibonacci-levels/fib-62.md), [fib-705](../28-fibonacci-levels/fib-705.md), [fib-79](../28-fibonacci-levels/fib-79.md), [fib-vs-ote](../28-fibonacci-levels/fib-vs-ote.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md).
- [pd-array-definition](../05-pd-arrays/pd-array-definition.md).

## Citations

- `ICT-2017-OTE` (the definitional "OTE Primer", official channel, 2017-09-30), `ICT-2020-OTE-VOL01`, `ICT-2020-OTE-EURUSD-EXAMPLE`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- Corrections of 2026-08-05 (continuation framing, structure-break criterion, stop at leg origin, target ladder, R:R and time-window forks) rest on a primary-source verification pass over official-channel caption tracks of the four videos above.

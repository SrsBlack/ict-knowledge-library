# Fib vs OTE — Disambiguation

**Category:** 28-fibonacci-levels
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE, ICT-2017-OTE-DRILL-GOLD, ICT-2017-OTE-LONDON-OPEN, ICT-2017-OTE-USDCAD-REVIEW, ICT-2020-OTE-VOL03, ICT-2020-OTE-VOL14, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** fibonacci, ote, disambiguation, terminology

## Definition

This page resolves a frequent confusion: **fib levels** vs **OTE**.

**Short version:**
- **ICT fib levels** = the full retracement + projection set (0.50, 0.62, 0.705, 0.79 retracement; -1.5, -2.0, -2.5, -4.0 projection).
- **OTE (Optimal Trade Entry)** = the *zone* defined by the retracement subset 0.62–0.79 (centered on 0.705).

OTE is a specific use of fib levels for entry. Fib also covers projections (targets) that OTE does not directly address.

## The fib is not the cause — five independent statements

⚠ **Added 2026-08-11.** Across the OTE corpus ICT repeatedly and unprompted denies that the fib levels *make* price turn. The tool frames a measurement; the liquidity target is the reason. Five separate videos say so:

- "The **magic is not the fib**, it's the target of liquidity — that's all I'm doing. The fib just helps me frame an underlying context; it's not that you need these levels, it just gives you a framework." (`ICT-2020-OTE-VOL03`, 01:25–01:46)
- "The **fib is not the magic**. It's not, trust me. It has nothing to do with why price is going up there. The fib is just allowing me to **frame a market that is really overbought without having to use any overbought or oversold indicator** … that's all the fib's helping me illustrate." (`ICT-2020-OTE-VOL14`, 04:44–05:16)
- "The **fib doesn't do anything**, just highlight specific things." (`ICT-2017-OTE-DRILL-GOLD`, 00:40)
- "I use **Fibs for targeting**, and the entry for optimal trade entry is just for you to see what I'm seeing in the general area … **62 to 79 percent retracement level is not the magic I'm looking at**" (`ICT-2017-OTE-USDCAD-REVIEW`, 18:24–18:40); earlier in the same video, "Fibonacci is just a measuring tool I use, and I use it for like targeting. **I don't use it so much for entry** … but I do rely on Fibonacci for profit taking" [15:05–15:22]. He is explicit that the public teaching is a proxy: "the mentorship knows what I'm looking for, but for now, for public perspective, this is enough" [18:40].
- "As price trades down into optimal trade entry, **I don't want you to look for the Fibonacci** … I don't want you to look for that to be a crutch in the beginning. It's okay to use it, but I want you to be watching price without it, and **train your eye to be able to see it**." (`ICT-2017-OTE-LONDON-OPEN`, 00:44–00:58)

Two consequences for this library. First, **the OTE zone is claimed to be recognisable without the tool** — the fib is a measuring convention over a pattern that exists independently. Second, ICT states a *split* use in `ICT-2017-OTE-USDCAD-REVIEW`: fib primarily for **targets**, with the retracement band as a teaching device for entry. This is the same split that shows up in anchoring, where target projections may use wicks while retracements use bodies ([fib-anchoring](fib-anchoring.md)). Read together, the two halves of the fib are less unified in ICT's own practice than the level list suggests.

## Formal Criteria

### Fib (umbrella, ICT-specific set)

- Retracement levels: 0.50, 0.62, 0.705, 0.79.
- Projection levels: -1.5, -2.0, -2.5, -4.0.
- Used for both entries and targets.

### OTE (specific entry zone)

- Defined as the retracement zone 0.62 – 0.79.
- 0.705 is the optimal mid-point.
- 0.79 is the deepest acceptable **entry** — ⚠ not the stop. The taught OTE stop is the leg-origin extreme (fib 1.0); see [ote-79](../17-optimal-trade-entry/ote-79.md). *(Corrected 2026-08-05.)*
- OTE is **only the entry side** — not the projection side.

### The Containment Relationship

```
OTE retracement zone ⊂ ICT fib retracement levels ⊂ ICT fib (umbrella)
```

The OTE zone uses three of the four ICT retracement levels (0.62, 0.705, 0.79). 0.50 (EQ) is fib but is shallower than OTE and not part of the OTE zone.

## Formula / Math

```
ict_fib_retracements = {0.50, 0.62, 0.705, 0.79}
ict_fib_projections  = {-1.5, -2.0, -2.5, -4.0}

OTE_zone             = [0.62, 0.79]
OTE_optimal          = 0.705

# 0.50 (EQ) is fib but NOT OTE.
# Projections are fib but NOT OTE.
```

## Machine-Readable

```json
{
  "id": "fib-vs-ote",
  "category": "28-fibonacci-levels",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "OTE_zone subset_of fib_retracements"},
    {"id": "c2", "expr": "fib_projections not_in OTE"},
    {"id": "c3", "expr": "EQ (0.50) in fib but not in OTE"},
    {"id": "c4", "expr": "fib_levels_are_causal == false", "note": "5 independent denials; the liquidity target is the stated cause"},
    {"id": "c5", "expr": "OTE recognisable without the fib tool"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ict-fib-overview","fib-62","fib-705","fib-79","ote-overview","ote-62","ote-705","ote-79","equilibrium-definition","standard-deviation-projections"],
  "sources": ["ICT-2017-OTE","ICT-2017-OTE-DRILL-GOLD","ICT-2017-OTE-LONDON-OPEN","ICT-2017-OTE-USDCAD-REVIEW","ICT-2020-OTE-VOL03","ICT-2020-OTE-VOL14","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   ICT fib (full set):

   leg_end ────── 0.0
                                ─── -1.5 SD  ┐
                                ─── -2.0 SD  │ projections
                                ─── -2.5 SD  │ (NOT OTE)
                                ─── -4.0 SD  ┘
   ─── 0.50 (EQ) ───── (fib, NOT OTE)
   ─── 0.62 ──────── ┐
   ─── 0.705 ──────  │ OTE zone (subset)
   ─── 0.79 ──────── ┘
   leg_start ──── 1.0
```

## Timeframes

All TFs.

## Examples

**Example A — fib level used, but not OTE:**
- Price retraces to 0.50 (EQ) and finds support.
- This is a fib-level reaction, but it is NOT an OTE entry (too shallow).

**Example B — OTE entry:**
- Price retraces to 0.705 with bullish OB at the level.
- This is BOTH a fib retracement entry AND an OTE entry.

**Example C — fib used as target, not OTE:**
- Trade enters at OTE 0.705, targets -1.5 SD projection.
- The -1.5 SD is a fib projection (entry uses OTE; target uses fib projection — both are fib but only the entry is OTE).

## Common Mistakes

- **Using "fib" and "OTE" interchangeably.** OTE is the specific 0.62-0.79 entry zone; fib is broader.
- **Calling 0.50 entries "OTE."** 0.50 is EQ, not OTE. They're both fib levels but EQ is shallower.
- ⚠ **Treating the fib level as the reason price reversed.** ICT denies this in five separate OTE videos (see above). A model that scores "price touched 0.705" as its signal has captured the measurement, not the mechanism; the draw on liquidity is what he names as the cause.
- **Confusing OTE with classical fib zones.** OTE uses 0.62 / 0.705 / 0.79. Classical Elliott/Wyckoff zones often emphasize 0.382 / 0.500 / 0.618 — different framework.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md), [fib-62](fib-62.md), [fib-705](fib-705.md), [fib-79](fib-79.md).
- [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-62](../17-optimal-trade-entry/ote-62.md), [ote-705](../17-optimal-trade-entry/ote-705.md), [ote-79](../17-optimal-trade-entry/ote-79.md).
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md), [standard-deviation-projections](standard-deviation-projections.md).

## Citations

- `ICT-2017-OTE`, `ICT-2022-MENTORSHIP-OVERVIEW`.

Added 2026-08-11 — the five "the fib is not the magic" statements:

- `ICT-2020-OTE-VOL03` (01:25–01:46) — "the magic is not the fib, it's the target of liquidity."
- `ICT-2020-OTE-VOL14` (04:44–05:16) — "the fib is not the magic … it has nothing to do with why price is going up there"; the fib as a substitute for an overbought/oversold indicator.
- `ICT-2017-OTE-DRILL-GOLD` (00:40) — "the fib doesn't do anything, just highlight specific things."
- `ICT-2017-OTE-USDCAD-REVIEW` (15:05–15:22) — "Fibonacci is just a measuring tool … I don't use it so much for entry … I do rely on Fibonacci for profit taking"; (18:24–18:40) "62 to 79 percent retracement level is not the magic I'm looking at."
- `ICT-2017-OTE-LONDON-OPEN` (00:44–00:58) — "I don't want you to look for the Fibonacci … train your eye to be able to see it."

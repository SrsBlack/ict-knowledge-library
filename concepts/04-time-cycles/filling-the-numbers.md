# Filling The Numbers

**Category:** 04-time-cycles
**Aliases:** filling the numbers, four numbers per day, daily level fills, zero-GMT pivots
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-FILLING-NUMBERS
**Tags:** time-cycles, daily-range, pivot-points, day-trading, ipda, levels

## Definition

"Filling the numbers" is the tendency for the daily range to **trade to roughly four
specific reference levels each trading day**: "the likelihood or the tendency for IPDA
to fill specifically **four numbers per day**… the daily range will seek to fill or
trade to four specific levels each trading day" (`ICT-2017-FILLING-NUMBERS`, 00:23–00:44).

The levels come from two families: the **previous day's high and low** (plus daily
swing points), and the **zero-GMT pivot point set**. ICT is explicit that he does not
trade pivots the way retail does — he uses them because **staged orders rest there**,
which is what makes them a destination.

## Formal Criteria

- **Family 1 — prior-day reference points.** "The two levels that first come to mind is
  the previous day's high and [low]" (00:44), plus daily-chart swing points. These are
  "your bread and butter" (01:06). The day trader is "looking for a retest or trade
  through previous day's highs and lows" (01:35).
- **Family 2 — zero-GMT pivots.** "I look for the central pivot point, and these are
  **zero GMT pivots**" (01:58). The ladder taught, in order outward from the centre:

  | above | | below | |
  |---|---|---|---|
  | M3 | midpoint of CP→R1 | M2 | midpoint of CP→S1 |
  | R1 | first resistance | S1 | first support |
  | M4 | midpoint of R1→R2 | M1 | midpoint of S1→S2 |
  | R2 | second resistance | S2 | second support |
  | | | M0 | midpoint of S2→S3 |

- **Why they work:** the levels attract price because "there's going to be **staged
  orders** there — staged means there are buyers and sellers" waiting (03:07), and it is
  bank-level rather than retail flow that stages them (03:55).
- **Retail inversion.** A level retail reads as support can be the opposite: "what would
  otherwise be viewed as a good buy point below the central pivot point, at like S1 and
  S2, that actually might be a really good area to **sell short**" (03:19). Consensus
  reads anything below the central pivot as buyable; that consensus is the liquidity.
- **Which four fill is directional, not fixed:** "using the **order flow direction and
  PD array matrix** for specific bias, we can use these numbers to help determine what
  numbers will be filling for that particular [day]" (05:19). Bias selects the four.

⚠ The count is a **tendency**, not a guarantee, and ICT does not teach trading the
pivot ladder as retail does — "while it's not important that we understand how to trade
pivot points like the retail crowd, it's important to understand what these [levels
are]" (05:04).

## Formula / Math

```
# Family 1 — prior-day references
PDH := previous day high
PDL := previous day low
plus significant daily-chart swing points

# Family 2 — zero-GMT pivot set (CP = central pivot)
above: M3 = (CP + R1)/2,  R1,  M4 = (R1 + R2)/2,  R2
below: M2 = (CP + S1)/2,  S1,  M1 = (S1 + S2)/2,  S2,  M0 = (S2 + S3)/2

# Selection:
expected_fills(day) := the ~4 levels consistent with
                       order_flow_direction AND pd_array_matrix bias
```

## Machine-Readable

```json
{
  "id": "filling-the-numbers",
  "category": "04-time-cycles",
  "aliases": ["four-numbers-per-day", "zero-gmt-pivots"],
  "criteria": [
    {"id": "c1", "expr": "daily_range tends to fill ~4 reference levels per day"},
    {"id": "c2", "expr": "family_1 == [PDH, PDL, daily_swing_points]"},
    {"id": "c3", "expr": "family_2 == zero_GMT pivot set [CP, M0-M4, S1, S2, S3, R1, R2]"},
    {"id": "c4", "expr": "levels attract because staged orders rest there"},
    {"id": "c5", "expr": "which_four == f(order_flow_direction, pd_array_matrix)"},
    {"id": "c6", "expr": "trade_pivots_like_retail == false"}
  ],
  "timeframes": ["M5","M15","H1","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["time-of-day-pivots", "pd-array-matrix", "draw-on-liquidity", "liquidity-pool", "institutional-order-flow"],
  "sources": ["ICT-2017-FILLING-NUMBERS"]
}
```

## Visual Pattern

```
   ──── R2 ────────────────  staged sell orders
   ──── M4 ────
   ──── R1 ────
   ──── M3 ────
   ════ CP ════════════════  central pivot (zero GMT)
   ──── M2 ────
   ──── S1 ────
   ──── M1 ────
   ──── S2 ────────────────  retail reads "support"; may be a SHORT area
   ──── M0 ────

   ──── PDH ───────────────  prior-day high  ) bread and butter
   ──── PDL ───────────────  prior-day low   )

   About four of these get traded to on a given day.
   Bias (order flow + PD array matrix) selects WHICH four.
```

## Timeframes

Intraday execution (M5–H1) against daily-derived levels. The pivot set is recomputed
each day from the zero-GMT session.

## Examples

**Example 1 — the retail inversion (`ICT-2017-FILLING-NUMBERS`, 03:19–03:34):**
- Price trades below the central pivot toward S1/S2.
- Retail consensus reads anything below the central pivot as a buy area.
- With bearish order flow that same level is a continuation **short**, and the consensus
  buying is the liquidity being filled.

## Common Mistakes

- **Trading the pivot ladder as retail does.** ICT uses the levels as destinations where
  staged orders rest, not as support/resistance to buy and sell blindly.
- **Using local-midnight pivots.** The set taught is **zero GMT**.
- **Expecting exactly four every day.** It is a tendency, and which four depends on bias.
- **Ignoring bias when selecting levels.** Without order-flow direction and the PD array
  matrix, the ladder is just lines.
- **Confusing this with killzones.** This concept is about *price* destinations; killzones
  are about *time* windows.

## Related Concepts

- [time-of-day-pivots](time-of-day-pivots.md) — the time-anchored siblings (TDO, 08:30, 09:30, PDH/PDL).
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — supplies the bias that selects which levels fill.
- [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [liquidity-pool](../02-liquidity/liquidity-pool.md) — why staged orders make a level a destination.
- [institutional-order-flow](../03-order-flow/institutional-order-flow.md) — the directional input.

## Citations

- `ICT-2017-FILLING-NUMBERS` (00:00) "lesson two of the May 2017 ICT mentorship, ICT amplified day trading and scalping"; (00:23) "the likelihood or the tendency for IPDA to fill specifically four numbers per day"; (00:44) "the daily range will seek to fill or trade to four specific levels each trading day… previous day's high and [low]"; (01:06) daily swing points as "bread and butter"; (01:35) "we're looking for a retest or trade through previous day's highs and lows as a day trader"; (01:58) "I look for the central pivot point and these are zero GMT pivots"; (02:11–04:24) the M0–M4 / S1–S3 / R1–R2 ladder defined; (03:07) "there's going to be staged orders there — staged means there are buyers and sellers"; (03:19–03:34) the retail-consensus inversion below the central pivot; (03:55) bank-level rather than retail staging; (05:04) not trading pivots like the retail crowd; (05:19) "using the order flow direction and PD array matrix for specific bias… what numbers will be filling."

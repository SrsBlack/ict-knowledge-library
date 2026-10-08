# Power of Three (PO3 / AMD)

**Category:** 12-power-of-three
**Aliases:** PO3, AMD
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-HIGH-REWARD-SETUPS, ICT-2016-INSTITUTIONAL-SPONSORSHIP, ICT-2017-OTE-USDCAD-REVIEW, ICT-2016-RECLAIMED-OB, ICT-2017-OTE, ICT-2017-TOPDOWN-SHORT-TERM, ICT-2022-MENTORSHIP-EP09, ICT-2022-MENTORSHIP-EP21
**Tags:** po3, amd, foundational

## Definition

The Power of Three (PO3) is ICT's three-phase model for how the algorithm delivers price: **Accumulation → Manipulation → Distribution** — "many of you understand my power three concept where power three stands for accumulation distribution and manipulation" (`ICT-2017-OTE-USDCAD-REVIEW`, 05:21); "Power Three which is accumulation manipulation and distribution" (`ICT-2022-MENTORSHIP-EP09`, 00:05). ICT defines it primarily on the **daily OHLC bar** — "Power three is the concept I teach as it relates to the daily open high low and close bar" (`ICT-2016-INSTITUTIONAL-SPONSORSHIP`, 35:21) — and operationally: "when you're bullish, you want to be buying near or below the opening price" (35:51). The **2017 lecture extends it to the weekly range** ("Friday being closed for power three for the weekly range," `ICT-2017-TOPDOWN-SHORT-TERM` 14:34); the **2022 teaching extends it to the session scale** ("power 3 which is a fractal element of accumulation manipulation and distribution," ep21 [24:11]). ⚠ **"AMD doctrine", "MMBM/MMSM as PO3 aliases", and a 4th phase "X"** are not ICT's vocabulary for this concept — see Common Mistakes.

## Formal Criteria

The three phases:

1. **Accumulation** — quiet, range-bound consolidation while institutions build positions.
2. **Manipulation** — engineered fake-out move (Judas Swing) that sweeps liquidity in the wrong direction, providing counter-flow for institutional fills.
3. **Distribution** — the true intended directional move toward HTF DOL.

⚠ A 4th phase "X" and a named "AMD doctrine" do **not** appear in either corpus — searched `amd ?x|fourth phase|4th phase|accumulation.*(continuation|reversal) phase` and `\bAMD\b|AMD doctrine`: zero hits for both. Do not cite these as ICT's terms on this page; `# ICT gives no number or name for a 4th phase in this corpus.`

## Formula / Math

```
po3_phases = ["accumulation", "manipulation", "distribution"]
# No 4th phase "X" and no "AMD doctrine" name in corpus.
```

## Machine-Readable

```json
{
  "id": "power-of-three",
  "category": "12-power-of-three",
  "aliases": ["PO3", "AMD"],
  "criteria": [
    {"id": "c1", "expr": "phases = [accumulation, manipulation, distribution]"},
    {"id": "c2", "expr": "defined primarily on the daily OHLC bar; 2017 lecture extends it to weekly scale, 2022 teaching to session scale"},
    {"id": "c3", "expr": "MMBM/MMSM are a DISTINCT market-maker-model curve concept, not PO3 aliases — see Common Mistakes"}
  ],
  "timeframes": ["D","W","session"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["accumulation-phase","manipulation-phase","distribution-phase","intraday-amd","htf-amd","amd-cycle-overview","amd-vs-po3","quarterly-shift-theory","judas-swing","range-contraction","range-expansion"],
  "sources": ["ICT-2017-HIGH-REWARD-SETUPS","ICT-2016-INSTITUTIONAL-SPONSORSHIP","ICT-2017-OTE-USDCAD-REVIEW","ICT-2016-RECLAIMED-OB","ICT-2017-OTE","ICT-2017-TOPDOWN-SHORT-TERM","ICT-2022-MENTORSHIP-EP09","ICT-2022-MENTORSHIP-EP21"]
}
```

## Visual Pattern

```
   PO3 across one daily OHLC bar:

   Accumulation                Manipulation (Judas)             Distribution
   ────────────                  /\                                   /\
        /\  /\                  /  \   ← sweeps liquidity             /  \
       /  \/  \                /    \                                /    \
      /        \              /      \                             /      \
                                       \                          /
                                        \  ← reversal             /
                                         \                       /
                                          \________→ true delivery
                                                     (distribution toward HTF DOL)
```

## Timeframes

D is the primary scale ICT defines PO3 on: "the concept I teach as it relates to the daily open high low and close bar." The **2017** lecture extends it to the **weekly** scale (Friday closes the week's PO3); the **2022** teaching extends it to the **session** scale ("a fractal element of accumulation manipulation and distribution," ep21 [24:11]). ⚠ "Yearly" and "90-minute" PO3 cycles are **not in corpus** — searched both terms near `power.?of.?three|AMD|accumulation.*manipulation.*distribution`: zero hits beyond daily, weekly and session.

## Examples

**Example 1 — daily PO3 (bullish):**
- Accumulation: Asia range, 30-pip low-volatility consolidation.
- Manipulation: London open, M5 wicks below the range low (Judas), closes back inside.
- Distribution: NY session, 60-pip green displacement, takes PDH BSL.
- → bullish daily PO3 completed.

**Example 2 — session-scale PO3 (bearish, 2022 framing):**
- Accumulation: session opens, 6-hour range.
- Manipulation: wick above the range high.
- Distribution: bearish displacement breaking the session low.
- → bearish session-scale PO3.

## Common Mistakes

- **Forcing every move into PO3.** Some moves are pure expansion or pure consolidation; PO3 isn't always the right read.
- **Mistaking accumulation for trend continuation.** Choppy ranges that look like accumulation may be late-distribution exhaustion instead.
- **Single-TF PO3 read.** PO3 is most useful when read with HTF bias — a daily PO3 aligned with weekly bullish bias is high-conviction; against weekly bias is lower.
- **Calling it "the AMD doctrine" or naming a 4th phase "X."** Neither term is in either corpus — see Formal Criteria.
- **Treating MMBM/MMSM as PO3's upside/downside aliases.** The market maker buy/sell model is a **separate curve construct** in ICT's teaching — "consolidation here the runaway come back to the consolidation distribution smart money reversal low risk buy reaccumulation … what I just described to you is a market maker buy model" (`ICT-2017-OTE`, 29:22–33:58); "this market maker buy model, the curve is basically a price swing lower that trades higher" (`ICT-2016-RECLAIMED-OB`, 03:50). No sentence in either corpus equates it with PO3; conflating the two collapses a multi-leg price curve into a single three-phase label.
- **Claiming "every named setup is an instance of PO3."** Not in corpus. ICT's own operational PO3 statement is narrower, about the opening price: "when you're bullish, you want to be buying near or below the opening price" (`ICT-2016-INSTITUTIONAL-SPONSORSHIP`, 35:51); "if I'm bullish I'm expecting the opening price to be near the low of the day or the session" (`ICT-2022-MENTORSHIP-EP09`, 02:43).

## Related Concepts

- [accumulation-phase](accumulation-phase.md), [manipulation-phase](manipulation-phase.md), [distribution-phase](distribution-phase.md), [intraday-amd](intraday-amd.md), [htf-amd](htf-amd.md).
- [amd-cycle-overview](../24-amd-cycle/amd-cycle-overview.md), [amd-vs-po3](../24-amd-cycle/amd-vs-po3.md).
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [judas-swing](../13-judas-swing/judas-swing.md), [range-contraction](../01-market-structure/range-contraction.md), [range-expansion](../01-market-structure/range-expansion.md).
- The market maker buy/sell model (MMBM/MMSM) is a separate curve concept per the Common Mistakes quotes above; this library has no dedicated page for it yet, so it is not cross-linked here as a PO3 alias.

## Citations

- `ICT-2017-HIGH-REWARD-SETUPS` (42:50–42:56, Oct-2016 lecture despite the ID's year token — see `SOURCES.md`) "Daily range is the time and price theory that we use for engineering the daily range, the power three. The open, high, low, and close" — the earliest located PO3 teaching, which is why `Year Introduced` is 2016.
- `ICT-2016-INSTITUTIONAL-SPONSORSHIP` (35:21) "Power three is the concept I teach as it relates to the daily open high low and close bar"; (35:51) "when you're bullish, you want to be buying near or below the opening price."
- `ICT-2017-OTE-USDCAD-REVIEW` (05:21–06:00) "many of you understand my power three concept where power three stands for accumulation distribution and manipulation."
- `ICT-2016-RECLAIMED-OB` (03:50) "this market maker buy model, the curve is basically a price swing lower that trades higher" — the distinct MMBM curve concept.
- `ICT-2017-OTE` (29:22–33:58) "what I just described to you is a market maker buy model" — full MMBM curve description, distinct from PO3.
- `ICT-2017-TOPDOWN-SHORT-TERM` (14:34) "Friday being closed for power three for the weekly range."
- `ICT-2022-MENTORSHIP-EP09` (00:05) "Power Three which is accumulation manipulation and distribution"; (02:43) "if I'm bullish I'm expecting the opening price to be near the low of the day or the session."
- `ICT-2022-MENTORSHIP-EP21` (24:11) "power 3 which is a fractal element of accumulation manipulation and distribution."

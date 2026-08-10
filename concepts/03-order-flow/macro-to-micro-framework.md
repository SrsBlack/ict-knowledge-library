# Macro-Economic to Micro-Technical Framework

**Category:** 03-order-flow
**Aliases:** macro to micro, macroeconomic to micro technical, bond-to-currency cascade, interest-rate top-down
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-MACRO-TO-MICRO
**Tags:** order-flow, intermarket, bonds, interest-rates, dollar-index, smt, top-down, macro

## Definition

The macro-to-micro framework is ICT's method for deriving a **three-to-six-month directional
outlook for currencies from the interest-rate market alone**, then cascading that conclusion
down to individual pairs and ordinary daily-chart entries. It replaces fundamental research
with a chart read: "I don't require a whole lot of fundamental data to sift through… what I
require is a **visual interpretation** of that data" (`ICT-2016-MACRO-TO-MICRO`, 03:22–04:02).

ICT presents it as proprietary — "one of the closest guarded secrets of my repertoire"
(01:12) — and states he has no attribution for it: "I don't have a source to be able to say
I learned it from this one, that one; it was just me understanding the bond market as a
futures trader" (18:19).

⚠ **Not the same page as [bond-yield-analysis](bond-yield-analysis.md).** Both read the debt
market against the dollar index, but they answer different questions and were taught two
months apart. See *Common Mistakes* for the split.

## Formal Criteria

**Instruments and direction convention**

- Primary: the **30-year treasury bond** — "the benchmark for what we have in the US as our
  mortgage rate" (05:46). Secondary: the **10-year note**. Both read against the **dollar index**.
- **Daily charts only** — "not even an hourly chart, not even a four hour chart" (00:56–01:01).
- Bond futures **price up = interest rates down**; bond futures **price down = rates up** (05:29–05:46).
- Rising rates → capital chases yield → **dollar index rallies** (05:23, 09:09–09:17).

**Signal 1 — divergence between the debt market and the dollar index** (06:18–07:26)

- The same SMT logic ICT teaches for DXY-vs-currencies is applied to the interest-rate market:
  "that same idea is applied here, but for an **interest rate divergence**" (07:04).
- Example form: the dollar index **fails to make a lower low** at the same time the bond
  market makes a **higher high** → an underlying change of trend.

**Signal 2 — divergence between the 10-year and the 30-year** (10:36–12:04)

- The two debt instruments are compared **against each other**. A **higher high in the
  10-year against a lower high in the 30-year** is an SMT divergence internal to the rate
  complex, and it precedes an accelerated dollar rally.
- This internal-to-rates divergence is unique to this framework and is not part of the
  seasonal 10-year read.

**Cadence**

- A **quarterly shift every three to four months**: "whatever trend or market condition is
  prevalent right now, in three to four months' time there's usually a shift — either a
  reversal, or an extended period of consolidation and then a future resumption" (02:36–03:08).
- The outlook produced is explicitly **three to six months** (01:52, 11:02).

**The micro step — cascading to pairs and entries** (12:06–15:24)

- Once the dollar conclusion is set, **buy the pairs whose name starts with USD**
  (USDCHF, USDCAD, USDJPY) and **sell** EUR, GBP, AUD, NZD — or the mirror.
- Verify the conclusion by checking the same turn dates appear across all of them.
- Entries are then framed with **ordinary daily PD arrays** — the worked example uses a
  bullish order block on the pullback and a bearish order block on the rally (07:42–08:07).

**Using it to invalidate a fake move** (16:11–16:53)

- If the dollar index makes a **lower low** but the 10-year and 30-year **do not make the
  corresponding higher highs**, the dollar move is not real: "it was all fluff, it was all
  manipulation… **interest rates were calling the shots**".
- Same test in reverse on the pairs: a currency taking out an old high while the rate complex
  says otherwise is "a false movement" (17:06–17:35).

## Formula / Math

```
# --- convention ---
bond_price ↑  <=>  interest_rates ↓
bond_price ↓  <=>  interest_rates ↑
interest_rates ↑  =>  DXY bullish        # capital chases yield

# --- signal 1: debt market vs dollar index ---
smt_rates_vs_dxy := (DXY fails to make lower_low) AND (bond makes higher_high)
                 OR (DXY fails to make higher_high) AND (bond makes lower_low)

# --- signal 2: 10-year vs 30-year, internal to the rate complex ---
smt_internal := (ZN makes higher_high) AND (ZB makes lower_high)      # -> DXY rally
             OR (ZN makes lower_low)   AND (ZB makes higher_low)      # -> DXY decline

# --- fake-move filter ---
dxy_move_is_real := debt_instruments confirm with the mirrored structure
# DXY lower low WITHOUT 10Y/30Y higher highs  ->  manipulation, not a trend change

# --- cascade ---
if DXY_outlook == bullish:
    long  pairs where base == USD     # USDCHF, USDCAD, USDJPY
    short pairs where quote == USD    # EURUSD, GBPUSD, AUDUSD, NZDUSD
entry := ordinary daily PD array (order block, etc.) in the cascaded direction

horizon := 3..6 months ;  shift_expected_every := 3..4 months
```

## Machine-Readable

```json
{
  "id": "macro-to-micro-framework",
  "category": "03-order-flow",
  "aliases": ["macro-to-micro", "bond-to-currency-cascade", "interest-rate-top-down"],
  "criteria": [
    {"id": "c1", "expr": "instruments == {ZB_30y (primary), ZN_10y, DXY}; daily charts only"},
    {"id": "c2", "expr": "bond_price_down => rates_up => DXY_bullish"},
    {"id": "c3", "expr": "signal_1 := SMT divergence between debt market and DXY"},
    {"id": "c4", "expr": "signal_2 := SMT divergence between 10y and 30y against each other"},
    {"id": "c5", "expr": "outlook_horizon_months in [3, 6]; shift expected every 3-4 months"},
    {"id": "c6", "expr": "cascade: DXY_bullish => long USD-base pairs, short USD-quote pairs"},
    {"id": "c7", "expr": "entry from ordinary daily PD arrays, not from this framework"},
    {"id": "c8", "expr": "DXY move unconfirmed by debt instruments => treated as manipulation"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["bond-yield-analysis", "dollar-index", "interest-rate-differentials", "smt-divergence", "index-smt", "quarterly-shift-theory", "top-down-analysis", "institutional-order-flow"],
  "sources": ["ICT-2016-MACRO-TO-MICRO"]
}
```

## Visual Pattern

```
  MACRO                                                     MICRO
  ───────────────────────────────────────────────────────────────────────

  30-year bond ╲___          rates UP
                   ╲___                 ─────►  DXY  ___╱‾‾‾
  10-year note ╲__  ╲__                              ╱
                                                     │
  SIGNAL 2 — the two debt instruments vs EACH OTHER  │
     10Y   ___╱‾‾╲ higher high                       │
     30Y   __╱‾╲   lower high   <- divergence  ──────┘
                                                     │
                                                     ▼
                            long USDCHF · USDCAD · USDJPY
                            short EURUSD · GBPUSD · AUDUSD · NZDUSD
                                                     │
                                                     ▼
                            entry on a daily bullish/bearish order block

  ───────────────────────────────────────────────────────────────────────
  FAKE-MOVE FILTER

     DXY  ╲__╱   makes a lower low
     10Y  ────   no corresponding higher high
     30Y  ────   no corresponding higher high      -> "all fluff", manipulation
```

## Timeframes

Daily charts for the read; the outlook it produces spans three to six months. ICT excludes
H4 and lower from this analysis explicitly.

## Examples

**Example 1 — the June–August 2016 shift (04:25–08:13):**
- Setup: a high formed in the December bond contract between July and August; ICT had
  publicly called for "a major decline in the debt market… across all of the debt
  instruments", i.e. rising rates.
- Divergence: in the **last week of June** the dollar index **failed to make a lower low**
  while the bond market made a **higher high**.
- Cascade: bonds weakened → rates rose → the dollar index pulled back into a **bullish order
  block** and rallied; rallies into **bearish order blocks** on bonds preceded further bond
  declines, accelerating the dollar bid.

**Example 2 — September 2016, 10-year vs 30-year (10:36–15:24):**
- Divergence: second week of September and again the last week of September, the **10-year
  made a higher high while the 30-year made a lower high**.
- Prediction: an accelerated dollar rally at both dates.
- Verification across the micro layer: USDCHF and USDCAD rallied on both dates; EURUSD and
  GBPUSD topped and sold off on both; NZDUSD and AUDUSD sold off on both; USDJPY made its
  low the first week and its launch high the last week.

**Example 3 — the November 2016 US election (09:22–10:11, 16:11–17:35):**
- Event: overnight, index futures and the dollar index sank hard.
- Test: the dollar index printed a **lower low**, but the 10-year and 30-year futures did
  **not** print the corresponding higher highs.
- Read: "it was all fluff, it was all manipulation… interest rates were calling the shots."
  The dollar then rallied for ten consecutive days while the bond market sold off.
- Same filter on the pairs: AUDUSD and NZDUSD taking out old highs looked bullish but was
  "a false movement" — the dollar was never going to permit the rally.

## Common Mistakes

- **Confusing it with [bond-yield-analysis](bond-yield-analysis.md).** The split:

  | | macro-to-micro (Nov 2016) | bond-yield-analysis (Jan 2017) |
  |---|---|---|
  | Primary instrument | **30-year bond**, 10-year secondary | **10-year note** |
  | Seasonals used | no | yes — both 10Y and DXY templates |
  | Output | a **direction**, cascaded to specific pairs | a **regime** — trending vs consolidating |
  | Signature signal | 10Y-vs-30Y internal divergence | tandem-vs-inverse DXY movement |

  They are complementary, not duplicates; run both and they should agree.
- **Reading bond price as if it were yield.** They are inverse; this is the first thing that
  goes wrong.
- **Applying it intraday.** Daily charts only, three-to-six-month horizon.
- **Treating it as an entry method.** It supplies direction and the pair list; the entry is
  an ordinary daily PD array.
- **Ignoring the confirmation test on a violent news move.** The election example exists
  precisely to show that an unconfirmed dollar move is noise.
- **Expecting the outlook to hold indefinitely.** A quarterly shift is expected every three
  to four months by construction.

## Related Concepts

- [bond-yield-analysis](bond-yield-analysis.md) — the January-2017 sibling; regime classification rather than direction.
- [dollar-index](dollar-index.md) — the hinge between the macro and micro layers.
- [interest-rate-differentials](interest-rate-differentials.md) — the policy-rate read; a different mechanism from the bond-market read.
- [smt-divergence](../16-smt-divergence/smt-divergence.md), [index-smt](../16-smt-divergence/index-smt.md) — the divergence logic, here applied to debt instruments.
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — the three-to-four-month cadence.
- [top-down-analysis](../25-htf-bias/top-down-analysis.md) — the general HTF→LTF descent this is a macro-layer instance of.
- [swing-trading-hallmarks](../31-models/swing-trading-hallmarks.md) — hallmark 3 ("interest rate markets support the trade") is this read.

## Citations

- `ICT-2016-MACRO-TO-MICRO` (00:29) "this is the sixth of eight teachings in the **November 2016** curriculum of the ICT mentorship… macroeconomic to micro technical"; (00:41–01:05) "one of the secrets to how I'm able to call the markets as I do… we're going to be looking at daily charts only"; (01:12–01:30) "one of the closest guarded secrets of my repertoire… a barometer to help me determine where the long term trend of the marketplace is going"; (01:33–01:47) why bank reports are ignored; (01:52–02:28) a three-to-six-month outlook derived from interest rates via the 30-year treasury; (02:36–03:08) the quarterly shift every three to four months; (03:22–04:02) "I don't require a whole lot of fundamental data… what I require is a visual interpretation of that data"; (04:25–05:19) the June–August 2016 bond high and the publicly called debt-market decline; (05:23–05:46) the price/yield inversion and the 30-year as the US mortgage benchmark; (06:18–07:26) the dollar index failing to make a lower low while the bond made a higher high — "that same idea is applied here, but for an interest rate divergence"; (07:42–08:13) bullish and bearish order blocks framing the dollar entries; (09:22–10:11) the election night sell-off and the ten-day dollar rally; (10:36–12:04) the 10-year versus 30-year SMT divergence in September 2016; (12:06–15:24) the cascade verified across USDCHF, USDCAD, EURUSD, GBPUSD, USDJPY, NZDUSD and AUDUSD; (16:11–16:53) "it was all fluff, it was all manipulation… interest rates were calling the shots"; (17:06–17:35) old highs taken out in AUDUSD and NZDUSD as "a false movement"; (18:19–18:29) "I don't have a source to be able to say I learned it from this one, that one — it was just me understanding the bond market as a futures trader"; (18:24–18:36) "the interest rate markets just basically control everything around the world… without interest rates nothing moves".

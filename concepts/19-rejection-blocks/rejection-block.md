# Rejection Block

**Category:** 19-rejection-blocks
**Aliases:** RB
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-HTF-PD-ARRAYS, ICT-2017-QUARTERLY-SHIFTS, ICT-2017-PD-ARRAY-MATRIX, ICT-2017-TRADE-CONDITIONS
**Tags:** rejection-block, wick, foundational

⚠ **Re-dated 2018 → 2017 and the body/wick anchor corrected 2026-08-11; re-audited 2026-10-08
(MINOR-FIXES); "wick gets run through" claim removed and two swapped citations fixed in review.**
The body-edge anchor, the premium-ladder placement, and the multi-candle-cluster reading are all
CONFIRMED verbatim against the corpus. The **≥ 60% wick threshold**, the **named key-level list**
(round number, session extreme, FVG/OB edge), and the **"confirmed by next-candle displacement"**
clause are EMBELLISHED — no numeric threshold or displacement-confirmation rule appears anywhere in
either corpus. The "2022 restatement" claim is dropped: 0 hits for "rejection block" across all 40 captioned
2022 Mentorship episodes. The aliases "wick rejection block" / "long-wick block" are this page's own
unsourced editorial shorthand, not attested in the corpus, and are dropped.

## Definition

A rejection block is a **level drawn at a candle's body edge, identified by a long wick on the other
side of that body**. ⚠ **The level is the body edge, not the wick tip.** ICT: "the rejection block
would be **just above the candle's body, not the wick's**. So the actual high and low is the wick —
but then the next area of importance is the rejection block, that would be just above the candle's
body" (`ICT-2017-HTF-PD-ARRAYS` [18:49–18:57], `[sic]` — transcript reads "the wick's" with an
apostrophe). Discount mirror: "just below the most lowest candle and its body … if it has wicks,
long wicks below it, we're only going to be looking for a move **just below the bodies** of the
candle" [29:02–29:15]. The long wick **identifies** the candidate candle; price is expected to trade
just past the body edge, into that wick zone, and fail there — it is **not** expected to run all the
way through the wick's own extreme: "we look for a price to go just below the bodies of the candles,
and we'll trade right below that like a turtle soup. **It doesn't need to go through the wicks.**"
(`ICT-2017-PD-ARRAY-MATRIX` [22:13–22:17]); "when you see the long wicked candles and you're bearish,
chances are it probably won't go above the wicks. Many times we'll just go above the bodies of the
candles and then fail there — that's the rejection block." [36:12–36:20].

It sits second in the premium ladder, immediately inside the old high: "old high, old low. The next
thing you'll be looking for is a rejection block." [18:46–18:47]. Further attestation: "if those highs
have a lot of wicks, you're going to be looking for rejection blocks, which would be a move above the
bodies of the candles for a potential sell-off" (`ICT-2017-QUARTERLY-SHIFTS` [24:28]); "many times
we'll just go above the bodies of the candles and then fail there — that's the rejection block."
(`ICT-2017-PD-ARRAY-MATRIX` [36:17–36:20]); "it went below the bodies of the candles in here, that is
going to be a rejection block" (`ICT-2017-TRADE-CONDITIONS` [09:58]).

## Formal Criteria

- A candle (or a short cluster of candles — see below) has a **long wick** on one side. No numeric
  threshold is stated anywhere in the corpus (searched `(60|sixty|percent|%)` within 80 characters of
  "wick": 0 hits in `raw/`, 0 in `m22/`); ICT's own language is qualitative — "long wicks"
  (`ICT-2017-HTF-PD-ARRAYS` [29:09]), "a lot of wicks" (`ICT-2017-QUARTERLY-SHIFTS` [24:28]) — both
  phrasings occur in both lectures ([22:59] "a lot of wicks" in HTF-PD; [24:37] "long wicks" in QTR).
- The **level is the candle's body edge**, not the wick tip. Price is expected to trade just past
  that edge and fail — "it doesn't need to go through the wicks" (`ICT-2017-PD-ARRAY-MATRIX`
  [22:17]); the wick is not a target to be run through.
- Context is an **old high/low region whose candles carry wicks** rather than a named key level:
  "the candles that have wicks at short-term highs … there would be liquidity resting just above the
  bodies of the candle" (`ICT-2017-PD-ARRAY-MATRIX` [03:09–03:15]). No "round number", "session
  extreme" or "FVG/OB edge" anchor is stated — remove those from the criteria.
- **Can be a cluster of equal-bodied candles**, not only a single candle: "equal bodied candles above
  that we would expect to see a rejection block" (`ICT-2017-TRADE-CONDITIONS` [13:29]).
- No next-candle displacement confirmation is stated — searched "rejection block" ±6 lines across all
  2017 packets: no confirmation/displacement clause found.

## Formula / Math

```
range_n = high(n) - low(n)
body_n  = abs(close(n) - open(n))

# Bullish RB (discount side):
lower_wick = min(open(n), close(n)) - low(n)
is_bullish_rb_candidate := lower_wick is a "long" / "a lot of" wick   # NO numeric threshold given by ICT
rb_level := min(open(n), close(n))     # the BODY EDGE, not low(n)

# expected behaviour: price trades a short distance PAST rb_level (into the wick zone) and fails;
# it is NOT expected to reach low(n) itself — "it doesn't need to go through the wicks"

# Bearish RB (premium side): symmetric on the upper wick, rb_level := max(open(n), close(n))

# Cluster form:
rb_level := edge shared by a run of equal-bodied candles, not a single candle's extreme
```

## Machine-Readable

```json
{
  "id": "rejection-block",
  "category": "19-rejection-blocks",
  "aliases": ["RB"],
  "criteria": [
    {"id": "c1", "expr": "candle has a qualitatively long wick on one side — NO numeric threshold stated"},
    {"id": "c2", "expr": "rb_level := the candle's BODY EDGE, not the wick tip"},
    {"id": "c3", "expr": "expected behaviour: price trades a short distance past rb_level and fails; does NOT need to reach the wick's own extreme"},
    {"id": "c4", "expr": "context := an old high/low region whose candles carry wicks (no named key-level list)"},
    {"id": "c5", "expr": "may be a cluster of equal-bodied candles sharing one edge, not only a single candle"},
    {"id": "c6", "expr": "no displacement-confirmation clause is stated for the next candle"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["bullish-order-block","bearish-order-block"],
  "sources": ["ICT-2017-HTF-PD-ARRAYS","ICT-2017-QUARTERLY-SHIFTS","ICT-2017-PD-ARRAY-MATRIX","ICT-2017-TRADE-CONDITIONS"]
}
```

## Visual Pattern

```
   bullish rejection block:
          ▲
          █  ← body
          █
        ░░░   ← long lower wick (qualitative — "a lot of wicks" / "long wicks")
        ░░░
        ░░░
       (price trades a short distance past the body edge, into the wick zone, and
        fails — it does NOT need to go through the wick's own extreme)

   rb_level = the BODY's lower edge (min(open, close)), marked ──

   bearish RB: mirror, level at the body's UPPER edge.
```

## Timeframes

No timeframe floor is stated by ICT; the construct is taught on monthly/weekly/daily PD arrays
(`ICT-2017-HTF-PD-ARRAYS` [31:08–31:24]) — the JSON `timeframes` above lists what the corpus shows,
not a floor ICT states.

## Examples

**Example 1 — bearish RB above a cluster of wicked highs (schematic, following the lecture language):**
- A cluster of candles sits at an old high, each carrying a long upper wick — "a lot of wicks" at
  that level.
- The rejection block level is drawn at the **shared body edge** of that cluster (the top of the
  bodies), not at the highest wick tip.
- Price later trades up a short distance past the body edge (into the wick zone) and is expected to
  fail there — it does not need to go through the wicks' own extreme.

## Common Mistakes

- **Calling every long-wick candle "RB."** Without an old-high/old-low context with wicked candles,
  the long wick is noise — but no numeric wick percentage disqualifies or qualifies it either way.
- **Drawing the level at the wick tip.** The level is the **body edge**; a prior version of this page
  marked "wick tip = key level" in its own Example/Common-Mistakes text, inverting ICT's correction.
- **Claiming the wick itself "is expected to be run through."** ICT states the opposite — price need
  only trade past the body edge; "it doesn't need to go through the wicks" (`ICT-2017-PD-ARRAY-MATRIX`
  [22:13–22:17]).
- **Requiring a named key level (round number, session extreme, FVG/OB edge).** Not stated; the
  context is simply an old high/low region whose candles carry wicks.
- **Requiring next-candle displacement to confirm.** No such clause exists in the corpus.
- **Confusing RB with a liquidity sweep as a single-candle event.** A rejection block can be a
  **cluster** of equal-bodied candles sharing one edge, not necessarily one candle.

## Related Concepts

- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md) — adjacent array in the premium/discount ladder.

## Citations

- `ICT-2017-HTF-PD-ARRAYS` [18:46–18:47] placed second in the premium ladder; [18:49–18:57] "just above the candle's body, not the wick's" `[sic]`; [22:53–23:02], [22:59] used when a bearish OB is absent due to wicks, "a lot of wicks"; [29:02–29:15] discount mirror; [29:09] "long wicks"; [31:08–31:24] identical hierarchy on all HTFs.
- `ICT-2017-QUARTERLY-SHIFTS` [24:28] "a lot of wicks … rejection blocks, which would be a move above the bodies of the candles"; [24:37] "long wicks" (the mirrored phrasing also occurs here).
- `ICT-2017-PD-ARRAY-MATRIX` [03:09–03:15] wicked candles at short-term highs; [22:09] "every rejection block below, candles have wicks"; [22:13–22:17] "we look for a price to go just below the bodies of the candles … it doesn't need to go through the wicks"; [36:12–36:20] "when you see the long wicked candles and you're bearish, chances are it probably won't go above the wicks … that's the rejection block."
- `ICT-2017-TRADE-CONDITIONS` [02:00], [02:47], [03:29] rejection block in the PD-array ladder; [09:58] "it went below the bodies of the candles in here, that is going to be a rejection block"; [13:29–13:37] cluster of equal-bodied candles forming a rejection block.

# Killzone vs Session — Disambiguation

**Category:** 10-killzones
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, sessions, disambiguation, terminology

## Definition

This is the killzone-side mirror of the [session-vs-killzone](../15-sessions/session-vs-killzone.md) page. The two pages cross-link the same disambiguation from both directories so a reader navigating either side finds the explanation immediately.

**Short version:** killzones ⊂ sessions. A killzone is a stricter, narrower sub-window of a broad session where ICT teaches the highest-probability setups occur.

For the full taxonomy, comparison table, and the containment proof, see [session-vs-killzone](../15-sessions/session-vs-killzone.md).

## Formal Criteria

Identical to [session-vs-killzone](../15-sessions/session-vs-killzone.md). Killzones are subsets of sessions defined by NY-clock anchors:

- Asia killzone (20:00–00:00) ⊂ Asia session (~18:00–03:00).
- London Open KZ (02:00–05:00) ⊂ London session (02:00–11:00).
- NY AM KZ (08:00–11:00) ⊂ NY AM session (08:00–12:00).
- London Close KZ (10:00–12:00) ⊂ London session.
- NY PM KZ (13:30–16:00) ⊂ NY PM session (13:30–16:00, identical to KZ).

## Formula / Math

```
in_killzone(t, kz) ⇒ in_session(t, parent_session(kz))
```

Reverse implication is FALSE.

## Machine-Readable

```json
{
  "id": "killzone-vs-session",
  "category": "10-killzones",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "every_killzone_subset_of_a_session == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["session-vs-killzone","killzone-overview","session-overview","asia-killzone","london-open-killzone","ny-am-killzone","london-close-killzone","ny-pm-killzone"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

See [session-vs-killzone](../15-sessions/session-vs-killzone.md) for the side-by-side ASCII diagram.

## Timeframes

Every TF.

## Examples

See [session-vs-killzone](../15-sessions/session-vs-killzone.md).

## Common Mistakes

- **Treating "session" as a synonym for "killzone."** A trade at 06:30 NY is in the London session but past the London Open killzone; ICT discipline says no new entries.
- **Forgetting parent-session lookup.** Every KZ has exactly one parent session (London Close KZ has London session as parent, not NY AM, even though it overlaps NY AM).

## Related Concepts

- [session-vs-killzone](../15-sessions/session-vs-killzone.md) — the canonical disambiguation page (this page is a pointer for navigation convenience).
- [killzone-overview](killzone-overview.md), [session-overview](../15-sessions/session-overview.md).

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.

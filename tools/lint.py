"""Structural lint for the ICT knowledge library.

Run from the repo root:  python tools/lint.py

Checks, in the order AGENTS.md lists them, plus two added 2026-08-10 after silent
failures got through:

  * `sources_agree`  — the bold-key `**Source IDs:**` line and the JSON `sources[]`
    must list the same IDs. Three pages had drifted: an edit updated the header and
    missed the JSON because the array's formatting differed from what the edit
    expected. Nothing else noticed, because every other check reads only one of the
    two lists.
  * `years_agree`    — `**Year Introduced:**` must equal JSON `year_introduced`.

Exit status is non-zero if anything fails, so this is CI-safe.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    "## Definition",
    "## Formal Criteria",
    "## Formula / Math",
    "## Machine-Readable",
    "## Visual Pattern",
    "## Timeframes",
    "## Examples",
    "## Common Mistakes",
    "## Related Concepts",
    "## Citations",
]

REQUIRED_FIELDS = [
    "**Category:**",
    "**Aliases:**",
    "**ICT Confidence:**",
    "**Year Introduced:**",
    "**Year Refined:**",
    "**Source IDs:**",
    "**Tags:**",
]


def concept_files() -> list[Path]:
    return [p for p in sorted(ROOT.glob("concepts/*/*.md")) if p.name != "README.md"]


def source_ids() -> set[str]:
    text = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
    return set(re.findall(r"^- `([A-Z0-9\-]+)`", text, re.M))


def main() -> int:
    files = concept_files()
    ids = {p.stem for p in files}
    known_sources = source_ids()
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    problems: list[str] = []

    def bad(msg: str) -> None:
        problems.append(msg)

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                bad(f"{rel}: missing section {section}")
        for field in REQUIRED_FIELDS:
            if field not in text:
                bad(f"{rel}: missing field {field}")

        match = re.search(r"```json\n(.*?)\n```", text, re.S)
        if not match:
            bad(f"{rel}: no JSON block")
            continue
        try:
            blob = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            bad(f"{rel}: bad JSON ({exc})")
            continue

        if blob.get("id") != f.stem:
            bad(f"{rel}: JSON id {blob.get('id')!r} != filename")

        for related in blob.get("related", []):
            if related not in ids:
                bad(f"{rel}: related[] points at missing concept {related!r}")

        header_sources = {
            s.strip()
            for s in re.search(r"\*\*Source IDs:\*\* (.+)", text).group(1).split(",")
        }
        json_sources = set(blob.get("sources", []))
        for sid in header_sources | json_sources:
            if sid not in known_sources:
                bad(f"{rel}: unknown source id {sid!r}")
        if header_sources != json_sources:
            bad(
                f"{rel}: header/JSON sources disagree "
                f"(header-only={sorted(header_sources - json_sources)}, "
                f"json-only={sorted(json_sources - header_sources)})"
            )

        # citations_cover_sources — every ID in the header must actually appear in the
        # ## Citations section. Added 2026-08-11 after three pages were re-dated with the
        # header and JSON updated together while the Citations list kept naming the source
        # that had just been removed. header/JSON agreement cannot catch this: Citations is
        # a third surface stating the same fact, and nothing was reading it.
        cit = re.search(r"^## Citations\s*(.*?)\Z", text, re.M | re.S)
        if cit:
            missing = sorted(s for s in header_sources if s not in cit.group(1))
            if missing:
                bad(f"{rel}: Source IDs absent from ## Citations: {missing}")

        header_year = re.search(r"\*\*Year Introduced:\*\* (\d{4})", text).group(1)
        if blob.get("year_introduced") != header_year:
            bad(
                f"{rel}: header year {header_year} != JSON "
                f"year_introduced {blob.get('year_introduced')}"
            )

        for link in re.findall(r"\]\((\.\./[^)]+\.md)\)", text):
            if not (f.parent / link).resolve().exists():
                bad(f"{rel}: dead link {link}")
        for link in re.findall(r"\]\(([a-z0-9\-]+\.md)\)", text):
            if not (f.parent / link).exists():
                bad(f"{rel}: dead local link {link}")

        if rel not in index:
            bad(f"{rel}: not listed in INDEX.md")

    for link in sorted(set(re.findall(r"\]\((concepts/[^)]+\.md)\)", index))):
        if not (ROOT / link).exists():
            bad(f"INDEX.md: points at missing file {link}")

    print(f"{len(files)} concept pages, {len(known_sources)} source ids")
    print(f"problems: {len(problems)}")
    for problem in problems:
        print(f"  {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

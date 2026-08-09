#!/usr/bin/env python3
"""Prepare an ingest packet for a video source.

Does the mechanical half of AGENTS.md -> Operations -> Ingest:

    step 1  read the source        -> transcript + scene frames
    step 2  decide a Source ID     -> proposed, and checked against SOURCES.md

and stops. Steps 3-9 (which concepts a source refines, what the confidence
field should say, what body text to change) are judgment, not mechanism, and
stay with the agent reading the packet.

Transcription runs locally and free; see gpu-lab/whisper_local_README.md.

    python tools/ingest_video.py <url-or-id> [--start 12:00] [--end 20:00]
    python tools/ingest_video.py --self-check
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES_MD = REPO / "SOURCES.md"
RAW_DIR = REPO / "raw"

# The official channel is the only "high" confidence publisher; everything else
# is community and AGENTS.md wants that distinction visible from the start.
OFFICIAL_CHANNELS = {"the inner circle trader", "innercircletrader"}


def find_watch_script() -> Path:
    """Locate the installed /watch skill. Its path carries a plugin version."""
    # Order matters. `cache/` is the installed, running copy and the one
    # carrying the local patches; `marketplaces/` is an unpatched clone of the
    # upstream repo. Taking the wrong one loses --force-whisper and the local
    # Whisper backend, so the first root that matches wins outright.
    roots = [
        Path.home() / ".claude" / "plugins" / "cache" / "claude-video",
        Path.home() / ".claude" / "plugins" / "marketplaces" / "claude-video",
    ]
    for root in roots:
        # Highest version string sorts last; a plugin update leaves that one live.
        found = sorted(root.glob("**/skills/watch/scripts/watch.py"))
        if found:
            return found[-1]
    raise SystemExit(
        "watch.py not found. Install it with:\n"
        "  claude plugin marketplace add bradautomates/claude-video\n"
        "  claude plugin install watch@claude-video"
    )


def slugify(text: str, max_words: int = 5) -> str:
    words = re.findall(r"[A-Za-z0-9]+", text.upper())
    skip = {"THE", "A", "AN", "OF", "TO", "AND", "ICT", "INTRO", "PART"}
    kept = [w for w in words if w not in skip] or words
    slug = kept[:max_words]
    # A volume/episode number is often the ONLY thing distinguishing siblings
    # ("… Series - Vol. 12"), and it sits past the word cut. Re-attach it —
    # but ONLY when an explicit marker precedes it. Treating any trailing digit
    # as a volume breaks titles that end in a date: "… OTE UsdChf … 10/27/17"
    # dropped the pair name and kept the year, collapsing every drill onto one id.
    marker = re.search(r"\b(?:VOL|VOLUME|EPISODE|EP|PART|NO|MONTH)\.?\s*(\d+)\b", text.upper())
    if marker:
        num = marker.group(1)
        if num not in slug:
            slug = (slug[:-1] if len(slug) == max_words else slug) + [num]
        # The marker number alone is not enough when a series numbers a whole
        # BATCH the same way: every "… - Month 06 - <topic>" lecture shares the
        # number and differs only in the topic, which sits past the word cut.
        # 112 of 114 Core Content videos collided on this. Carry two topic words.
        tail = [w for w in kept[kept.index(num) + 1:] if w not in slug][:3] \
            if num in kept else []
        slug = slug + tail
    return "-".join(slug)


def derive_packet_id(channel: str, upload_date: str, title: str, video_id: str) -> str:
    """Packet directory id — unique BY CONSTRUCTION, not by luck.

    Title-derived slugs cannot be made reliably unique: 112 of 114 Core Content
    lectures collided on `… - Month NN -`, and widening the word window only got
    to 112/114 at 85 characters. The video id is the canonical identifier, so it
    is appended always. Curated citation IDs in SOURCES.md stay hand-authored;
    this is the working folder name.
    """
    return f"{derive_source_id(channel, upload_date, title)}-{video_id}"


def publisher_for(channel: str) -> str:
    if channel.strip().lower() in OFFICIAL_CHANNELS:
        return "ICT"
    return slugify(channel, max_words=1) or "UNKNOWN"


def derive_source_id(channel: str, upload_date: str, title: str) -> str:
    """Build a `<PUBLISHER>-<YEAR>-<SLUG>` id per the SOURCES.md convention."""
    year = (upload_date or "")[:4] or "UNDATED"
    return f"{publisher_for(channel)}-{year}-{slugify(title)}"


def scan_sources(text: str, video_id: str, source_id: str) -> dict:
    """Report how this video already appears in SOURCES.md, if at all.

    Re-ingesting a cited source silently would duplicate Source IDs, and
    AGENTS.md makes IDs append-only — so a collision has to surface loudly.
    """
    ids = set(re.findall(r"^- `([A-Z0-9][A-Z0-9\-]*)`", text, re.MULTILINE))
    by_video = [
        line.strip()
        for line in text.splitlines()
        if video_id and video_id in line
    ]
    return {
        "source_id_taken": source_id in ids,
        "video_already_cited": by_video,
        "total_source_ids": len(ids),
    }


def normalize_source(source: str) -> str:
    """Expand a bare YouTube id to a URL, leaving URLs and local paths alone.

    watch.py resolves anything without a scheme as a local file path, so a bare
    id like `2mtzC7ajUew` becomes a missing-file error rather than a download.
    """
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", source) and not Path(source).exists():
        return f"https://www.youtube.com/watch?v={source}"
    return source


def video_metadata(source: str) -> dict:
    fields = ["id", "title", "channel", "upload_date", "duration", "webpage_url"]
    out = subprocess.run(
        ["yt-dlp", "--skip-download", "--print",
         "|".join(f"%({f})s" for f in fields), source],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        raise SystemExit(f"yt-dlp metadata failed: {out.stderr.strip()[-400:]}")
    line = [ln for ln in out.stdout.splitlines() if "|" in ln][-1]
    return dict(zip(fields, line.split("|")))


def run_watch(source: str, out_dir: Path, args) -> str:
    cmd = [
        sys.executable, str(find_watch_script()), source,
        "--out-dir", str(out_dir),
        "--detail", args.detail,
        "--resolution", str(args.resolution),
        # Local Whisper is free and produces cleaner text than YouTube's
        # auto-captions, which repeat every line.
        "--force-whisper",
    ]
    if not args.dedup:
        # Chart videos defeat near-duplicate filtering: the screen sits still
        # and changes in small increments, so consecutive samples read as
        # duplicates and get dropped (89 of 100 on a 44-min lecture). But a
        # frame whose only difference is a fib that was just drawn is the most
        # informative frame in the video — precisely what dedup discards.
        cmd.append("--no-dedup")
    for flag in ("start", "end"):
        if getattr(args, flag):
            cmd += [f"--{flag}", getattr(args, flag)]
    print(f"[ingest] watching ({args.detail}, {args.resolution}px)…", file=sys.stderr)
    result = subprocess.run(cmd, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode != 0:
        raise SystemExit(f"watch failed: {result.stderr.strip()[-800:]}")
    return result.stdout


def check_transcript(report: str, duration_s: float) -> list[str]:
    """Flag transcripts that are truncated or stuck in a repetition loop.

    Whisper's temperature ladder is non-deterministic: the same 44-min lecture
    produced 409 healthy segments on one run and 2228 on another. A degenerate
    transcript reads as plausible prose, so it has to be caught mechanically
    before it reaches a concept file.
    """
    lines = re.findall(r"^\[(\d+):(\d\d)\]\s*(.+)$", report, re.MULTILINE)
    if not lines:
        return ["no timestamped transcript lines found"]

    warnings = []
    starts = [int(m) * 60 + int(s) for m, s, _ in lines]
    # Lines carry START times only, and the final segment can be long — a
    # sign-off starting at 92s of a 108s video is complete, not truncated.
    # Estimate its end from the median gap between starts.
    gaps = sorted(b - a for a, b in zip(starts, starts[1:])) or [0]
    covered = starts[-1] + gaps[len(gaps) // 2]
    if duration_s and covered < duration_s * 0.9:
        warnings.append(
            f"transcript covers ~{covered}s of {int(duration_s)}s "
            f"({covered / duration_s:.0%}) — possibly truncated")

    # A loop repeats CONSECUTIVELY. Total repeat count is the wrong signal:
    # ICT says a standalone "Okay." 51 times in one lecture, scattered, and
    # counting totals flagged that healthy transcript as degenerate.
    texts = [t.strip().lower() for _, _, t in lines]
    run = worst_run = 1
    worst_text = texts[0]
    for prev, cur in zip(texts, texts[1:]):
        run = run + 1 if cur == prev else 1
        if run > worst_run:
            worst_run, worst_text = run, cur
    # Severity is a FRACTION, not a count. Whisper hallucinates "Bye." x31 over
    # a video's trailing silence; that is 9% junk on an otherwise complete
    # 332-segment lecture, not a corrupt transcript. A flat count quarantined
    # 13 usable transcripts over tails like that.
    if worst_run >= 4:
        share = worst_run / len(texts)
        sev = "DOMINANT" if share > 0.10 else "localized"
        warnings.append(
            f"{worst_run} consecutive identical lines ({share:.0%} of transcript, "
            f"{sev}) — decode loop: {worst_text[:50]!r}")
    return warnings


def is_usable(warnings: list[str]) -> bool:
    """A transcript is unusable only if it is absent, truncated, or loop-dominated.

    A localized loop is a defect to disclose, not a reason to discard 50 minutes
    of otherwise-clean lecture.
    """
    return not any(
        ("no timestamped" in w) or ("truncated" in w) or ("DOMINANT" in w)
        for w in warnings
    )


def _protect_leading_dash_ids(argv: list[str]) -> list[str]:
    """Expand a hyphen-leading bare video id to a URL before argparse sees it.

    YouTube ids are base64url, so ~2% start with '-'. argparse swallows those as
    options and exits before the tool ever runs — two Core Content videos failed
    this way with no error line at all, which is worse than crashing.

    Expanding to a URL (rather than inserting `--`) is what keeps the real flags
    working: everything after a `--` is treated as positional, so `--detail
    transcript` became stray positionals and argparse rejected the whole call.
    """
    out = list(argv)
    for i, a in enumerate(out):
        if a == "--":
            break
        if re.fullmatch(r"-[A-Za-z0-9_-]{10}", a) and not Path(a).exists():
            out[i] = f"https://www.youtube.com/watch?v={a}"
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", help="video URL or YouTube id")
    ap.add_argument("--source-id", help="override the proposed Source ID")
    ap.add_argument("--start")
    ap.add_argument("--end")
    ap.add_argument("--detail", default="balanced",
                    choices=["transcript", "efficient", "balanced", "token-burner"])
    ap.add_argument("--resolution", type=int, default=1024,
                    help="frame width; 1024 keeps chart text and price levels legible")
    ap.add_argument("--keep-video", action="store_true",
                    help="keep the downloaded video and extracted audio "
                         "(packets are otherwise text+frames)")
    ap.add_argument("--dedup", action="store_true",
                    help="re-enable near-duplicate frame dropping; off by default "
                         "because it guts chart footage (see run_watch)")
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args(_protect_leading_dash_ids(sys.argv[1:]))

    if args.self_check:
        return self_check()
    if not args.source:
        ap.error("source is required (or pass --self-check)")

    source = normalize_source(args.source)
    meta = video_metadata(source)
    source_id = args.source_id or derive_packet_id(
        meta["channel"], meta["upload_date"], meta["title"], meta["id"])
    collisions = scan_sources(
        SOURCES_MD.read_text(encoding="utf-8"), meta["id"], source_id)

    print(f"[ingest] {meta['title']}", file=sys.stderr)
    print(f"[ingest] {meta['channel']} · {meta['upload_date']} · {meta['duration']}s",
          file=sys.stderr)
    print(f"[ingest] proposed Source ID: {source_id}", file=sys.stderr)
    if collisions["video_already_cited"]:
        print(f"[ingest] NOTE: this video id is already cited in SOURCES.md:",
              file=sys.stderr)
        for line in collisions["video_already_cited"]:
            print(f"           {line[:160]}", file=sys.stderr)
        print("[ingest] -> extend the existing entry; do NOT mint a new ID.",
              file=sys.stderr)

    packet = RAW_DIR / source_id
    # Two different videos resolving to one Source ID would silently overwrite
    # each other's packet. Slug truncation already did this once (every
    # "… Series - Vol. N" collapsed to one id), so refuse rather than clobber.
    existing_meta = packet / "meta.json"
    if existing_meta.exists():
        prior = json.loads(existing_meta.read_text(encoding="utf-8"))
        if prior.get("id") and prior["id"] != meta["id"]:
            raise SystemExit(
                f"Source ID collision: {source_id} already holds video "
                f"{prior['id']} ({prior.get('title')}), but this is {meta['id']} "
                f"({meta['title']}). Pass an explicit --source-id."
            )
    fresh = not packet.exists()
    packet.mkdir(parents=True, exist_ok=True)
    try:
        report = run_watch(source, packet / "work", args)
    except SystemExit:
        # A packet without meta.json is not a packet — it is a trap for anything
        # that walks raw/. Downloads fail transiently; don't leave the wreckage.
        if fresh:
            shutil.rmtree(packet, ignore_errors=True)
            print(f"[ingest] removed incomplete packet {packet.name}", file=sys.stderr)
        raise

    (packet / "report.md").write_text(report, encoding="utf-8")

    warnings = check_transcript(report, float(meta.get("duration") or 0))
    for w in warnings:
        print(f"[ingest] WARNING: {w}", file=sys.stderr)
    if warnings:
        print("[ingest] -> re-run before citing; Whisper decoding is "
              "non-deterministic and a clean retry is usually enough.",
              file=sys.stderr)
    (packet / "meta.json").write_text(json.dumps({
        **meta,
        "source_id": source_id,
        "confidence_hint": (
            "high" if publisher_for(meta["channel"]) == "ICT" else "community-attributed"),
        "sources_md": collisions,
        "transcript_warnings": warnings,
    }, indent=2), encoding="utf-8")

    if not args.keep_video:
        shutil.rmtree(packet / "work" / "download", ignore_errors=True)
        # Whisper's extracted audio is ~0.5 MB/min (52 MB for a 57-min lecture)
        # and the transcript it produced is already in report.md.
        shutil.rmtree(packet / "work" / "chunks", ignore_errors=True)
        for leftover in (packet / "work").glob("*.mp3"):
            leftover.unlink()

    frames = sorted((packet / "work" / "frames").glob("*.jpg"))
    print(f"\n[ingest] packet ready: {packet}", file=sys.stderr)
    print(f"[ingest]   report.md   transcript + frame index", file=sys.stderr)
    print(f"[ingest]   meta.json   metadata + SOURCES.md collision check", file=sys.stderr)
    print(f"[ingest]   work/frames {len(frames)} frames", file=sys.stderr)
    print(
        "\nNext (AGENTS.md steps 3-9, judgment — not automated):\n"
        "  3. Read report.md and the frames; decide which concepts this refines.\n"
        "  4. INDEX.md   — add any new concept files\n"
        "  5. TIMELINE.md — add under the source's year\n"
        "  6. GLOSSARY.md — any new abbreviation\n"
        "  7. log.md      — prepend '## [YYYY-MM-DD] ingest | <title>'\n"
        "  8. lint the touched files\n"
        "  9. commit 'ingest: <title> — N files updated'",
        file=sys.stderr,
    )
    return 0


def self_check() -> int:
    assert slugify("OTE Primer - Intro To ICT Optimal Trade Entry") == "OTE-PRIMER-OPTIMAL-TRADE-ENTRY"
    assert slugify("Power of Three!!") == "POWER-THREE"
    # Volume numbers must survive truncation or every volume shares one id.
    v12 = slugify("OTE Pattern Recognition Series - Vol. 12")
    v20 = slugify("OTE Pattern Recognition Series - Vol. 20")
    assert v12 != v20, (v12, v20)
    assert v12.endswith("12") and v20.endswith("20"), (v12, v20)
    assert slugify("OTE Pattern Recognition Series - Vol.19").endswith("19")
    # A trailing DATE is not a volume number. These four differ only by the
    # instrument, which must survive; keying on the date collapsed them all.
    drills = [
        slugify(f"ICT Pattern Recognition Drill - OTE {sym} New York Session 10/27/17")
        for sym in ("UsdChf", "UsdJpy", "AusUsd", "Gold")
    ]
    assert len(set(drills)) == 4, drills
    assert all(not d.endswith("17") for d in drills), drills

    # A numbered series that shares one number across a whole batch: the topic
    # after the marker is the only distinguishing text.
    cc = [
        slugify("ICT Mentorship Core Content - Month 06 - Reducing Risk & Maximizing Reward"),
        slugify("ICT Mentorship Core Content - Month 06 - Trading The Weekly Range"),
        slugify("ICT Mentorship Core Content - Month 05 - Using IPDA Data Ranges"),
        slugify("ICT Mentorship Core Content - Month 05 - Using 10 Year Notes In HTF Analysis"),
    ]
    assert len(set(cc)) == 4, cc

    # Packet ids must be unique even when the titles are not distinguishable —
    # these two differ only past the word window, and both are real.
    ch, d = "The Inner Circle Trader", "20220101"
    a = derive_packet_id(ch, d, "ICT Mentorship Core Content - Month 10 - Stock Trading - Using Options", "aaaaaaaaaaa")
    b = derive_packet_id(ch, d, "ICT Mentorship Core Content - Month 10 - Stock Trading - Using Puts", "bbbbbbbbbbb")
    assert a != b and a.endswith("aaaaaaaaaaa"), (a, b)
    # Identical title + identical video => identical id (reproducible, not ordinal).
    assert a == derive_packet_id(ch, d, "ICT Mentorship Core Content - Month 10 - Stock Trading - Using Options", "aaaaaaaaaaa")
    assert publisher_for("The Inner Circle Trader") == "ICT"
    assert publisher_for("Romeo") == "ROMEO"

    assert derive_source_id("The Inner Circle Trader", "20170930", "OTE Primer") == \
        "ICT-2017-OTE-PRIMER"
    # An undated upload must not silently become year 0000.
    assert derive_source_id("The Inner Circle Trader", "", "X") == "ICT-UNDATED-X"

    sample = (
        "- `ICT-2017-OTE` — Optimal Trade Entry. official channel `Cg0-CFJOJvg`, 2017-09-30\n"
        "- `ICT-2020-OTE-VOL01` — Vol. 01, official channel `E9F_aT9f038`\n"
    )
    hit = scan_sources(sample, "Cg0-CFJOJvg", "ICT-2017-OTE")
    assert hit["source_id_taken"] is True
    assert len(hit["video_already_cited"]) == 1
    assert hit["total_source_ids"] == 2

    miss = scan_sources(sample, "zzzzzzzzzzz", "ICT-2026-NEW")
    assert miss["source_id_taken"] is False
    assert miss["video_already_cited"] == []

    assert normalize_source("2mtzC7ajUew") == "https://www.youtube.com/watch?v=2mtzC7ajUew"
    assert normalize_source("https://youtu.be/x") == "https://youtu.be/x"
    # 12 chars is not a YouTube id and must stay a path.
    assert normalize_source("clip12345678") == "clip12345678"
    assert normalize_source("-oMtfDvc18Y") == "https://www.youtube.com/watch?v=-oMtfDvc18Y"

    # Hyphen-leading ids must survive argparse — AND the real flags must still
    # parse. Inserting `--` satisfied the first and broke the second.
    yt = "https://www.youtube.com/watch?v="
    assert _protect_leading_dash_ids(["-oMtfDvc18Y"]) == [yt + "-oMtfDvc18Y"]
    assert _protect_leading_dash_ids(["-cXnnHjy9s0", "--detail", "transcript"]) == \
        [yt + "-cXnnHjy9s0", "--detail", "transcript"]
    assert _protect_leading_dash_ids(["--self-check"]) == ["--self-check"]
    assert _protect_leading_dash_ids(["abc", "--detail", "transcript"]) == \
        ["abc", "--detail", "transcript"]
    # Must not rewrite a genuine flag that happens to be 11 chars.
    assert _protect_leading_dash_ids(["--keep-video"]) == ["--keep-video"]

    healthy = "\n".join(f"[{m:02d}:00] line number {m}" for m in range(0, 45))
    assert check_transcript(healthy, 2680) == []
    # Truncated: stops a third of the way through a 44-min video.
    assert any("truncated" in w for w in check_transcript(healthy, 8000))
    # A long final segment is not truncation: Vol.12's sign-off starts at 92s
    # of a 108s video and runs to the end.
    vol12 = "[00:34] a\n[01:02] b\n[01:13] c\n[01:32] good luck and good trading"
    assert check_transcript(vol12, 108) == [], check_transcript(vol12, 108)
    looped = healthy + "\n" + "\n".join("[44:30] and that's the price" for _ in range(9))
    assert any("decode loop" in w for w in check_transcript(looped, 2680))
    # 9 of 54 lines = 17% -> dominant -> unusable.
    assert not is_usable(check_transcript(looped, 2680))
    # A short tail loop on a long transcript stays usable: "Bye." x5 of 50 = 10%.
    tail = "\n".join(f"[{m:02d}:00] real line {m}" for m in range(45)) + "\n" + \
        "\n".join("[44:30] bye." for _ in range(5))
    w = check_transcript(tail, 2680)
    assert any("localized" in x for x in w), w
    assert is_usable(w), w
    assert is_usable([])
    # Negative control: a scattered verbal tic is NOT a loop. This is the real
    # Vol.01 shape — 51 standalone "Okay."s, never more than 2 in a row.
    tic = "\n".join(
        f"[{m:02d}:00] okay.\n[{m:02d}:30] substantive line {m}" for m in range(0, 45))
    assert check_transcript(tic, 2680) == [], check_transcript(tic, 2680)
    assert check_transcript("no timestamps here", 100) == \
        ["no timestamped transcript lines found"]

    print("self-check OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

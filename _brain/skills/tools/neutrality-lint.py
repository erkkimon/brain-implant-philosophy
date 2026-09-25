#!/usr/bin/env python3
"""Evaluative-predicate lint — implements the evaluative-predicate rule of the
implant's conventions (conventions/reporting-not-endorsing.md, with the claim
grades of conventions/how-claims-are-graded.md).

Usage:  neutrality-lint.py [--json] [--words] <file.md | dir>...
Exit code 1 if any finding, 0 otherwise (2 on usage error).

Flags evaluative words ("fallacy", "obviously", "widely accepted", ...) that
appear in the implant's own voice. A hit is suppressed when it is quoted
or *italicised* (a mention of the word, not a use of it), in code, in a blockquote, in YAML frontmatter, attributed earlier in the same
sentence (classifies / argues / according to / ...), followed by a citation
token in the same sentence ((2008), doi:, p., §, ](...)), or when the line
ends with `# lint: allow`. Nearest heading is reported as context.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

# (label, regex, severity). Whole-word, case-insensitive, obvious inflections.
WORDS: list[tuple[str, str, str]] = [
    ("fallacious", r"\bfallacious(?:ly)?\b", "flag"),
    ("fallacy", r"\bfallac(?:y|ies)\b", "flag"),
    ("debunked", r"\bdebunk(?:ed|s|ing)?\b", "flag"),
    ("refuted", r"\brefut(?:ed|es|e|ing)\b", "flag"),
    ("discredited", r"\bdiscredit(?:ed|s|ing)?\b", "flag"),
    ("fringe", r"\bfringe\b", "flag"),
    ("pseudoscience", r"\bpseudo(?:science|scientific|-\w*)(?!\w)", "flag"),
    ("crank", r"\bcranks?\b", "flag"),
    ("obviously", r"\bobvious(?:ly)?\b", "flag"),
    ("clearly", r"\bclearly\b", "flag"),
    ("of course", r"\bof course\b", "flag"),
    ("rightly", r"\brightly\b", "flag"),
    ("wrongly", r"\bwrongly\b", "flag"),
    ("correctly", r"\bcorrectly\b", "flag"),
    ("incorrectly", r"\bincorrectly\b", "flag"),
    ("fails", r"\bfail(?:s|ed|ing)?\b", "flag"),
    ("succeeds", r"\bsucceed(?:s|ed|ing)?\b", "flag"),
    ("widely regarded", r"\bwidely regarded\b", "flag"),
    ("widely accepted", r"\bwidely accepted\b", "flag"),
    ("generally accepted", r"\bgenerally accepted\b", "flag"),
    ("mainstream", r"\bmainstream\b", "flag"),
    ("notorious", r"\bnotorious(?:ly)?\b", "flag"),
    ("infamous", r"\binfamous(?:ly)?\b", "flag"),
    ("so-called", r"\bso-called\b", "flag"),
    ("controversial", r"\bcontroversial(?:ly)?\b", "flag"),
    ("naive", r"\bna(?:i|ï)ve(?:ly)?\b", "flag"),
    ("sophisticated", r"\bsophisticated\b", "flag"),
    ("compelling", r"\bcompelling(?:ly)?\b", "flag"),
    ("unconvincing", r"\bunconvincing(?:ly)?\b", "flag"),
    ("convincing", r"\bconvincing(?:ly)?\b", "flag"),
    ("the truth is", r"\bthe truth is\b", "flag"),
    ("in fact", r"\bin fact\b", "weak"),
    ("it is clear that", r"\bit is clear that\b", "flag"),
    ("undeniably", r"\bundeniabl[ey]\b", "flag"),
    ("indisputably", r"\bindisputabl[ey]\b", "flag"),
    ("everyone agrees", r"\beveryone agrees\b", "flag"),
    ("no serious", r"\bno serious\b", "flag"),
    ("settled", r"\bsettled\b", "flag"),
]
_WORD_RE = [(label, re.compile(rx, re.IGNORECASE), sev) for label, rx, sev in WORDS]

ATTRIBUTION_MARKERS = [
    "classifies", "classify", "classified", "argues", "argued", "holds", "held",
    "calls", "called", "describes", "described", "according to", "writes", "wrote",
    "says", "said", "claims", "claimed", "objects", "in the words of", "per ",
    "classes", "classed", "treats", "treated", "counts as", "count as",
    "regards", "regarded", "ranks", "ranked", "labels", "labelled", "labeled",
]
_ATTRIB_RE = re.compile(
    "|".join(r"\b" + re.escape(m.rstrip()) + (r"\s" if m.endswith(" ") else r"\b")
             for m in ATTRIBUTION_MARKERS),
    re.IGNORECASE,
)
# Year in parentheses (closing paren optional: sentence splitting may cut it),
# doi:, p./pp. page refs, section sign, markdown link target.
_CITATION_RE = re.compile(
    r"\([^)]*?\b(?:1[5-9]\d\d|20\d\d)[a-z]?\b|doi:|\bpp?\.|§|\]\(",
    re.IGNORECASE,
)

# Sections whose purpose is attribution; documented for context, same rule applies.
ATTRIBUTION_SECTIONS = {
    "classified as a fallacy by", "classified as legitimate by", "critique",
    "reception", "the case for", "the case against", "replies", "objections",
    "interpretations and critique", "descriptive definitions",
}

ALLOW_MARKER_RE = re.compile(r"\s*#\s*lint:\s*allow\s*$", re.IGNORECASE)
_INLINE_CODE_RE = re.compile(r"`[^`]*`")
_QUOTED_RE = re.compile(r"\"[^\"]*\"|“[^”]*”")
# A short *italicised* span is a mention of a word, not a use of it —
# the use/mention convention philosophy already follows ("*fallacy* is a term").
_MENTION_RE = re.compile(r"(?<![*\w])\*(?!\s)[^*\n]{1,40}?(?<!\s)\*(?![*\w])")
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")
_FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")
# Sentence boundary: . ; ? ! followed by space — but not after a lone letter
# or common abbreviation (p. 19, pp. 3-4, cf., e.g., i.e., vs., et al.).
_SENT_SPLIT_RE = re.compile(
    r"(?<!\b[A-Za-z]\.)(?<!\bpp\.)(?<!\bcf\.)(?<!\be\.g\.)(?<!\bi\.e\.)(?<!\bvs\.)(?<!\bal\.)"
    r"(?<=[.;?!])\s+"
)


def _blank(m: re.Match) -> str:
    return " " * (m.end() - m.start())


def _sentences(text: str) -> list[tuple[int, str]]:
    """Yield (offset, sentence) pairs covering the text."""
    out: list[tuple[int, str]] = []
    pos = 0
    for m in _SENT_SPLIT_RE.finditer(text):
        out.append((pos, text[pos:m.start()]))
        pos = m.end()
    out.append((pos, text[pos:]))
    return out


def lint_text(text: str, path: str = "<text>") -> tuple[list[dict[str, Any]], int]:
    """Return (findings, suppressed_by_marker_count) for one markdown document.

    Prose is linted paragraph by paragraph (a paragraph = consecutive
    non-blank prose lines), so a sentence wrapped over several lines keeps its
    attribution marker and its citation token in the same sentence.
    """
    findings: list[dict[str, Any]] = []
    suppressed = 0
    lines = text.splitlines()
    in_frontmatter = False
    in_fence = False
    fence_char = ""
    heading = ""
    # Paragraph accumulator: list of (lineno, cleaned_line, allow_flag)
    para: list[tuple[int, str, bool]] = []

    def flush() -> None:
        nonlocal suppressed
        if not para:
            return
        joined = " ".join(l for _, l, _ in para)
        # Map character offsets of the joined text back to line numbers.
        starts: list[tuple[int, int, bool]] = []
        pos = 0
        for ln, l, allow in para:
            starts.append((pos, ln, allow))
            pos += len(l) + 1
        def locate(off: int) -> tuple[int, bool]:
            ln, allow = starts[0][1], starts[0][2]
            for st, l_no, al in starts:
                if st <= off:
                    ln, allow = l_no, al
            return ln, allow
        for offset, sentence in _sentences(joined):
            for label, rx, sev in _WORD_RE:
                for m in rx.finditer(sentence):
                    before = sentence[: m.start()]
                    after = sentence[m.end():]
                    if _ATTRIB_RE.search(before) or _CITATION_RE.search(after):
                        continue
                    lineno, allow = locate(offset + m.start())
                    if allow:
                        suppressed += 1
                        continue
                    findings.append({
                        "path": path,
                        "line": lineno,
                        "word": m.group(0),
                        "label": label,
                        "severity": sev,
                        "sentence": " ".join(sentence.split()),
                        "section": heading,
                        "attribution_section": heading.strip().lower() in ATTRIBUTION_SECTIONS,
                    })
        para.clear()

    for lineno, raw in enumerate(lines, 1):
        stripped = raw.strip()
        # YAML frontmatter: opens on the very first line only.
        if lineno == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped in ("---", "..."):
                in_frontmatter = False
            continue
        fm = _FENCE_RE.match(raw)
        if fm:
            flush()
            if not in_fence:
                in_fence, fence_char = True, fm.group(1)
            elif fm.group(1) == fence_char:
                in_fence = False
            continue
        if in_fence:
            continue
        hm = _HEADING_RE.match(raw)
        if hm:
            flush()
            heading = hm.group(1)
            continue
        if stripped.startswith(">") or not stripped:
            flush()
            continue
        # A list item or table row starts a new paragraph.
        if re.match(r"^\s*([-*+]|\d+[.)])\s", raw) or stripped.startswith("|"):
            flush()

        allow = bool(ALLOW_MARKER_RE.search(raw))
        line = ALLOW_MARKER_RE.sub(_blank, raw)
        line = _INLINE_CODE_RE.sub(_blank, line)
        line = _QUOTED_RE.sub(_blank, line)
        line = _MENTION_RE.sub(_blank, line)
        para.append((lineno, line, allow))
    flush()
    return findings, suppressed


def collect_files(paths: list[str]) -> list[str]:
    files: list[str] = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = sorted(d for d in dirs if not d.startswith("."))
                for n in sorted(names):
                    if n.lower().endswith(".md"):
                        files.append(os.path.join(root, n))
        elif os.path.isfile(p):
            files.append(p)
        else:
            raise FileNotFoundError(p)
    return files


def format_finding(f: dict[str, Any]) -> str:
    sent = f["sentence"]
    if len(sent) > 120:
        sent = sent[:117] + "..."
    word = f["word"] + (" (weak)" if f["severity"] == "weak" else "")
    section = f["section"] or "(none)"
    return f'{f["path"]}:{f["line"]}: {word} — "{sent}"  [section: {section}]'


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="neutrality-lint.py",
        description="Flag evaluative predicates in the implant's own voice.",
    )
    ap.add_argument("paths", nargs="*", help="markdown files or directories (recursed for *.md)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--words", action="store_true", help="print the word list and exit")
    args = ap.parse_args(argv)

    if args.words:
        for label, rx, sev in WORDS:
            print(f"{label:22} {sev:5} {rx}")
        return 0
    if not args.paths:
        ap.error("give at least one path (or --words)")

    try:
        files = collect_files(args.paths)
    except FileNotFoundError as exc:
        print(f"error: no such file or directory: {exc}", file=sys.stderr)
        return 2

    findings: list[dict[str, Any]] = []
    suppressed = 0
    for path in files:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as exc:
            print(f"error: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        f, s = lint_text(text, path)
        findings.extend(f)
        suppressed += s

    if args.json:
        print(json.dumps({
            "files": len(files),
            "findings": findings,
            "count": len(findings),
            "suppressed": suppressed,
        }, indent=2, ensure_ascii=False))
    else:
        for f in findings:
            print(format_finding(f))
        print(
            f"{len(findings)} finding{'s' if len(findings) != 1 else ''} in {len(files)} "
            f"file{'s' if len(files) != 1 else ''}, {suppressed} suppressed by '# lint: allow'"
        )
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

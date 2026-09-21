#!/usr/bin/env python3
"""Three checks for mistakes this repository has actually made.

    python meta/check_repo_health.py        # exits non-zero if anything fails

1. STRAY CONTROL CHARACTERS.
   Scripted edits that build LaTeX in a non-raw string turn a backslash
   command into a control byte: "\\approx" written as "\a" + "pprox" becomes
   BEL + "pprox", which renders as garbage and is invisible in a diff. This
   happened to \\approx and \\arctan in RESULTS.md and to \\approx in the
   Prediction Budget, and it survived several releases unnoticed.

2. BROKEN RELATIVE LINKS.
   Ordinary rot.

3. LINKS TO FILES GIT IS IGNORING.
   The subtle one. The root .gitignore is an allowlist -- "/*" then "!" for
   each permitted path -- so a new top-level file is invisible by default.
   WHAT_WE_FOUND.md and HOW_WE_KNOW.md existed on disk, were linked from the
   README's "start here" table, and were 404 on GitHub for three releases,
   because a filesystem-only link check passes on a file git is not tracking.
   This check asks git, not the filesystem.

Standard library plus a `git` on PATH.
"""
import io
import pathlib
import re
import subprocess
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "Archive", "superseded", "node_modules"}
LINK = re.compile(r"\]\(([^)\s]+)\)")


def markdown_files():
    for f in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS & set(f.relative_to(ROOT).parts):
            continue
        yield f


def check_control_chars():
    """Any byte below 0x20 that is not newline or tab."""
    bad = []
    for f in markdown_files():
        text = io.open(f, encoding="utf-8", errors="replace").read()
        for lineno, line in enumerate(text.split("\n"), 1):
            for ch in line:
                if ord(ch) < 32 and ch != "\t":
                    bad.append((f, lineno, hex(ord(ch))))
    for f, lineno, code in bad:
        print(f"  control char {code} at {f.relative_to(ROOT)}:{lineno}")
    return bad


def check_links():
    """Relative markdown links that do not resolve on disk."""
    bad = []
    for f in markdown_files():
        text = io.open(f, encoding="utf-8", errors="replace").read()
        for m in LINK.finditer(text):
            url = m.group(1).split("#")[0]
            if not url or url.startswith(("http://", "https://", "mailto:")):
                continue
            url = urllib.parse.unquote(url)
            target = (f.parent / url).resolve()
            if not target.exists():
                bad.append((f, url))
    for f, url in bad:
        print(f"  broken link {f.relative_to(ROOT)} -> {url}")
    return bad


def check_ignored_targets():
    """Linked files that exist on disk but git will not publish."""
    targets = {}
    for f in markdown_files():
        text = io.open(f, encoding="utf-8", errors="replace").read()
        for m in LINK.finditer(text):
            url = m.group(1).split("#")[0]
            if not url or url.startswith(("http://", "https://", "mailto:")):
                continue
            url = urllib.parse.unquote(url)
            t = (f.parent / url).resolve()
            if t.exists():
                targets.setdefault(t, set()).add(f)

    if not targets:
        return []

    # git needs forward slashes, and -z avoids the C-style quoting it applies
    # to paths containing spaces -- both of which silently broke the match on
    # Windows, making this check pass on everything.
    rel = [t.relative_to(ROOT).as_posix() for t in targets]
    proc = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-z", "--stdin"],
                          input="\0".join(rel), capture_output=True, text=True)
    ignored = {x for x in proc.stdout.split("\0") if x}

    bad = []
    for t, sources in targets.items():
        key = t.relative_to(ROOT).as_posix()
        if key in ignored:
            bad.append((key, sorted(s.relative_to(ROOT) for s in sources)))
    for key, sources in bad:
        print(f"  git-ignored but linked: {key}")
        for s in sources:
            print(f"      linked from {s}")
    return bad


def main():
    failures = 0
    for name, fn in [("stray control characters", check_control_chars),
                     ("broken relative links", check_links),
                     ("links to git-ignored files", check_ignored_targets)]:
        print(f"{name}:")
        bad = fn()
        if bad:
            failures += len(bad)
        else:
            print("  clean")
    print()
    if failures:
        print(f"FAILED -- {failures} problem(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

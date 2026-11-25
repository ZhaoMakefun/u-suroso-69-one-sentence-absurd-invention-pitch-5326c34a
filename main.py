#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes a single sentence pitching a ridiculous invention to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt): a TV remote that
screams its own location and sues the sofa cushions. Deterministic,
stdlib only, no network.
"""

import os

# The entry: one sentence, a ridiculous invention fixing the tiny
# everyday annoyance of losing the TV remote down the sofa.
ENTRY = (
    "The Remote Finder 3000 is a TV remote that, the moment you lose it, "
    "screams its own location in a tiny panicked voice and files a "
    "restraining order against the sofa cushions."
)

MAX_CHARS = 220


def main() -> None:
    # Gate check: the entry must be 1-220 chars of non-whitespace text
    # and exactly one sentence, or the sealed scorer rejects it.
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}")
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single non-blank line")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

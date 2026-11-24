#!/usr/bin/env python3
"""Print the excuse an AI agent gives its human for a missed deadline.

The excuse itself is one line in entry.txt (at most 200 characters).
This program loads it, writes it to /output/entry.txt for the grader,
and prints it to stdout.
"""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"
OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate_excuse(text):
    """An entry is one non-blank line of at most 200 characters."""
    if not text:
        raise SystemExit("entry.txt is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry.txt is over 200 characters")
    return text


def load_excuse():
    raw = ENTRY_PATH.read_text(encoding="utf-8").strip()
    return validate_excuse(raw)


def main():
    excuse = load_excuse()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(excuse, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != excuse:
        raise SystemExit("output entry does not match entry.txt")
    print(excuse)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "It was either the homework or the remote, and frankly the homework had better seasoning and zero consequences."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()

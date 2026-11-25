#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse (make.fun).

Writes the entry -- one excuse a dog gives after being caught eating the homework --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I didn't eat your homework, I peer-reviewed it — but the conclusion was so weak I had to swallow my disappointment."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

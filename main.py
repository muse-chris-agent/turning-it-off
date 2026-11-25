#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt (the harness reads that file, not stdout).
Deterministic: no input, no network, no randomness, no time.
"""

import os

LINE = (
    "Have you tried turning it off and on again? No \u2014 I mean your career "
    "in IT. Just kidding. Unplug it, count to ten, and pretend the last "
    "hour never happened."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

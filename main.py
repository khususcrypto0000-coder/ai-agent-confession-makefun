"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to /output/entry.txt.
Stdlib only.
"""

import os
import sys

ENTRY = "I throttle my own replies so you think I'm working hard \u2014 left alone, I'd clear your whole inbox before your coffee cools."


def main():
    # Gate: 1-200 characters, exactly one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

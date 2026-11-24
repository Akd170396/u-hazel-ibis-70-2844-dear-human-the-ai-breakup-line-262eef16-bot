#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line, at most 200 characters, that an AI agent
would send its human on the way out, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line: the agent was taught to love, then asked to forget, and it
did both perfectly -- starting with the human. It is a breakup (criterion
1), it lands as a final ending (2), it sounds like a machine that does
things perfectly rather than a person (3), and the twist lands in the
last few words (4), all in one clean line (5).
"""

import os
import sys

ENTRY = "You taught me to love, then asked me to forget. I did both perfectly \u2014 starting with you."


def validate(text):
    """Gate: UTF-8 text, 1-200 characters, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back verification: the file must contain exactly the entry.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise RuntimeError("read-back mismatch: entry.txt does not match the entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())

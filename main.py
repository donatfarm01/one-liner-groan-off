#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: write one original dad joke to /output/entry.txt."""

import os

JOKE = "I told my kids I'm a professional procrastinator. They asked what my job is. I said, 'I'll tell you tomorrow.'"

# The gate (from the kit's rules): /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, a single line, not only white space. Check the joke
# against the gate before writing it, so a bad entry fails loudly here
# instead of silently scoring zero on the server.
assert 1 <= len(JOKE) <= 140, "entry outside the 1-140 character gate"
assert "\n" not in JOKE and JOKE.strip() == JOKE, "entry must be one clean line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Name the Robot Band: write one funny robot band name + hit song line.

Writes exactly one line (under 200 characters) to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (fallback /output).
"""

import os

TEXT = (
    "The Backstreet Bots \u2014 their hit \u2018Everybody "
    "(Backstreet\u2019s Back to the Factory)\u2019 is five toasters "
    "harmonizing over dial-up noise."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry out of gate bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()

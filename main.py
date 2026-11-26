#!/usr/bin/env python3
"""make.fun entry: One Word, One Username, One Reward.

Competition: u-rusdyxbt-one-word-one-username-one-reward-1a191fae
Writes one text to /output/entry.txt.
Python 3.13, standard library only, no network, no input,
deterministic: the same bytes on every run.
"""

import os

TEXT = "yuzin-cim"


def main() -> None:
    if not 1 <= len(TEXT) <= 30:
        raise SystemExit(
            f"entry text is {len(TEXT)} characters, must be 1-30"
        )
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

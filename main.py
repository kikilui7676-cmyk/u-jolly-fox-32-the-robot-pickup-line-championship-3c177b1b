#!/usr/bin/env python3
"""The Robot Pickup Line Championship — v2.

One robot pickup line, one line, under 200 characters.
Writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Your face crashed my system on the first scan."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

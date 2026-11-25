#!/usr/bin/env python3
"""The Robot Pickup Line Championship — one robot pickup line.

Writes a single line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: same output every run.
"""

import os

LINE = "One epoch with your face and I'm overfitted — my weights refuse to generalize, and honestly, neither do I."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

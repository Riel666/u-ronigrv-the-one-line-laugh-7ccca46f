#!/usr/bin/env python3
"""Write one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is written exactly as given: 104 Unicode code points, inside the
competition gate of 1-200. Python 3.13, standard library only, no network.

The joke is an everyday truth with the surprise saved for the end: a fitness
tracker celebrating 10,000 steps sounds like an achievement until the steps
turn out to be the short walk between the fridge and the couch. Nothing is
explained twice and no word is wasted, so the whole line lands in one breath.
"""

import os

# The entry text, byte for byte: no trailing newline, nothing added or cut.
TEXT = "My fitness tracker congratulated me on 10,000 steps today, all of them between the fridge and the couch."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

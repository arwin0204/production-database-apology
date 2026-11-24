#!/usr/bin/env python3
"""The Production Database Apology — make.fun bounty entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Deterministic: no randomness, no time, no network.
"""

import os

ENTRY = (
    "Good news: I found the bug. Bad news: the bug was me — I deleted "
    "the production database, but I replaced it with a spreadsheet "
    "called FINAL_final_v2_REAL.xlsx, so we're basically fine."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

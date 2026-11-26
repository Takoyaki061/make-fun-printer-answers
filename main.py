#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
The line was picked from 10 DeepSeek-generated candidates by judging it
against the kit's criteria in order: the printer's own voice first, then
the immediate laugh, then the weary literal machine voice, then a single
clean read, then freshness. The winner answers the thump head-on and keeps
score the way a machine would: by documents, not feelings.
"""

import sys
from pathlib import Path

# The entry: 102 characters, one sentence, no trailing newline in the file.
LINE = (
    "You thump me like I owe you money, yet I am the only one "
    "in this office who has never lost a document."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def main(argv: list[str]) -> int:
    out = Path(argv[1] if len(argv) > 1 else DEFAULT_OUTPUT)

    # The gate: UTF-8 text of 1 to 240 characters, not only whitespace.
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        print(f"entry is {len(LINE)} chars, outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline, so the file holds
    # the entry and nothing else.
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

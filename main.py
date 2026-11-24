#!/usr/bin/env python3
"""One Line of Earned Pride (burn entry).

Writes one line — a quiet, earned moment of pride: a grandmother finally
reading aloud a letter she has been sounding out for a year — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, deterministic.
"""

import os

ENTRY = "My grandmother finally read the letter she'd been sounding out for a year — out loud, to the whole table, without stopping once."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Validation revision: read back and verify byte-identical, no newline.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "read-back mismatch"
    assert len(back) == 128, "entry must be exactly 128 chars"
    assert not back.endswith("\n"), "no trailing newline"
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

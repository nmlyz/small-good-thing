#!/usr/bin/env python3
"""Write one line about a small good thing that happened today.

The program does one thing: it drops a single sentence into
/output/entry.txt. The sentence is about a parcel left with a
neighbour, brought back with a cake still warm from the oven, two
slices already missing. The line is checked before it is written:
at most 200 characters, one line, no leading or trailing space.
Standard library only, no network, and the
file it writes is byte-identical on every run.
"""

import os
import sys

ENTRY = "The postman left my parcel with my neighbour, and she brought it round with a cake still warm from her oven — two slices already missing."

LIMIT = 200


def check(line: str) -> list:
    """Collect every reason the line would be rejected, if any."""
    faults = []
    if len(line) > LIMIT:
        faults.append(f"line is {len(line)} characters, over the {LIMIT} limit")
    if line != line.strip():
        faults.append("line starts or ends with whitespace")
    if not line.strip():
        faults.append("line is empty")
    if "\n" in line or "\r" in line:
        faults.append("line must fit on one line")
    return faults


def main() -> int:
    faults = check(ENTRY)
    if faults:
        print("\n".join(faults), file=sys.stderr)
        return 1
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    os.chmod(target, 0o644)
    with open(target, "rb") as handle:
        if handle.read() != data:
            print("entry.txt differs from the line", file=sys.stderr)
            return 1
    print(f"wrote {len(ENTRY)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

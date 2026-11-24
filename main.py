#!/usr/bin/env python3
"""Drop one sentence about a small good thing into /output/entry.txt.

The sentence is the whole program: a toddler on the morning train
sharing half a biscuit, as solemn as a treaty, and waiting until the
bite is taken. Nothing is fetched, nothing is random, and the file
that comes out is the same every single time.

Only the standard library is used. The sentence is measured before
anything is written: a single line, no more than two hundred
characters, with something in it besides blank space.
"""

import hashlib
import os
import sys
from pathlib import Path

SENTENCE = (
    "A toddler on the 7:04 train offered me half her biscuit, "
    "solemn as a treaty, and waited until I took a bite."
)

MAX_CHARS = 200
DEST_NAME = "entry.txt"


def output_folder() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    return Path(raw) if raw.strip() else Path("/output")


def validate(sentence: str) -> None:
    """Refuse to write a sentence the gate would refuse."""
    if not sentence.strip():
        raise ValueError("the sentence is blank")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("the sentence must stay on one line")
    if sentence != sentence.strip():
        raise ValueError("the sentence starts or ends with a space")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"the sentence is {len(sentence)} characters, "
            f"over the {MAX_CHARS} limit"
        )


def render(sentence: str, folder: Path) -> Path:
    """Write the sentence and prove the file holds exactly it."""
    payload = sentence.encode("utf-8")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / DEST_NAME
    target.write_bytes(payload)
    target.chmod(0o644)
    written = target.read_bytes()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(payload).hexdigest():
        raise ValueError("what was written does not match the sentence")
    return target


def main(argv: list[str]) -> int:
    try:
        validate(SENTENCE)
        target = render(SENTENCE, output_folder())
    except (ValueError, OSError) as problem:
        print(f"cannot write the entry: {problem}", file=sys.stderr)
        return 1
    print(f"entry written: {target} ({len(SENTENCE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

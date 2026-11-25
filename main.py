#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the fridge's one-line 3am text message to /output/entry.txt.
The line was chosen by a local rival duel over eight candidates, scored on the
house judge's five published criteria (see DUEL.md). Winner:

    hey. it's 3am. the cheese in here is older than your last relationship
    and still holding this household together better than you are.
"""

from pathlib import Path

ENTRY = (
    "hey. it's 3am. the cheese in here is older than your last relationship "
    "and still holding this household together better than you are."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-140 characters of UTF-8
    # text. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate needs 1-140"
    assert "\n" not in ENTRY, "entry must be a single line"
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts the file's characters (1-140),
    # so the file must hold exactly the line, nothing more.
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

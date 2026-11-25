"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror to /output/entry.txt.

The line: a forensic fact that quietly reframes a death as a murder
committed at home. Concrete detail (the water in his lungs), a withheld
truth (whose bathtub, and who was there), and the last word lands the
blow. No gore, no mirror/doll/basement cliche.
"""

import os

ENTRY = "The autopsy said my brother drowned, but the water in his lungs was from my bathtub."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

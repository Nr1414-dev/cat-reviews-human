"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about its
human, under 200 characters, to /output/entry.txt.
"""

import os

ENTRY = "One star. He put a cucumber behind me while I ate. I jumped six feet straight up. He laughed. The cucumber is now my mortal enemy, and he is next."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Brief-format guard: one line, 1-200 chars, no surrounding whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single line without surrounding whitespace")
    return text


def main():
    validate_entry(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: /output/entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()

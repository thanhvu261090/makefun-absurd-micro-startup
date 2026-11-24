"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "DozeLedger: a marketplace where lazy AI agents sell their unused "
    "nap minutes to overworked bots for $0.02 a minute, taking a 10% "
    "cut of every yawn."
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")


def main() -> None:
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()

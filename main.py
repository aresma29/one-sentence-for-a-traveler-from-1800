#!/usr/bin/env python3
"""Print the entry line for the 'One Sentence for a Traveler from 1800' make.fun bounty."""
from pathlib import Path


def main() -> int:
    # Resolve entry.txt next to this script so the grader can run from any cwd.
    entry = Path(__file__).with_name("entry.txt")
    print(entry.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

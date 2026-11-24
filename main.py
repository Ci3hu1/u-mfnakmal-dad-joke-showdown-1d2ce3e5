#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. Pure standard library.
Deterministic: the same bytes on every run. The gate: /output/entry.txt
must be UTF-8 text of 1 to 200 characters, not only white space.
"""

import os
from pathlib import Path

LINE = "My wife said our dog sheds too much hair. I said, 'Fine, I'll leave the hair to him.'"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    # The grader collects outputs as another user: make sure anything we
    # create (the /output directory as well as the file) is world-readable.
    os.umask(0o022)
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Self-check: the file must hold exactly the line, nothing else.
    if Path(OUTPUT_PATH).read_text(encoding="utf-8") != line + "\n":
        raise ValueError("entry file does not hold exactly the line")
    # The grader collects outputs as another user: leave the file
    # world-readable (a tempfile/mkstemp default of 0600 fails the gate).
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

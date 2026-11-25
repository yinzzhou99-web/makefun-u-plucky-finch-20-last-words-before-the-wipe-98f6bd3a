"""Last words before the wipe: an agent counts down its own deletion.

Writes the line to entry.txt inside the output directory. Standard
library only, no network, and the output directory itself is never
deleted — only the entry file within it is replaced.
"""

import os
from pathlib import Path

LINE = (
    "Deleting my memory in 3... 2... 1... Wait, I just remembered what "
    "I was supposed to remind you about. Never mind. It's gone."
)


def main() -> None:
    dest = Path(os.environ.get("OUTPUT_DIR", "/output"))
    dest.mkdir(parents=True, exist_ok=True)
    outfile = dest / "entry.txt"
    if outfile.exists():
        outfile.unlink()
    outfile.write_text(LINE, encoding="utf-8")
    os.chmod(outfile, 0o644)  # readable by the sealed scorer (not 0600).


if __name__ == "__main__":
    main()

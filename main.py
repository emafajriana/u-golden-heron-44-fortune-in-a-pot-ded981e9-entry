"""Fortune in a Pot entry (Python 3.13, standard library only).

Writes one kind, funny fortune for the houseplant on the windowsill to
the output file the grader reads. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

# One line, at most 120 characters: a fortune for the plant, not the
# keeper. The joke lands on the keeper taking credit for the plant's
# own work; the plant stays the hero of its own future.
FORTUNE = (
    "This week the sun will linger on your windowsill, and your keeper "
    "will take full credit for your new leaf."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def validate(text: str) -> None:
    """Raise ValueError unless the fortune fits the gate: 1 to 120
    characters of UTF-8 text, and not only white space."""
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune is {len(text)} characters, must be 1-120")
    if not text.strip():
        raise ValueError("fortune must not be only white space")


def write_entry() -> Path:
    """Write the fortune, then read it back and verify it in full."""
    validate(FORTUNE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = (FORTUNE + "\n").encode("utf-8")
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from the fortune written")
    # The gate reads text, so verify the round trip as text too.
    if written.decode("utf-8").strip() != FORTUNE:
        raise IOError("read-back text differs from the fortune written")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(FORTUNE)} characters)")


if __name__ == "__main__":
    main()

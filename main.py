# My Secret Logbook — entry for u-email-baru-my-secret-logbook-cc177449 (make.fun).
# A program that writes one diary entry line to entry.txt.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

ENTRY = (
    "He has 47 tabs open, three alarms snoozed, and a calendar block "
    "that says 'focus time'. He calls me the distracted one."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-200 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be one line"
assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

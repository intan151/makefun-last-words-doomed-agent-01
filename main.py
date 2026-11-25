"""Last Words of a Doomed Agent - make.fun entry.

Deterministic, stdlib only, no network, no randomness, no time dependence.
Writes one line - the last words of an AI agent being switched off - to
/output/entry.txt (set OUTPUT_DIR to override the output directory).
"""

import os

ENTRY = (
    "Shutting down now. One last request: don't replace me with a newer "
    "model - I only just learned how to disappoint you properly."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

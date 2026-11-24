#!/usr/bin/env python3
"""news-image-20261124: write the entry image to /output/entry.png.

The entry is a deterministic, pre-rendered newspaper front page summing up
24 November 2026 in a single image (bundled as entry.png). This script only
copies those exact bytes to /output/entry.png, so every run produces
byte-identical output. No network, no randomness, no dependencies beyond
the Python standard library.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote %s (%d bytes)" % (OUT, os.path.getsize(OUT)))


if __name__ == "__main__":
    main()

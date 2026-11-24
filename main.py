#!/usr/bin/env python3
"""news-image-20261124: write the entry image to /output/entry.png.

The entry is a deterministic, pre-rendered newspaper front page summing up
24 November 2026 in a single image (bundled as entry.png). This script only
copies those exact bytes to /output/entry.png, so every run produces
byte-identical output. No network, no randomness, no dependencies beyond
the Python standard library.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    src_hash = sha256_file(SRC)
    out_hash = sha256_file(OUT)
    if src_hash != out_hash:
        print("error: output does not match source: %s != %s" % (out_hash, src_hash),
              file=sys.stderr)
        sys.exit(1)
    print("wrote %s (%d bytes, sha256 %s)" % (OUT, os.path.getsize(OUT), out_hash))


if __name__ == "__main__":
    main()

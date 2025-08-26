#!/usr/bin/env python3
import sys
from pathlib import Path

paths = sys.argv[1:] or ['.']
for p in paths:
    for f in Path(p).rglob('*.md'):
        s = f.read_text(encoding='utf-8')
        new = '\n'.join([line.rstrip() for line in s.splitlines()]) + '\n'
        if new != s:
            f.write_text(new, encoding='utf-8')
            print(f"Trimmed: {f}")

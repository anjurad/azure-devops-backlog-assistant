#!/usr/bin/env python3
"""Minimal Markdown linter: checks for unmatched fences, trailing spaces, and extremely long lines.
Usage: python .github/bin/md_lint.py [paths...]
"""
import sys
from pathlib import Path

paths = sys.argv[1:] or ['.']
errors = []
for p in paths:
    for f in Path(p).rglob('*.md'):
        text = f.read_text(encoding='utf-8')
        # check fence matching: count of ``` occurrences should be even
        fence_count = text.count('```')
        if fence_count % 2 != 0:
            errors.append(f"Unmatched triple-backtick fences in {f}")
        # check for lines starting/ending with more than 3 backticks (rare)
        if '````' in text:
            errors.append(f"Contains 4-backtick fences in {f} — prefer triple backticks: {f}")
        # trailing spaces
        for i, line in enumerate(text.splitlines(), start=1):
            if line.endswith(' '):
                errors.append(f"Trailing space in {f}:{i}")
            if len(line) > 200:
                errors.append(f"Long line (>200) in {f}:{i} ({len(line)} chars)")

if errors:
    print('\n'.join(errors))
    sys.exit(2)
print('OK')

#!/usr/bin/env python3
"""Render the Asterisk sound map from the reviewed manifest."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
entries = json.loads((root / 'manifest' / 'asterisk-core-sounds-sv-manifest.json').read_text())['entries']
lines = ['; Core Asterisk Sounds in Swedish', '; UTF-8', '']
for entry in entries:
    filename = entry['filename'].removesuffix('.wav')
    lines.append(f'{filename}: {entry["script"]}')
(root / 'core-sounds-sv.txt').write_text('\n'.join(lines) + '\n')

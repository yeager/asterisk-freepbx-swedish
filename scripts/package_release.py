#!/usr/bin/env python3
"""Validate and package one complete Swedish Asterisk core-sound voice."""
import argparse
import gzip
import hashlib
import json
import tarfile
import wave
from pathlib import Path

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--voice', choices=('anton', 'louise'), required=True)
parser.add_argument('--source', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()

manifest = json.loads((root / 'manifest' / 'asterisk-core-sounds-sv-manifest.json').read_text())['entries']
filenames = [entry['filename'] for entry in manifest]
missing = [name for name in filenames if not (args.source / name).is_file()]
extra = [path.relative_to(args.source).as_posix() for path in args.source.rglob('*.wav')
         if path.relative_to(args.source).as_posix() not in set(filenames)]
if missing or extra:
    raise SystemExit(f'Wrong file map: missing={missing[:3]}, extra={extra[:3]}')

for filename in filenames:
    with wave.open(str(args.source / filename)) as audio:
        format_ok = (audio.getnchannels(), audio.getsampwidth(), audio.getframerate(), audio.getcomptype()) == (1, 2, 48000, 'NONE')
        if not format_ok or not audio.getnframes():
            raise SystemExit(f'Invalid WAV: {filename}')

args.output.mkdir(parents=True, exist_ok=True)
archive = args.output / f'asterisk-core-sounds-sv-{args.voice}-1.6.1.tar.gz'
with archive.open('wb') as raw:
    with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as compressed:
        with tarfile.open(mode='w', fileobj=compressed, format=tarfile.PAX_FORMAT) as package:
            for filename in filenames:
                package.add(args.source / filename, arcname=filename, recursive=False)
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
(archive.with_suffix(archive.suffix + '.sha256')).write_text(f'{digest}  {archive.name}\n')
print(f'Created {archive} with {len(filenames)} WAV files')

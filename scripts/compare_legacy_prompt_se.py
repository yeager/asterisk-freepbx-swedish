#!/usr/bin/env python3
"""Compare the 2006 asterisk-prompt-se sound tree with the Anton manifest."""
import argparse
import collections
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--legacy-sounds', type=Path, required=True,
                    help='The extracted sounds/ directory from asterisk-prompt-se')
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()

manifest = json.loads((root / 'manifest' / 'asterisk-core-sounds-sv-manifest.json').read_text())['entries']
anton = {entry['filename'].removesuffix('.wav') for entry in manifest}
legacy = {}
for path in args.legacy_sounds.rglob('*.gsm'):
    parts = list(path.relative_to(args.legacy_sounds).with_suffix('').parts)
    # The old package puts the language code either immediately below sounds/
    # or below an application subdirectory such as digits/ or letters/.
    if parts[0] == 'se':
        name = Path(*parts[1:]).as_posix()
    elif len(parts) > 1 and parts[1] == 'se':
        name = Path(parts[0], *parts[2:]).as_posix()
    else:
        name = Path(*parts).as_posix()
    legacy.setdefault(name, []).append(path.relative_to(args.legacy_sounds).as_posix())

legacy_names = set(legacy)
missing = sorted(legacy_names - anton)
anton_only = sorted(anton - legacy_names)
categories = collections.Counter(name.split('/', 1)[0] if '/' in name else 'root' for name in missing)
report = {
    'legacy_package': 'asterisk-prompt-se 1.045 (2006)',
    'comparison_policy': 'Compare normalized filename paths without the .gsm/.wav extension; retain old application subdirectories.',
    'legacy_unique_files': len(legacy_names),
    'anton_files': len(anton),
    'shared_files': len(legacy_names & anton),
    'missing_in_anton_count': len(missing),
    'missing_in_anton_by_category': dict(sorted(categories.items())),
    'missing_in_anton': missing,
    'anton_only_count': len(anton_only),
    'anton_only': anton_only,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'Legacy={len(legacy_names)}, Anton={len(anton)}, shared={len(legacy_names & anton)}, missing={len(missing)}')

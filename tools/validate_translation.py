"""Validate French coverage against the installed upstream mod (read-only)."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

PROJECT = Path(__file__).resolve().parents[1]
MOD = PROJECT / 'Contents/mods/batman_ArtelManufactoryFR'
SOURCE = Path(r'D:\SteamLibrary\steamapps\workshop\content\108600\3794133594\mods\ArtelManufactory\42\media\lua\shared\Translate\EN')


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate key: {key}')
        result[key] = value
    return result


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=no_duplicates)


def markers(value):
    return Counter(re.findall(r'%[1-9]|%%|%[-+0-9.]*[sdf]|<[^>]+>|\n|\\n', value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=SOURCE)
    args = parser.parse_args()
    target = MOD / '42.21/media/lua/shared/Translate/FR'
    errors = []
    total = 0
    unchanged = []
    expected = {p.name for p in args.source.glob('*.json') if p.name != 'language.json'}
    manifest = read(PROJECT / 'source-manifest.json')
    for name, digest in manifest['source_sha256'].items():
        path = args.source / name
        if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            print(f'UPSTREAM CHANGED: {name}; review modified texts even if keys still match.')
    actual = {p.name for p in target.glob('*.json')}
    if actual != expected:
        errors.append(f'Files: missing={expected-actual}, extra={actual-expected}')
    for name in sorted(expected & actual):
        source, french = read(args.source / name), read(target / name)
        if list(source) != list(french):
            errors.append(f'{name}: key/order mismatch, missing={source.keys()-french.keys()}, extra={french.keys()-source.keys()}')
        for key in source.keys() & french.keys():
            if not isinstance(french[key], str) or not french[key].strip():
                errors.append(f'{name}:{key}: empty or non-string value')
            elif markers(source[key]) != markers(french[key]):
                errors.append(f'{name}:{key}: markers {markers(source[key])} != {markers(french[key])}')
            if source[key] == french[key]:
                unchanged.append(f'{name}:{key}={french[key]}')
        total += len(french)
        print(f'{name}: {len(french)} keys')
    info = (MOD / '42.21/mod.info').read_text(encoding='utf-8')
    for line in ('id=batman_ArtelManufactoryFR', 'require=\\ArtelManufactory', 'loadModAfter=ArtelManufactory', 'versionMin=42.21'):
        if line not in info.splitlines():
            errors.append(f'Missing metadata: {line}')
    if not (MOD / 'common').is_dir():
        errors.append('Missing common directory')
    if list(MOD.rglob('*.lua')):
        errors.append('Unexpected Lua gameplay files')
    print(f'Total: {total} keys; {len(unchanged)} identical values (review proper names and shared terminology).')
    for entry in unchanged:
        print(f'IDENTICAL: {entry}')
    for error in errors:
        print(f'ERROR: {error}')
    print('PASS' if not errors else 'FAIL')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())

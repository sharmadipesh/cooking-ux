#!/usr/bin/env python3
"""Build the portable ZIP or check that an existing ZIP matches the source files."""
import argparse
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'__pycache__', '.DS_Store', '.git', '.venv', '.pytest_cache'}


def source_files(root):
    files = {}
    for file in sorted(root.rglob('*')):
        relative = file.relative_to(root)
        if any(part in IGNORED for part in relative.parts) or file.suffix in {'.pyc', '.pyo'}:
            continue
        if file.is_symlink():
            raise ValueError('Package symlinks are not supported: ' + str(relative))
        if file.is_file():
            files[root.name + '/' + relative.as_posix()] = file
    return files


def build_archive(root, output):
    files = source_files(root)
    # Use stable metadata so unchanged packages produce identical ZIP bytes.
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, file in files.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file.read_bytes())


def check_archive(root, output):
    errors = []
    expected = source_files(root)
    try:
        with zipfile.ZipFile(output) as archive:
            if archive.testzip() is not None:
                return ['Archive CRC check failed']
            names = archive.namelist()
            if len(names) != len(set(names)):
                errors.append('Archive has duplicate member names')
            for name in sorted(set(expected) - set(names)):
                errors.append('Missing archive member: ' + name)
            for name in sorted(set(names) - set(expected)):
                errors.append('Unexpected archive member: ' + name)
            for name in sorted(set(expected) & set(names)):
                if archive.read(name) != expected[name].read_bytes():
                    errors.append('Changed content: ' + name)
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        errors.append('Cannot read archive: ' + str(exc))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify without rebuilding')
    parser.add_argument('--output', type=Path, default=ROOT.parent / (ROOT.name + '.zip'))
    args = parser.parse_args()
    try:
        if not args.check:
            build_archive(ROOT, args.output)
        errors = check_archive(ROOT, args.output)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    for error in errors:
        print('FAIL: ' + error, file=sys.stderr)
    if errors:
        return 1
    print('PASS: ZIP member set, CRC, and bytes match the package')
    return 0


if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(errors='backslashreplace')
    sys.exit(main())

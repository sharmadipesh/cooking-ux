#!/usr/bin/env python3
"""Validate package integrity offline; optionally GET public source URLs.

This does not evaluate agent behavior, scientific validity, or WCAG conformance.
"""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['Definition', 'Core idea', 'When to use it', 'Practical UI applications',
          'Implementation guidance', 'Good example', 'Bad example',
          'Trade-offs and limitations', 'Related laws', 'Source']
CATEGORIES = ['visual-hierarchy-and-perception', 'cognitive-load-and-decision-making',
              'interaction-and-feedback', 'psychology-and-mental-models']


def anchor(text):
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')


def load_manifest(root):
    """Read the release's source evidence and reject incomplete records clearly."""
    manifest = json.loads((root / 'tests/source-manifest.json').read_text(encoding='utf-8'))
    if not isinstance(manifest, dict):
        raise ValueError('expected an object')
    for key in ('verified_date', 'inventory_source'):
        if not isinstance(manifest.get(key), str) or not manifest[key]:
            raise ValueError('missing or invalid ' + key)
    for key in ('concepts', 'articles'):
        if not isinstance(manifest.get(key), list):
            raise ValueError('missing or invalid ' + key)
        for row in manifest[key]:
            if not isinstance(row, dict):
                raise ValueError(key + ' records must be objects')
            if not isinstance(row.get('url'), str) or not row['url'].startswith('https://'):
                raise ValueError(key + ' record needs an HTTPS source URL')
            if row.get('status') != 200 or not isinstance(row.get('sha256'), str) or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
                raise ValueError(key + ' record needs status 200 and a SHA256 hash')
            if key == 'concepts' and (not isinstance(row.get('name'), str) or not row['name']):
                raise ValueError('concept record needs a name')
    return manifest


def validate(root=ROOT):
    errors = []
    required = ['SKILL.md', 'README.md', 'LICENSE', 'references/ux-laws-index.md',
                'references/source-links.md', 'references/related-concepts.md',
                'references/usability-review-checklist.md', 'tests/source-manifest.json',
                'tests/test-prompts.md', 'tests/expected-behaviors.md',
                'workflows/design-from-scratch.md', 'workflows/ui-audit.md',
                'workflows/improve-existing-ui.md', 'workflows/frontend-implementation.md',
                'examples/good-and-bad-design-decisions.md', 'examples/ui-review-example.md',
                'examples/implementation-example.md']
    required += ['references/' + c + '.md' for c in CATEGORIES]
    for name in required:
        if not (root / name).is_file():
            errors.append('Missing required file: ' + name)
    if errors:
        return errors
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    if not front:
        errors.append('Missing YAML frontmatter')
    else:
        metadata = dict(re.findall(r'^(name|description): (.+)$', front.group(1), re.M))
        name = metadata.get('name', '')
        if name != root.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append('Invalid or mismatched skill name')
        if not 1 <= len(metadata.get('description', '')) <= 1024:
            errors.append('Invalid skill description')
    if len(skill.split()) > 1500:
        errors.append('Entrypoint exceeds package context budget (1500 words)')
    try:
        manifest = load_manifest(root)
    except (OSError, ValueError) as exc:
        return errors + ['Invalid source manifest: ' + str(exc)]
    concepts = manifest['concepts']
    if len(concepts) != 30 or len({r['url'] for r in concepts}) != 30:
        errors.append('Expected 30 unique verified concepts in this release')
    if len(manifest['articles']) != 8:
        errors.append('Expected 8 public articles in this release')
    definitions = {}
    for category in CATEGORIES:
        text = (root / 'references' / (category + '.md')).read_text(encoding='utf-8')
        for section in re.split(r'^## ', text, flags=re.M)[1:]:
            name = section.splitlines()[0]
            if name in definitions:
                errors.append('Duplicate concept: ' + name)
            definitions[name] = section
            for field in FIELDS:
                if not re.search(r'^- \*\*' + re.escape(field) + r':\*\* \S', section, re.M):
                    errors.append(name + ': missing nonempty ' + field)
    if set(definitions) != {r['name'] for r in concepts}:
        errors.append('Definitions do not exactly match verified inventory')
    index = (root / 'references/ux-laws-index.md').read_text(encoding='utf-8')
    for row in concepts:
        if row['status'] != 200 or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
            errors.append('Invalid source evidence: ' + row['name'])
        if row['url'] not in definitions.get(row['name'], '') or row['url'] not in index:
            errors.append('Missing/mismatched attribution: ' + row['name'])
    for testfile in ['tests/test-prompts.md', 'tests/expected-behaviors.md']:
        ids = re.findall(r'^## T(\d+):', (root / testfile).read_text(encoding='utf-8'), re.M)
        if ids != [str(n) for n in range(1, 8)]:
            errors.append('Expected T1–T7 exactly once and in order: ' + testfile)
    for file in root.rglob('*.md'):
        text = file.read_text(encoding='utf-8')
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'https?://', link):
                continue
            path, _, fragment = link.partition('#')
            target = (file.parent / unquote(path)).resolve() if path else file.resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append('Local link escapes package: ' + str(file.relative_to(root)) + ': ' + link)
            elif not target.is_file():
                errors.append('Broken local link: ' + str(file.relative_to(root)) + ': ' + link)
            elif fragment:
                headings = re.findall(r'^#{1,6} (.+)$', target.read_text(encoding='utf-8'), re.M)
                if unquote(fragment) not in [anchor(h) for h in headings]:
                    errors.append('Broken heading link: ' + str(file.relative_to(root)) + ': ' + link)
    return errors


def check_url(url):
    try:
        with urlopen(Request(url, headers={'User-Agent': 'UXSkillSourceCheck/1.0'}), timeout=30) as response:
            body = response.read()
            return {'url': url, 'status': response.status, 'final_url': response.url,
                    'sha256': hashlib.sha256(body).hexdigest()}
    except Exception as exc:
        return {'url': url, 'error': str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--online', action='store_true', help='Also GET external source links')
    args = parser.parse_args()
    errors = validate()
    if args.online and not errors:
        manifest = load_manifest(ROOT)
        urls = {manifest['inventory_source']}
        urls.update(r['url'] for r in manifest['concepts'] + manifest['articles'])
        for file in ROOT.rglob('*.md'):
            urls.update(u.rstrip('.,;:') for u in re.findall(r'https?://[^\s)<>|`]+', file.read_text(encoding='utf-8')))
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(check_url, sorted(urls)))
        print(json.dumps({'remote_checks': results}, ensure_ascii=False, indent=2))
        errors.extend('Remote failure: ' + r['url'] + ': ' + r.get('error', str(r.get('status')))
                      for r in results if r.get('status') != 200)
    for error in errors:
        print('FAIL: ' + error, file=sys.stderr)
    if errors:
        return 1
    print('PASS: package structure, 30 complete concept entries, attribution coverage, local links/anchors, seven scenario rubrics, and entrypoint budget')
    print('NOTE: structural checks do not execute behavioral scenarios or establish UX outcomes.')
    return 0


if __name__ == '__main__':
    # Keep diagnostics printable even on terminals with legacy encodings.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(errors='backslashreplace')
    sys.exit(main())

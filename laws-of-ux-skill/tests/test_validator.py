"""Regression checks for portable package integrity; no network or third-party modules."""
import importlib.util
from pathlib import Path
import os
import subprocess
import sys
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / ROOT.name
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__', 'node_modules', 'test-results', 'playwright-report'))

    def tearDown(self):
        self.temp.cleanup()

    def test_release_is_consistent(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_definition_guidance_is_detected(self):
        file = self.root / 'references/interaction-and-feedback.md'
        file.write_text(file.read_text(encoding='utf-8').replace('- **Implementation guidance:**', '- **Omitted:**', 1), encoding='utf-8')
        self.assertTrue(any('missing nonempty Implementation guidance' in e for e in validator.validate(self.root)))

    def test_source_mismatch_is_detected(self):
        file = self.root / 'references/interaction-and-feedback.md'
        file.write_text(file.read_text(encoding='utf-8').replace('https://lawsofux.com/doherty-threshold/', 'https://example.com/unknown/', 1), encoding='utf-8')
        self.assertTrue(any('Missing/mismatched attribution' in e for e in validator.validate(self.root)))

    def test_broken_reference_anchor_is_detected(self):
        file = self.root / 'SKILL.md'
        file.write_text(file.read_text(encoding='utf-8') + '\n[Broken](references/ux-laws-index.md#does-not-exist)\n', encoding='utf-8')
        self.assertTrue(any('Broken heading link' in e for e in validator.validate(self.root)))

    def test_missing_scenario_is_detected(self):
        file = self.root / 'tests/test-prompts.md'
        file.write_text(file.read_text(encoding='utf-8').replace('## T7:', '## Removed:'), encoding='utf-8')
        self.assertTrue(any('Expected T1–T7' in e for e in validator.validate(self.root)))

    def test_missing_workflow_is_detected(self):
        (self.root / 'workflows/ui-audit.md').unlink()
        self.assertTrue(any('Missing required file' in e for e in validator.validate(self.root)))


    def test_missing_version_metadata_is_detected(self):
        file = self.root / 'SKILL.md'
        file.write_text(file.read_text(encoding='utf-8').replace('  version: "', '  release: "', 1), encoding='utf-8')
        self.assertTrue(any('metadata.version' in e for e in validator.validate(self.root)))

    def test_non_utf8_locale_can_validate_package(self):
        env = dict(os.environ, LC_ALL='C', PYTHONUTF8='0', PYTHONCOERCECLOCALE='0')
        result = subprocess.run([sys.executable, '-B', str(self.root / 'scripts/validate.py')],
                                env=env, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode('ascii', errors='replace'))

    def test_malformed_manifest_returns_diagnostic(self):
        (self.root / 'tests/source-manifest.json').write_text('{bad json', encoding='utf-8')
        self.assertTrue(any('Invalid source manifest' in e for e in validator.validate(self.root)))

    def test_incomplete_manifest_returns_diagnostic(self):
        (self.root / 'tests/source-manifest.json').write_text('{}', encoding='utf-8')
        self.assertTrue(any('Invalid source manifest' in e for e in validator.validate(self.root)))


    def test_optional_browser_dependencies_are_not_skill_content(self):
        dependency = self.root / 'tests/browser/node_modules/example'
        dependency.mkdir(parents=True)
        (dependency / 'README.md').write_text('[Unrelated](missing.md)', encoding='utf-8')
        self.assertEqual(validator.validate(self.root), [])


if __name__ == '__main__':
    unittest.main()

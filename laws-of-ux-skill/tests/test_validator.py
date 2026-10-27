"""Regression checks for portable package integrity; no network or third-party modules."""
import importlib.util
from pathlib import Path
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
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def test_release_is_consistent(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_definition_guidance_is_detected(self):
        file = self.root / 'references/interaction-and-feedback.md'
        file.write_text(file.read_text().replace('- **Implementation guidance:**', '- **Omitted:**', 1))
        self.assertTrue(any('missing nonempty Implementation guidance' in e for e in validator.validate(self.root)))

    def test_source_mismatch_is_detected(self):
        file = self.root / 'references/interaction-and-feedback.md'
        file.write_text(file.read_text().replace('https://lawsofux.com/doherty-threshold/', 'https://example.com/unknown/', 1))
        self.assertTrue(any('Missing/mismatched attribution' in e for e in validator.validate(self.root)))

    def test_broken_reference_anchor_is_detected(self):
        file = self.root / 'SKILL.md'
        file.write_text(file.read_text() + '\n[Broken](references/ux-laws-index.md#does-not-exist)\n')
        self.assertTrue(any('Broken heading link' in e for e in validator.validate(self.root)))

    def test_missing_scenario_is_detected(self):
        file = self.root / 'tests/test-prompts.md'
        file.write_text(file.read_text().replace('## T7:', '## Removed:'))
        self.assertTrue(any('Expected T1–T7' in e for e in validator.validate(self.root)))

    def test_missing_workflow_is_detected(self):
        (self.root / 'workflows/ui-audit.md').unlink()
        self.assertTrue(any('Missing required file' in e for e in validator.validate(self.root)))


if __name__ == '__main__':
    unittest.main()

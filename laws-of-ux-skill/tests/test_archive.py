"""Check that the shareable archive stays in sync with the portable folder."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package', ROOT / 'scripts/package.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / ROOT.name
        self.root.mkdir()
        (self.root / 'SKILL.md').write_text('# Skill\n', encoding='utf-8')
        self.archive = Path(self.temp.name) / 'skill.zip'

    def tearDown(self):
        self.temp.cleanup()

    def test_round_trip_excludes_generated_cache(self):
        cache = self.root / '__pycache__'
        cache.mkdir()
        (cache / 'generated.pyc').write_bytes(b'cache')
        package.build_archive(self.root, self.archive)
        self.assertEqual(package.check_archive(self.root, self.archive), [])
        import zipfile
        with zipfile.ZipFile(self.archive) as z:
            self.assertEqual(z.namelist(), [self.root.name + '/SKILL.md'])

    def test_stale_contents_are_detected(self):
        package.build_archive(self.root, self.archive)
        (self.root / 'SKILL.md').write_text('# Changed\n', encoding='utf-8')
        self.assertTrue(any('Changed content' in e for e in package.check_archive(self.root, self.archive)))

    def test_added_file_requires_archive_rebuild(self):
        package.build_archive(self.root, self.archive)
        (self.root / 'README.md').write_text('# New\n', encoding='utf-8')
        self.assertTrue(any('Missing archive member' in e for e in package.check_archive(self.root, self.archive)))

    def test_missing_archive_returns_diagnostic(self):
        self.assertTrue(any('Cannot read archive' in e for e in package.check_archive(self.root, self.archive)))


if __name__ == '__main__':
    unittest.main()

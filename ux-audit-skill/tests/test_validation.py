"""Report traceability and portable-package regression checks; no external packages."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('audit_validator',ROOT/'scripts/validate.py')
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class ReportTests(unittest.TestCase):
    def setUp(self):
        self.report=json.loads((ROOT/'examples/report.json').read_text(encoding='utf-8'))

    def test_example_and_package_are_consistent(self):
        self.assertEqual(validator.validate_report(self.report),[])
        self.assertEqual(validator.validate_package(ROOT),[])

    def test_unknown_evidence_is_rejected(self):
        self.report['findings'][0]['evidence_ids']=['E-NOT-CAPTURED']
        self.assertTrue(any('unknown evidence' in e for e in validator.validate_report(self.report)))

    def test_missing_priority_reason_is_rejected(self):
        del self.report['findings'][0]['priority_reason']
        self.assertTrue(any('priority_reason' in e for e in validator.validate_report(self.report)))

    def test_severity_and_priority_have_distinct_types(self):
        self.report['findings'][0]['priority']='Major'
        self.assertTrue(any('priority' in e for e in validator.validate_report(self.report)))

    def test_duplicate_evidence_is_rejected(self):
        self.report['evidence'].append(copy.deepcopy(self.report['evidence'][0]))
        self.assertTrue(any('duplicate evidence' in e for e in validator.validate_report(self.report)))

    def test_unassessed_dimensions_remain_explicit(self):
        self.report['coverage'].pop()
        self.assertTrue(any('coverage' in e for e in validator.validate_report(self.report)))

    def test_invalid_container_returns_diagnostic(self):
        self.assertTrue(validator.validate_report([]))

    def test_no_findings_can_be_valid_with_clear_scope(self):
        self.report['findings']=[]
        self.assertEqual(validator.validate_report(self.report),[])

    def test_malformed_enum_returns_diagnostic(self):
        self.report['findings'][0]['priority']=[]
        self.report['coverage'][0]['status']=[]
        self.assertTrue(validator.validate_report(self.report))

class PackageTests(unittest.TestCase):
    def test_missing_version_metadata_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/ROOT.name
            shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__','node_modules','test-results'))
            skill=root/'SKILL.md'
            skill.write_text(skill.read_text(encoding='utf-8').replace('  version: "','  release: "',1),encoding='utf-8')
            self.assertTrue(any('metadata.version' in e for e in validator.validate_package(root)))

if __name__=='__main__':
    unittest.main()

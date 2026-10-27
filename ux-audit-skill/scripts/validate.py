#!/usr/bin/env python3
"""Check skill integrity and optional JSON audit-report structure, not UX truth."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
DIMENSIONS=['Usability and task clarity','Accessibility','Visual hierarchy and readability','Consistency',
 'Navigation and information architecture','Journey and flow','Interaction and system feedback',
 'Responsive and content resilience','Friction and cognitive load','Error prevention and recovery','Trust and user control']
IGNORED={'node_modules','__pycache__','.git','.venv','test-results'}
COVERAGE={'Inspected','Partial','Not assessed','Out of scope'}


def nonempty(value):
    return isinstance(value,str) and bool(value.strip())


def validate_report(report):
    errors=[]
    if not isinstance(report,dict):return ['Report must be an object']
    scope=report.get('scope')
    if not isinstance(scope,dict):errors.append('Missing scope object')
    else:
        for key in ['source_type','task','audience']:
            if not nonempty(scope.get(key)):errors.append('Missing scope '+key)
        for key in ['inspected','not_assessed','limitations']:
            if not isinstance(scope.get(key),list) or any(not nonempty(v) for v in scope.get(key,[])):
                errors.append('Invalid scope '+key+' list')
    evidence=report.get('evidence')
    if not isinstance(evidence,list):errors.append('Missing evidence list');evidence=[]
    ids=set()
    for row in evidence:
        if not isinstance(row,dict):errors.append('Evidence must be an object');continue
        for key in ['id','locator','basis','state','note']:
            if not nonempty(row.get(key)):errors.append('Missing evidence '+key)
        eid=row.get('id')
        if isinstance(eid,str):
            if eid in ids:errors.append('duplicate evidence '+eid)
            ids.add(eid)
        if row.get('basis') not in ['Observed','Supplied','Code inference']:
            errors.append('Invalid evidence basis')
    coverage=report.get('coverage')
    if not isinstance(coverage,list):errors.append('Missing coverage list');coverage=[]
    dimensions=[]
    for row in coverage:
        if not isinstance(row,dict):errors.append('Invalid coverage row');continue
        dimensions.append(row.get('dimension'))
        if not isinstance(row.get('status'),str) or row.get('status') not in COVERAGE or not nonempty(row.get('reason')):
            errors.append('Invalid coverage status/reason')
    if len(dimensions)!=len(DIMENSIONS) or any(dimensions.count(d)!=1 for d in DIMENSIONS):
        errors.append('coverage must explicitly include each audit dimension once')
    findings=report.get('findings')
    if not isinstance(findings,list):errors.append('Missing findings list');findings=[]
    finding_ids=set()
    fields=['id','title','location','observation','impact','severity_reason','priority_reason',
            'confidence_reason','recommendation','suggested_pattern','acceptance_check']
    for row in findings:
        if not isinstance(row,dict):errors.append('Finding must be an object');continue
        label=row.get('id') if nonempty(row.get('id')) else 'Finding'
        for key in fields:
            if not nonempty(row.get(key)):errors.append(str(label)+': missing '+key)
        if isinstance(row.get('id'),str):
            if row['id'] in finding_ids:errors.append('duplicate finding '+row['id'])
            finding_ids.add(row['id'])
        for key,allowed in [('severity',{'Critical','Major','Moderate','Minor'}),('priority',{'P0','P1','P2','P3'}),
                            ('confidence',{'High','Medium','Low'}),('kind',{'observed issue','design risk','hypothesis'})]:
            if not isinstance(row.get(key),str) or row.get(key) not in allowed:errors.append(str(label)+': invalid '+key)
        links=row.get('evidence_ids')
        if not isinstance(links,list) or not links:errors.append(str(label)+': missing evidence_ids')
        else:
            for eid in links:
                if not isinstance(eid,str) or eid not in ids:errors.append(str(label)+': unknown evidence '+str(eid))
        if not isinstance(row.get('assumptions'),list) or any(not nonempty(v) for v in row.get('assumptions',[])):
            errors.append(str(label)+': invalid assumptions list')
    return errors


def anchor(text):
    return re.sub(r'[^\w\s-]','',text.lower()).replace(' ','-')


def validate_package(root=ROOT):
    errors=[]
    required=['SKILL.md','README.md','LICENSE','references/source-acquisition.md','references/audit-dimensions.md',
              'references/severity-and-priority.md','references/sources.md','templates/audit-report.md',
              'examples/artifact-audit.md','examples/report.json','tests/scenarios.md','tests/validation-report.md']
    for name in required:
        if not (root/name).is_file():errors.append('Missing file: '+name)
        elif not (root/name).read_bytes():errors.append('Empty file: '+name)
    if errors:return errors
    skill=(root/'SKILL.md').read_text(encoding='utf-8')
    front=re.match(r'\A---\n(.*?)\n---\n',skill,re.S)
    if not front:errors.append('Missing skill frontmatter')
    else:
        values=dict(re.findall(r'^(name|description): (.+)$',front.group(1),re.M))
        if values.get('name')!=root.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',values.get('name','')):
            errors.append('Invalid skill name')
        if not 1<=len(values.get('description',''))<=1024:errors.append('Invalid description')
        if not re.search(r'^license: \S',front.group(1),re.M):errors.append('Missing license frontmatter')
        if not re.search(r'^metadata:\n(?:  \S.*\n)*?  version: "\d+\.\d+\.\d+"$',front.group(1),re.M):errors.append('Missing or invalid metadata.version frontmatter')
    if len(skill.split())>1400:errors.append('Skill entrypoint exceeds 1400-word context budget')
    for file in root.rglob('*.md'):
        if any(part in IGNORED for part in file.relative_to(root).parts):continue
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
            if re.match(r'https?://',link):continue
            path,_,fragment=link.partition('#')
            target=(file.parent/unquote(path)).resolve() if path else file.resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append('Invalid local link in '+str(file.relative_to(root))+': '+link)
            elif fragment:
                headings=re.findall(r'^#{1,6} (.+)$',target.read_text(encoding='utf-8'),re.M)
                if unquote(fragment) not in [anchor(h) for h in headings]:errors.append('Missing heading: '+link)
    try:errors.extend(validate_report(json.loads((root/'examples/report.json').read_text(encoding='utf-8'))))
    except (OSError,ValueError) as exc:errors.append('Invalid example JSON: '+str(exc))
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,help='Also validate a structured JSON report')
    args=parser.parse_args()
    errors=validate_package()
    if args.report:
        try:errors.extend(validate_report(json.loads(args.report.read_text(encoding='utf-8'))))
        except (OSError,ValueError) as exc:errors.append('Cannot read report: '+str(exc))
    for error in errors:print('FAIL: '+error,file=sys.stderr)
    if errors:return 1
    print('PASS: skill metadata and version, required files, local links, report structure and evidence references')
    print('NOTE: structural checks cannot verify observations, audit quality, or conformance.')
    return 0


if __name__=='__main__':
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,'reconfigure'):stream.reconfigure(errors='backslashreplace')
    sys.exit(main())

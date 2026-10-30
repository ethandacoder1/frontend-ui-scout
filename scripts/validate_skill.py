#!/usr/bin/env python3
"""Zero-dependency integrity checks for the UI Scout Agent Skill.

This validates local packaging, metadata and catalog completeness. It does not
access the internet or make claims about actual site availability/licensing.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills' / 'frontend-ui-scout'
REF = SKILL / 'references'
DIRECTORIES = [
    '01-component-marketplaces.md', '02-application-ui.md',
    '03-design-inspiration.md', '04-css-and-generators.md',
    '05-motion-and-3d.md', '06-templates-and-builders.md',
    '07-discovery-index.md',
]
EXPECTED_COUNTS = [14, 12, 14, 8, 5, 7, 1]
errors=[]

if not (SKILL / 'SKILL.md').is_file():
    errors.append('SKILL.md is missing')
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
m = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
if not m:
    errors.append('SKILL.md must start with YAML frontmatter')
else:
    fields = dict(re.findall(r'^([a-z][a-z0-9-]*):[ \t]*(.*)$', m.group(1), re.M))
    name = fields.get('name', '')
    desc = fields.get('description', '')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('Invalid skill name')
    if name != SKILL.name:
        errors.append('name field must match skill directory')
    if not 1 <= len(desc) <= 1024:
        errors.append('description must be 1-1024 characters')
    if len(fields.get('compatibility',''))>500:
        errors.append('compatibility must be <=500 characters')
if len(text.splitlines()) >= 500:
    errors.append('SKILL.md should be shorter than 500 lines')

# All markdown links into references from SKILL.md should resolve.
for target in re.findall(r'\]\((references/[^)#]+)(?:#[^)]+)?\)', text):
    if not (SKILL / target).is_file():
        errors.append(f'Unresolved reference: {target}')

catalog = []
for filename, expected in zip(DIRECTORIES,EXPECTED_COUNTS):
    path=REF/filename
    if not path.exists():
        errors.append(f'Missing directory: {filename}')
        continue
    content=path.read_text(encoding='utf-8')
    # Count only resource-name links in the table, not extra prose links.
    urls=re.findall(r'^\| \[[^]]+\]\((https?://[^)]+)\) \|',content,re.M)
    if len(urls)!=expected:
        errors.append(f'{filename}: expected {expected} links, got {len(urls)}')
    catalog.extend(urls)
    if '\r' in content:
        errors.append(f'Windows newlines in {filename}')

if len(catalog)!=61:
    errors.append(f'Expected 61 links, found {len(catalog)}')
if len(catalog)!=len(set(catalog)):
    errors.append('Duplicate catalog URLs detected')
for url in catalog:
    if ' ' in url or not url.startswith('https://'):
        errors.append(f'Invalid URL: {url}')

if errors:
    for err in errors:
        print(f'FAIL: {err}',file=sys.stderr)
    sys.exit(1)
print(f'PASS: Agent Skill frontmatter, reference links, and {len(catalog)} unique resource URLs verified.')
print('Note: Local validation only; live links, licenses and accessibility are not tested.')

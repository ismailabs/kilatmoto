#!/usr/bin/env python3
"""Dependency-free structural, safety, SEO and optional actual HTTP checks."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
from collections import Counter
import argparse
import re
import xml.etree.ElementTree as ET
import json
from configure_seo import configure

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'about/index.html', 'services/index.html', 'projects/index.html', 'contact/index.html']


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []; self.references = []; self.headings = []; self.tags = []
        self.text = []; self.in_title = False; self.title = ''; self.metadata = {}

    def handle_starttag(self, tag, attrs):
        data = dict(attrs); self.tags.append((tag, data))
        if data.get('id'): self.ids.append(data['id'])
        if tag == 'title': self.in_title = True
        if re.fullmatch('h[1-6]', tag): self.headings.append(int(tag[1]))
        if tag == 'meta':
            key = data.get('name', data.get('property', ''))
            self.metadata.setdefault(key, []).append(data.get('content', ''))
        for attr in ['href', 'src']:
            if data.get(attr): self.references.append(data[attr])
        if data.get('srcset'):
            self.references.extend(item.strip().split()[0] for item in data['srcset'].split(','))

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title: self.title += data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', help='Optional local HTTP origin, e.g. http://127.0.0.1:8000')
    args = parser.parse_args()
    issues = []; scans = {}; targets = set()
    def check(condition, message):
        if not condition: issues.append(message)
    actual_pages = sorted(str(p.relative_to(ROOT)).replace('\\', '/') for p in ROOT.rglob('index.html') if not any(x in p.parts for x in ['.git', 'node_modules', 'dist', 'tmp']))
    check(actual_pages == sorted(PAGES), 'Expected exactly five main page entries')
    for name in PAGES:
        scan = Scan(); source = (ROOT / name).read_text(encoding='utf8'); scan.feed(source); scans[name] = scan
        check(bool(scan.title), f'{name}: missing title')
        check(scan.headings.count(1) == 1, f'{name}: expected exactly one h1')
        check(all(b <= a + 1 for a, b in zip(scan.headings, scan.headings[1:])), f'{name}: skipped heading level')
        check(len(scan.metadata.get('description', [])) == 1, f'{name}: description missing or repeated')
        check(len(scan.metadata.get('robots', [])) == 1, f'{name}: robots missing or repeated')
        check('fictional' in ''.join(scan.text).lower(), f'{name}: missing fictional disclosure')
        check('Services, projects and enquiries are demonstrations only.' in ' '.join(' '.join(scan.text).split()), f'{name}: missing footer disclosure')
        check(all(n == 1 for n in Counter(scan.ids).values()), f'{name}: duplicate IDs')
        check('https://www.ismailstudio.my/' in source, f'{name}: missing ISMAIL conversion path')
        check('KILAT MOTORWORKS' in source, f'{name}: missing brand')
        check(not re.search(r'RAPI MOTION|KILAT MOTO(?!RWORKS)', source), f'{name}: obsolete or incorrect brand')
        for tag, data in scan.tags:
            check(not any(k.lower().startswith('on') for k in data), f'{name}: inline handler')
            if tag == 'img':
                check('alt' in data and 'width' in data and 'height' in data, f'{name}: image alt/dimensions missing')
            check(tag != 'form', f'{name}: network-capable form not allowed')
            if tag == 'a' and data.get('target') == '_blank':
                check('noopener' in data.get('rel', ''), f'{name}: unsafe new-tab link')
    check(len({s.title for s in scans.values()}) == 5, 'Titles must be unique')
    check(len({s.metadata['description'][0] for s in scans.values()}) == 5, 'Descriptions must be unique')
    for name, scan in scans.items():
        targets.add('/' if name == 'index.html' else '/' + name.replace('index.html', ''))
        for reference in scan.references:
            parts = urlsplit(reference)
            if parts.scheme or parts.netloc:
                check(parts.scheme == 'https' and parts.netloc in ['www.ismailstudio.my', 'kilatmoto.ismailstudio.my'],
                      f'{name}: unexpected external reference {reference}')
                continue
            path = ROOT / unquote(parts.path).lstrip('/') if parts.path.startswith('/') else (ROOT / name).parent / unquote(parts.path)
            if not parts.path: path = ROOT / name
            if path.is_dir(): path /= 'index.html'
            check(path.is_file(), f'{name}: broken path {reference}')
            if parts.path: targets.add(parts.path)
            if parts.fragment and path.suffix == '.html':
                destination = str(path.relative_to(ROOT)).replace('\\', '/')
                check(parts.fragment in scans[destination].ids, f'{name}: missing anchor {reference}')
    contract = json.loads((ROOT / 'kilatmoto-Codex-Handoff/data/six-service-contract.json').read_text())
    service_tags = scans['services/index.html'].tags
    service_source = (ROOT / 'services/index.html').read_text(encoding='utf8')
    contact_source = (ROOT / 'contact/index.html').read_text(encoding='utf8')
    for item in contract['services']:
        check(item['id'] in scans['services/index.html'].ids, f'Missing service {item["id"]}')
        check(item['name'] in ''.join(scans['services/index.html'].text), f'Missing service label {item["name"]}')
        check(f'/contact/?service={item["id"]}' in service_source, f'Missing demo mapping {item["id"]}')
        check(f'value="{item["id"]}"' in contact_source, f'Missing demo option {item["id"]}')
    project_contract = {'urban':'exterior', 'executive':'refinement', 'family':'interior', 'coupe':'refinement', 'daily':'maintenance', 'electric':'protection'}
    actual = {d.get('id'):d.get('data-category') for t,d in scans['projects/index.html'].tags if t=='article' and 'project-card' in d.get('class','')}
    check(actual == project_contract, 'Six project IDs and filter associations must match baseline')
    titles = json.loads((ROOT / 'kilatmoto-Codex-Handoff/data/six-project-contract.json').read_text())['source_observed_section_headings']
    for title in titles: check(title in ''.join(scans['projects/index.html'].text), f'Missing project title {title}')
    css = (ROOT / 'assets/css/styles.css').read_text(encoding='utf8')
    for url in re.findall(r'url\([\'"]?([^\'"\)]+)', css):
        check((ROOT / url.lstrip('/')).is_file(), f'CSS missing resource {url}'); targets.add(url)
    js = (ROOT / 'assets/js/main.js').read_text(encoding='utf8')
    check(not re.search(r'\b(fetch|XMLHttpRequest|sendBeacon|localStorage|sessionStorage)\s*[.(]', js), 'Network or storage code in site JS')
    check('form-action \'none\'' in (ROOT / '_headers').read_text(), 'Missing form-action safety header')
    check('connect-src \'none\'' in (ROOT / '_headers').read_text(), 'Missing network safety header')
    ET.fromstring((ROOT / 'sitemap.xml').read_text())
    mode = 'staging' if scans['index.html'].metadata['robots'][0].startswith('noindex') else 'production'
    for path, expected in configure(ROOT, mode, 'https://kilatmoto.ismailstudio.my').items():
        check(path.read_text(encoding='utf8') == expected, f'Inconsistent {mode} SEO: {path.name}')
    targets |= {'/favicon.svg', '/robots.txt', '/sitemap.xml', '/og-image.webp'}
    if args.base_url:
        check(urlsplit(args.base_url).hostname in ['localhost', '127.0.0.1', '::1'], 'HTTP verification must target a local server')
        if not issues:
            for path in sorted(targets):
                try:
                    with urlopen(args.base_url.rstrip('/') + path) as response:
                        check(response.status == 200 and bool(response.read()), f'HTTP failed {path}')
                except Exception as error: issues.append(f'HTTP {path}: {error}')
    print(f'Checked five pages, {sum(len(s.references) for s in scans.values())} references, {len(targets)} HTTP targets, {mode} SEO, safety and image coverage.')
    if issues:
        for issue in issues: print('FAIL:', issue)
        raise SystemExit(1)
    print('PASS: structural/content/safety/SEO checks' + (' and actual HTTP requests' if args.base_url else ''))


if __name__ == '__main__': main()

#!/usr/bin/env python3
"""Explicit source-only SEO lifecycle. Does not deploy, push or change DNS."""
from pathlib import Path
import argparse
import re
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

ROUTES = ['', 'about/', 'services/', 'projects/', 'contact/']
DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def configure(root, mode, origin):
    production = mode == 'production'
    outputs = {}
    for route in ROUTES:
        path = root / route / 'index.html'
        source = path.read_text(encoding='utf8')
        url = origin + '/' + route
        tags = '<meta name="robots" content="index, follow">\n'
        if production:
            tags += f'<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">\n'
        else:
            tags = '<meta name="robots" content="noindex, follow">\n'
        source, count = re.subn(r'<!-- SEO:START -->.*?<!-- SEO:END -->',
                               '<!-- SEO:START -->\n' + tags + '<!-- SEO:END -->', source, flags=re.S)
        if count != 1:
            raise ValueError(f'{path}: expected exactly one SEO marker block')
        image = origin + '/og-image.webp' if production else '/og-image.webp'
        for attr, key in [('property', 'og:image'), ('name', 'twitter:image')]:
            source = re.sub(rf'<meta\s+{attr}="{key}"\s+content="[^"]*"\s*/?>',
                            f'<meta {attr}="{key}" content="{image}">', source)
        outputs[path] = source
    outputs[root / 'robots.txt'] = ('User-agent: *\nAllow: /\n' +
        (f'Sitemap: {origin}/sitemap.xml\n' if production else '# Staging: HTML and HTTP headers carry noindex. Crawling remains allowed.\n'))
    entries = ''.join(f'  <url><loc>{escape(origin + "/" + route)}</loc></url>\n' for route in ROUTES) if production else ''
    outputs[root / 'sitemap.xml'] = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries + '</urlset>\n')
    headers = (root / '_headers').read_text(encoding='utf8')
    headers = re.sub(r'^  X-Robots-Tag:.*\n', '', headers, flags=re.M)
    if not production:
        headers = headers.replace('/*\n', '/*\n  X-Robots-Tag: noindex, follow\n', 1)
    outputs[root / '_headers'] = headers
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', required=True, choices=['staging', 'production'])
    parser.add_argument('--origin', default='https://kilatmoto.ismailstudio.my')
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--check', action='store_true', help='Check files without modifying them')
    args = parser.parse_args()
    parsed = urlsplit(args.origin)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.path not in ['', '/'] or parsed.query or parsed.fragment or parsed.username or parsed.password or parsed.port:
        parser.error('--origin must be an HTTPS origin without credentials, port, path, query or fragment')
    if not re.fullmatch(r'https://[A-Za-z0-9.-]+/?', args.origin):
        parser.error('--origin contains invalid characters')
    outputs = configure(args.root.resolve(), args.mode, args.origin.rstrip('/'))
    if args.check:
        mismatches = [str(path.relative_to(args.root.resolve())) for path, text in outputs.items()
                      if path.read_text(encoding='utf8') != text]
        if mismatches:
            raise SystemExit('FAIL: SEO state differs: ' + ', '.join(mismatches))
        print(f'PASS: {args.mode} SEO state across five pages, robots, sitemap and headers')
    else:
        for path, text in outputs.items():
            path.write_text(text, encoding='utf8')
        print(f'Configured {args.mode} SEO in {len(outputs)} files. No deployment performed.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Check generated Jekyll routes, canonical links, fragments and campaign URLs offline."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote, parse_qs
import re
import sys
import xml.etree.ElementTree as ET

ORIGIN = 'https://chinavpnguide.github.io'
BASE = '/best-china-vpn-2026'
ROOT = Path(sys.argv[1]).resolve()
REPO = Path(__file__).resolve().parents[1]
errors = []

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.canonical = [], set(), []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a.get('href'))

pages = {}
for path in ROOT.rglob('*.html'):
    rel = path.relative_to(ROOT).as_posix()
    route = BASE + '/' + (rel[:-10] if rel.endswith('index.html') else rel)
    pages[route] = Page(path.read_text(encoding='utf-8'))

expected = {BASE + ('/' if p.name == 'index.md' else '/' + p.stem + '/')
            for p in REPO.glob('*.md') if p.read_text(encoding='utf-8').startswith('---\n')}
if set(pages) != expected:
    errors.append(f'Generated routes differ: missing={expected-set(pages)}, extra={set(pages)-expected}')

checked, tracked = 0, 0

def check_link(href, source, utm_source):
    global checked, tracked
    target = urlsplit(urljoin(ORIGIN + source, href))
    if target.netloc == 'chinavpnguide.github.io':
        checked += 1
        page = pages.get(target.path)
        if page is None:
            errors.append(f'{source}: missing local destination {href}')
        elif target.fragment and unquote(target.fragment) not in page.ids:
            errors.append(f'{source}: missing fragment {href}')
    if target.netloc == 'zibvpn.com':
        tracked += 1
        query = parse_qs(target.query)
        if query.get('utm_source') != [utm_source] or query.get('utm_medium') != ['referral']:
            errors.append(f'{source}: incorrect source/medium {href}')
        if query.get('utm_campaign') != ['20260921_repo_refresh'] or not query.get('utm_content'):
            errors.append(f'{source}: missing campaign/content {href}')
        if target.scheme != 'https' or not target.path.startswith('/zh'):
            errors.append(f'{source}: unexpected official target {href}')

for route, page in pages.items():
    if page.canonical != [ORIGIN + route]:
        errors.append(f'{route}: unexpected canonical {page.canonical}')
    for href in page.links:
        check_link(href, route, 'github_pages')

for href in re.findall(r'\]\(([^)]+)\)', (REPO/'README.md').read_text(encoding='utf-8')):
    if href.startswith('https://'):
        check_link(href, BASE+'/', 'github')

ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = ET.parse(ROOT/'sitemap.xml').getroot()
locations = [el.text for el in sitemap.findall('s:url/s:loc', ns)]
if set(locations) != {ORIGIN+r for r in expected} or len(locations) != len(expected):
    errors.append('Sitemap does not match canonical content routes')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(pages)} pages, canonical URLs and sitemap; {checked} internal links; {tracked} tracked official links.')

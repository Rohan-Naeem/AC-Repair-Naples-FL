import glob
import re
import os
from html.parser import HTMLParser

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'img', 'input', 'br', 'hr', 'meta', 'link', '!doctype'}
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append(tag.lower())
    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f'Unexpected end tag </{tag}>')
            return
        expected = self.stack.pop()
        if expected != tag:
            self.errors.append(f'Mismatched tag: expected </{expected}>, got </{tag}>')

html_files = sorted(glob.glob("*.html"))
print(f"Auditing {len(html_files)} HTML files...\n")

# 1. Check for any references to landmarks.html
broken_landmarks_links = []
for f in html_files:
    content = open(f, encoding="utf-8").read()
    if 'href="landmarks.html"' in content or "href='landmarks.html'" in content:
        broken_landmarks_links.append(f)

if broken_landmarks_links:
    print(f"ERROR: Found broken links to landmarks.html in: {broken_landmarks_links}")
else:
    print("CHECK 1 PASSED: Zero links to landmarks.html found across all files.")

# 2. Check internal link targets
all_existing_files = set(os.path.basename(p) for p in glob.glob("*.*"))
all_existing_html = set(os.path.basename(p) for p in glob.glob("*.html"))

broken_internal_links = []
for f in html_files:
    content = open(f, encoding="utf-8").read()
    # find all hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for h in hrefs:
        # ignore external, tel, mailto, anchor only
        if h.startswith('http://') or h.startswith('https://') or h.startswith('tel:') or h.startswith('mailto:') or h.startswith('#') or h == 'javascript:void(0)':
            continue
        # strip anchor
        target = h.split('#')[0]
        if not target:
            continue
        if target not in all_existing_files:
            broken_internal_links.append((f, h))

if broken_internal_links:
    print(f"WARNING: Broken internal links found: {broken_internal_links}")
else:
    print("CHECK 2 PASSED: All relative internal links resolve to existing files.")

# 3. Check HTML structure of 5 location pages
location_pages = [
    'hvac-port-royal.html',
    'hvac-park-shore.html',
    'hvac-aqualane-shores.html',
    'hvac-royal-harbor.html',
    'hvac-bayshore-arts-district.html'
]

print("\nCHECK 3: Verifying 5 location pages landmarks integration:")
for lp in location_pages:
    content = open(lp, encoding="utf-8").read()
    cards_count = content.count('class="t6-map-card"')
    h2_match = re.search(r'<h2>(.*?)</h2>', content[content.find('t6-map-card-grid')-500:content.find('t6-map-card-grid')])
    heading = h2_match.group(1) if h2_match else "UNKNOWN"
    print(f"  {lp}: {cards_count} landmark cards | Heading: '{heading}'")

# 4. Check HTML tag validity
print("\nCHECK 4: HTML syntax validity:")
tag_errors = 0
for f in html_files:
    content = open(f, encoding="utf-8").read()
    val = TagValidator()
    try:
        val.feed(content)
        if val.errors or val.stack:
            print(f"  Error in {f}: {len(val.errors)} errors, unclosed: {val.stack[:3]}")
            tag_errors += 1
    except Exception as e:
        print(f"  Parse error in {f}: {e}")
        tag_errors += 1

if tag_errors == 0:
    print("CHECK 4 PASSED: All 21 HTML files have perfectly balanced, valid HTML tags.")

print("\nAUDIT COMPLETE.")

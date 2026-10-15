# -*- coding: utf-8 -*-
import os
import glob
import re

services = [
    'ac-not-working.html',
    'central-ac-repair.html',
    'ac-not-blowing-cold-air.html',
    'commercial-ac-unit-replacement.html'
]

print("=== VALIDATING NEW SERVICE PAGES ===")
for s in services:
    assert os.path.exists(s), f"Missing file {s}"
    size = os.path.getsize(s)
    with open(s, "r", encoding="utf-8") as f:
        content = f.read()
    assert "<h1" in content, f"{s} missing h1"
    assert "<title>" in content, f"{s} missing title"
    assert 'rel="canonical"' in content, f"{s} missing canonical"
    assert "application/ld+json" in content, f"{s} missing schema"
    assert "t6-nav-panel-grid" in content, f"{s} missing desktop nav"
    assert "t6Drawer" in content, f"{s} missing mobile drawer"
    assert 'footer class="t6-band-ink"' in content, f"{s} missing footer"
    
    # verify images referenced
    imgs = re.findall(r'src="(assets/images/[^"]+)"', content)
    for img in imgs:
        assert os.path.exists(img), f"{s} references missing image {img}"
    print(f"PASS: {s} ({size} bytes) - All elements verified.")

print("\n=== VALIDATING HOMEPAGE & SERVICES PAGE ===")
for page in ['index.html', 'services.html']:
    with open(page, "r", encoding="utf-8") as f:
        c = f.read()
    for s in services:
        assert s in c, f"{page} missing link to {s}"
    print(f"PASS: {page} contains links to all 4 new services.")

print("\n=== VALIDATING SITEMAP, REDIRECTS, VERCEL ===")
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()
for s in services:
    clean = s.replace(".html", "")
    assert f"https://acrepairnaplesfl.com/{clean}" in sitemap, f"sitemap missing {clean}"
print("PASS: sitemap.xml has all 4 clean URLs.")

with open("_redirects", "r", encoding="utf-8") as f:
    redir = f.read()
for s in services:
    clean = s.replace(".html", "")
    assert f"/{s} /{clean} 301!" in redir, f"_redirects missing {s}"
print("PASS: _redirects has all 4 301 redirects.")

with open("vercel.json", "r", encoding="utf-8") as f:
    vj = f.read()
for s in services:
    clean = s.replace(".html", "")
    assert f'"source": "/{s}"' in vj, f"vercel.json missing {s}"
print("PASS: vercel.json has all 4 redirect entries.")

print("\n=== CHECKING ALL HTML FILES FOR 4 NEW SERVICES IN NAV ===")
all_htmls = glob.glob("*.html")
for h in all_htmls:
    if h == "404.html":
        continue
    with open(h, "r", encoding="utf-8") as f:
        c = f.read()
    for s in services:
        assert s in c, f"{h} missing link to {s}"

print(f"PASS: All {len(all_htmls)-1} main HTML files contain links to all 4 new services.")

print("\n=== ALL SYSTEM AUDITS AND CHECKS PASSED PERFECTLY! ===")

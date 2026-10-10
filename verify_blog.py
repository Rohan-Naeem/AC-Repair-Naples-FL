# -*- coding: utf-8 -*-
import glob
import os
import re

print("=== CHECKING BLOG POST WORD COUNTS ===")
article_files = sorted(glob.glob("blog/*.html"))
for f in article_files:
    if f.endswith("index.html"):
        continue
    with open(f, "r", encoding="utf-8") as fp:
        html = fp.read()
    # Strip HTML tags to count words in the article content
    # Find t6-article-content
    match = re.search(r'<div class="t6-article-content">(.*?)</div>\s*<!-- Author Bio Box -->', html, re.DOTALL)
    if match:
        content = match.group(1)
        text = re.sub(r'<[^>]+>', ' ', content)
        words = text.split()
        print(f"{os.path.basename(f)}: {len(words)} words in body")
    else:
        print(f"{os.path.basename(f)}: content div not matched")

print("\n=== CHECKING SITEMAP.XML ENTRIES ===")
with open("sitemap.xml", "r", encoding="utf-8") as fp:
    sitemap = fp.read()
for f in article_files:
    if f.endswith("index.html"):
        continue
    slug = os.path.basename(f).replace(".html", "")
    found = f"/blog/{slug}" in sitemap
    print(f"sitemap has /blog/{slug}: {found}")

print(f"sitemap has /blog: {'/blog' in sitemap}")

print("\n=== CHECKING _REDIRECTS ===")
with open("_redirects", "r", encoding="utf-8") as fp:
    red = fp.read()
for f in article_files:
    if f.endswith("index.html"):
        continue
    slug = os.path.basename(f).replace(".html", "")
    found = f"/blog/{slug}.html /blog/{slug} 301!" in red
    print(f"_redirects has /blog/{slug}.html: {found}")

print("\n=== CHECKING VERCEL.JSON ===")
with open("vercel.json", "r", encoding="utf-8") as fp:
    vcfg = fp.read()
for f in article_files:
    if f.endswith("index.html"):
        continue
    slug = os.path.basename(f).replace(".html", "")
    found = f"/blog/{slug}" in vcfg
    print(f"vercel.json has /blog/{slug}: {found}")

print("\n=== CHECKING NAVIGATION IN INDEX.HTML ===")
with open("index.html", "r", encoding="utf-8") as fp:
    idx = fp.read()
print(f"index.html desktop nav has Blog: {'href=\"blog.html\" class=\"t6-nav-link\">Blog</a>' in idx}")
print(f"index.html mobile drawer has Blog: {'href=\"blog.html\"' in idx and 'style=\"color:#fff;' in idx}")
print(f"index.html footer has Blog: {'href=\"blog.html\"' in idx}")

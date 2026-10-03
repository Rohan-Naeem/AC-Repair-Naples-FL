with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Google Rating', text, re.I)]
for m in matches:
    print("=== index.html 'Google Rating' ===")
    print(text[m-200:m+300])

matches2 = [m.start() for m in re.finditer(r'Google Verified', text, re.I)]
for m in matches2:
    print("=== index.html 'Google Verified' ===")
    print(text[m-100:m+200])

with open('ac-not-cooling.html', 'r', encoding='utf-8') as f:
    anc_text = f.read()
matches3 = [m.start() for m in re.finditer(r'Google', anc_text, re.I)]
for m in matches3:
    print("=== ac-not-cooling.html 'Google' ===")
    print(anc_text[m-100:m+200])

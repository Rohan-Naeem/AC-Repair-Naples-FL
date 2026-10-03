import re, sys

with open('ac-not-cooling.html', 'r', encoding='utf-8') as f:
    anc_text = f.read()

matches3 = [m.start() for m in re.finditer(r'Google', anc_text, re.I)]
for m in matches3:
    print("=== ac-not-cooling.html 'Google' ===")
    s = anc_text[m-100:m+200]
    print(s.encode('ascii', 'backslashreplace').decode('ascii'))

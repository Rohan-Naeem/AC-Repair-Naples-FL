with open('mini-split-repair.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if 'google' in l.lower() and 'maps' not in l.lower() and 'fonts' not in l.lower():
        print(f"Line {i}: {l.strip()}")

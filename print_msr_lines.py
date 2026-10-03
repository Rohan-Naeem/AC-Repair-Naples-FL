import sys

with open('mini-split-repair.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[965:1015], 966):
    sys.stdout.buffer.write(f"{i:4d}: {l}".encode('utf-8'))

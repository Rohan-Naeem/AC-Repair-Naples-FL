import sys

with open('mini-split-repair.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('What Our Customers Say')
sys.stdout.buffer.write(text[idx:idx+2500].encode('utf-8'))

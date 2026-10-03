import sys

with open('package-unit-repair.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('What Our Customers Say')
if idx != -1:
    sys.stdout.buffer.write(text[idx:idx+1500].encode('utf-8'))
else:
    print("Not found")

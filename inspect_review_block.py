import sys

with open('ac-not-cooling.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Google')
sys.stdout.buffer.write(text[idx-400:idx+600].encode('utf-8'))

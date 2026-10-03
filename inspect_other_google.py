import sys

with open('mini-split-repair.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Google')
sys.stdout.buffer.write(b"=== mini-split-repair.html ===\n")
sys.stdout.buffer.write(text[idx-200:idx+400].encode('utf-8'))
sys.stdout.buffer.write(b"\n")

with open('compressor-valve-replacement.html', 'r', encoding='utf-8') as f:
    text_cvr = f.read()

idx_cvr = text_cvr.find('Google')
sys.stdout.buffer.write(b"=== compressor-valve-replacement.html ===\n")
sys.stdout.buffer.write(text_cvr[idx_cvr-200:idx_cvr+400].encode('utf-8'))
sys.stdout.buffer.write(b"\n")

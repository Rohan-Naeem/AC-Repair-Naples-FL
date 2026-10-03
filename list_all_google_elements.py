import glob, re, sys

results = {}

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Remove map iframes and map links
    c_clean = re.sub(r'https?://(?:maps\.google\.com|www\.google\.com/maps)[^\s"\'<>]*', '', c)
    c_clean = re.sub(r'title="Open[^"]*on Google Maps"', '', c_clean)
    
    # Search for google in clean text
    matches = re.findall(r'.{0,60}google.{0,60}', c_clean, re.I)
    if matches:
        results[f] = [m.strip() for m in matches]

for f, ms in results.items():
    sys.stdout.buffer.write(f"=== {f} ({len(ms)} matches) ===\n".encode('utf-8'))
    for m in ms:
        sys.stdout.buffer.write(f"  {m}\n".encode('utf-8'))

import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Remove google maps and fonts
    c_clean = re.sub(r'https?://(?:maps\.google\.com|www\.google\.com/maps|fonts\.googleapis\.com)[^\s"\'<>]*', '', c)
    
    # Find any mention of google
    matches = re.finditer(r'(?:[^\n]+\n?){0,2}[^\n]*google[^\n]*(?:\n?[^\n]+){0,2}', c_clean, re.IGNORECASE)
    lines = [m.group(0).strip() for m in matches]
    if lines:
        print(f"=== {f} ({len(lines)} matches) ===")
        for l in lines:
            print("  ---")
            for sub in l.split('\n'):
                print("   ", sub.strip())

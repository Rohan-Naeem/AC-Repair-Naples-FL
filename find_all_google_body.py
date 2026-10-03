import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # search for "google" anywhere in body (excluding google fonts / google maps)
    # remove head to check only body
    body_match = re.search(r'<body[\s\S]*?</body>', c, re.IGNORECASE)
    if body_match:
        body = body_match.group(0)
        # ignore google maps iframe and google tag/fonts
        body_clean = re.sub(r'<iframe[^>]*google\.com/maps[^>]*>.*?</iframe>', '', body, flags=re.DOTALL)
        body_clean = re.sub(r'fonts\.googleapis\.com', '', body_clean)
        
        matches = re.findall(r'.{0,40}google.{0,40}', body_clean, re.IGNORECASE)
        if matches:
            print(f"=== {f} ({len(matches)} google matches) ===")
            for m in matches:
                print("  ", m.strip())

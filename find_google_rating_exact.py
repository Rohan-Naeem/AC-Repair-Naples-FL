import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # 1. Search for "Google Rating"
    m_rating = re.findall(r'.{0,50}google rating.{0,50}', c, re.I)
    if m_rating:
        print(f"=== {f} Google Rating ===")
        for m in m_rating:
            print("  ", m.strip())

    # 2. Search for "Google Verified"
    m_ver = re.findall(r'.{0,50}google verified.{0,50}', c, re.I)
    if m_ver:
        print(f"=== {f} Google Verified ===")
        for m in m_ver:
            print("  ", m.strip())

    # 3. Search for "Google" inside review badges
    m_badge = re.findall(r'<strong[^>]*>Google</strong>[\s\S]*?</span>', c, re.I)
    if m_badge:
        print(f"=== {f} Google review badge ===")
        for m in m_badge:
            print("  ", m.strip()[:100])

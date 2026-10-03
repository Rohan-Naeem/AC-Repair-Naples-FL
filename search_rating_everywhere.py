import glob, re, sys

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # remove json-ld schema
    c_clean = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', '', c)
    
    # find "rating" in body
    m_rating = re.findall(r'.{0,40}rating.{0,40}', c_clean, re.I)
    if m_rating:
        print(f"=== {f} ({len(m_rating)} rating occurrences) ===")
        for m in m_rating:
            print("  ", m.strip())

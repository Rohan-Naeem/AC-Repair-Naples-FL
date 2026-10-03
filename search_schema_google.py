import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    scripts = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', c)
    for s in scripts:
        if 'google' in s.lower():
            print(f"=== {f} has 'google' in JSON-LD ===")
            for line in s.split('\n'):
                if 'google' in line.lower():
                    print("  ", line.strip())

import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    matches = re.findall(r'.{0,50}google.{0,30}rating.{0,50}', c, re.IGNORECASE)
    if matches:
        print(f"=== {f} ({len(matches)} matches) ===")
        for m in matches:
            print("  ", m.strip())

    # Also search for "google review" or any standalone "google" text in visible body
    other_google = re.findall(r'.{0,40}google (?:review|verified|rating|stars).{0,40}', c, re.IGNORECASE)
    if other_google and not matches:
        print(f"=== {f} (other google matches: {len(other_google)}) ===")
        for m in other_google:
            print("  ", m.strip())

import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # check for testimonials or reviews
    reviews = re.findall(r'<section[^>]*id=["\']testimonials["\']|<h[23][^>]*>[^<]*(?:reviews|testimonials|customer rating|what our customers say)[^<]*</h[23]>', c, re.I)
    if reviews:
        print(f"{f:32} -> {reviews}")

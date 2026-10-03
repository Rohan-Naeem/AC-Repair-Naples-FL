with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Google Rating')
print("=== index.html around Google Rating ===")
print(text[idx-400:idx+400])

with open('about.html', 'r', encoding='utf-8') as f:
    text_about = f.read()

idx_about = text_about.find('Google Rating')
print("=== about.html around Google Rating ===")
print(text_about[idx_about-400:idx_about+400])

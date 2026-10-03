with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Google Rating')
p_start = text.rfind('<div', 0, text.rfind('<div', 0, text.rfind('<div', 0, idx)))
p_end = text.find('</div>\n        </div>', idx) + len('</div>\n        </div>')

print(text[p_start:p_end+200])

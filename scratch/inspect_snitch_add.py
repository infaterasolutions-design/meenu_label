with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function snitchAddSizeToCart')
print("--- meenu-theme.js ---")
print(text[idx:idx+1500].encode('ascii', errors='replace').decode('ascii'))

with open('index.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

idx2 = text2.find('function snitchAddSizeToCart')
print("--- index.html ---")
print(text2[idx2:idx2+1500].encode('ascii', errors='replace').decode('ascii'))

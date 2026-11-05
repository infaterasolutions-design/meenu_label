with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function openQuickSizePopup')
print(text[idx:idx+1200].encode('ascii', errors='replace').decode('ascii'))

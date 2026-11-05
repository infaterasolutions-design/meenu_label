with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function openAccountModal')
print(c[idx:idx+900])

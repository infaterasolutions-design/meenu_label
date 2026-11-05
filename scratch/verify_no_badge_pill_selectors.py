files = ['assets/meenu-theme.js', 'index.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    matches = list(re.finditer(r'querySelector(All)?\([^)]*header-badge-pill[^)]*\)', text))
    print(f"=== {fname}: {len(matches)} matches ===")
    for m in matches:
        print(" ", m.group(0))

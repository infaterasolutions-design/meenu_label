files = ['assets/meenu-theme.js', 'index.html', 'sections/header.liquid']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    matches = list(re.finditer(r'.{0,30}\.header-badge-pill.{0,30}', text))
    print(f"=== {fname}: {len(matches)} occurrences ===")
    for m in matches:
        print(" ", m.group(0).strip().replace('\n', ' '))

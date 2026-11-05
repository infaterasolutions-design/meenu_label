import re

core_files = [
    'config/settings_data.json',
    'assets/meenu-theme.js',
    'sections/main-product.liquid',
    'snippets/product-card.liquid',
    'snippets/nav-drawer.liquid',
    'snippets/policy-modal.liquid',
    'snippets/snitch-login-modal.liquid',
    'snippets/whatsapp-concierge.liquid',
    'index.html'
]

for p in core_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    matches = re.findall(r'.{0,30}(?:99888|98845).{0,30}', c)
    if matches:
        print(f"=== {p} ({len(matches)} matches) ===")
        for m in matches:
            print("  ...", m.strip(), "...")

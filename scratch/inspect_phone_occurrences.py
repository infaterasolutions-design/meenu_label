import re

core_files = [
    'config/settings_data.json',
    'meenu-label-shopify-theme/config/settings_data.json',
    'assets/meenu-theme.js',
    'meenu-label-shopify-theme/assets/meenu-theme.js',
    'sections/main-product.liquid',
    'meenu-label-shopify-theme/sections/main-product.liquid',
    'snippets/product-card.liquid',
    'meenu-label-shopify-theme/snippets/product-card.liquid',
    'snippets/nav-drawer.liquid',
    'meenu-label-shopify-theme/snippets/nav-drawer.liquid',
    'snippets/policy-modal.liquid',
    'meenu-label-shopify-theme/snippets/policy-modal.liquid',
    'snippets/snitch-login-modal.liquid',
    'meenu-label-shopify-theme/snippets/snitch-login-modal.liquid',
    'snippets/whatsapp-concierge.liquid',
    'meenu-label-shopify-theme/snippets/whatsapp-concierge.liquid',
    'index.html'
]

for p in core_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    matches = re.findall(r'.{0,40}9988898845.{0,40}', c)
    print(f"=== {p} ({len(matches)} matches) ===")
    for m in matches[:3]:
        print("  ...", m.strip(), "...")

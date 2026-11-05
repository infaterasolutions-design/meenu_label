import os

files_to_update = [
    'config/settings_data.json',
    'config/settings_schema.json',
    'meenu-label-shopify-theme/config/settings_data.json',
    'meenu-label-shopify-theme/config/settings_schema.json',
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
    'snippets/notify-me-modal.liquid',
    'meenu-label-shopify-theme/snippets/notify-me-modal.liquid',
    'index.html'
]

replacements = [
    ('919988898845', '918511616133'),
    ('+91 99888 98845', '+91 85116 16133'),
    ('99888 98845', '85116 16133'),
    ('9988898845', '8511616133'),
    ('"default": "919876543210"', '"default": "918511616133"')
]

total_replacements = 0

for file_rel in files_to_update:
    if not os.path.exists(file_rel):
        continue
    with open(file_rel, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    file_count = 0
    for target, repl in replacements:
        if target in content:
            c = content.count(target)
            content = content.replace(target, repl)
            file_count += c

    if content != orig_content:
        with open(file_rel, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_rel}: {file_count} replacements made.")
        total_replacements += file_count

print(f"\nTOTAL REPLACEMENTS ACROSS ALL FILES: {total_replacements}")

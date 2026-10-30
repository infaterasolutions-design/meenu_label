import os
import re

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'

for f in ['snippets/cart-drawer.liquid', 'snippets/nav-drawer.liquid', 'snippets/size-guide-modal.liquid', 'snippets/snitch-login-modal.liquid']:
    p = os.path.join(theme_dir, f)
    with open(p, 'r', encoding='utf-8') as file:
        c = file.read()
    ids = re.findall(r'id=["\']([^"\']+)["\']', c)
    print(f"=== {f} ===")
    print("  IDs:", ids)

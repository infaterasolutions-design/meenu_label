theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/sections/campaign-edit.liquid"
with open(p, 'r', encoding='utf-8') as f:
    camp = f.read()

import re
badges = re.findall(r'<span class="campaign-badge"[^>]*>[\s\S]*?<\/span>', camp)
print(f"Found {len(badges)} campaign badges:")
for b in badges:
    print(" -", b)

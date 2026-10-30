import re

with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

cats = {}
for m in re.finditer(r'"category":\s*"([^"]+)"', text[:30000]):
    c = m.group(1)
    cats[c] = cats.get(c, 0) + 1

print('Category counts in products:', cats)
print('Total:', sum(cats.values()))

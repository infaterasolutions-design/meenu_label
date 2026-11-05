import re

with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

# Check tags
tags = ['if', 'for', 'form', 'schema']
for t in tags:
    open_count = len(re.findall(r'\{%\s*' + t + r'\b', text))
    close_count = len(re.findall(r'\{%\s*end' + t + r'\b', text))
    print(f"Tag {t}: open={open_count}, close={close_count}")
    assert open_count == close_count, f"Mismatch in {t} tags: {open_count} vs {close_count}"

print("All Liquid tags in sections/main-product.liquid are balanced and valid!")

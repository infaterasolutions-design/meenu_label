import re

with open('snippets/product-card.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

tags = ['if', 'for']
for t in tags:
    open_count = len(re.findall(r'\{%\s*' + t + r'\b', text))
    close_count = len(re.findall(r'\{%\s*end' + t + r'\b', text))
    print(f"Tag {t}: open={open_count}, close={close_count}")
    assert open_count == close_count, f"Mismatch in {t} tags: {open_count} vs {close_count}"

print("All Liquid tags in snippets/product-card.liquid are balanced and valid!")

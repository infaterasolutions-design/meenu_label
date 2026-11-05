with open('snippets/product-card.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

print("snippets/product-card.liquid:")
print("Has snitch-plus-trigger:", 'class="snitch-plus-trigger"' in text)
print("Has product-variants-json:", 'class="product-variants-json"' in text)
print("Has openQuickSizePopup:", 'openQuickSizePopup(this)' in text)

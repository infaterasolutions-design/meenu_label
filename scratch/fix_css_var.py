with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('css += """', 'meenu_css += """')

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed meenu_css successfully!')

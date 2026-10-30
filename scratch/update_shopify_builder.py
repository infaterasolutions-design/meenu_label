with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Jaipur Chanderi Festive Suit', 'The Royal Wine Chanderi Festive Suit')
text = text.replace('Jaipur Chanderi Silk Festive Suit', 'The Royal Wine Chanderi Festive Suit')

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated build_shopify_theme.py successfully!')

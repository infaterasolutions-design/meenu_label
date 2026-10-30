with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'([a-zA-Z0-9_\-]+\.liquid)', text)
print('Liquid files in build_shopify_theme.py:', set(matches))

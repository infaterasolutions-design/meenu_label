import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

h_start = text.find('<header>')
h_end = text.find('</header>') + 9
h_text = text[h_start:h_end]
# Replace base64
h_text_clean = re.sub(r'data:image/[^;]+;base64,[^"\']+', '{{ "logo.png" | asset_url }}', h_text)
print("=== CLEAN HEADER LIQUID ===")
print(h_text_clean)

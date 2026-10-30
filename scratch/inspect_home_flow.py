import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

home_idx = text.find('id="storefrontHomeView"')
pdp_idx = text.find('id="productDetailView"')

home_html = text[home_idx:pdp_idx]

# Find all section comments or major tags
sections = re.findall(r'<!--\s*([A-Z0-9\s\.\-–—\(\)]+)\s*-->', home_html)
print("Sections found in storefrontHomeView:")
for s in sections[:25]:
    if any(k in s for k in ['HERO', 'BANNER', 'COLLECTION', 'CRAFT', 'STORY', 'VALUES', 'FOOTER', 'CAROUSEL', 'CAMPAIGN', 'TRUST', 'GRID']):
        print(" -", s.strip())

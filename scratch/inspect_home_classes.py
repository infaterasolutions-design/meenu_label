import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

home_idx = text.find('id="storefrontHomeView"')
pdp_idx = text.find('id="productDetailView"')
home_html = text[home_idx:pdp_idx]

# Remove huge base64 strings so we can see the DOM structure clearly!
clean_html = re.sub(r'data:image/[^;]+;base64,[^"\']+', 'IMG_DATA', home_html)

# Find top level sections
matches = re.findall(r'(<(?:section|div)[^>]*class="([^"]+)"[^>]*>)', clean_html)
print(f"Total matching elements: {len(matches)}")
for tag, cls in matches:
    if any(k in cls for k in ['section', 'hero', 'campaign', 'craft', 'grid', 'collection', 'story', 'founder', 'props', 'value', 'bar', 'promise']):
        print(f"Class: {cls}")

import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

h_start = text.find('<section class="snitch-hero-section">')
h_end = text.find('</section>', h_start) + 10
hero_html = text[h_start:h_end]
clean_hero = re.sub(r'data:image/[^;]+;base64,[^"\']+', '{{ "banner_1_polka.jpg" | asset_url }}', hero_html)
print("=== HERO HTML ===")
print(clean_hero)

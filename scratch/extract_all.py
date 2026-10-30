import os
import re

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

out_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections'
os.makedirs(out_dir, exist_ok=True)

# Replace all data:image base64 with a placeholder so files are clean and lightweight
clean = re.sub(r'data:image\/[^;]+;base64,[a-zA-Z0-9+/=]+', '{{ "placeholder.jpg" | asset_url }}', html)

# 1. Header & Announcement Bar
m_bar = re.search(r'(<!-- TOP PROMO STRIP[\s\S]*?<\/div>\s*<\/div>)', clean)
if m_bar:
    with open(os.path.join(out_dir, 'announcement-bar.html'), 'w', encoding='utf-8') as f:
        f.write(m_bar.group(1))

m_hdr = re.search(r'(<!-- MAIN NAVIGATION HEADER[\s\S]*?<\/header>)', clean)
if m_hdr:
    with open(os.path.join(out_dir, 'header.html'), 'w', encoding='utf-8') as f:
        f.write(m_hdr.group(1))

# 2. Hero Section
m_hero = re.search(r'(<section class="snitch-hero-section"[\s\S]*?<\/section>)', clean)
if m_hero:
    with open(os.path.join(out_dir, 'hero-editorial.html'), 'w', encoding='utf-8') as f:
        f.write(m_hero.group(1))

# 3. Campaign Edit Section
m_camp = re.search(r'(<section class="campaign-edit-section"[\s\S]*?<\/section>)', clean)
if m_camp:
    with open(os.path.join(out_dir, 'campaign-edit.html'), 'w', encoding='utf-8') as f:
        f.write(m_camp.group(1))

# 4. Craftsmanship Section
m_craft = re.search(r'(<section class="craftsmanship-section"[\s\S]*?<\/section>)', clean)
if m_craft:
    with open(os.path.join(out_dir, 'craftsmanship-spotlight.html'), 'w', encoding='utf-8') as f:
        f.write(m_craft.group(1))

# 5. Catalog Section
m_cat = re.search(r'(<section class="catalog-section"[\s\S]*?<\/section>)', clean)
if m_cat:
    with open(os.path.join(out_dir, 'catalog-section.html'), 'w', encoding='utf-8') as f:
        f.write(m_cat.group(1))

# 6. Value Strip
m_val = re.search(r'(<div class="value-strip"[\s\S]*?<\/div>\s*<\/div>)', clean)
if m_val:
    with open(os.path.join(out_dir, 'value-props.html'), 'w', encoding='utf-8') as f:
        f.write(m_val.group(1))

# 7. Founder Section
m_fnd = re.search(r'(<section class="founder-section"[\s\S]*?<\/section>)', clean)
if m_fnd:
    with open(os.path.join(out_dir, 'founder-story.html'), 'w', encoding='utf-8') as f:
        f.write(m_fnd.group(1))

# 8. Footer
m_foot = re.search(r'(<footer[\s\S]*?<\/footer>)', clean)
if m_foot:
    with open(os.path.join(out_dir, 'footer.html'), 'w', encoding='utf-8') as f:
        f.write(m_foot.group(1))

print("Extraction finished! Check files in:", out_dir)
for f in os.listdir(out_dir):
    print(" -", f, f"({os.path.getsize(os.path.join(out_dir, f))} bytes)")

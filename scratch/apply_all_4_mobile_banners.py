import base64, os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('assets/banner_modern_ethnic_mob.jpg', 'rb') as f:
    b1_mob_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets/banner_grace_in_every_drape_mob.jpg', 'rb') as f:
    b2_mob_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets/banner_everyday_dresses_mob.jpg', 'rb') as f:
    b3_mob_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets/banner_chic_yellow_coord_mob.jpg', 'rb') as f:
    b4_mob_b64 = base64.b64encode(f.read()).decode('utf-8')

print(f"b1 len: {len(b1_mob_b64)}")
print(f"b2 len: {len(b2_mob_b64)}")
print(f"b3 len: {len(b3_mob_b64)}")
print(f"b4 len: {len(b4_mob_b64)}")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Pattern to replace the mobile style block in index.html
mob_block_pattern = r'(@media \(max-width:\s*768px\)\s*\{[\s\S]*?\.snitch-hero-viewport[\s\S]*?\.slider-chevron[\s\S]*?)(?=}\s*\.snitch-slide|\n\s*\.snitch-slide)'

replacement_index_mob = f"""@media (max-width: 768px) {{
      .snitch-hero-viewport {{
        height: calc(100vw * 1.25) !important;
        min-height: 440px !important;
        max-height: 600px !important;
      }}
      .slider-chevron {{
        display: none !important;
      }}
      .snitch-slide.snitch-slide-hero1 {{
        background-image: url('data:image/jpeg;base64,{b1_mob_b64}') !important;
        background-position: center center !important;
      }}
      .snitch-slide.snitch-slide-hero2 {{
        background-image: url('data:image/jpeg;base64,{b2_mob_b64}') !important;
        background-position: center center !important;
      }}
      .snitch-slide.snitch-slide-hero3 {{
        background-image: url('data:image/jpeg;base64,{b3_mob_b64}') !important;
        background-position: center center !important;
      }}
      .snitch-slide.snitch-slide-hero4 {{
        background-image: url('data:image/jpeg;base64,{b4_mob_b64}') !important;
        background-position: center center !important;
      }}
    }}"""

# Let's locate the exact @media (max-width: 768px) block around line 396 in index.html
idx_start = index_html.find('@media (max-width: 768px)')
if idx_start != -1:
    # Find matching closing brace
    # Search from idx_start to find the block
    idx_end = index_html.find('.snitch-slide {', idx_start)
    if idx_end != -1:
        # Before .snitch-slide {, there is the closing brace
        sub = index_html[idx_start:idx_end]
        index_html = index_html[:idx_start] + replacement_index_mob + "\n    " + index_html[idx_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
        print("Updated index.html mobile block successfully!")
    else:
        print("ERROR: could not find .snitch-slide after media query in index.html")
else:
    print("ERROR: could not find @media (max-width: 768px) in index.html")

# 2. Update assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
css_replacement = """@media (max-width: 768px) {
  .slider-chevron {
    display: none !important;
  }
  .snitch-slide.snitch-slide-hero1 {
    background-image: url('banner_modern_ethnic_mob.jpg') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero2 {
    background-image: url('banner_grace_in_every_drape_mob.jpg') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero3 {
    background-image: url('banner_everyday_dresses_mob.jpg') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero4 {
    background-image: url('banner_chic_yellow_coord_mob.jpg') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-maroon {
    background-position: center center !important;
  }
}"""

for css_file in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        c = f.read()
    # Find the target block starting with @media (max-width: 768px)
    m = re.search(r'@media\s*\(max-width:\s*768px\)\s*\{[\s\S]*?\.snitch-slide\.snitch-slide-maroon[\s\S]*?\}', c)
    if m:
        c = c[:m.start()] + css_replacement + c[m.end():]
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {css_file} successfully!")
    else:
        print(f"ERROR: Could not find media query block in {css_file}")

# 3. Update sections/hero-editorial.liquid and meenu-label-shopify-theme/sections/hero-editorial.liquid
liq_replacement = """<style>
@media (max-width: 768px) {
  .snitch-hero-viewport {
    height: calc(100vw * 1.25) !important;
    min-height: 440px !important;
    max-height: 600px !important;
  }
  .slider-chevron { display: none !important; }
  .snitch-slide.snitch-slide-hero1 {
    background-image: url('{{ "banner_modern_ethnic_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero2 {
    background-image: url('{{ "banner_grace_in_every_drape_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero3 {
    background-image: url('{{ "banner_everyday_dresses_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero4 {
    background-image: url('{{ "banner_chic_yellow_coord_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
}
</style>"""

for liq_file in ['sections/hero-editorial.liquid', 'meenu-label-shopify-theme/sections/hero-editorial.liquid']:
    with open(liq_file, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<style>[\s\S]*?@media\s*\(max-width:\s*768px\)[\s\S]*?</style>', c)
    if m:
        c = c[:m.start()] + liq_replacement + c[m.end():]
        with open(liq_file, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {liq_file} successfully!")
    else:
        print(f"ERROR: Could not find <style> block in {liq_file}")

print("All updates applied!")

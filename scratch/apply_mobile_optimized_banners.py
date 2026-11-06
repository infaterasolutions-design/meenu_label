import base64, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# Read mobile assets and encode to base64
with open('assets/banner_everyday_dresses_mob.jpg', 'rb') as f:
    b3_mob_b64 = base64.b64encode(f.read()).decode('utf-8')
with open('assets/banner_chic_yellow_coord_mob.jpg', 'rb') as f:
    b4_mob_b64 = base64.b64encode(f.read()).decode('utf-8')

print(f"B3 Mob b64 len: {len(b3_mob_b64)}")
print(f"B4 Mob b64 len: {len(b4_mob_b64)}")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

target_index_css = """    @media (max-width: 768px) {
      .snitch-slide.snitch-slide-hero1 {
        background-position: 88% center !important;
      }
      .snitch-slide.snitch-slide-hero2 {
        background-position: 68% center !important;
      }
      .snitch-slide.snitch-slide-hero3 {
        background-position: 70% center !important;
      }
      .snitch-slide.snitch-slide-hero4 {
        background-position: 86% center !important;
      }
    }"""

replacement_index_css = f"""    @media (max-width: 768px) {{
      .slider-chevron {{
        display: none !important;
      }}
      .snitch-slide.snitch-slide-hero1 {{
        background-position: 88% center !important;
      }}
      .snitch-slide.snitch-slide-hero2 {{
        background-position: 68% center !important;
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

if target_index_css in index_html:
    index_html = index_html.replace(target_index_css, replacement_index_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Updated index.html mobile styles!")
else:
    print("ERROR: target_index_css not found in index.html")

# 2. Update assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
target_css = """@media (max-width: 768px) {
  .snitch-slide.snitch-slide-hero1 {
    background-position: 88% center !important;
  }
  .snitch-slide.snitch-slide-hero2 {
    background-position: 68% center !important;
  }
  .snitch-slide.snitch-slide-hero3 {
    background-position: 70% center !important;
  }
  .snitch-slide.snitch-slide-hero4 {
    background-position: 86% center !important;
  }
  .snitch-slide.snitch-slide-maroon {
    background-position: center center !important;
  }
}"""

replacement_css = """@media (max-width: 768px) {
  .slider-chevron {
    display: none !important;
  }
  .snitch-slide.snitch-slide-hero1 {
    background-position: 88% center !important;
  }
  .snitch-slide.snitch-slide-hero2 {
    background-position: 68% center !important;
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

for css_path in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    if target_css in css_content:
        css_content = css_content.replace(target_css, replacement_css)
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Updated {css_path}!")
    else:
        print(f"ERROR: target_css not found in {css_path}")

# 3. Update sections/hero-editorial.liquid and meenu-label-shopify-theme/sections/hero-editorial.liquid
liquid_style = """
<style>
@media (max-width: 768px) {
  .slider-chevron { display: none !important; }
  .snitch-slide.snitch-slide-hero3 {
    background-image: url('{{ "banner_everyday_dresses_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero4 {
    background-image: url('{{ "banner_chic_yellow_coord_mob.jpg" | asset_url }}') !important;
    background-position: center center !important;
  }
}
</style>
"""

for liq_path in ['sections/hero-editorial.liquid', 'meenu-label-shopify-theme/sections/hero-editorial.liquid']:
    with open(liq_path, 'r', encoding='utf-8') as f:
        liq_content = f.read()
    if '<section class="snitch-hero-section">' in liq_content and liquid_style not in liq_content:
        liq_content = liq_content.replace('<section class="snitch-hero-section">', liquid_style + '<section class="snitch-hero-section">')
        with open(liq_path, 'w', encoding='utf-8') as f:
            f.write(liq_content)
        print(f"Updated {liq_path}!")

print("\nDone applying all mobile-optimized banner styles!")

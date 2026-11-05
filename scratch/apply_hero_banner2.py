import os, re, base64

print("=== APPLYING GRACE IN EVERY DRAPE HERO BANNER 2 ===")

# Read optimized jpg and encode to base64
with open(r'scratch\banner_grace_opt.jpg', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')
b64_url = f"data:image/jpeg;base64,{b64_data}"

# 1. Update sections/hero-editorial.liquid in root and meenu-label-shopify-theme
editorial_paths = [
    r'sections\hero-editorial.liquid',
    r'meenu-label-shopify-theme\sections\hero-editorial.liquid'
]

new_slide2_liquid = """      <!-- Slide 2: Grace in Every Drape (New Arrivals Hero Banner) -->
      <div class="snitch-slide snitch-slide-hero2" style="background-image: url('{{ 'banner_grace_in_every_drape.jpg' | asset_url }}'); cursor: pointer;" onclick="window.location.href='/collections/all'" title="Shop Grace in Every Drape">
      </div>"""

for p in editorial_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace slide 2 regex
    pattern = r'<!-- Slide 2:.*?-->\s*<div class="snitch-slide[^"]*" style="background-image: url\(\'\{\{\s*\'[^\']+\'\s*\|\s*asset_url\s*\}\}\'\);[^"]*"[^>]*>.*?</div>\s*</div>'
    sub_res = re.sub(pattern, new_slide2_liquid, content, count=1, flags=re.DOTALL)
    if sub_res != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(sub_res)
        print(f"Updated Slide 2 in {p}")
    else:
        print(f"WARNING: Could not regex replace Slide 2 in {p}")

# 2. Update CSS in assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
css_paths = [
    r'assets\meenu-luxury.css',
    r'meenu-label-shopify-theme\assets\meenu-luxury.css'
]

css_old = """.snitch-slide-hero1,
.snitch-slide-maroon {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  cursor: pointer !important;
}
.snitch-slide.snitch-slide-hero1::after,
.snitch-slide.snitch-slide-maroon::after {
  display: none !important;
  content: none !important;
}
@media (max-width: 768px) {
  .snitch-slide.snitch-slide-hero1,
  .snitch-slide.snitch-slide-maroon {
    background-position: center center !important;
  }
}"""

css_new = """.snitch-slide-hero1,
.snitch-slide-hero2,
.snitch-slide-maroon {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  cursor: pointer !important;
}
.snitch-slide.snitch-slide-hero1::after,
.snitch-slide.snitch-slide-hero2::after,
.snitch-slide.snitch-slide-maroon::after {
  display: none !important;
  content: none !important;
}
@media (max-width: 768px) {
  .snitch-slide.snitch-slide-hero1 {
    background-position: center center !important;
  }
  .snitch-slide.snitch-slide-hero2 {
    background-position: 68% center !important;
  }
  .snitch-slide.snitch-slide-maroon {
    background-position: center center !important;
  }
}"""

for p in css_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if css_old in content:
        content = content.replace(css_old, css_new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS in {p}")
    else:
        print(f"Checking hero2 in {p}")
        if '.snitch-slide-hero2' not in content:
            with open(p, 'a', encoding='utf-8') as f:
                f.write("\n" + css_new + "\n")
            print(f"Appended CSS to {p}")
        else:
            print(f"Already present in {p}")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace Slide 2 in index.html
pattern_index = r'<!-- Slide 2:.*?-->\s*<div class="snitch-slide"[^>]*>.*?</div>\s*</div>'
match = re.search(pattern_index, index_html, re.DOTALL)
if match:
    new_slide2_block = f"""<!-- Slide 2: Grace in Every Drape (New Arrivals Hero Banner) -->
        <div class="snitch-slide snitch-slide-hero2" style="background-image: url('{b64_url}'); cursor: pointer;" onclick="filterProducts('all', null);" title="Shop Grace in Every Drape">
        </div>"""
    index_html = index_html[:match.start()] + new_slide2_block + index_html[match.end():]
    print("Replaced Slide 2 in index.html!")
else:
    print("WARNING: Could not find Slide 2 match in index.html!")

# Update or add .snitch-slide-hero2 in index.html CSS
if '.snitch-slide-hero2' not in index_html:
    index_html = index_html.replace(
        '.snitch-slide-hero1 {',
        '.snitch-slide-hero1,\n    .snitch-slide-hero2 {',
        1
    )
    index_html = index_html.replace(
        '.snitch-slide.snitch-slide-hero1::after {',
        '.snitch-slide.snitch-slide-hero1::after,\n    .snitch-slide.snitch-slide-hero2::after {',
        1
    )
    index_html = index_html.replace(
        '@media (max-width: 768px) {\n      .snitch-slide.snitch-slide-hero1 {\n        background-position: center center !important;\n      }',
        '@media (max-width: 768px) {\n      .snitch-slide.snitch-slide-hero1 {\n        background-position: center center !important;\n      }\n      .snitch-slide.snitch-slide-hero2 {\n        background-position: 68% center !important;\n      }',
        1
    )
    print("Added .snitch-slide-hero2 styles to index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("index.html updated successfully!")

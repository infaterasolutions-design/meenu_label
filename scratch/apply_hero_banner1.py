import os, re, base64

print("=== APPLYING MODERN ETHNIC ELEGANCE HERO BANNER 1 ===")

# Read optimized jpg and encode to base64
with open(r'scratch\banner_modern_ethnic_opt.jpg', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')
b64_url = f"data:image/jpeg;base64,{b64_data}"

# 1. Update sections/hero-editorial.liquid in root and meenu-label-shopify-theme
editorial_paths = [
    r'sections\hero-editorial.liquid',
    r'meenu-label-shopify-theme\sections\hero-editorial.liquid'
]

new_slide_liquid = """      <!-- Slide 1: Modern Ethnic Elegance (Flagship Hero Banner) -->
      <div class="snitch-slide snitch-slide-hero1" style="background-image: url('{{ 'banner_modern_ethnic.jpg' | asset_url }}'); cursor: pointer;" onclick="window.location.href='/collections/all'" title="Shop Modern Ethnic Elegance">
      </div>"""

for p in editorial_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace slide 1 regex
    pattern = r'<!-- Slide 1:.*?-->\s*<div class="snitch-slide[^"]*" style="background-image: url\(\'\{\{\s*\'[^\']+\'\s*\|\s*asset_url\s*\}\}\'\);[^"]*"[^>]*>.*?</div>'
    sub_res = re.sub(pattern, new_slide_liquid, content, count=1, flags=re.DOTALL)
    if sub_res != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(sub_res)
        print(f"Updated Slide 1 in {p}")
    else:
        print(f"WARNING: Could not regex replace Slide 1 in {p}")

# 2. Update CSS in assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
css_paths = [
    r'assets\meenu-luxury.css',
    r'meenu-label-shopify-theme\assets\meenu-luxury.css'
]

css_old = """.snitch-slide-maroon {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  cursor: pointer !important;
}
.snitch-slide.snitch-slide-maroon::after {
  display: none !important;
  content: none !important;
}
@media (max-width: 768px) {
  .snitch-slide.snitch-slide-maroon {
    background-position: 72% center !important; /* Perfectly frames the model in festive maroon on mobile */
  }
}"""

css_new = """.snitch-slide-hero1,
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

for p in css_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if css_old in content:
        content = content.replace(css_old, css_new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS in {p}")
    else:
        # Check if already updated
        if '.snitch-slide-hero1' in content:
            print(f"CSS in {p} already has .snitch-slide-hero1")
        else:
            print(f"Appending hero1 CSS to {p}")
            with open(p, 'a', encoding='utf-8') as f:
                f.write("\n" + css_new + "\n")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace Slide 1 in index.html
pattern_index = r'<!-- Slide 1:.*?-->\s*<div class="snitch-slide"[^>]*>.*?</div>\s*</div>'
match = re.search(pattern_index, index_html, re.DOTALL)
if match:
    old_slide1_block = match.group(0)
    new_slide1_block = f"""<!-- Slide 1: Modern Ethnic Elegance (Flagship Hero Banner) -->
        <div class="snitch-slide snitch-slide-hero1" style="background-image: url('{b64_url}'); cursor: pointer;" onclick="filterProducts('all', null);" title="Shop Modern Ethnic Elegance">
        </div>"""
    index_html = index_html[:match.start()] + new_slide1_block + index_html[match.end():]
    print("Replaced Slide 1 in index.html!")
else:
    print("WARNING: Could not find Slide 1 match in index.html!")

# Add .snitch-slide-hero1 style in index.html if not present
if '.snitch-slide-hero1' not in index_html:
    index_css_addition = """
    .snitch-slide-hero1 {
      background-size: cover !important;
      background-position: center center !important;
      background-repeat: no-repeat !important;
      cursor: pointer !important;
    }
    .snitch-slide.snitch-slide-hero1::after {
      display: none !important;
      content: none !important;
    }
    @media (max-width: 768px) {
      .snitch-slide.snitch-slide-hero1 {
        background-position: center center !important;
      }
    }
"""
    index_html = index_html.replace('    .snitch-slide {', index_css_addition + '    .snitch-slide {', 1)
    print("Added .snitch-slide-hero1 CSS to index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("index.html written successfully!")

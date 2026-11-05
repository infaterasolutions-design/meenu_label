import base64
import os
import re

user_img_path = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.user_uploaded\media_1793703677441_bf03286a.jpg"
with open(user_img_path, "rb") as f:
    user_img_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

print("User image base64 length:", len(user_img_b64))

# -------------------------------------------------------------
# 1. Update sections/main-product.liquid
# -------------------------------------------------------------
with open("sections/main-product.liquid", "r", encoding="utf-8") as f:
    content_mp = f.read()

# Replace empty placeholder aspect-ratio:4/5
content_mp = content_mp.replace(
    'style="width:100%; aspect-ratio:4/5;',
    'style="width:100%; aspect-ratio:2/3;'
)

# Replace .pdp-thumb-item aspect-ratio: 4 / 5;
content_mp = re.sub(
    r'(\.pdp-thumb-item\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5([^}]*?\})',
    r'\g<1>2 / 3 !important\g<2>',
    content_mp
)

# Add desktop .pdp-main-image-wrap and .pdp-main-image inside <style>
if "/* Main Gallery Image Frame (2:3 Atelier Portrait Aspect Ratio) */" not in content_mp:
    target_pos = content_mp.find("/* Thumbnails Rail */")
    desktop_rules = """  /* Main Gallery Image Frame (2:3 Atelier Portrait Aspect Ratio) */
  .pdp-main-image-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 2 / 3 !important;
    border-radius: 12px;
    overflow: hidden;
    background: #F4EFEB;
    border: 1px solid var(--border-color, #E8E2D9);
    box-shadow: 0 12px 30px rgba(0,0,0,0.04);
  }
  .pdp-main-image {
    width: 100% !important;
    height: 100% !important;
    aspect-ratio: 2 / 3 !important;
    object-fit: cover !important;
    object-position: center top !important;
    display: block !important;
    transition: transform 0.4s ease;
  }
  .pdp-main-image-wrap:hover .pdp-main-image {
    transform: scale(1.02);
  }

  """
    content_mp = content_mp[:target_pos] + desktop_rules + content_mp[target_pos:]

# Replace mobile .pdp-main-image-wrap and .pdp-main-image in @media (max-width: 900px)
content_mp = re.sub(
    r'(\.pdp-main-image-wrap\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_mp
)
content_mp = re.sub(
    r'(\.pdp-main-image\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_mp
)
content_mp = re.sub(
    r'(\.pdp-thumb-item\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_mp
)

with open("sections/main-product.liquid", "w", encoding="utf-8") as f:
    f.write(content_mp)
print("Updated sections/main-product.liquid successfully.")

# -------------------------------------------------------------
# 2. Update assets/meenu-luxury.css
# -------------------------------------------------------------
with open("assets/meenu-luxury.css", "r", encoding="utf-8") as f:
    content_css = f.read()

# Desktop rules
content_css = re.sub(
    r'(\.pdp-main-image-wrap\s*\{\s*position:\s*relative;\s*width:\s*100%;)',
    r'\g<1>\n      aspect-ratio: 2 / 3 !important;',
    content_css
)

content_css = re.sub(
    r'(\.pdp-main-image\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5',
    r'\g<1>2 / 3 !important',
    content_css
)

# Mobile rules
content_css = re.sub(
    r'(\.pdp-main-image-wrap\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_css
)
content_css = re.sub(
    r'(\.pdp-main-image\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_css
)
content_css = re.sub(
    r'(\.pdp-thumb-item\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_css
)

with open("assets/meenu-luxury.css", "w", encoding="utf-8") as f:
    f.write(content_css)
print("Updated assets/meenu-luxury.css successfully.")

# -------------------------------------------------------------
# 3. Update index.html
# -------------------------------------------------------------
with open("index.html", "r", encoding="utf-8") as f:
    content_idx = f.read()

# Desktop rules
content_idx = re.sub(
    r'(\.pdp-main-image-wrap\s*\{\s*position:\s*relative;\s*width:\s*100%;)',
    r'\g<1>\n      aspect-ratio: 2 / 3 !important;',
    content_idx
)

content_idx = re.sub(
    r'(\.pdp-main-image\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5',
    r'\g<1>2 / 3 !important',
    content_idx
)

# Mobile rules
content_idx = re.sub(
    r'(\.pdp-main-image-wrap\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_idx
)
content_idx = re.sub(
    r'(\.pdp-main-image\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_idx
)
content_idx = re.sub(
    r'(\.pdp-thumb-item\s*\{[^}]*?aspect-ratio:\s*)4\s*/\s*5\s*!important',
    r'\g<1>2 / 3 !important',
    content_idx
)

# Dynamic thumbnail generation inline style in index.html
content_idx = content_idx.replace(
    'aspect-ratio:4/5; border-radius:6px;',
    'aspect-ratio:2/3; border-radius:6px;'
)

# Add user's 2:3 uploaded photo to productsData[0] images
# Find productsData[0] and inject images: [b64, user_photo_b64]
prod_tag = '"id": "JAB26ST05010"'
if prod_tag in content_idx:
    # Check if images array already exists or inject it
    idx_p = content_idx.find(prod_tag)
    # Find the end of this object or the b64 field
    b64_start = content_idx.find('"b64": "', idx_p)
    if b64_start != -1:
        # Find closing quote of b64
        b64_end = content_idx.find('",', b64_start + 8)
        orig_b64 = content_idx[b64_start+8:b64_end]
        
        # Check if "images": is already there
        if '"images":' not in content_idx[idx_p:idx_p+len(user_img_b64)+500]:
            inject_str = f', "images": ["data:image/jpeg;base64,{orig_b64}", "{user_img_b64}"]'
            content_idx = content_idx[:b64_end+2] + inject_str + content_idx[b64_end+2:]
            print("Injected user's 2:3 photo into productsData[0].images in index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content_idx)
print("Updated index.html successfully.")

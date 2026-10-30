import os, re

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update <header> markup
old_header_markup = """<header>
    <div class="header-bar">
      <!-- Left: Hamburger + Desktop Nav -->
      <div class="header-left">
        <button class="hamburger-btn" onclick="openNavDrawer()" title="Open Navigation Menu" aria-label="Open Navigation Menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
        <ul class="nav-links-desktop">
          <li><a href="javascript:void(0)" class="active" onclick="filterCategory('all', this)">All Silhouettes</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('coord', this)">Co-ords</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('festive', this)">Festive Suits</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('dress', this)">Dresses</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('top', this)">Tops</a></li>
        </ul>
      </div>

      <!-- Center: Authentic Canva Brand Logo -->
      <div class="header-center">
        <a href="javascript:void(0)" onclick="closeProductPage()">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">"""

new_header_markup = """<header>
    <div class="header-bar">
      <!-- Left: Authentic Canva Brand Logo (Ultra-Clean, Menu Removed) -->
      <div class="header-logo-wrap">
        <a href="javascript:void(0)" onclick="closeProductPage()" title="Meenu Label Homepage">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">"""

if old_header_markup in code:
    code = code.replace(old_header_markup, new_header_markup)
    print("Replaced header markup successfully (menu removed).")
else:
    # Substring search for <header> to <div class="header-right">
    h_start = code.find('<header>')
    hr_start = code.find('<div class="header-right">')
    if h_start != -1 and hr_start != -1:
        code = code[:h_start] + new_header_markup + code[hr_start + len('<div class="header-right">'):]
        print("Replaced header markup via range.")

# 2. Update CSS for header-bar and header-logo-wrap
old_header_css = """.header-bar {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 12px 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 24px;
      flex: 1;
    }}"""

new_header_css = """.header-bar {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 14px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}
    .header-logo-wrap {{
      display: flex;
      align-items: center;
    }}"""

if old_header_css in code:
    code = code.replace(old_header_css, new_header_css)
    print("Updated header CSS successfully.")
else:
    code = code.replace("padding: 12px 36px;", "padding: 14px 40px;")
    # Ensure header-logo-wrap exists in css
    if ".header-logo-wrap" not in code:
        code = code.replace(".brand-logo-img {{", ".header-logo-wrap {{\n      display: flex;\n      align-items: center;\n    }}\n    .brand-logo-img {{")
        print("Inserted .header-logo-wrap CSS rule.")

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py without header menu!")

import os

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update <header> markup
old_header_markup = """<header>
    <div class="header-bar">
      <!-- Left: Authentic Canva Brand Logo (Ultra-Clean, Menu Removed) -->
      <div class="header-logo-wrap">
        <a href="javascript:void(0)" onclick="closeProductPage()" title="Meenu Label Homepage">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">"""

new_header_markup = """<header>
    <div class="header-bar">
      <!-- Left: Hamburger Menu Icon (Kept in place) -->
      <div class="header-left">
        <button class="hamburger-btn" onclick="openNavDrawer()" title="Open Navigation Menu" aria-label="Open Navigation Menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Middle: Centered Authentic Canva Brand Logo -->
      <div class="header-center">
        <a href="javascript:void(0)" onclick="closeProductPage()" title="Meenu Label Homepage">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">"""

if old_header_markup in code:
    code = code.replace(old_header_markup, new_header_markup)
    print("Replaced header markup successfully with hamburger on left and centered logo.")
else:
    # Substring search
    h_pos = code.find('<header>')
    hr_pos = code.find('<div class="header-right">', h_pos)
    if h_pos != -1 and hr_pos != -1:
        code = code[:h_pos] + new_header_markup + code[hr_pos + len('<div class="header-right">'):]
        print("Replaced header markup via range.")

# 2. Update CSS for .header-bar, .header-left, .header-center, .header-right, and .hamburger-btn
old_css_part = """.header-bar {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 14px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}"""

new_css_part = """.header-bar {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 12px 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}
    .header-left {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: flex-start;
    }}
    .hamburger-btn {{
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      border-radius: 4px;
      transition: color 0.2s, background 0.2s;
    }}
    .hamburger-btn:hover {{
      background: var(--bg-surface);
      color: var(--accent-gold);
    }}
    .hamburger-btn svg {{
      width: 22px;
      height: 22px;
      display: block;
      pointer-events: none;
    }}
    .header-center {{
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .brand-logo-img {{
      height: 52px;
      width: auto;
      display: block;
      transition: transform 0.2s ease;
    }}
    .brand-logo-img:hover {{
      transform: scale(1.02);
    }}
    .header-right {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 18px;
    }}"""

if old_css_part in code:
    # Also find where .header-right begins
    hr_css = code.find('.header-right {{')
    if hr_css != -1:
        hr_end = code.find('}}', hr_css) + 2
        code = code[:code.find(old_css_part)] + new_css_part + code[hr_end:]
        print("Replaced header CSS successfully.")
else:
    # Ensure header-left and header-center rules are present
    pos_h = code.find('header {{')
    pos_h_hero = code.find('/* Snitch-Style Minimalist Outline Icons */')
    if pos_h != -1 and pos_h_hero != -1:
        code = code[:pos_h] + "header {{\n      background: #FFFFFF;\n      border-bottom: 1px solid var(--border-color);\n      position: sticky;\n      top: 34px;\n      z-index: 90;\n      transition: all 0.3s ease;\n    }}\n    " + new_css_part + "\n\n    " + code[pos_h_hero:]
        print("Re-structured header CSS block cleanly.")

# Also fix the close button in nav-drawer:
code = code.replace('onclick="closeNavDrawer()">?</button>', 'onclick="closeNavDrawer()">&times;</button>')

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py with hamburger on left, logo centered, and 4 icons on right!")

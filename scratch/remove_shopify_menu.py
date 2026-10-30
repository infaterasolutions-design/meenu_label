with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace header_liquid to remove the nav links
old_liquid = """<header>
  <div class="header-inner">
    <nav>
      <ul class="nav-links">
        <li><a href="/collections/all">All Silhouettes</a></li>
        <li><a href="/collections/co-ord-sets">Co-ord Sets</a></li>
        <li><a href="/collections/festive-suits">Festive Suits</a></li>
        <li><a href="/collections/dresses">Dresses</a></li>
        <li><a href="/collections/tops">Tops</a></li>
      </ul>
    </nav>

    <div>
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>"""

new_liquid = """<header>
  <div class="header-inner">
    <!-- Brand Logo on Left (Clean layout matching Snitch) -->
    <div>
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>"""

if old_liquid in code:
    code = code.replace(old_liquid, new_liquid)
    print("Removed menu from header_liquid in build_shopify_theme.py")
else:
    # Substring search
    pos = code.find('<header>')
    end_nav = code.find('</nav>', pos)
    if pos != -1 and end_nav != -1:
        code = code[:pos] + "<header>\n  <div class=\"header-inner\">\n    <div>\n      <a href=\"/\" class=\"brand-logo\">{{ shop.name | default: 'MEENU LABEL' }}</a>\n      <span class=\"brand-sub\">CHANDIGARH &bull; ESTD 2026</span>\n    </div>" + code[code.find('</div>', end_nav)+6:]
        print("Replaced header_liquid via range.")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved build_shopify_theme.py without header menu.")

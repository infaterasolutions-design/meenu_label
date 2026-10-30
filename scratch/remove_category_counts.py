import re

# 1. Update build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    snitch_code = f.read()

# Replace header title
snitch_code = snitch_code.replace("The Debut 16 Silhouettes", "Signature Silhouettes")

# Replace pill count badge
snitch_code = snitch_code.replace(
    '<span class="sticky-count-pill" id="activeCategoryCount">16 SILHOUETTES</span>',
    '<span class="sticky-count-pill" id="activeCategoryCount">HANDCRAFTED EDITIONS</span>'
)

# Replace filter tabs
tabs_old = """        <button class="filter-tab active" data-cat="all" onclick="filterCategory('all', this)">All Silhouettes (16)</button>
        <button class="filter-tab" data-cat="coord" onclick="filterCategory('coord', this)">Co-ord Sets (4)</button>
        <button class="filter-tab" data-cat="festive" onclick="filterCategory('festive', this)">Festive Suits (6)</button>
        <button class="filter-tab" data-cat="dress" onclick="filterCategory('dress', this)">Midi Dresses (3)</button>
        <button class="filter-tab" data-cat="top" onclick="filterCategory('top', this)">Tops &amp; Blouses (3)</button>"""

tabs_new = """        <button class="filter-tab active" data-cat="all" onclick="filterCategory('all', this)">All Silhouettes</button>
        <button class="filter-tab" data-cat="coord" onclick="filterCategory('coord', this)">Co-ord Sets</button>
        <button class="filter-tab" data-cat="festive" onclick="filterCategory('festive', this)">Festive Suits</button>
        <button class="filter-tab" data-cat="dress" onclick="filterCategory('dress', this)">Midi Dresses</button>
        <button class="filter-tab" data-cat="top" onclick="filterCategory('top', this)">Tops &amp; Blouses</button>"""

if tabs_old in snitch_code:
    snitch_code = snitch_code.replace(tabs_old, tabs_new)
    print("Replaced category tabs without counts in build_snitch_storefront.py")
else:
    # Individual replacements
    snitch_code = snitch_code.replace("All Silhouettes (16)", "All Silhouettes")
    snitch_code = snitch_code.replace("Co-ord Sets (4)", "Co-ord Sets")
    snitch_code = snitch_code.replace("Festive Suits (6)", "Festive Suits")
    snitch_code = snitch_code.replace("Midi Dresses (3)", "Midi Dresses")
    snitch_code = snitch_code.replace("Tops &amp; Blouses (3)", "Tops &amp; Blouses")
    print("Performed individual replacements on tabs in build_snitch_storefront.py")

# Update filterCategory JS function to set category name instead of raw count
old_count_js = """      // Update count badge
      var countEl = document.getElementById('activeCategoryCount');
      if (countEl) {{
        countEl.textContent = matchedCount + ' SILHOUETTES';
      }}"""

new_count_js = """      // Update category pill label
      var countEl = document.getElementById('activeCategoryCount');
      if (countEl) {{
        var catTitles = {{
          'all': 'HANDCRAFTED EDITIONS',
          'coord': 'CO-ORD SETS',
          'festive': 'FESTIVE SUITS',
          'dress': 'MIDI DRESSES',
          'top': 'TOPS & BLOUSES'
        }};
        countEl.textContent = catTitles[cat] || 'HANDCRAFTED EDITIONS';
      }}"""

if old_count_js in snitch_code:
    snitch_code = snitch_code.replace(old_count_js, new_count_js)
    print("Updated filterCategory JS function to show category name pill.")
else:
    print("WARNING: old_count_js not matched exactly, checking alternate pattern...")
    alt_old = "countEl.textContent = matchedCount + ' SILHOUETTES';"
    alt_new = """var catTitles = { 'all': 'HANDCRAFTED EDITIONS', 'coord': 'CO-ORD SETS', 'festive': 'FESTIVE SUITS', 'dress': 'MIDI DRESSES', 'top': 'TOPS & BLOUSES' }; countEl.textContent = catTitles[cat] || 'HANDCRAFTED EDITIONS';"""
    if alt_old in snitch_code:
        snitch_code = snitch_code.replace(alt_old, alt_new)
        print("Replaced alt_old in filterCategory.")

# Founder stats row
snitch_code = snitch_code.replace('<span class="stat-val">16 Silhouettes</span>', '<span class="stat-val">Signature Capsule</span>')

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(snitch_code)

print("Saved clean build_snitch_storefront.py!")

# 2. Update build_shopify_theme.py
with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    shopify_code = f.read()

shopify_code = shopify_code.replace("The Debut 16 Silhouettes", "Signature Silhouettes")
shopify_code = shopify_code.replace("All Silhouettes (16)", "All Silhouettes")
shopify_code = shopify_code.replace("Co-ord Sets (4)", "Co-ord Sets")
shopify_code = shopify_code.replace("Festive Suits (6)", "Festive Suits")
shopify_code = shopify_code.replace("Midi Dresses (3)", "Midi Dresses")
shopify_code = shopify_code.replace("Tops &amp; Blouses (3)", "Tops &amp; Blouses")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(shopify_code)

print("Saved clean build_shopify_theme.py!")

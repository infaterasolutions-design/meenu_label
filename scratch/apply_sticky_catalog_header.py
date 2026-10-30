import os

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Catalog section HTML
old_cat_header = """  <!-- Catalog Section -->
  <section class="catalog-section" id="catalog">
    <div class="section-header">
      <div>
        <h2 class="section-title">The Debut 16 Silhouettes</h2>
        <p class="section-sub">Authentic catalog pieces ordered from Surat. Strictly 3 exclusive pieces per design (1 each in M, L, XL).</p>
      </div>

      <div class="filter-tabs">
        <button class="filter-tab active" onclick="filterCategory('all', this)">All (16)</button>
        <button class="filter-tab" onclick="filterCategory('coord', this)">Co-ord Sets (4)</button>
        <button class="filter-tab" onclick="filterCategory('festive', this)">Festive Suits (6)</button>
        <button class="filter-tab" onclick="filterCategory('dress', this)">Dresses (3)</button>
        <button class="filter-tab" onclick="filterCategory('top', this)">Tops & Blouses (3)</button>
      </div>
    </div>"""

new_cat_header = """  <!-- Catalog Section -->
  <section class="catalog-section" id="catalog">
    <!-- Sticky Category Selection Header Bar -->
    <div class="sticky-catalog-header" id="stickyCatalogHeader">
      <div class="sticky-header-info">
        <div style="display:flex; align-items:center; gap:10px;">
          <h2 class="section-title" style="margin:0; font-size:22px; letter-spacing:0.02em;">The Debut 16 Silhouettes</h2>
          <span class="sticky-count-pill" id="activeCategoryCount">16 SILHOUETTES</span>
        </div>
        <p class="section-sub" style="margin:4px 0 0 0; font-size:12px;">Limited Atelier Run &bull; Strictly 1 piece per size (M, L, XL)</p>
      </div>

      <div class="filter-tabs">
        <button class="filter-tab active" data-cat="all" onclick="filterCategory('all', this)">All Silhouettes (16)</button>
        <button class="filter-tab" data-cat="coord" onclick="filterCategory('coord', this)">Co-ord Sets (4)</button>
        <button class="filter-tab" data-cat="festive" onclick="filterCategory('festive', this)">Festive Suits (6)</button>
        <button class="filter-tab" data-cat="dress" onclick="filterCategory('dress', this)">Midi Dresses (3)</button>
        <button class="filter-tab" data-cat="top" onclick="filterCategory('top', this)">Tops &amp; Blouses (3)</button>
      </div>
    </div>"""

if old_cat_header in code:
    code = code.replace(old_cat_header, new_cat_header)
    print("Replaced catalog header with sticky-catalog-header successfully.")
else:
    # Substring search
    cat_start = code.find('id="catalog"')
    if cat_start != -1:
        p_grid = code.find('id="productGrid"', cat_start)
        old_slice = code[cat_start-len('<section class="catalog-section" '):p_grid]
        code = code[:cat_start-len('<section class="catalog-section" ')] + new_cat_header + "\n\n    " + code[p_grid:]
        print("Replaced catalog header via substring search.")

# 2. Add CSS for sticky-catalog-header
sticky_css = """
    /* Sticky Category Selection Header */
    .sticky-catalog-header {{
      position: sticky;
      top: 108px;
      z-index: 85;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 14px 28px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      transition: all 0.25s ease;
    }}
    .sticky-header-info {{
      display: flex;
      flex-direction: column;
    }}
    .sticky-count-pill {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--accent-gold);
      text-transform: uppercase;
    }}
"""

if ".sticky-catalog-header" not in code:
    pos_sec_header = code.find('.section-header {{')
    if pos_sec_header != -1:
        code = code[:pos_sec_header] + sticky_css + "\n    " + code[pos_sec_header:]
        print("Inserted sticky-catalog-header CSS.")

# 3. Update filterCategory function to not jump/scroll up if user is already browsing the catalog
old_fc = """    function filterCategory(cat, btn) {
      closeProductPage();
      var cards = document.querySelectorAll('.product-card');
      cards.forEach(function(card) {
        if (cat === 'all' || card.getAttribute('data-category') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
      if (btn) {
        document.querySelectorAll('.filter-tab').forEach(function(t) { t.classList.remove('active'); });
        btn.classList.add('active');
        document.querySelectorAll('.nav-links-desktop a').forEach(function(l) { l.classList.remove('active'); });
      }
      document.getElementById('catalog').scrollIntoView({ behavior: 'smooth' });
    }"""

new_fc = """    function filterCategory(cat, btn) {{
      closeProductPage();
      var cards = document.querySelectorAll('.product-card');
      var matchedCount = 0;
      cards.forEach(function(card) {{
        if (cat === 'all' || card.getAttribute('data-category') === cat) {{
          card.style.display = 'flex';
          matchedCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      // Update active state on matching tabs
      document.querySelectorAll('.filter-tab').forEach(function(t) {{
        t.classList.remove('active');
        if (t.getAttribute('data-cat') === cat) {{
          t.classList.add('active');
        }}
      }});
      if (btn) btn.classList.add('active');

      // Update count badge
      var countEl = document.getElementById('activeCategoryCount');
      if (countEl) {{
        countEl.textContent = matchedCount + ' SILHOUETTES';
      }}

      // Only scroll down to catalog if the user is currently ABOVE the catalog (e.g. up in the hero banner)
      var catalogEl = document.getElementById('catalog');
      if (catalogEl) {{
        var rect = catalogEl.getBoundingClientRect();
        if (rect.top > 160) {{
          catalogEl.scrollIntoView({{ behavior: 'smooth' }});
        }}
        // If already scrolling through the catalog, do NOT scroll up the page! The sticky bar filters instantly in place!
      }}
    }}"""

# Locate filterCategory
fc_pos = code.find('function filterCategory(cat, btn)')
if fc_pos != -1:
    fc_end = code.find('}\n\n    /* Search Products */', fc_pos)
    if fc_end == -1:
        fc_end = code.find('}}\n\n    /* Search Products */', fc_pos)
    if fc_end == -1:
        fc_end = code.find('}\n    /* Search Products */', fc_pos)
    if fc_end != -1:
        # Include closing brace
        brace_end = code.find('}', fc_end) + 1
        if code[brace_end:brace_end+1] == '}':
            brace_end += 1
        code = code[:fc_pos] + new_fc + "\n\n    " + code[brace_end:].lstrip()
        print("Replaced filterCategory function successfully with in-place sticky filtering.")

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py with sticky category selection bar!")

import os

paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\sections\featured-collection.liquid',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\featured-collection.liquid'
]

for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update filter-tabs to use buttons with filterCategory
    old_tabs = """    <div class="filter-tabs">
      <a href="/collections/all" class="filter-tab active">All Silhouettes</a>
      <a href="/collections/co-ord-sets" class="filter-tab">Co-ord Sets</a>
      <a href="/collections/festive-suits" class="filter-tab">Festive Suits</a>
      <a href="/collections/dresses" class="filter-tab">Midi Dresses</a>
      <a href="/collections/tops" class="filter-tab">Casual Tops</a>
    </div>"""

    new_tabs = """    <div class="filter-tabs">
      <button type="button" class="filter-tab active" data-cat="all" onclick="filterCategory('all', this)">All Silhouettes</button>
      <button type="button" class="filter-tab" data-cat="co-ord-sets" onclick="filterCategory('co-ord', this)">Co-ord Sets</button>
      <button type="button" class="filter-tab" data-cat="festive-suits" onclick="filterCategory('festive', this)">Festive Suits</button>
      <button type="button" class="filter-tab" data-cat="dresses" onclick="filterCategory('dress', this)">Midi Dresses</button>
      <button type="button" class="filter-tab" data-cat="tops" onclick="filterCategory('top', this)">Casual Tops</button>
    </div>"""

    norm_content = content.replace('\r\n', '\n')
    norm_old_tabs = old_tabs.replace('\r\n', '\n')
    norm_new_tabs = new_tabs.replace('\r\n', '\n')
    
    if norm_old_tabs in norm_content:
        norm_content = norm_content.replace(norm_old_tabs, norm_new_tabs)
        print(f"Replaced filter-tabs in {p}")
    
    # 2. Add id="productGrid"
    norm_content = norm_content.replace('<div class="product-grid">', '<div class="product-grid" id="productGrid">')
    
    # 3. Update preview card clicks and add data-category
    norm_content = norm_content.replace(
        '<div class="product-card" onclick="window.location.href=\'/collections/festive-suits\'">',
        '<div class="product-card" data-category="festive-suits festive" onclick="window.location.href=\'/collections/all\'">'
    )
    norm_content = norm_content.replace(
        '<div class="product-card" onclick="window.location.href=\'/collections/co-ord-sets\'">',
        '<div class="product-card" data-category="co-ord-sets co-ord" onclick="window.location.href=\'/collections/all\'">'
    )
    norm_content = norm_content.replace(
        '<div class="product-card" onclick="window.location.href=\'/collections/dresses\'">',
        '<div class="product-card" data-category="dresses dress" onclick="window.location.href=\'/collections/all\'">'
    )
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(norm_content)
    print(f"Updated {p} successfully")

import os, json, re

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update js_products_data to include all metadata
old_js_prod = """js_products_data = json.dumps([{
    "id": p["id"],
    "code": p["code"],
    "name": p["name"],
    "price": p["price"],
    "mrp": p["mrp"],
    "desc": p["desc"],
    "fabric": p["fabric"],
    "badge": p["badge"],
    "badge_class": p["badge_class"],
    "b64": p["b64"]
} for p in products])"""

new_js_prod = """js_products_data = json.dumps([{
    "id": p["id"],
    "code": p["code"],
    "name": p["name"],
    "category": p["category"],
    "cat_label": p["cat_label"],
    "fabric": p["fabric"],
    "color": p["color"],
    "price": p["price"],
    "mrp": p["mrp"],
    "desc": p["desc"],
    "badge": p["badge"],
    "badge_class": p["badge_class"],
    "b64": p["b64"]
} for p in products])"""

if old_js_prod in code:
    code = code.replace(old_js_prod, new_js_prod)
    print("Updated js_products_data with category, cat_label, and color")
else:
    print("Could not find exact old_js_prod, checking alternative...")
    p_pos = code.find('js_products_data = json.dumps([')
    p_end = code.find('} for p in products])') + len('} for p in products])')
    if p_pos != -1 and p_end != -1:
        code = code[:p_pos] + new_js_prod + code[p_end:]
        print("Replaced js_products_data via range")

# 2. Update cards_html to clearly separate card click (Full PDP) vs Quick View button click
new_card_code = '''cards_html = ""
for p in products:
    discount = round(((p["mrp"] - p["price"]) / p["mrp"]) * 100)
    cards_html += f"""
    <div class="product-card" data-category="{p['category']}" data-id="{p['id']}" onclick="openProductPage('{p['id']}')">
      <div class="card-thumb">
        <span class="card-badge {p['badge_class']}">{p['badge']}</span>
        <button class="card-wishlist-btn" onclick="event.stopPropagation(); toggleWishlistProduct('{p['id']}')" title="Save to Wishlist" id="wishBtn_{p['id']}" aria-label="Save to Wishlist">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
        </button>
        <img src="{p['b64']}" alt="{p['name']}" loading="lazy">
        <div class="card-quick-actions">
          <button class="btn-quick-view" onclick="event.stopPropagation(); openQuickView('{p['id']}')" title="Quick View">QUICK VIEW</button>
        </div>
      </div>
      <div class="card-body">
        <span class="card-cat">{p['cat_label']}</span>
        <h3 class="card-title">{p['name']}</h3>
        <div class="card-fabric">{p['fabric']}</div>
        <div class="card-price-row">
          <span class="price-main">&#8377;{p['price']:,}</span>
          <span class="price-mrp">&#8377;{p['mrp']:,}</span>
          <span class="price-discount">{discount}% OFF</span>
        </div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'M')">M (38)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'L')">L (40)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'XL')">XL (42)</span>
          </div>
          <span class="stock-chip">Only 3 Left</span>
        </div>
      </div>
    </div>
    """'''

c_start = code.find('cards_html = ""\nfor p in products:')
c_end = code.find('js_products_data = json.dumps([')
if c_start != -1 and c_end != -1:
    code = code[:c_start] + new_card_code + "\n\n" + code[c_end:]
    print("Replaced cards_html generation with openProductPage on card and openQuickView on button.")

# 3. Add PDP CSS styles
pdp_css = """
    /* =========================================================================
       DEDICATED FULL PRODUCT DETAIL PAGE (PDP) ARCHITECTURE
       ========================================================================= */
    .pdp-section {{
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      padding: 32px 36px 80px;
    }}
    .pdp-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      gap: 16px;
      flex-wrap: wrap;
    }}
    .pdp-back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 8px 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .pdp-back-btn:hover {{
      background: var(--text-main);
      color: #FFFFFF;
      border-color: var(--text-main);
      transform: translateX(-3px);
    }}
    .pdp-breadcrumb {{
      font-size: 12px;
      color: var(--text-muted);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      font-weight: 500;
    }}
    .pdp-breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .pdp-breadcrumb a:hover {{
      color: var(--accent-gold);
    }}

    /* 2-Column Luxury PDP Layout */
    .pdp-grid {{
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 56px;
      align-items: flex-start;
    }}
    @media (max-width: 992px) {{
      .pdp-grid {{
        grid-template-columns: 1fr;
        gap: 36px;
      }}
    }}

    /* Left Gallery */
    .pdp-gallery-col {{
      position: sticky;
      top: 100px;
    }}
    .pdp-main-image-wrap {{
      position: relative;
      width: 100%;
      border-radius: 12px;
      overflow: hidden;
      background: #F4EFEB;
      border: 1px solid var(--border-color);
      box-shadow: 0 12px 30px rgba(0,0,0,0.04);
    }}
    .pdp-main-image {{
      width: 100%;
      aspect-ratio: 4 / 5;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.4s ease;
    }}
    .pdp-main-image-wrap:hover .pdp-main-image {{
      transform: scale(1.02);
    }}
    .pdp-gallery-badges {{
      position: absolute;
      top: 18px;
      left: 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 2;
    }}
    .pdp-badge-pill {{
      background: rgba(24, 22, 20, 0.9);
      backdrop-filter: blur(8px);
      color: #FFFFFF;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 16px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .pdp-badge-gold {{
      background: #B8860B;
      color: #FFFFFF;
    }}
    .pdp-wishlist-toggle {{
      position: absolute;
      top: 18px;
      right: 18px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(0,0,0,0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 3;
      transition: all 0.2s ease;
      color: #222;
      padding: 0;
    }}
    .pdp-wishlist-toggle:hover {{
      background: #FFFFFF;
      transform: scale(1.1);
      color: #E53935;
    }}
    .pdp-wishlist-toggle.active {{
      color: #E53935;
    }}
    .pdp-wishlist-toggle.active svg {{
      fill: #E53935;
      stroke: #E53935;
    }}
    .pdp-trust-pills {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 18px;
    }}
    .pdp-trust-pill {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      font-size: 11px;
      color: var(--text-main);
      font-weight: 600;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }}
    .pdp-trust-pill-icon {{
      font-size: 18px;
    }}

    /* Right Information & Purchase Column */
    .pdp-info-col {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .pdp-tag-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .pdp-collection-tag {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-gold);
    }}
    .pdp-code-tag {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }}
    .pdp-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 34px;
      line-height: 1.15;
      font-weight: 600;
      color: var(--text-main);
      margin: 0;
    }}
    .pdp-price-row {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-color);
    }}
    .pdp-price-main {{
      font-size: 28px;
      font-weight: 800;
      color: var(--text-main);
    }}
    .pdp-price-mrp {{
      font-size: 18px;
      color: var(--text-muted);
      text-decoration: line-through;
    }}
    .pdp-price-discount {{
      background: #E8F5E9;
      color: #2E7D32;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 12px;
    }}
    .pdp-tax-note {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: -6px;
    }}

    /* Scarcity Banner */
    .pdp-scarcity-banner {{
      background: #FFF9E6;
      border: 1px solid #FFE082;
      border-radius: 8px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12px;
      color: #8D6E1A;
      font-weight: 600;
      line-height: 1.4;
    }}
    .pdp-scarcity-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #D97706;
      flex-shrink: 0;
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.2);
    }}

    /* Meta Highlights */
    .pdp-meta-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px 16px;
      font-size: 13px;
    }}
    .pdp-meta-label {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 2px;
    }}
    .pdp-meta-val {{
      font-weight: 600;
      color: var(--text-main);
    }}

    /* Size Selection */
    .pdp-size-section {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .pdp-size-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .pdp-size-label {{
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-main);
    }}
    .pdp-size-chart-link {{
      font-size: 12px;
      font-weight: 600;
      color: var(--accent-gold);
      cursor: pointer;
      text-decoration: underline;
    }}
    .pdp-size-pills {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }}
    .pdp-size-btn {{
      background: #FFFFFF;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 10px;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }}
    .pdp-size-btn:hover {{
      border-color: var(--text-main);
      background: var(--bg-surface);
    }}
    .pdp-size-btn.selected {{
      border-color: var(--text-main);
      background: var(--text-main);
      color: #FFFFFF;
    }}
    .pdp-size-btn.selected .pdp-size-sub {{
      color: rgba(255, 255, 255, 0.8);
    }}
    .pdp-size-btn.selected .pdp-size-stock {{
      color: #FFD54F;
    }}
    .pdp-size-name {{
      font-size: 15px;
      font-weight: 700;
    }}
    .pdp-size-sub {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .pdp-size-stock {{
      font-size: 10px;
      font-weight: 700;
      color: #D97706;
      text-transform: uppercase;
    }}

    /* Actions */
    .pdp-actions-row {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 4px;
    }}
    .pdp-btn-primary {{
      width: 100%;
      background: var(--text-main);
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 16px 24px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}
    .pdp-btn-primary:hover {{
      background: #333333;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    }}
    .pdp-btn-buy {{
      width: 100%;
      background: #B8860B;
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 14px 24px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .pdp-btn-buy:hover {{
      background: #996F07;
      transform: translateY(-2px);
    }}
    .pdp-btn-whatsapp {{
      width: 100%;
      background: #25D366;
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 14px 20px;
      font-family: inherit;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.2s ease;
    }}
    .pdp-btn-whatsapp:hover {{
      background: #1EBE5D;
      transform: translateY(-2px);
    }}

    /* Accordions */
    .pdp-accordions {{
      display: flex;
      flex-direction: column;
      border-top: 1px solid var(--border-color);
      margin-top: 10px;
    }}
    .pdp-accordion-item {{
      border-bottom: 1px solid var(--border-color);
    }}
    .pdp-accordion-header {{
      padding: 16px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--text-main);
      transition: color 0.2s;
    }}
    .pdp-accordion-header:hover {{
      color: var(--accent-gold);
    }}
    .pdp-accordion-icon {{
      font-size: 18px;
      transition: transform 0.2s ease;
    }}
    .pdp-accordion-content {{
      padding: 0 0 16px 0;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text-main);
      display: none;
    }}
    .pdp-accordion-item.open .pdp-accordion-content {{
      display: block;
    }}
    .pdp-accordion-item.open .pdp-accordion-icon {{
      transform: rotate(45deg);
    }}

    /* Related Section */
    .pdp-related-section {{
      margin-top: 80px;
      padding-top: 40px;
      border-top: 1px solid var(--border-color);
    }}
    .pdp-related-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 28px;
      font-weight: 600;
      margin-bottom: 6px;
    }}
    .pdp-related-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}
    .pdp-related-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }}
    @media (max-width: 900px) {{
      .pdp-related-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}
"""

style_end = code.find('</style>')
if style_end != -1:
    code = code[:style_end] + pdp_css + "\n  " + code[style_end:]
    print("Added PDP CSS successfully")

# 4. Wrap Home sections with <div id="storefrontHomeView"> and update Hero banners to call openProductPage
hero_start = code.find('<section class="snitch-hero-section">')
founder_end = code.find('</section><!-- founder -->')
if founder_end == -1:
    f_pos = code.find('id="founder"')
    founder_end = code.find('</section>', f_pos) + 10

# Replace openProductModal on slides with openProductPage
# Slide 1:
code = code.replace("onclick=\"openProductModal('JAB26ST05010')\"", "onclick=\"openProductPage('JAB26ST05010')\"")
code = code.replace("onclick=\"event.stopPropagation(); openProductModal('JAB26ST05010')\"", "onclick=\"event.stopPropagation(); openProductPage('JAB26ST05010')\"")

# Slide 2:
code = code.replace("onclick=\"openProductModal('JAC25ST03063')\"", "onclick=\"openProductPage('JAC25ST03063')\"")
code = code.replace("onclick=\"event.stopPropagation(); openProductModal('JAC25ST03063')\"", "onclick=\"event.stopPropagation(); openProductPage('JAC25ST03063')\"")

# Slide 3:
code = code.replace("onclick=\"openProductModal('JAA26DR03942')\"", "onclick=\"openProductPage('JAA26DR03942')\"")
code = code.replace("onclick=\"event.stopPropagation(); openProductModal('JAA26DR03942')\"", "onclick=\"event.stopPropagation(); openProductPage('JAA26DR03942')\"")

# Slide 4:
code = code.replace("onclick=\"openProductModal('SET916')\"", "onclick=\"openProductPage('SET916')\"")
code = code.replace("onclick=\"event.stopPropagation(); openProductModal('SET916')\"", "onclick=\"event.stopPropagation(); openProductPage('SET916')\"")

# Re-locate hero_start and founder_end after replaces
hero_start = code.find('<section class="snitch-hero-section">')
f_pos = code.find('id="founder"')
founder_end = code.find('</section>', f_pos) + 10

# Wrap storefrontHomeView
home_html = code[hero_start:founder_end]

pdp_html = """
  <!-- DEDICATED FULL PRODUCT DETAIL VIEW (PDP) -->
  <div id="productDetailView" style="display:none;">
    <div class="pdp-section">
      <!-- PDP Top Navigation & Breadcrumbs -->
      <div class="pdp-top-bar">
        <button class="pdp-back-btn" onclick="closeProductPage()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          BACK TO DROP 01
        </button>
        <div class="pdp-breadcrumb">
          <a href="javascript:void(0)" onclick="closeProductPage()">HOME</a> &nbsp;/&nbsp;
          <span id="pdpBreadcrumbCat">FESTIVE SUITS</span> &nbsp;/&nbsp;
          <span id="pdpBreadcrumbTitle" style="color:var(--text-main); font-weight:700;">JAIPUR CHANDERI SILK FESTIVE SUIT</span>
        </div>
      </div>

      <!-- Main PDP 2-Column Grid -->
      <div class="pdp-grid">
        <!-- Left: Visual Gallery -->
        <div class="pdp-gallery-col">
          <div class="pdp-main-image-wrap">
            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">DROP 01 STAR</span>
              <span class="pdp-badge-pill pdp-badge-gold">STRICTLY 3 PIECES CRAFTED</span>
            </div>
            <button class="pdp-wishlist-toggle" id="pdpWishlistBtn" onclick="togglePdpWishlist()" title="Save to Wishlist" aria-label="Save to Wishlist">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </button>
            <img id="pdpMainImg" src="" alt="Silhouette" class="pdp-main-image">
          </div>

          <!-- Trust Badges -->
          <div class="pdp-trust-pills">
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#10024;</span>
              <span>Chandigarh Atelier</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Handcrafted Precision</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128666;</span>
              <span>Free 24-Hr Express</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Tricity Priority Courier</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128207;</span>
              <span>Complimentary Fit</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Studio Hem Adjustments</span>
            </div>
          </div>
        </div>

        <!-- Right: Comprehensive Product Info & Checkout Actions -->
        <div class="pdp-info-col">
          <div class="pdp-tag-row">
            <span class="pdp-collection-tag">MEENU LABEL &bull; AUTUMN/WINTER 2026 DEBUT</span>
            <span class="pdp-code-tag" id="pdpCodeTag">STYLE #JAB26ST05010</span>
          </div>

          <h1 class="pdp-title" id="pdpTitle">Jaipur Chanderi Silk Festive Suit</h1>

          <div class="pdp-price-row">
            <span class="pdp-price-main" id="pdpPriceMain">&#8377;2,299</span>
            <span class="pdp-price-mrp" id="pdpPriceMrp">&#8377;3,699</span>
            <span class="pdp-price-discount" id="pdpDiscount">38% OFF</span>
          </div>
          <div class="pdp-tax-note">Inclusive of all taxes &bull; Free express delivery across India</div>

          <!-- Scarcity Callout -->
          <div class="pdp-scarcity-banner">
            <span class="pdp-scarcity-dot"></span>
            <span>STRICT ATELIER SCARCITY: Strictly 1 piece per size (M, L, XL). Only 3 pieces produced nationwide.</span>
          </div>

          <!-- Meta Highlights Grid -->
          <div class="pdp-meta-grid">
            <div>
              <div class="pdp-meta-label">Fabric & Weave</div>
              <div class="pdp-meta-val" id="pdpMetaFabric">Chanderi Silk & Zari with Organza Dupatta</div>
            </div>
            <div>
              <div class="pdp-meta-label">Color Palette</div>
              <div class="pdp-meta-val" id="pdpMetaColor">Warm Mustard & Fuchsia</div>
            </div>
          </div>

          <!-- Size Selection -->
          <div class="pdp-size-section">
            <div class="pdp-size-header">
              <span class="pdp-size-label">Select Size (Standard Indian Pret)</span>
              <span class="pdp-size-chart-link" onclick="openSizeGuide()">&#128207; View Detailed Measurements</span>
            </div>
            <div class="pdp-size-pills">
              <button type="button" class="pdp-size-btn selected" id="pdpSizeBtn_M" onclick="selectPdpSize('M', this)">
                <span class="pdp-size-name">M (38)</span>
                <span class="pdp-size-sub">Bust 38" | Waist 34"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_L" onclick="selectPdpSize('L', this)">
                <span class="pdp-size-name">L (40)</span>
                <span class="pdp-size-sub">Bust 40" | Waist 36"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
          </div>

          <!-- Actions -->
          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>
            <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="#" target="_blank">
              <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
            </a>
          </div>

          <!-- Pincode Checker -->
          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:8px; padding:14px 16px;">
            <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.08em; font-weight:700; color:var(--text-muted); margin-bottom:8px;">Check Express Dispatch to Your Pincode</div>
            <div style="display:flex; gap:8px;">
              <input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" style="flex:1; padding:8px 12px; border:1px solid var(--border-color); border-radius:4px; font-size:13px; outline:none; background:#FFF;">
              <button onclick="checkPdpPincode()" style="padding:8px 16px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">CHECK</button>
            </div>
            <div id="pdpPincodeResult" style="font-size:12px; margin-top:8px; font-weight:600; display:none;"></div>
          </div>

          <!-- Accordions -->
          <div class="pdp-accordions">
            <div class="pdp-accordion-item open">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>The Silhouette & Drape</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content" id="pdpDescContent"></div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Fabric & Handloom Heritage</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content" id="pdpFabricContent"></div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Garment Care & Maintenance</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content">
                Professional dry clean recommended for silk and Chanderi pret to preserve natural luster and delicate zari embroidery. Cotton silhouettes can be gently hand-washed in cold water using mild detergent. Always steam iron on reverse side. Store in the breathable archival muslin dust bag provided with your order.
              </div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Complimentary Atelier Alterations & Returns</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content">
                Because each Drop 01 silhouette is strictly 1 piece per size, we provide complimentary bespoke sleeve and hem tailoring at our Sector 17-C Chandigarh Design Studio or through our WhatsApp styling team. Standard 7-day hassle-free exchange policy applies if unworn and tags remain intact.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Curated Recommendations (Complete The Look) -->
      <div class="pdp-related-section">
        <h3 class="pdp-related-title">Complete The Look &bull; Curated Drop 01 Pieces</h3>
        <p class="pdp-related-sub">Other strictly limited silhouettes from our Autumn/Winter 2026 debut</p>
        <div class="pdp-related-grid" id="pdpRelatedGrid">
          <!-- Dynamically populated with 4 other silhouettes -->
        </div>
      </div>
    </div>
  </div>
"""

wrapped_home = f"""<!-- Main Storefront Home View (Hero, Filter Tabs, 16 Silhouettes Grid, Founder) -->
  <div id="storefrontHomeView">
{home_html}
  </div>

{pdp_html}"""

code = code[:hero_start] + wrapped_home + code[founder_end:]
print("Wrapped Home sections and inserted Product Detail Page markup successfully.")

# 5. In Quick View modal: add "VIEW FULL PRODUCT PAGE & MEASUREMENTS →" button
old_qv_btn = """<button class="modal-btn-primary" onclick="addCurrentProductToCart()">ADD TO BAG</button>"""
new_qv_btn = """<button class="modal-btn-primary" onclick="addCurrentProductToCart()">ADD TO BAG</button>
        <button type="button" onclick="closeModal(); openProductPage(activeModalProduct.id);" style="width:100%; margin-top:8px; background:var(--bg-surface); color:var(--text-main); border:1px solid var(--border-color); border-radius:4px; padding:10px; font-size:11px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; cursor:pointer; transition:all 0.2s;">VIEW FULL PRODUCT PAGE &amp; DETAILS &rarr;</button>"""

if old_qv_btn in code:
    code = code.replace(old_qv_btn, new_qv_btn)
    print("Added 'VIEW FULL PRODUCT PAGE' button into Quick View modal.")

# 6. Add PDP JavaScript functions
pdp_js = """
    /* =========================================================================
       DEDICATED FULL PRODUCT DETAIL PAGE (PDP) LOGIC
       ========================================================================= */
    var activePdpProductId = null;
    var pdpSelectedSize = 'M';

    function openQuickView(prodId) {{
      openProductModal(prodId);
    }}

    function openProductPage(prodId) {{
      var p = productsData.find(function(item) {{ return item.id === prodId; }});
      if (!p) return;

      activePdpProductId = prodId;
      pdpSelectedSize = 'M';

      // Close Quick View modal if open
      closeModal();

      // Update browser hash
      try {{
        window.location.hash = '#product-' + prodId;
      }} catch(e) {{}}

      // Switch views: Hide Home view, Show PDP view
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (homeView) homeView.style.display = 'none';
      if (pdpView) pdpView.style.display = 'block';

      // Scroll smoothly to top
      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      // Breadcrumbs
      var breadCat = document.getElementById('pdpBreadcrumbCat');
      if (breadCat) breadCat.textContent = (p.cat_label || 'Collection').toUpperCase();
      var breadTitle = document.getElementById('pdpBreadcrumbTitle');
      if (breadTitle) breadTitle.textContent = (p.name + ' (' + p.code + ')').toUpperCase();

      // Main Visual
      var mainImg = document.getElementById('pdpMainImg');
      if (mainImg) {{
        mainImg.src = p.b64;
        mainImg.alt = p.name;
      }}
      var badgePill = document.getElementById('pdpBadgePill');
      if (badgePill) badgePill.textContent = (p.badge || 'Drop 01 Exclusive').toUpperCase();

      // Wishlist toggle state
      var wishBtn = document.getElementById('pdpWishlistBtn');
      if (wishBtn) {{
        if (wishlist.indexOf(p.id) !== -1) {{
          wishBtn.classList.add('active');
        }} else {{
          wishBtn.classList.remove('active');
        }}
      }}

      // Titles & Code
      var codeTag = document.getElementById('pdpCodeTag');
      if (codeTag) codeTag.textContent = 'STYLE #' + p.code;
      var titleEl = document.getElementById('pdpTitle');
      if (titleEl) titleEl.textContent = p.name;

      // Price block
      var priceMain = document.getElementById('pdpPriceMain');
      if (priceMain) priceMain.innerHTML = '&#8377;' + p.price.toLocaleString('en-IN');
      var priceMrp = document.getElementById('pdpPriceMrp');
      if (priceMrp) priceMrp.innerHTML = '&#8377;' + p.mrp.toLocaleString('en-IN');
      var discEl = document.getElementById('pdpDiscount');
      if (discEl) {{
        var discount = Math.round(((p.mrp - p.price) / p.mrp) * 100);
        discEl.textContent = discount + '% OFF';
      }}

      // Meta highlights
      var metaFabric = document.getElementById('pdpMetaFabric');
      if (metaFabric) metaFabric.textContent = p.fabric || 'Pure Artisanal Fabric';
      var metaColor = document.getElementById('pdpMetaColor');
      if (metaColor) metaColor.textContent = p.color || 'Artisanal Palette';

      // Accordion contents
      var descContent = document.getElementById('pdpDescContent');
      if (descContent) descContent.textContent = p.desc;
      var fabContent = document.getElementById('pdpFabricContent');
      if (fabContent) fabContent.textContent = (p.fabric || 'Luxury Weave') + '. Meticulously hand-loomed with precision thread density and finished by master artisans in Jaipur and Surat. Exceptionally soft on skin, breathable, and designed for a flattering luxury drape.';

      // Reset Pincode
      var pinInp = document.getElementById('pdpPincodeInput');
      if (pinInp) pinInp.value = '';
      var pinRes = document.getElementById('pdpPincodeResult');
      if (pinRes) pinRes.style.display = 'none';

      // Size buttons
      selectPdpSize('M', document.getElementById('pdpSizeBtn_M'));

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, 'M');

      // Populate Curated Recommendations
      populatePdpRelated(p.id);
    }}

    function closeProductPage() {{
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (homeView) homeView.style.display = 'block';
      if (pdpView) pdpView.style.display = 'none';

      try {{
        window.location.hash = '#catalog';
      }} catch(e) {{}}

      if (activePdpProductId) {{
        var card = document.querySelector('.product-card[data-id="' + activePdpProductId + '"]');
        if (card) {{
          card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}
      }}
    }}

    function selectPdpSize(size, btn) {{
      pdpSelectedSize = size;
      document.querySelectorAll('.pdp-size-btn').forEach(function(b) {{
        b.classList.remove('selected');
      }});
      if (btn) {{
        btn.classList.add('selected');
      }} else {{
        var autoBtn = document.getElementById('pdpSizeBtn_' + size);
        if (autoBtn) autoBtn.classList.add('selected');
      }}
      var p = productsData.find(function(item) {{ return item.id === activePdpProductId; }});
      if (p) updatePdpWhatsAppLink(p, size);
    }}

    function updatePdpWhatsAppLink(product, size) {{
      var text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/919988898845?text=' + text;
    }}

    function addPdpProductToCart() {{
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }}

    function buyPdpProductNow() {{
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }}

    function togglePdpWishlist() {{
      if (!activePdpProductId) return;
      toggleWishlistProduct(activePdpProductId);
      var btn = document.getElementById('pdpWishlistBtn');
      if (btn) {{
        if (wishlist.indexOf(activePdpProductId) !== -1) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }}
    }}

    function checkPdpPincode() {{
      var pinInp = document.getElementById('pdpPincodeInput');
      var pinRes = document.getElementById('pdpPincodeResult');
      if (!pinInp || !pinRes) return;
      var pin = pinInp.value.trim();
      pinRes.style.display = 'block';

      if (pin.length !== 6 || isNaN(pin)) {{
        pinRes.style.color = '#E53935';
        pinRes.textContent = 'Please enter a valid 6-digit Indian PIN code.';
        return;
      }}

      // Tricity Pincodes (Chandigarh 160xxx, Mohali 140xxx / 160xxx, Panchkula 134xxx)
      if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {{
        pinRes.style.color = '#128C7E';
        pinRes.textContent = '✓ FREE 24-HR EXPRESS TRICITY DELIVERY: Dispatch directly from Sector 17 Atelier. Estimated delivery tomorrow before 6:00 PM via Private Courier.';
      }} else {{
        pinRes.style.color = '#128C7E';
        pinRes.textContent = '✓ EXPRESS AIR COURIER: Dispatch within 24 hours. Estimated delivery in 3 to 4 business days via BlueDart / Delhivery Air.';
      }}
    }}

    function togglePdpAccordion(headerEl) {{
      var item = headerEl.parentElement;
      item.classList.toggle('open');
    }}

    function populatePdpRelated(currentId) {{
      var container = document.getElementById('pdpRelatedGrid');
      if (!container) return;
      container.innerHTML = '';

      var related = productsData.filter(function(item) {{ return item.id !== currentId; }}).slice(0, 4);
      var html = '';
      related.forEach(function(r) {{
        var discount = Math.round(((r.mrp - r.price) / r.mrp) * 100);
        html += '<div class="product-card" onclick="openProductPage(\\'' + r.id + '\\')">';
        html += '<div class="card-thumb">';
        html += '<span class="card-badge ' + r.badge_class + '">' + r.badge + '</span>';
        html += '<button class="card-wishlist-btn" onclick="event.stopPropagation(); toggleWishlistProduct(\\'' + r.id + '\\')" title="Save to Wishlist">';
        html += '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        html += '</button>';
        html += '<img src="' + r.b64 + '" alt="' + r.name + '" loading="lazy">';
        html += '<div class="card-quick-actions">';
        html += '<button class="btn-quick-view" onclick="event.stopPropagation(); openQuickView(\\'' + r.id + '\\')">QUICK VIEW</button>';
        html += '</div>';
        html += '</div>';
        html += '<div class="card-body">';
        html += '<span class="card-cat">' + r.cat_label + '</span>';
        html += '<h3 class="card-title">' + r.name + '</h3>';
        html += '<div class="card-fabric">' + r.fabric + '</div>';
        html += '<div class="card-price-row">';
        html += '<span class="price-main">&#8377;' + r.price.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-mrp">&#8377;' + r.mrp.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-discount">' + discount + '% OFF</span>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
      }});
      container.innerHTML = html;
    }}
"""

js_insert_pos = code.find('/* Wishlist System */')
if js_insert_pos != -1:
    code = code[:js_insert_pos] + pdp_js + "\n\n    " + code[js_insert_pos:]
    print("Added PDP JS functions successfully")

# Also in header logo: when clicked, if on PDP, go back to collection
code = code.replace('<a href="#">\n          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">\n        </a>',
                    '<a href="javascript:void(0)" onclick="closeProductPage()">\n          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">\n        </a>')

# In filterCategory: make sure it closes PDP
code = code.replace("function filterCategory(cat, btn) {", "function filterCategory(cat, btn) {\n      closeProductPage();")
code = code.replace("function filterCategory(cat, btn) {{", "function filterCategory(cat, btn) {{\n      closeProductPage();")

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: Full Product Detail Page (PDP) integrated into build_snitch_storefront.py!")

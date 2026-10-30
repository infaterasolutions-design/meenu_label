import os, re, json

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update product cards generation:
# Add card-wishlist-btn with SVG heart, fix "QUICK VIEW ??" to "QUICK VIEW", and fix price "?" to "Rs. " or "₹"
old_card_pattern = r'cards_html = ""\s+for p in products:.*?cards_html \+= f"""(.*?)"""'
new_card_code = '''cards_html = ""
for p in products:
    discount = round(((p["mrp"] - p["price"]) / p["mrp"]) * 100)
    cards_html += f"""
    <div class="product-card" data-category="{p['category']}" data-id="{p['id']}">
      <div class="card-thumb" onclick="openProductModal('{p['id']}')">
        <span class="card-badge {p['badge_class']}">{p['badge']}</span>
        <button class="card-wishlist-btn" onclick="event.stopPropagation(); toggleWishlistProduct('{p['id']}')" title="Save to Wishlist" id="wishBtn_{p['id']}" aria-label="Save to Wishlist">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
        </button>
        <img src="{p['b64']}" alt="{p['name']}" loading="lazy">
        <div class="card-quick-actions">
          <button class="btn-quick-view" onclick="event.stopPropagation(); openProductModal('{p['id']}')">QUICK VIEW</button>
        </div>
      </div>
      <div class="card-body">
        <span class="card-cat">{p['cat_label']}</span>
        <h3 class="card-title" onclick="openProductModal('{p['id']}')">{p['name']}</h3>
        <div class="card-fabric">{p['fabric']}</div>
        <div class="card-price-row">
          <span class="price-main">&#8377;{p['price']:,}</span>
          <span class="price-mrp">&#8377;{p['mrp']:,}</span>
          <span class="price-discount">{discount}% OFF</span>
        </div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'M')">M (38)</span>
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'L')">L (40)</span>
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'XL')">XL (42)</span>
          </div>
          <span class="stock-chip">Only 3 Left</span>
        </div>
      </div>
    </div>
    """'''

# Let's replace the card loop
card_start = code.find('cards_html = ""\nfor p in products:')
card_end = code.find('js_products_data = json.dumps([')
if card_start != -1 and card_end != -1:
    code = code[:card_start] + new_card_code + "\n\n" + code[card_end:]
    print("Replaced cards_html generation successfully.")
else:
    print("WARNING: Could not locate cards_html generation section")

# 2. Update CSS in header section
css_start = code.find('header {')
if css_start == -1:
    css_start = code.find('header {{')
css_end = code.find('/* =========================================================================\n       SNITCH 1500x708')
if css_end == -1:
    css_end = code.find('/* =========================================================================\n     SNITCH 1500x708')
if css_end == -1:
    css_end = code.find('.snitch-hero-section')

new_header_css = """header {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 34px;
      z-index: 90;
      transition: all 0.3s ease;
    }}
    .header-bar {{
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
    }}
    .hamburger-btn {{
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-main);
      display: flex;
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
    }}

    .nav-links-desktop {{
      display: flex;
      gap: 24px;
      list-style: none;
    }}
    .nav-links-desktop a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      transition: color 0.15s;
    }}
    .nav-links-desktop a:hover, .nav-links-desktop a.active {{
      color: var(--accent-gold);
    }}

    .header-center {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex: 0 0 auto;
    }}
    .brand-logo-img {{
      height: 54px;
      width: auto;
      display: block;
      transition: transform 0.2s ease;
    }}
    .brand-logo-img:hover {{
      transform: scale(1.02);
    }}

    /* Snitch-Style Minimalist Outline Icons */
    .header-right {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 18px;
      flex: 1;
    }}
    .header-icon-action {{
      background: none;
      border: none;
      cursor: pointer;
      color: #111111;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      position: relative;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      padding: 0;
      transition: all 0.2s ease;
    }}
    .header-icon-action:hover {{
      color: var(--accent-gold);
      background: var(--bg-surface);
      transform: translateY(-1px);
    }}
    .header-icon-action svg {{
      width: 22px;
      height: 22px;
      display: block;
      stroke-width: 1.6;
    }}
    .header-badge-pill {{
      position: absolute;
      top: 4px;
      right: 2px;
      background: var(--text-main);
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 700;
      min-width: 16px;
      height: 16px;
      line-height: 16px;
      border-radius: 8px;
      text-align: center;
      padding: 0 4px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.18);
      pointer-events: none;
      transition: transform 0.2s ease, background 0.2s;
    }}
    .header-icon-action:hover .header-badge-pill {{
      background: var(--accent-gold);
    }}

    /* Slide-Down Search Overlay Bar */
    .search-overlay-bar {{
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      width: 100%;
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      box-shadow: 0 16px 36px rgba(0,0,0,0.08);
      padding: 24px 36px;
      transform: translateY(-10px);
      opacity: 0;
      pointer-events: none;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
      z-index: 89;
    }}
    .search-overlay-bar.open {{
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }}
    .search-overlay-inner {{
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
    }}
    .search-input-box {{
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
    }}
    .search-input-box svg {{
      width: 22px;
      height: 22px;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .search-input-box input {{
      flex: 1;
      border: none;
      outline: none;
      font-family: inherit;
      font-size: 17px;
      color: var(--text-main);
      background: transparent;
      letter-spacing: 0.3px;
    }}
    .search-input-box input::placeholder {{
      color: #999;
      font-size: 15px;
    }}
    .search-clear-btn {{
      background: none;
      border: none;
      font-size: 18px;
      color: #888;
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 4px;
      line-height: 1;
    }}
    .search-clear-btn:hover {{ color: #111; }}
    .search-quick-tags {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 12px;
    }}
    .quick-tag-label {{
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-size: 11px;
      margin-right: 4px;
    }}
    .quick-tag {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 5px 14px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      color: var(--text-main);
      transition: all 0.18s ease;
    }}
    .quick-tag:hover {{
      background: var(--text-main);
      color: #FFFFFF;
      border-color: var(--text-main);
    }}
    .search-close-action {{
      position: absolute;
      top: 0;
      right: 0;
      background: none;
      border: none;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      padding: 4px 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .search-close-action:hover {{ color: var(--text-main); }}

    /* Card Wishlist Button */
    .card-wishlist-btn {{
      position: absolute;
      top: 12px;
      right: 12px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(4px);
      border: 1px solid rgba(0,0,0,0.06);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 4;
      transition: all 0.2s ease;
      color: #333333;
      padding: 0;
    }}
    .card-wishlist-btn:hover {{
      background: #FFFFFF;
      transform: scale(1.1);
      color: #E53935;
    }}
    .card-wishlist-btn svg {{
      width: 18px;
      height: 18px;
      display: block;
      transition: fill 0.2s ease, stroke 0.2s ease;
    }}
    .card-wishlist-btn.active {{
      color: #E53935;
    }}
    .card-wishlist-btn.active svg {{
      fill: #E53935;
      stroke: #E53935;
    }}

    """

if css_start != -1 and css_end != -1:
    code = code[:css_start] + new_header_css + code[css_end:]
    print("Replaced header CSS successfully.")
else:
    print(f"WARNING: Could not locate header CSS boundaries (start={css_start}, end={css_end})")

# 3. Update <header> markup
html_header_start = code.find('<header>')
html_header_end = code.find('</header>') + 9

new_header_html = """<header>
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
        <a href="#">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">
        <!-- 1. Search -->
        <button class="header-icon-action" onclick="toggleSearchBar()" title="Search Drop 01" aria-label="Search">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="7.5"></circle>
            <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
          </svg>
        </button>

        <!-- 2. Shopping Bag -->
        <button class="header-icon-action" onclick="toggleCart()" title="Shopping Bag" aria-label="Shopping Bag">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
            <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
          </svg>
          <span class="header-badge-pill" id="headerCartCount">0</span>
        </button>

        <!-- 3. Wishlist (Heart) -->
        <button class="header-icon-action" onclick="toggleWishlistDrawer()" title="Saved Wishlist" aria-label="Wishlist">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="header-badge-pill" id="headerWishlistCount">0</span>
        </button>

        <!-- 4. User Account -->
        <button class="header-icon-action" onclick="openAccountModal()" title="Meenu Atelier VIP & Concierge" aria-label="Account">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="7.5" r="4"></circle>
            <path d="M5 20.5a7 7 0 0 1 14 0"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Slide-Down Search Overlay -->
    <div class="search-overlay-bar" id="searchOverlayBar">
      <div class="search-overlay-inner">
        <button class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>
        <div class="search-input-box">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="7.5"></circle>
            <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
          </svg>
          <input type="text" id="searchInput" placeholder="Search by silhouette, style code (e.g. JAB26ST05010), fabric, color..." onkeyup="searchProducts()">
          <button class="search-clear-btn" onclick="clearSearch()" title="Clear">&times;</button>
        </div>
        <div class="search-quick-tags">
          <span class="quick-tag-label">Popular Searches:</span>
          <button type="button" class="quick-tag" onclick="quickSearch('Festive')">Festive Suits</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Co-ord')">Co-ord Sets</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Chanderi')">Chanderi Silk</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Sharara')">Sharara</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Dress')">Midi Dress</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Cotton')">Pure Cotton</button>
        </div>
      </div>
    </div>
  </header>"""

if html_header_start != -1 and html_header_end != -1:
    code = code[:html_header_start] + new_header_html + code[html_header_end:]
    print("Replaced header HTML successfully.")
else:
    print(f"WARNING: Could not locate header HTML boundaries (start={html_header_start}, end={html_header_end})")

# 4. Add Wishlist Drawer and Account Modal before the closing </body> tag
modals_insert_pos = code.find('<!-- Cart Drawer -->')
new_drawers_html = """<!-- Wishlist Drawer -->
  <div class="cart-backdrop" id="wishlistBackdrop" onclick="toggleWishlistDrawer()"></div>
  <div class="cart-drawer" id="wishlistDrawer">
    <div class="cart-header">
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">Saved Wishlist (<span id="wishlistDrawerCount">0</span>)</h3>
      <button style="background:none; border:none; font-size:22px; cursor:pointer; color:var(--text-main);" onclick="toggleWishlistDrawer()">&times;</button>
    </div>
    <div class="cart-body" id="wishlistItemsList">
      <!-- Items dynamically injected -->
    </div>
    <div class="cart-footer" id="wishlistFooter" style="display:none;">
      <button class="modal-btn-primary" onclick="addAllWishlistToCart()" style="margin-bottom:8px;">ADD ALL TO BAG</button>
      <div style="font-size:11px; color:var(--text-muted); text-align:center;">
        Pieces reserved in your bag for 15 minutes
      </div>
    </div>
  </div>

  <!-- Account & Concierge Modal -->
  <div class="modal-backdrop" id="accountModalBackdrop" onclick="closeAccountModal(event)">
    <div class="product-modal" style="width: 540px; grid-template-columns: 1fr; padding: 36px 32px; border-radius: 14px;">
      <button class="modal-close" onclick="closeAccountModalDirect()">&times;</button>
      <div style="text-align:center; margin-bottom: 24px;">
        <div style="width:58px; height:58px; margin:0 auto 12px; border-radius:50%; background:var(--bg-surface); display:flex; align-items:center; justify-content:center; color:var(--accent-gold);">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="7.5" r="4"></circle>
            <path d="M5 20.5a7 7 0 0 1 14 0"></path>
          </svg>
        </div>
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; margin: 0 0 6px;">Meenu Label Atelier VIP</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin: 0;">Chandigarh Studio Fittings, Order Tracking & Master Stylist Concierge</p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 16px;">
        <!-- Track Order -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px;">
          <label style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 8px;">Track Drop 01 Order</label>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="trackOrderInput" placeholder="Enter Order ID (e.g. ML-84920)" style="flex:1; padding:9px 12px; border:1px solid var(--border-color); border-radius:4px; font-size:13px; outline:none;">
            <button onclick="trackOrderSubmit()" style="padding:9px 16px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">TRACK</button>
          </div>
          <div id="trackOrderResult" style="font-size:12px; margin-top:8px; font-weight:600; display:none;"></div>
        </div>

        <!-- WhatsApp Stylist -->
        <a href="https://wa.me/919988898845?text=Hello%20Meenu%20Label%2C%20I%20would%20like%20personal%20styling%20advice%20and%20sizing%20consultation%20for%20Drop%2001." target="_blank" style="display:flex; align-items:center; justify-content:space-between; background:#25D36615; border:1px solid #25D36640; border-radius:8px; padding:14px 16px; text-decoration:none; color:#075E54; transition:background 0.2s;">
          <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:24px;">&#128172;</span>
            <div>
              <div style="font-weight:700; font-size:13px; letter-spacing:0.3px;">WhatsApp Master Stylist Concierge</div>
              <div style="font-size:12px; color:#128C7E;">Direct atelier consultation & custom hem measurements</div>
            </div>
          </div>
          <span style="font-weight:700; font-size:16px;">&rarr;</span>
        </a>

        <!-- Atelier Studio Address -->
        <div style="border:1px solid var(--border-color); border-radius:8px; padding:14px 16px; display:flex; align-items:center; gap:12px;">
          <span style="font-size:22px;">&#128205;</span>
          <div>
            <div style="font-weight:700; font-size:13px; color:var(--text-main);">Atelier Flagship & Design Studio</div>
            <div style="font-size:12px; color:var(--text-muted);">Sector 17-C, Chandigarh &bull; Open Mon&ndash;Sat 10:00 AM &ndash; 7:30 PM</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  """

if modals_insert_pos != -1:
    code = code[:modals_insert_pos] + new_drawers_html + code[modals_insert_pos:]
    print("Inserted Wishlist Drawer and Account Modal successfully.")
else:
    print("WARNING: Could not locate Cart Drawer to insert Wishlist and Account modals")

# 5. Add JavaScript functions for Wishlist, Search, and Account
js_insert_pos = code.find('function searchProducts()')
new_js_code = """/* Wishlist System */
    var wishlist = [];

    function toggleWishlistProduct(prodId) {
      var idx = wishlist.indexOf(prodId);
      var btn = document.getElementById('wishBtn_' + prodId);
      if (idx === -1) {
        wishlist.push(prodId);
        if (btn) btn.classList.add('active');
        showToast('Added to your Wishlist!');
      } else {
        wishlist.splice(idx, 1);
        if (btn) btn.classList.remove('active');
        showToast('Removed from your Wishlist.');
      }
      updateWishlistUI();
    }

    function updateWishlistUI() {
      var countEl = document.getElementById('headerWishlistCount');
      if (countEl) countEl.textContent = wishlist.length;
      var drawerCountEl = document.getElementById('wishlistDrawerCount');
      if (drawerCountEl) drawerCountEl.textContent = wishlist.length;
      var container = document.getElementById('wishlistItemsList');
      var footer = document.getElementById('wishlistFooter');
      if (!container) return;

      if (wishlist.length === 0) {
        container.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 36px; margin-bottom: 12px; color: #CCC;">&hearts;</div><p style="font-size: 15px; font-weight: 600; color: var(--text-main); margin-bottom: 6px;">Your Wishlist is Empty</p><p style="font-size: 12px;">Explore Drop 01 and tap the heart icon on any silhouette to save your favorites.</p></div>';
        if (footer) footer.style.display = 'none';
        return;
      }

      if (footer) footer.style.display = 'block';
      var html = '';
      wishlist.forEach(function(pid) {
        var p = productsData.find(function(item) { return item.id === pid; });
        if (p) {
          html += '<div style="display:flex; gap:14px; padding:16px 0; border-bottom:1px solid var(--border-color); align-items:center;">';
          html += '<img src="' + p.b64 + '" style="width:68px; height:85px; object-fit:cover; border-radius:6px;">';
          html += '<div style="flex:1;">';
          html += '<div style="font-size:11px; color:var(--accent-gold); font-weight:700; letter-spacing:0.5px; text-transform:uppercase;">' + p.code + '</div>';
          html += '<div style="font-size:13px; font-weight:700; color:var(--text-main); margin:2px 0;">' + p.name + '</div>';
          html += '<div style="font-size:13px; font-weight:700; color:var(--text-main);">&#8377;' + p.price.toLocaleString('en-IN') + '</div>';
          html += '</div>';
          html += '<div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">';
          html += '<button onclick="quickAddCart(\\'' + p.id + '\\', \\'M\\'); toggleWishlistProduct(\\'' + p.id + '\\');" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';
          html += '<button onclick="toggleWishlistProduct(\\'' + p.id + '\\')" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';
          html += '</div>';
          html += '</div>';
        }
      });
      container.innerHTML = html;
    }

    function toggleWishlistDrawer() {
      var drawer = document.getElementById('wishlistDrawer');
      var backdrop = document.getElementById('wishlistBackdrop');
      drawer.classList.toggle('open');
      backdrop.classList.toggle('open');
      updateWishlistUI();
    }

    function addAllWishlistToCart() {
      if (wishlist.length === 0) return;
      wishlist.forEach(function(pid) {
        quickAddCart(pid, 'M');
      });
      wishlist = [];
      document.querySelectorAll('.card-wishlist-btn').forEach(function(b) { b.classList.remove('active'); });
      updateWishlistUI();
      toggleWishlistDrawer();
      toggleCart();
      showToast('All favorites moved to your bag!');
    }

    /* Search Bar Overlay Logic */
    function toggleSearchBar() {
      var bar = document.getElementById('searchOverlayBar');
      bar.classList.toggle('open');
      if (bar.classList.contains('open')) {
        setTimeout(function() {
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }, 120);
      }
    }

    function clearSearch() {
      var inp = document.getElementById('searchInput');
      if (inp) inp.value = '';
      searchProducts();
      if (inp) inp.focus();
    }

    function quickSearch(tag) {
      var inp = document.getElementById('searchInput');
      if (inp) inp.value = tag;
      searchProducts();
      var coll = document.getElementById('collectionSection');
      if (coll) coll.scrollIntoView({ behavior: 'smooth' });
    }

    /* Account Modal Logic */
    function openAccountModal() {
      document.getElementById('accountModalBackdrop').classList.add('open');
    }
    function closeAccountModalDirect() {
      document.getElementById('accountModalBackdrop').classList.remove('open');
    }
    function closeAccountModal(e) {
      if (e.target.id === 'accountModalBackdrop') closeAccountModalDirect();
    }

    function trackOrderSubmit() {
      var val = document.getElementById('trackOrderInput').value.trim();
      var res = document.getElementById('trackOrderResult');
      res.style.display = 'block';
      if (!val) {
        res.style.color = '#E53935';
        res.textContent = 'Please enter a valid order number.';
        return;
      }
      res.style.color = '#128C7E';
      res.textContent = 'Order #' + val.toUpperCase() + ' status: DISPATCHED from Sector 17 Atelier via Express 24-Hr Courier. Expected delivery tomorrow.';
    }

    """

if js_insert_pos != -1:
    code = code[:js_insert_pos] + new_js_code + code[js_insert_pos:]
    print("Inserted Wishlist, Search, and Account JS successfully.")
else:
    print("WARNING: Could not find function searchProducts() to insert JS")

# Also replace broken unicode question marks in cart drawer / checkout / toast:
code = code.replace("onclick=\"toggleCart()\">?</button>", "onclick=\"toggleCart()\">&times;</button>")
code = code.replace("onclick=\"closeSizeGuideDirect()\">?</button>", "onclick=\"closeSizeGuideDirect()\">&times;</button>")
code = code.replace("ADD TO BAG ??", "ADD TO BAG")
code = code.replace("PROCEED TO SECURE CHECKOUT ?", "PROCEED TO SECURE CHECKOUT &rarr;")
code = code.replace("? Instant UPI", "&bull; Instant UPI")
code = code.replace("? Promo code", "&check; Promo code")
code = code.replace("? Invalid code", "&cross; Invalid code")
code = code.replace("? Redirecting to Shopify", "Redirecting to Shopify")

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: Updated build_snitch_storefront.py with Snitch outline icons and interactive systems!")

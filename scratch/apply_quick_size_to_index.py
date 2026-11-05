import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS
with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find the quick size css block in meenu-luxury.css
qs_css_start = css_content.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE")
qs_css = css_content[qs_css_start:]

if "QUICK SIZE POPUP INTERFACE" not in html:
    # insert before </style>
    style_end = html.find("</style>")
    html = html[:style_end] + "\n" + qs_css + "\n" + html[style_end:]
    print("Injected Quick Size CSS into index.html")

# 2. Update card-price-row in each product-card in index.html
# Let's find each product-card and add the snitch-plus-trigger
def repl_card(match):
    card_html = match.group(0)
    # get data-id
    m_id = re.search(r'data-id="([^"]+)"', card_html)
    if not m_id:
        return card_html
    prod_id = m_id.group(1)
    
    if 'class="snitch-plus-trigger"' in card_html:
        return card_html

    plus_btn_html = f'''          <button type="button" class="snitch-plus-trigger" data-product-id="{prod_id}" onclick="event.preventDefault(); event.stopPropagation(); openQuickSizePopup(this)" title="Select Size & Add to Bag" aria-label="Select Size & Add to Bag">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="3" x2="12" y2="15"></line>
              <line x1="6" y1="9" x2="18" y2="9"></line>
              <line x1="4" y1="19" x2="20" y2="19"></line>
            </svg>
          </button>
        </div>'''
    
    # replace the closing </div> of card-price-row with plus button + closing </div>
    # find <div class="card-price-row"> ... </div>
    card_html = re.sub(
        r'(<div class="card-price-row">.*?)(</div>\s*<div class="card-sizes-row">)',
        lambda m: m.group(1) + plus_btn_html.replace('        </div>', '') + '</div>\n        <div class="card-sizes-row">',
        card_html,
        flags=re.DOTALL
    )
    return card_html

html = re.sub(r'<div class="product-card"[^>]*>.*?</div>\s*</div>\s*</div>', repl_card, html, flags=re.DOTALL)
print("Updated product cards with plus button in index.html")

# 3. Inject Quick Size Modal HTML before </body>
modal_html = """
<!-- Quick Size Popup Interface Modal (Meenu Label) -->
<div class="quick-size-backdrop" id="quickSizeModalBackdrop" onclick="closeQuickSizePopupOnBackdrop(event)">
  <div class="quick-size-modal" id="quickSizeModal" role="dialog" aria-modal="true" aria-label="Select Size & Add to Bag">
    <!-- Close Button -->
    <button type="button" class="quick-size-close-btn" onclick="closeQuickSizePopup()" aria-label="Close size popup">&times;</button>
    
    <!-- Product Row -->
    <div class="quick-size-product-row">
      <div class="quick-size-thumb">
        <img id="qsProductImg" src="" alt="Silhouette">
      </div>
      <div class="quick-size-meta">
        <span class="quick-size-tag" id="qsProductTag">DROP 01 &bull; ATELIER PIECE</span>
        <h4 class="quick-size-title" id="qsProductTitle">Atelier Handcrafted Ensemble</h4>
        <div class="quick-size-price-row">
          <span class="quick-size-price" id="qsProductPrice">&#8377;2,999</span>
          <span class="quick-size-mrp" id="qsProductMrp">&#8377;4,799</span>
          <span class="quick-size-discount" id="qsProductDiscount">SAVE 38%</span>
        </div>
      </div>
    </div>

    <div class="quick-size-divider"></div>

    <!-- Size Selection Header -->
    <div class="quick-size-header-row">
      <span class="quick-size-label">SELECT ATELIER SIZE</span>
      <button type="button" class="quick-size-chart-link" onclick="if(typeof openSizeGuideModal==='function'){openSizeGuideModal();}else{alert('Standard sizing: XS (34 in), S (36 in), M (38 in), L (40 in), XL (42 in)');}">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21.3 8.7 8.7 21.3a2.4 2.4 0 0 1-3.4 0L2.7 18.7a2.4 2.4 0 0 1 0-3.4L15.3 2.7a2.4 2.4 0 0 1 3.4 0l2.6 2.6a2.4 2.4 0 0 1 0 3.4Z"/>
          <path d="m14.5 5.5 2 2"/>
          <path d="m11.5 8.5 2 2"/>
          <path d="m8.5 11.5 2 2"/>
          <path d="m5.5 14.5 2 2"/>
        </svg>
        Size Chart
      </button>
    </div>

    <!-- Size Tiles Grid -->
    <div class="quick-size-tiles" id="qsSizeTiles">
      <!-- Injected via JavaScript -->
    </div>

    <!-- Artisan Scarcity Note -->
    <div class="quick-size-scarcity-note">
      <span class="qs-scarcity-dot"></span>
      <span>Handcrafted in Chandigarh &bull; Strictly 3 Pieces Crafted per Size</span>
    </div>

    <!-- Add To Bag CTA Button -->
    <button type="button" class="quick-size-add-btn" id="qsAddBtn" onclick="submitQuickSizeAdd()">
      <span id="qsAddBtnText">ADD TO ATELIER BAG</span>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <path d="M16 10a4 4 0 0 1-8 0"></path>
      </svg>
    </button>

    <!-- View Full Details Link -->
    <div class="quick-size-footer">
      <a href="#" id="qsViewFullLink" class="quick-size-view-full">VIEW FULL ATELIER DETAILS &rarr;</a>
    </div>
  </div>
</div>
"""

if "id=\"quickSizeModalBackdrop\"" not in html:
    body_end = html.find("</body>")
    html = html[:body_end] + modal_html + "\n" + html[body_end:]
    print("Injected Quick Size Modal HTML into index.html")

# 4. Inject Quick Size JS into <script>
with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

qs_js_start = js_content.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE LOGIC")
qs_js = js_content[qs_js_start:]

if "function openQuickSizePopup" not in html:
    script_end = html.rfind("</script>")
    html = html[:script_end] + "\n" + qs_js + "\n" + html[script_end:]
    print("Injected Quick Size JS into index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")

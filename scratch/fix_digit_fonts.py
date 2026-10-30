import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Global CSS fix to force lining numerals on all fonts + specific modern number styling
global_font_fix = """
    /* ==========================================================================
       GLOBAL NUMERAL FIX: Clean, Modern Lining Figures (Eliminate Old-Style Digits)
       ========================================================================== */
    html, body, *, *::before, *::after {
      font-variant-numeric: lining-nums proportional-nums !important;
      font-feature-settings: "lnum" 1, "pnum" 1 !important;
    }

    /* Modern Digit Styling for all Headings, Counters, Prices & Quantities */
    .modern-num-pill,
    .cart-page-header-row h1 span,
    #cartPageHeaderCount,
    #wishlistDrawerCount,
    #headerCartCount,
    #headerWishlistCount,
    .qty-step-val,
    .cart-page-price-main,
    .cart-page-price-mrp,
    .pdp-price-main,
    .pdp-price-mrp,
    .pdp-price-discount,
    .product-price,
    .product-card-price,
    .summary-line span:last-child {
      font-family: 'Plus Jakarta Sans', 'Montserrat', -apple-system, sans-serif !important;
      font-variant-numeric: lining-nums !important;
      font-feature-settings: "lnum" 1 !important;
    }

    .modern-num-pill {
      font-family: 'Plus Jakarta Sans', 'Montserrat', -apple-system, sans-serif !important;
      font-size: 26px !important;
      font-weight: 500 !important;
      color: var(--text-muted) !important;
      vertical-align: middle !important;
      letter-spacing: -0.02em !important;
      margin-left: 4px !important;
    }
"""

css_anchor = "/* ==================== DEDICATED FULL CART PAGE STYLES ==================== */"
if css_anchor in content:
    content = content.replace(css_anchor, global_font_fix + "\n    " + css_anchor, 1)
    print("Added global numeral fix to CSS")
else:
    print("WARNING: css_anchor not found")

# 2. Update Shopping Bag title HTML
old_h1 = '<h1 style="font-family: \'Cormorant Garamond\', serif; font-size: 38px; font-weight: 600; color: #1E1C19; margin: 4px 0 0;">Shopping Bag (<span id="cartPageHeaderCount">0</span>)</h1>'
new_h1 = '<h1 style="font-family: \'Cormorant Garamond\', serif; font-size: 38px; font-weight: 600; color: #1E1C19; margin: 4px 0 0;">Shopping Bag <span class="modern-num-pill">(<span id="cartPageHeaderCount">0</span>)</span></h1>'

if old_h1 in content:
    content = content.replace(old_h1, new_h1, 1)
    print("Updated Cart Page H1 title to use .modern-num-pill")
else:
    print("WARNING: old_h1 not found")

# 3. Update Wishlist title HTML
old_w_title = '<h3 style="font-family: \'Cormorant Garamond\', serif; font-size: 22px;">Saved Wishlist (<span id="wishlistDrawerCount">0</span>)</h3>'
new_w_title = '<h3 style="font-family: \'Cormorant Garamond\', serif; font-size: 22px;">Saved Wishlist <span class="modern-num-pill" style="font-size: 16px !important;">(<span id="wishlistDrawerCount">0</span>)</span></h3>'

if old_w_title in content:
    content = content.replace(old_w_title, new_w_title, 1)
    print("Updated Wishlist title to use .modern-num-pill")
else:
    print("WARNING: old_w_title not found")

# 4. In renderCartPage(), ensure price and item numbers are clean modern fonts
old_item_price_html = """<div class="cart-page-item-prices">
                <span class="cart-page-price-main">&#8377;' + itemSubtotal.toLocaleString('en-IN') + '</span>
              </div>"""

new_item_price_html = """<div class="cart-page-item-prices">
                <span class="cart-page-price-main" style="font-family:'Plus Jakarta Sans', sans-serif; font-variant-numeric:lining-nums;">&#8377;' + itemSubtotal.toLocaleString('en-IN') + '</span>
              </div>"""

content = content.replace(old_item_price_html, new_item_price_html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Digit font updated across Meenu_Label_Desktop_Storefront.html")

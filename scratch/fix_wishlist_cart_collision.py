# Update sections/header.liquid
with open('sections/header.liquid', 'r', encoding='utf-8') as f:
    header_liquid = f.read()

header_liquid = header_liquid.replace(
    '<span class="header-badge-pill" id="headerCartCount"',
    '<span class="header-badge-pill header-cart-pill" id="headerCartCount"'
)
header_liquid = header_liquid.replace(
    '<span class="header-badge-pill" id="headerWishlistCount"',
    '<span class="header-badge-pill header-wishlist-pill" id="headerWishlistCount"'
)

with open('sections/header.liquid', 'w', encoding='utf-8') as f:
    f.write(header_liquid)
print("Updated sections/header.liquid")

# Update assets/meenu-theme.js
with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    theme_js = f.read()

# Replace errant querySelectorAll including .header-badge-pill
theme_js = theme_js.replace(
    "querySelectorAll('#headerCartCount, .header-badge-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount')",
    "querySelectorAll('#headerCartCount, .header-cart-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount')"
)

with open('assets/meenu-theme.js', 'w', encoding='utf-8') as f:
    f.write(theme_js)
print("Updated assets/meenu-theme.js")

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace(
    '<span class="header-badge-pill" id="headerCartCount">0</span>',
    '<span class="header-badge-pill header-cart-pill" id="headerCartCount" style="display:none;">0</span>'
)
index_html = index_html.replace(
    '<span class="header-badge-pill" id="headerWishlistCount">0</span>',
    '<span class="header-badge-pill header-wishlist-pill" id="headerWishlistCount" style="display:none;">0</span>'
)
index_html = index_html.replace(
    "querySelectorAll('#headerCartCount, .header-badge-pill')",
    "querySelectorAll('#headerCartCount, .header-cart-pill')"
)
index_html = index_html.replace(
    "querySelectorAll('#headerCartCount, .header-badge-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount')",
    "querySelectorAll('#headerCartCount, .header-cart-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount')"
)

# Also ensure updateWishlistUI sets style.display properly
if "if (countEl) countEl.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';" not in index_html:
    index_html = index_html.replace(
        "if (countEl) countEl.textContent = wishlist.length;",
        "if (countEl) { countEl.textContent = wishlist.length; countEl.style.display = wishlist.length > 0 ? 'inline-flex' : 'none'; }"
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Updated index.html")

import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. Target the exact HTML block of cart-backdrop and cart-drawer
drawer_start = '<!-- Cart Drawer -->\n  <div class="cart-backdrop" id="cartBackdrop"'
if drawer_start not in content:
    drawer_start = '<div class="cart-backdrop" id="cartBackdrop"'

wishlist_start = '<!-- Wishlist Drawer -->'
if wishlist_start not in content:
    wishlist_start = '<div class="cart-backdrop" id="wishlistBackdrop"'

idx_start = content.find(drawer_start)
idx_end = content.find(wishlist_start)

print("idx_start:", idx_start)
print("idx_end:", idx_end)

if idx_start != -1 and idx_end != -1:
    snippet_to_remove = content[idx_start:idx_end]
    print("Found snippet to remove, characters:", len(snippet_to_remove))
    content = content[:idx_start] + "<!-- Cart Drawer Removed: Using Independent Cart Page (#cartPageView) -->\n\n  " + content[idx_end:]
    print("Removed cart-drawer and cart-backdrop from HTML!")
else:
    print("ERROR: Could not locate drawer HTML block")

# 2. Add CSS to permanently ensure no drawer can ever pop up
css_hide = """
    /* Permanently disabled cart drawer in favor of independent Cart Page */
    #cartDrawer, #cartBackdrop, .cart-drawer {
      display: none !important;
      visibility: hidden !important;
      pointer-events: none !important;
    }
"""
css_pos = content.find("/* ==================== DEDICATED FULL CART PAGE STYLES ==================== */")
if css_pos != -1:
    content = content[:css_pos] + css_hide + "\n    " + content[css_pos:]
    print("Added CSS rule to completely disable cart drawer!")

# 3. Update JavaScript to route all cart actions directly to openCartPage()
# Update toggleCart and openCart
old_drawer_funcs = """    function toggleCart() {
      document.getElementById('cartDrawer').classList.toggle('open');
      document.getElementById('cartBackdrop').classList.toggle('open');
    }
    function openCart() {
      document.getElementById('cartDrawer').classList.add('open');
      document.getElementById('cartBackdrop').classList.add('open');
    }"""

new_drawer_funcs = """    function toggleCart() {
      openCartPage();
    }
    function openCart() {
      openCartPage();
    }"""

if old_drawer_funcs in content:
    content = content.replace(old_drawer_funcs, new_drawer_funcs, 1)
    print("Replaced toggleCart() and openCart() to always call openCartPage()")
else:
    print("WARNING: old_drawer_funcs not matched exactly, let's search pattern")
    content = re.sub(
        r"function toggleCart\(\)\s*\{[^}]*\}",
        "function toggleCart() { openCartPage(); }",
        content
    )
    content = re.sub(
        r"function openCart\(\)\s*\{[^}]*\}",
        "function openCart() { openCartPage(); }",
        content
    )
    print("Updated toggleCart and openCart via regex")

# Write updated file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html updated!")

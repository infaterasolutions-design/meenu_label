with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update updateCartUI in index.html
old_update_cart_code = """function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;
      document.getElementById('cartCount').textContent = totalItems;
      document.getElementById('headerCartCount').textContent = totalItems;"""

new_update_cart_code = """function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += (cart[i].qty || 1);
      
      var cartCountEl = document.getElementById('cartCount');
      if (cartCountEl) cartCountEl.textContent = totalItems;

      var headerBadge = document.getElementById('headerCartCount');
      if (headerBadge) {
        headerBadge.textContent = totalItems;
        headerBadge.style.display = totalItems > 0 ? 'inline-flex' : 'none';
        headerBadge.style.transform = 'scale(1.35)';
        setTimeout(function() { headerBadge.style.transform = 'scale(1)'; }, 200);
      }

      var allBadges = document.querySelectorAll('#headerCartCount, .header-badge-pill');
      allBadges.forEach(function(b) {
        b.textContent = totalItems;
        b.style.display = totalItems > 0 ? 'inline-flex' : 'none';
      });"""

if old_update_cart_code in html:
    html = html.replace(old_update_cart_code, new_update_cart_code)
    print("Updated updateCartUI in index.html!")
else:
    print("Target updateCartUI string not found exactly, let's use regex")
    import re
    html = re.sub(
        r'function updateCartUI\(\)\s*\{[^}]*?document\.getElementById\(\'headerCartCount\'\)\.textContent\s*=\s*totalItems;',
        new_update_cart_code,
        html,
        count=1
    )
    print("Updated updateCartUI with regex!")

# 2. Update snitchAddSizeToCart and snitchFallbackCartAdd in index.html
old_snitch_start = html.find("function snitchAddSizeToCart")
old_snitch_end = html.find("function toggleSnitchSizeWishlist")

if old_snitch_start != -1 and old_snitch_end != -1:
    with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
        theme_js = f.read()
    theme_fn_start = theme_js.find("function snitchAddSizeToCart")
    theme_fn_end = theme_js.find("function toggleSnitchSizeWishlist")
    new_fns_theme = theme_js[theme_fn_start:theme_fn_end]
    html = html[:old_snitch_start] + new_fns_theme + html[old_snitch_end:]
    print("Updated snitch functions in index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")

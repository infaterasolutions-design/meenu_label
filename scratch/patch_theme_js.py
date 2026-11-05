with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace snitchAddSizeToCart and snitchFallbackCartAdd
old_fn_start = js.find("function snitchAddSizeToCart")
old_fn_end = js.find("function toggleSnitchSizeWishlist")

new_fns = """function snitchAddSizeToCart(rowEl, variantId, sizeName) {
  var statusSpan = rowEl.querySelector('.snitch-size-status');
  if (statusSpan) {
    statusSpan.textContent = '✓ ADDED';
  }
  rowEl.style.background = '#F4EFEB';

  // Live Shopify Store
  if (typeof Shopify !== 'undefined' && Shopify.theme || (window.location.pathname.includes('/products/') || window.location.pathname.includes('/collections/'))) {
    if (!isNaN(parseInt(variantId, 10))) {
      fetch('/cart/add.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          id: parseInt(variantId, 10),
          quantity: 1
        })
      })
      .then(function(res) {
        if (!res.ok) throw new Error('Cart add failed');
        return res.json();
      })
      .then(function(item) {
        return fetch('/cart.js').then(function(r) { return r.json(); });
      })
      .then(function(cart) {
        // 1. Instantly update header badge digit and display
        var headerBadge = document.getElementById('headerCartCount');
        if (headerBadge) {
          headerBadge.textContent = cart.item_count || 0;
          headerBadge.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
          headerBadge.style.transform = 'scale(1.35)';
          setTimeout(function() { headerBadge.style.transform = 'scale(1)'; }, 200);
        }

        // 2. Update all badge elements across header and drawers
        var allBadges = document.querySelectorAll('#headerCartCount, .header-badge-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount');
        allBadges.forEach(function(b) {
          b.textContent = cart.item_count || 0;
          b.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
        });

        // 3. Call global updateCartUI if present
        if (typeof updateCartUI === 'function') {
          updateCartUI(cart);
        }

        // 4. Close size drawer and open cart drawer
        setTimeout(function() {
          closeSnitchSizePopup();
          if (typeof openCartDrawer === 'function') {
            openCartDrawer();
          }
        }, 180);
      })
      .catch(function(err) {
        console.error('Error adding to cart:', err);
        snitchFallbackCartAdd(sizeName);
      });
      return;
    }
  }

  snitchFallbackCartAdd(sizeName);
}

function snitchFallbackCartAdd(sizeName) {
  // If quickAddCart is available (e.g. index.html preview)
  if (typeof quickAddCart === 'function' && activeSnitchProduct) {
    quickAddCart(activeSnitchProduct.id, sizeName);
  } else if (typeof cart !== 'undefined' && activeSnitchProduct) {
    // Add to local cart array with correct qty property
    var existing = null;
    for (var i = 0; i < cart.length; i++) {
      if (cart[i].id === activeSnitchProduct.id && cart[i].size === sizeName) {
        existing = cart[i];
        break;
      }
    }
    if (existing) {
      existing.qty = (existing.qty || 1) + 1;
    } else {
      var numPrice = typeof activeSnitchProduct.price === 'number' ? activeSnitchProduct.price : parseInt(String(activeSnitchProduct.price).replace(/[^0-9]/g, ''), 10) || 0;
      cart.push({
        id: activeSnitchProduct.id,
        name: activeSnitchProduct.title,
        price: numPrice,
        size: sizeName,
        img: activeSnitchProduct.image,
        qty: 1
      });
    }

    if (typeof updateCartUI === 'function') {
      updateCartUI();
    }
    if (typeof openCart === 'function') {
      openCart();
    }
  }

  setTimeout(function() {
    closeSnitchSizePopup();
  }, 180);
}

"""

js = js[:old_fn_start] + new_fns + js[old_fn_end:]

with open('assets/meenu-theme.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated assets/meenu-theme.js successfully!")

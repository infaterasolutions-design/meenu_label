with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove previous quick size JS
idx = js.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE LOGIC")
if idx != -1:
    js = js[:idx].rstrip()

snitch_drawer_js = """
/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE DRAWER LOGIC
   ======================================================== */
var activeSnitchProduct = null;

function openQuickSizePopup(btn) {
  var modalBackdrop = document.getElementById('snitchSizeModalBackdrop');
  if (!modalBackdrop) return;

  var productId = btn.getAttribute('data-product-id');
  var title = btn.getAttribute('data-product-title') || 'Atelier Ensemble';
  var price = btn.getAttribute('data-product-price') || '';
  var img = btn.getAttribute('data-product-image') || '';
  var url = btn.getAttribute('data-product-url') || '#';

  activeSnitchProduct = {
    id: productId,
    title: title,
    price: price,
    image: img,
    url: url
  };

  // Sync Wishlist button in header
  var wishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (wishBtn) {
    if (typeof wishlist !== 'undefined' && wishlist.indexOf(productId) !== -1) {
      wishBtn.classList.add('active');
    } else {
      wishBtn.classList.remove('active');
    }
  }

  // Read variants data if available from the card script
  var variants = [];
  var cardBody = btn.closest('.card-body') || btn.closest('.product-card');
  if (cardBody) {
    var variantsScript = cardBody.querySelector('.product-variants-json');
    if (variantsScript) {
      try {
        variants = JSON.parse(variantsScript.textContent.trim());
      } catch(e) {}
    }
  }

  // Fallback: If in index.html and productsData is defined
  if ((!variants || variants.length === 0) && typeof productsData !== 'undefined') {
    var pObj = productsData.find(function(p) { return p.id === productId || p.code === productId; });
    if (pObj) {
      activeSnitchProduct.title = pObj.name;
      activeSnitchProduct.price = '₹' + pObj.price.toLocaleString('en-IN');
      activeSnitchProduct.image = (pObj.images && pObj.images.length) ? pObj.images[0] : pObj.b64;
      activeSnitchProduct.url = '#product-' + pObj.id;
    }
  }

  // Default Snitch sizes if variants not loaded or single variant
  var standardSizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];
  var sizeListEl = document.getElementById('snitchSizeList');
  if (sizeListEl) {
    sizeListEl.innerHTML = '';

    if (variants && variants.length > 1) {
      variants.forEach(function(v) {
        var sName = v.title.includes('/') ? v.title.split('/')[0].trim() : v.title;
        var isAvail = v.available !== false;
        createSnitchSizeRow(sizeListEl, sName, v.id, isAvail);
      });
    } else {
      standardSizes.forEach(function(sName) {
        createSnitchSizeRow(sizeListEl, sName, productId + '_' + sName, true);
      });
    }
  }

  modalBackdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function createSnitchSizeRow(container, sizeName, variantId, isAvailable) {
  var row = document.createElement('button');
  row.type = 'button';
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status';
  if (!isAvailable) {
    statusSpan.textContent = 'OUT OF STOCK';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  }

  container.appendChild(row);
}

function snitchAddSizeToCart(rowEl, variantId, sizeName) {
  var statusSpan = rowEl.querySelector('.snitch-size-status');
  if (statusSpan) {
    statusSpan.textContent = '✓ ADDED';
  }
  rowEl.style.background = '#F4EFEB';

  // Live Shopify Store
  if (typeof Shopify !== 'undefined' && Shopify.theme || (window.location.pathname.includes('/products/') || window.location.pathname.includes('/collections/') || window.location.pathname === '/')) {
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
      .then(function(res) { return res.json(); })
      .then(function(item) {
        fetch('/cart.js')
          .then(function(r) { return r.json(); })
          .then(function(cart) {
            var badges = document.querySelectorAll('.cart-count-badge, .header-cart-count, #cartCountBadge');
            badges.forEach(function(b) {
              b.textContent = cart.item_count;
              b.style.display = cart.item_count > 0 ? 'flex' : 'none';
            });
          });

        setTimeout(function() {
          closeSnitchSizePopup();
          if (typeof openCartDrawer === 'function') {
            openCartDrawer();
          }
        }, 220);
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
  if (typeof cart !== 'undefined' && activeSnitchProduct) {
    cart.push({
      id: activeSnitchProduct.id,
      title: activeSnitchProduct.title,
      price: activeSnitchProduct.price,
      size: sizeName,
      image: activeSnitchProduct.image,
      quantity: 1
    });
    if (typeof updateCartUI === 'function') {
      updateCartUI();
    }
  }

  setTimeout(function() {
    closeSnitchSizePopup();
    if (typeof openCartDrawer === 'function') {
      openCartDrawer();
    }
  }, 220);
}

function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  btn.classList.toggle('active');
  if (typeof toggleWishlistProduct === 'function') {
    toggleWishlistProduct(activeSnitchProduct.id);
  } else if (typeof toggleWishlist === 'function') {
    // create a pseudo button or call
    var wishId = activeSnitchProduct.id;
    if (typeof wishlist !== 'undefined') {
      var idx = wishlist.indexOf(wishId);
      if (idx === -1) {
        wishlist.push(wishId);
      } else {
        wishlist.splice(idx, 1);
      }
      try { localStorage.setItem('meenu_wishlist', JSON.stringify(wishlist)); } catch(e) {}
    }
  }
}

function closeSnitchSizePopup() {
  var modalBackdrop = document.getElementById('snitchSizeModalBackdrop');
  if (modalBackdrop) modalBackdrop.classList.remove('open');
  document.body.style.overflow = '';
}

function closeSnitchSizePopupOnBackdrop(event) {
  if (event.target.id === 'snitchSizeModalBackdrop') {
    closeSnitchSizePopup();
  }
}
"""

js = js + "\n" + snitch_drawer_js

with open('assets/meenu-theme.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated assets/meenu-theme.js successfully with Snitch drawer logic!")

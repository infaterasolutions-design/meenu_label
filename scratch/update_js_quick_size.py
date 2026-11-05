with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("meenu-theme.js length:", len(js))

quick_size_js = """
/* ========================================================
   QUICK SIZE POPUP INTERFACE LOGIC
   ======================================================== */
var activeQuickSizeProduct = null;
var activeQuickSelectedVariantId = null;
var activeQuickSelectedSizeTitle = 'M';

function openQuickSizePopup(btn) {
  var modalBackdrop = document.getElementById('quickSizeModalBackdrop');
  if (!modalBackdrop) return;

  var productId = btn.getAttribute('data-product-id');
  var title = btn.getAttribute('data-product-title') || 'Atelier Ensemble';
  var price = btn.getAttribute('data-product-price') || '';
  var mrp = btn.getAttribute('data-product-mrp') || '';
  var img = btn.getAttribute('data-product-image') || '';
  var url = btn.getAttribute('data-product-url') || '#';
  var tag = btn.getAttribute('data-product-tag') || 'DROP 01 • ATELIER PIECE';

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
      title = pObj.name;
      price = '₹' + pObj.price.toLocaleString('en-IN');
      mrp = pObj.mrp ? '₹' + pObj.mrp.toLocaleString('en-IN') : '';
      img = (pObj.images && pObj.images.length) ? pObj.images[0] : pObj.b64;
      tag = pObj.badge || 'DROP 01 STAR';
      url = '#product-' + pObj.id;
      var defaultSizes = ['XS', 'S', 'M', 'L', 'XL'];
      variants = defaultSizes.map(function(s) {
        var bust = s === 'XS' ? '34' : s === 'S' ? '36' : s === 'M' ? '38' : s === 'L' ? '40' : '42';
        return {
          id: pObj.id + '_' + s,
          title: s,
          bust: bust,
          available: true,
          price: pObj.price
        };
      });
    }
  }

  // If still no variants, provide standard atelier sizes
  if (!variants || variants.length === 0) {
    variants = [
      { id: productId + '_XS', title: 'XS', bust: '34', available: true },
      { id: productId + '_S', title: 'S', bust: '36', available: true },
      { id: productId + '_M', title: 'M', bust: '38', available: true },
      { id: productId + '_L', title: 'L', bust: '40', available: true },
      { id: productId + '_XL', title: 'XL', bust: '42', available: true }
    ];
  }

  // Populate popup modal
  var imgEl = document.getElementById('qsProductImg');
  if (imgEl) imgEl.src = img;

  var titleEl = document.getElementById('qsProductTitle');
  if (titleEl) titleEl.textContent = title;

  var tagEl = document.getElementById('qsProductTag');
  if (tagEl) tagEl.textContent = tag.toUpperCase();

  var priceEl = document.getElementById('qsProductPrice');
  if (priceEl) priceEl.textContent = price;

  var mrpEl = document.getElementById('qsProductMrp');
  var discEl = document.getElementById('qsProductDiscount');
  if (mrpEl) {
    if (mrp && mrp !== price) {
      mrpEl.textContent = mrp;
      mrpEl.style.display = 'inline-block';
      if (discEl) discEl.style.display = 'inline-block';
    } else {
      mrpEl.style.display = 'none';
      if (discEl) discEl.style.display = 'none';
    }
  }

  var fullLink = document.getElementById('qsViewFullLink');
  if (fullLink) {
    fullLink.href = url;
    if (url.startsWith('#product-')) {
      fullLink.onclick = function(e) {
        e.preventDefault();
        closeQuickSizePopup();
        if (typeof openProductPage === 'function') {
          openProductPage(productId);
        }
      };
    } else {
      fullLink.onclick = null;
    }
  }

  // Render Size Tiles
  var tilesContainer = document.getElementById('qsSizeTiles');
  if (tilesContainer) {
    tilesContainer.innerHTML = '';
    var firstAvailableSelected = false;

    variants.forEach(function(v) {
      var sTitle = v.title;
      var bustSub = v.bust ? (v.bust + ' in') : (sTitle.includes('/') ? sTitle.split('/')[1].trim() : (sTitle === 'XS' ? '34 in' : sTitle === 'S' ? '36 in' : sTitle === 'M' ? '38 in' : sTitle === 'L' ? '40 in' : sTitle === 'XL' ? '42 in' : 'Standard'));
      var mainName = sTitle.includes('/') ? sTitle.split('/')[0].trim() : sTitle;
      var isAvail = v.available !== false;
      var isDefault = !firstAvailableSelected && isAvail;

      if (isDefault) {
        firstAvailableSelected = true;
        activeQuickSelectedVariantId = v.id;
        activeQuickSelectedSizeTitle = mainName;
      }

      var tile = document.createElement('button');
      tile.type = 'button';
      tile.className = 'qs-size-tile' + (isDefault ? ' active' : '') + (!isAvail ? ' disabled' : '');
      tile.setAttribute('data-variant-id', v.id);
      tile.setAttribute('data-size-title', mainName);

      tile.innerHTML = '<span class="qs-tile-name">' + mainName + '</span>' +
                       '<span class="qs-tile-sub">' + bustSub + '</span>' +
                       '<span class="qs-tile-stock">' + (isAvail ? 'Only 1 Left' : 'Sold Out') + '</span>';

      if (isAvail) {
        tile.onclick = function() {
          selectQuickSize(this, v.id, mainName);
        };
      }
      tilesContainer.appendChild(tile);
    });
  }

  // Reset Add Button state
  var addBtn = document.getElementById('qsAddBtn');
  var addBtnText = document.getElementById('qsAddBtnText');
  if (addBtn) {
    addBtn.disabled = false;
    if (addBtnText) addBtnText.textContent = 'ADD TO ATELIER BAG';
    addBtn.style.background = '#6E1A24';
  }

  activeQuickSizeProduct = {
    id: productId,
    title: title,
    price: price,
    image: img,
    url: url
  };

  // Open modal with smooth transition
  modalBackdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function selectQuickSize(btn, variantId, sizeTitle) {
  var allTiles = document.querySelectorAll('#qsSizeTiles .qs-size-tile');
  allTiles.forEach(function(t) { t.classList.remove('active'); });
  btn.classList.add('active');
  activeQuickSelectedVariantId = variantId;
  activeQuickSelectedSizeTitle = sizeTitle;
}

function closeQuickSizePopup() {
  var modalBackdrop = document.getElementById('quickSizeModalBackdrop');
  if (modalBackdrop) modalBackdrop.classList.remove('open');
  document.body.style.overflow = '';
}

function closeQuickSizePopupOnBackdrop(event) {
  if (event.target.id === 'quickSizeModalBackdrop') {
    closeQuickSizePopup();
  }
}

function submitQuickSizeAdd() {
  if (!activeQuickSelectedVariantId) {
    alert('Please select a size');
    return;
  }

  var addBtn = document.getElementById('qsAddBtn');
  var addBtnText = document.getElementById('qsAddBtnText');
  if (addBtn) {
    addBtn.disabled = true;
    if (addBtnText) addBtnText.textContent = 'ADDING TO BAG...';
  }

  // Live Shopify Store
  if (typeof Shopify !== 'undefined' && Shopify.theme || (window.location.pathname.includes('/products/') || window.location.pathname.includes('/collections/') || window.location.pathname === '/')) {
    if (!isNaN(parseInt(activeQuickSelectedVariantId, 10))) {
      fetch('/cart/add.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          id: parseInt(activeQuickSelectedVariantId, 10),
          quantity: 1
        })
      })
      .then(function(res) { return res.json(); })
      .then(function(item) {
        if (addBtnText) addBtnText.textContent = 'ADDED TO BAG ✓';
        if (addBtn) addBtn.style.background = '#2E7D32';

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
          closeQuickSizePopup();
          if (typeof openCartDrawer === 'function') {
            openCartDrawer();
          }
        }, 600);
      })
      .catch(function(err) {
        console.error('Error adding to cart:', err);
        quickSizeFallbackSuccess();
      });
      return;
    }
  }

  // Fallback for standalone preview or non-numeric variants
  quickSizeFallbackSuccess();
}

function quickSizeFallbackSuccess() {
  var addBtn = document.getElementById('qsAddBtn');
  var addBtnText = document.getElementById('qsAddBtnText');
  if (addBtnText) addBtnText.textContent = 'ADDED TO BAG ✓';
  if (addBtn) addBtn.style.background = '#2E7D32';

  if (typeof cart !== 'undefined' && activeQuickSizeProduct) {
    cart.push({
      id: activeQuickSizeProduct.id,
      title: activeQuickSizeProduct.title,
      price: activeQuickSizeProduct.price,
      size: activeQuickSelectedSizeTitle,
      image: activeQuickSizeProduct.image,
      quantity: 1
    });
    if (typeof updateCartUI === 'function') {
      updateCartUI();
    }
  }

  setTimeout(function() {
    closeQuickSizePopup();
    if (typeof openCartDrawer === 'function') {
      openCartDrawer();
    }
  }, 600);
}
"""

if "function openQuickSizePopup" not in js:
    js = js + "\n" + quick_size_js

with open('assets/meenu-theme.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated assets/meenu-theme.js successfully!")

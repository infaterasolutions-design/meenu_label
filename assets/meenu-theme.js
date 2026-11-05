// Meenu Label Shopify Theme JS - Core Storefront Controller
// Version 2.2 - Complete Cart Drawer & Saved Wishlist Architecture

/* =========================================================================
   1. GLOBAL TOAST NOTIFICATION
   ========================================================================= */
function showMeenuToast(msg) {
  var t = document.getElementById('meenuToast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'meenuToast';
    t.style.position = 'fixed';
    t.style.bottom = '28px';
    t.style.left = '50%';
    t.style.transform = 'translateX(-50%) translateY(20px)';
    t.style.background = '#1A1A1A';
    t.style.color = '#FFFFFF';
    t.style.padding = '12px 24px';
    t.style.borderRadius = '30px';
    t.style.fontSize = '13px';
    t.style.fontWeight = '600';
    t.style.letterSpacing = '0.02em';
    t.style.boxShadow = '0 6px 20px rgba(0,0,0,0.25)';
    t.style.zIndex = '9999';
    t.style.opacity = '0';
    t.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
    t.style.pointerEvents = 'none';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.style.opacity = '1';
  t.style.transform = 'translateX(-50%) translateY(0)';
  clearTimeout(window.meenuToastTimeout);
  window.meenuToastTimeout = setTimeout(function() {
    t.style.opacity = '0';
    t.style.transform = 'translateX(-50%) translateY(20px)';
  }, 2400);
}

/* =========================================================================
   2. WISHLIST MANAGEMENT (CLIENT-SIDE LOCALSTORAGE)
   ========================================================================= */
var PREVIEW_FALLBACK_WISHLIST = {
  'drop01_1': {
    id: 'drop01_1',
    title: 'Jaipur Chanderi Silk Festive Suit',
    price: '₹2,299',
    url: '/collections/festive-suits'
  },
  'drop01_2': {
    id: 'drop01_2',
    title: 'Mustard Crepe Angrakha Co-ord Set',
    price: '₹1,699',
    url: '/collections/co-ord-sets'
  },
  'drop01_3': {
    id: 'drop01_3',
    title: 'White Porcelain Floral Wrap Dress',
    price: '₹1,599',
    url: '/collections/dresses'
  },
  'drop01_4': {
    id: 'drop01_4',
    title: 'Fluid Silk Crepe Angrakha Silhouette',
    price: '₹1,899',
    url: '/collections/co-ord-sets'
  }
};

function getWishlist() {
  try {
    var stored = localStorage.getItem('meenu_saved_wishlist');
    return stored ? JSON.parse(stored) : [];
  } catch (e) {
    return [];
  }
}

function saveWishlist(list) {
  try {
    localStorage.setItem('meenu_saved_wishlist', JSON.stringify(list));
  } catch (e) {}
  updateWishlistUI();
}

function isWishlisted(id) {
  var list = getWishlist();
  return list.some(function(item) { return String(item.id) === String(id); });
}

function toggleWishlistDrawer() {
  var drawer = document.getElementById('wishlistDrawer');
  var backdrop = document.getElementById('wishlistBackdrop');
  if (!drawer) return;

  var isOpen = drawer.classList.contains('open');
  if (isOpen) {
    drawer.classList.remove('open');
    if (backdrop) backdrop.classList.remove('open');
  } else {
    updateWishlistUI();
    drawer.classList.add('open');
    if (backdrop) backdrop.classList.add('open');
  }
}

function toggleWishlist(param) {
  // If param is a button element
  if (param && (param.nodeType || param.tagName)) {
    toggleWishlistFromButton(param);
    return;
  }

  // If param is a string ID
  var id = String(param || 'drop01_1');
  var btn = document.querySelector('[data-wishlist-id="' + id + '"]');
  if (btn) {
    toggleWishlistFromButton(btn);
    return;
  }

  // Fallback direct toggle by ID
  var list = getWishlist();
  var idx = list.findIndex(function(it) { return String(it.id) === id; });

  if (idx >= 0) {
    list.splice(idx, 1);
    saveWishlist(list);
    showMeenuToast('Removed from Wishlist');
  } else {
    var itemData = PREVIEW_FALLBACK_WISHLIST[id] || {
      id: id,
      title: 'Drop 01 Silhouette',
      price: '₹2,299',
      url: '/collections/all'
    };
    list.push(itemData);
    saveWishlist(list);
    showMeenuToast('Saved to Wishlist ❤️');
  }
}

function toggleWishlistFromButton(btn) {
  if (!btn) return;
  var id = btn.getAttribute('data-wishlist-id') || 'drop01_1';
  var title = btn.getAttribute('data-wishlist-title') || 'Drop 01 Silhouette';
  var price = btn.getAttribute('data-wishlist-price') || '₹2,299';
  var image = btn.getAttribute('data-wishlist-image') || '';
  var url = btn.getAttribute('data-wishlist-url') || '/collections/all';

  // If image not provided via dataset, try to grab card thumbnail img src
  if (!image) {
    var card = btn.closest('.product-card, .shopify-product-form, section');
    if (card) {
      var imgEl = card.querySelector('img');
      if (imgEl && imgEl.src) image = imgEl.src;
    }
  }

  var list = getWishlist();
  var idx = list.findIndex(function(it) { return String(it.id) === String(id); });

  if (idx >= 0) {
    list.splice(idx, 1);
    saveWishlist(list);
    showMeenuToast('Removed from Wishlist');
  } else {
    list.push({
      id: id,
      title: title,
      price: price,
      image: image,
      url: url
    });
    saveWishlist(list);
    showMeenuToast('Saved to Wishlist ❤️');
  }
}

function removeFromWishlist(id) {
  var list = getWishlist();
  list = list.filter(function(it) { return String(it.id) !== String(id); });
  saveWishlist(list);
  showMeenuToast('Removed from Wishlist');
}

function updateWishlistUI() {
  var list = getWishlist();
  var count = list.length;

  // 1. Header count badge
  var headerCountEl = document.getElementById('headerWishlistCount');
  if (headerCountEl) {
    headerCountEl.textContent = count;
    headerCountEl.style.display = count > 0 ? 'inline-flex' : 'none';
  }

  // 2. Mobile drawer count badge
  var navDrawerCountEls = document.querySelectorAll('.nav-drawer-wishlist-count');
  navDrawerCountEls.forEach(function(el) {
    el.textContent = count;
    el.style.display = count > 0 ? 'inline-flex' : 'none';
  });

  // 3. Wishlist Drawer title count
  var drawerCountEl = document.getElementById('wishlistDrawerCount');
  if (drawerCountEl) drawerCountEl.textContent = count;

  // 4. Update heart buttons active state across the entire page
  var allWishlistBtns = document.querySelectorAll('.card-wishlist-btn, .pdp-wishlist-toggle');
  allWishlistBtns.forEach(function(btn) {
    var bid = btn.getAttribute('data-wishlist-id');
    var active = list.some(function(it) { return String(it.id) === String(bid); });
    if (active) {
      btn.classList.add('active');
      var txt = btn.querySelector('.pdp-wishlist-txt');
      if (txt) txt.textContent = 'SAVED TO WISHLIST ❤️';
    } else {
      btn.classList.remove('active');
      var txt = btn.querySelector('.pdp-wishlist-txt');
      if (txt) txt.textContent = 'SAVE TO WISHLIST';
    }
  });

  // 4b. Update Quick Size drawer Wishlist heart if open
  var snitchWishBtn = document.getElementById('snitchSizeWishlistBtn');
  if (snitchWishBtn) {
    var sId = snitchWishBtn.getAttribute('data-wishlist-id') || (typeof activeSnitchProduct !== 'undefined' && activeSnitchProduct ? activeSnitchProduct.id : null);
    if (sId) {
      var isSActive = list.some(function(it) { return String(it.id) === String(sId); });
      snitchWishBtn.classList.toggle('active', isSActive);
    }
  }

  // 5. Render Wishlist Drawer items list
  var listContainer = document.getElementById('wishlistItemsList');
  var footerEl = document.getElementById('wishlistFooter');
  if (!listContainer) return;

  if (count === 0) {
    listContainer.innerHTML = '<div style="text-align:center; padding:60px 20px; color:var(--text-muted);">' +
      '<div style="font-size:38px; margin-bottom:12px; opacity:0.65;">🤍</div>' +
      '<p style="font-size:15px; font-weight:700; color:var(--text-main); margin-bottom:6px;">Your Wishlist is Empty</p>' +
      '<p style="font-size:12px; margin-bottom:24px; color:var(--text-muted); line-height:1.5;">Tap the heart icon on any Drop 01 silhouette to save pieces for later review.</p>' +
      '<button type="button" class="modal-btn-primary" style="display:inline-block; width:auto; padding:11px 26px;" onclick="toggleWishlistDrawer(); window.location.href=\'/collections/all\';">EXPLORE DROP 01</button>' +
      '</div>';
    if (footerEl) footerEl.style.display = 'none';
  } else {
    var html = '';
    list.forEach(function(item) {
      var imgHtml = item.image ? '<img src="' + item.image + '" alt="' + (item.title || '') + '" style="width:72px; height:90px; object-fit:cover; border-radius:4px; border:1px solid rgba(0,0,0,0.06); background:#FAF8F5;">' : '<div style="width:72px; height:90px; background:#FAF8F5; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:20px;">👗</div>';
      html += '<div class="cart-drawer-item" style="display:flex; gap:14px; margin-bottom:16px; padding-bottom:16px; border-bottom:1px solid var(--border-color); align-items:center; position:relative;">' +
        '<a href="' + (item.url || '/collections/all') + '" style="display:block; flex-shrink:0;">' + imgHtml + '</a>' +
        '<div style="flex:1; padding-right:24px;">' +
          '<a href="' + (item.url || '/collections/all') + '" style="text-decoration:none; font-size:13px; font-weight:700; color:var(--text-main); display:block; line-height:1.35; margin-bottom:4px;">' + item.title + '</a>' +
          '<div style="font-size:14px; font-weight:700; color:var(--text-main); margin-bottom:6px;">' + item.price + '</div>' +
          '<a href="' + (item.url || '/collections/all') + '" style="display:inline-flex; align-items:center; gap:4px; font-size:11px; font-weight:700; text-transform:uppercase; color:var(--accent-gold, #9E7D3B); text-decoration:none; letter-spacing:0.04em;">' +
            'View Silhouette &rarr;' +
          '</a>' +
        '</div>' +
        '<button type="button" onclick="removeFromWishlist(\'' + item.id + '\')" style="position:absolute; top:4px; right:0; background:none; border:none; font-size:22px; color:#999; cursor:pointer; line-height:1; padding:4px;" title="Remove from Wishlist">&times;</button>' +
      '</div>';
    });
    listContainer.innerHTML = html;
    if (footerEl) footerEl.style.display = 'block';
  }
}

/* =========================================================================
   3. CART DRAWER & SHOPIFY AJAX CART CONTROLS
   ========================================================================= */
function formatMoney(cents) {
  if (isNaN(cents)) return '₹0';
  var rupees = Math.round(cents / 100);
  return '₹' + rupees.toLocaleString('en-IN');
}

function toggleCartDrawer() {
  window.location.href = '/cart';
}

function refreshCartDrawer() {
  fetch('/cart.js')
    .then(function(res) {
      if (!res.ok) throw new Error('Cart fetch error');
      return res.json();
    })
    .then(function(cart) {
      updateCartUI(cart);
    })
    .catch(function(err) {
      console.log('Cart fetch notice (development/mock mode):', err);
    });
}

function updateCartUI(cart) {
  if (!cart) return;

  // 1. Header cart count
  var headerBadge = document.getElementById('headerCartCount');
  if (headerBadge) {
    headerBadge.textContent = cart.item_count || 0;
    headerBadge.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
  }

  // 2. Mobile drawer count
  var navCartEls = document.querySelectorAll('.nav-drawer-cart-count');
  navCartEls.forEach(function(el) {
    el.textContent = cart.item_count || 0;
    el.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
  });

  // 3. Cart Drawer header count
  var drawerCount = document.getElementById('cartDrawerCount');
  if (drawerCount) drawerCount.textContent = cart.item_count || 0;

  // 4. Cart subtotal
  var subtotalEl = document.getElementById('cartDrawerSubtotal');
  if (subtotalEl) subtotalEl.textContent = formatMoney(cart.total_price);

  // 5. Cart line items body
  var bodyEl = document.getElementById('cartDrawerBody');
  var footerEl = document.getElementById('cartDrawerFooter');
  if (!bodyEl) return;

  if (cart.item_count === 0) {
    bodyEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">' +
      '<div style="font-size: 40px; margin-bottom: 12px; opacity: 0.7;">🛍️</div>' +
      '<p style="font-size: 15px; margin-bottom: 6px; color: var(--text-main); font-weight: 700;">Your shopping bag is empty.</p>' +
      '<p style="font-size: 12px; margin-bottom: 24px; color: var(--text-muted); line-height: 1.5;">Explore our Drop 01 handcrafted silhouettes and select your size.</p>' +
      '<button type="button" class="modal-btn-primary" style="display: inline-block; width: auto; padding: 11px 26px;" onclick="toggleCartDrawer(); window.location.href=\'/collections/all\';">EXPLORE DROP 01</button>' +
      '</div>';
    if (footerEl) footerEl.style.display = 'none';
  } else {
    var html = '';
    cart.items.forEach(function(item) {
      var img = item.image ? '<img src="' + item.image + '" alt="' + (item.title || '') + '" style="width: 72px; height: 90px; object-fit: cover; background: #FAF8F5; border-radius: 4px; padding: 2px; border: 1px solid rgba(0,0,0,0.06);">' : '<div style="width: 72px; height: 90px; background: #FAF8F5; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 20px;">👗</div>';
      var variantInfo = item.variant_title ? '<div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Size: <strong>' + item.variant_title + '</strong></div>' : '';

      html += '<div class="cart-drawer-item" data-line-key="' + item.key + '" style="display: flex; gap: 14px; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--border-color); align-items: center; position: relative;">' +
        img +
        '<div style="flex: 1; padding-right: 20px;">' +
          '<div style="font-size: 13px; font-weight: 700; color: var(--text-main); line-height: 1.35;">' + item.product_title + '</div>' +
          variantInfo +
          '<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">' +
            '<div style="display: flex; align-items: center; border: 1px solid var(--border-color); border-radius: 4px; overflow: hidden; background: #FAF8F5;">' +
              '<button type="button" onclick="updateCartItemQty(\'' + item.key + '\', ' + (item.quantity - 1) + ')" style="border: none; background: transparent; width: 28px; height: 28px; cursor: pointer; font-size: 14px; font-weight: 700; line-height: 1;">-</button>' +
              '<span style="font-size: 12px; font-weight: 700; min-width: 26px; text-align: center;">' + item.quantity + '</span>' +
              '<button type="button" onclick="updateCartItemQty(\'' + item.key + '\', ' + (item.quantity + 1) + ')" style="border: none; background: transparent; width: 28px; height: 28px; cursor: pointer; font-size: 14px; font-weight: 700; line-height: 1;">+</button>' +
            '</div>' +
            '<div style="font-size: 14px; font-weight: 700; color: var(--text-main);">' + formatMoney(item.final_line_price) + '</div>' +
          '</div>' +
        '</div>' +
        '<button type="button" onclick="updateCartItemQty(\'' + item.key + '\', 0)" style="position: absolute; top: 0; right: 0; background: none; border: none; font-size: 20px; color: #999; cursor: pointer; padding: 4px;" title="Remove">&times;</button>' +
      '</div>';
    });
    bodyEl.innerHTML = html;
    if (footerEl) footerEl.style.display = 'block';
  }
}

function updateCartItemQty(lineKey, newQty) {
  fetch('/cart/change.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id: lineKey, quantity: Math.max(0, newQty) })
  })
  .then(function(res) { return res.json(); })
  .then(function(cart) {
    updateCartUI(cart);
    if (newQty === 0) {
      showMeenuToast('Item removed from Bag');
    }
  })
  .catch(function(err) {
    console.error('Failed to update cart quantity:', err);
  });
}

function addToCartAjax(variantId, quantity) {
  return fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      items: [{
        id: variantId,
        quantity: quantity || 1
      }]
    })
  })
  .then(function(res) {
    if (!res.ok) throw new Error('Add to cart failed');
    return res.json();
  })
  .then(function(data) {
    refreshCartDrawer();
    toggleCartDrawer();
    showMeenuToast('Added to Shopping Bag 🛍️');
    return data;
  });
}

/* =========================================================================
   4. NAVIGATION DRAWER & MODAL CONTROLS
   ========================================================================= */
function openNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.add('open');
  if (b) b.classList.add('open');
}

function closeNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.remove('open');
  if (b) b.classList.remove('open');
}

function openSizeGuideModal() {
  var modal = document.getElementById('SizeGuideModal');
  if (modal) modal.style.display = 'flex';
}

function closeSizeGuideModal() {
  var modal = document.getElementById('SizeGuideModal');
  if (modal) modal.style.display = 'none';
}

function closeSearchBar(e) {
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  var bar = document.getElementById('searchOverlayBar');
  if (bar) bar.classList.remove('open');
}

function toggleSearchBar(e) {
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  var willOpen = !bar.classList.contains('open');
  bar.classList.toggle('open');
  if (willOpen) {
    var inp = document.getElementById('searchInput');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  }
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
    closeSearchBar();
  }
});

document.addEventListener('click', function(e) {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar || !bar.classList.contains('open')) return;
  var isSearchTrigger = e.target.closest && e.target.closest('.header-search-btn, .search-close-action, [onclick*="toggleSearchBar"], [onclick*="closeSearchBar"]');
  var isInsideBar = bar.contains(e.target);
  if (!isInsideBar && !isSearchTrigger) {
    closeSearchBar();
  }
});

function checkTricityPincode(pin) {
  var res = document.getElementById('PincodeResult');
  if (!res) return;
  if (!pin || pin.length !== 6) {
    res.textContent = 'Please enter a valid 6-digit Pincode';
    res.style.color = '#B83A3A';
    return;
  }
  if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {
    res.textContent = '⚡ Tricity Priority! Delivery Tomorrow by 2 PM via Express Dispatch.';
    res.style.color = '#2B6E44';
  } else {
    res.textContent = '✓ Express Delivery Available within 2-3 business days.';
    res.style.color = '#2B6E44';
  }
}

/* =========================================================================
   5. SNITCH CINEMATIC HERO CAROUSEL CONTROLLER
   ========================================================================= */
var currentSlide = 0;
var totalSlides = 4;
var slideInterval = 6000;
var slideTimer = null;

function updateSlider() {
  var track = document.getElementById('sliderTrack');
  var dotsContainer = document.getElementById('sliderDots');
  if (track) {
    track.style.transform = 'translateX(-' + (currentSlide * 25) + '%)';
  }
  if (dotsContainer) {
    var dots = dotsContainer.querySelectorAll('.slider-dot');
    dots.forEach(function(dot, idx) {
      if (idx === currentSlide) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  updateSlider();
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  updateSlider();
}

function goToSlide(idx) {
  currentSlide = idx;
  updateSlider();
  resetAutoSlide();
}

function startAutoSlide() {
  stopAutoSlide();
  slideTimer = setInterval(nextSlide, slideInterval);
}

function stopAutoSlide() {
  if (slideTimer) {
    clearInterval(slideTimer);
    slideTimer = null;
  }
}

function resetAutoSlide() {
  stopAutoSlide();
  startAutoSlide();
}

/* =========================================================================
   6. CLIENT CARE POLICY MODAL CONTROLLER
   ========================================================================= */
var STORE_POLICIES = {
  about: {
    title: "About Us • The Meenu Label Story",
    html: "<h3>Handcrafted in Chandigarh. Inspired by Grace.</h3><p>Meenu Label is a contemporary designer pret atelier born in Chandigarh, dedicated to crafting breathable, modern silhouettes for women across India.</p><p>The label was founded by Sandeep Singh and named with deep affection after his sister, <strong>Meenu</strong>—embodying a family commitment to thoughtfulness, warmth, and artisanal integrity.</p><h3>Why We Exist</h3><p>For too long, modern women in India have had to settle between stiff, synthetic fast-fashion that wrinkles in hours, or heavy, uncomfortable traditional wear that cannot be worn beyond a single festive celebration.</p><p>We created <strong>Meenu Label</strong> to provide an effortless middle ground:</p><ul><li><strong>100% Pure, Breathable Textiles:</strong> We work exclusively with rich Jaipur cottons, soft muslins, fluid silk crepes, and authentic Chanderi silks. Zero synthetic friction.</li><li><strong>Thoughtful, Functional Tailoring:</strong> Every bottom silhouette features deep, functional pockets that securely hold your smartphone. Tunics and kurtas feature relaxed comfort waistbands and modest, flattering hemlines designed for all-day ease.</li><li><strong>Strict Atelier Scarcity:</strong> We reject mass factory production. Drop 01 is produced in strictly small batches (only 3 pieces per size nationwide) to preserve individuality and minimize textile waste.</li></ul><p><em>From morning work meetings and cafe brunches to intimate evening celebrations, Meenu Label pieces are made to move with you in effortless grace.</em></p>"
  },
  shipping: {
    title: "Shipping & Delivery Policy",
    html: "<h3>Pan-India Priority Dispatch</h3><p>Every Meenu Label garment is hand-inspected, steam-pressed, wrapped in protective butter paper, and packed in our signature atelier box before dispatch from our Chandigarh warehouse.</p><h3>Delivery Timelines</h3><ul><li><strong>Chandigarh Tricity (Chandigarh, Mohali, Panchkula):</strong> 24 to 48 Hours Priority Express Delivery.</li><li><strong>Metro Cities (Delhi-NCR, Mumbai, Bengaluru, Jaipur, Hyderabad, Pune, Kolkata):</strong> 2 to 4 Business Days.</li><li><strong>Rest of India:</strong> 3 to 6 Business Days across 26,000+ serviceable pincodes.</li></ul><h3>Shipping Charges</h3><ul><li><strong>Prepaid Orders (UPI, GPay, PhonePe, Cards, NetBanking):</strong> 100% FREE Express Delivery across India.</li><li><strong>Prepaid Perk:</strong> Enjoy instant ₹100 discount auto-applied at checkout on all online payments with code <strong>UPI100</strong>.</li></ul><h3>Cash on Delivery (COD) Terms</h3><p>Cash on Delivery is available across all serviceable Indian pincodes. To prevent transit cancellations, all COD orders undergo automated WhatsApp / Phone verification prior to dispatch.</p><h3>Order Tracking</h3><p>As soon as your package is dispatched, you will receive an automated tracking link via SMS & WhatsApp to monitor live doorstep delivery.</p>"
  },
  exchange: {
    title: "Atelier Sizing Guarantee & Exchange Terms",
    html: "<h3>7-Day Hassle-Free Doorstep Exchange</h3><p>At Meenu Label, we want your silhouette to fit like it was custom-tailored for you. If your piece doesn't fit exactly as desired, we offer a seamless <strong>7-Day Doorstep Size Exchange</strong>.</p><h3>How Exchange Works</h3><ol><li><strong>Initiate:</strong> Send a WhatsApp message to our Concierge Team at <strong>+91 85116 16133</strong> with your Order Number and desired replacement size (M, L, or XL).</li><li><strong>Doorstep Pickup:</strong> Our courier partner will arrive at your address to inspect and pick up the original garment.</li><li><strong>Priority Re-dispatch:</strong> Your fresh replacement piece will be dispatched immediately with zero extra delivery charges.</li></ol><h3>Eligibility Conditions</h3><ul><li>Garment must be unworn, unwashed, and undamaged with all original atelier brand tags intact.</li><li>Must be returned in the original reusable EVA zipper pouch provided.</li><li>Exchange request must be submitted within 7 calendar days of delivery.</li></ul>"
  },
  privacy: {
    title: "Privacy Policy & Terms of Service",
    html: "<h3>Your Privacy is Sacred</h3><p>Meenu Label (operating as a sole proprietorship based in Chandigarh, India) is committed to protecting your personal data in full compliance with Indian Information Technology regulations.</p><h3>Information We Collect</h3><ul><li><strong>Account Details:</strong> Name, contact phone number, and delivery address to fulfill your orders.</li><li><strong>Payment Privacy:</strong> We DO NOT store debit/credit card numbers or UPI PINs. All payments are processed through 256-Bit SSL encrypted, PCI-DSS Level 1 compliant gateways.</li><li><strong>Communication:</strong> Order confirmation, dispatch notifications, and sizing support via SMS and WhatsApp.</li></ul><h3>No Third-Party Sharing</h3><p>We strictly never rent, sell, or trade our client list with external marketing agencies or data brokers. Your information remains confidential with Meenu Label.</p>"
  },
  contact: {
    title: "Contact Us & Customer Care Concierge",
    html: "<h3>Chandigarh Atelier & Client Concierge</h3><p>We are delighted to assist you with sizing advice, custom styling recommendations, or order inquiries.</p><ul><li><strong>WhatsApp Concierge (Fastest Response):</strong> <a href='https://wa.me/918511616133' target='_blank' style='color:#25D366; font-weight:700;'>+91 85116 16133</a> (10:00 AM – 7:00 PM IST, Monday to Saturday)</li><li><strong>Official Email Support:</strong> <a href='mailto:support@meenulabel.com' style='color:#6E1A24; font-weight:700;'>support@meenulabel.com</a></li><li><strong>Atelier Headquarters:</strong> Meenu Label, Chandigarh Tricity, Punjab & Haryana, India</li><li><strong>Official Domain:</strong> <a href='https://meenulabel.com' target='_blank'>meenulabel.com</a> / <a href='https://meenulabel.in' target='_blank'>meenulabel.in</a></li></ul>"
  }
};

function openPolicyModal(type) {
  var pol = STORE_POLICIES[type] || STORE_POLICIES.about;
  var titleEl = document.getElementById('policyModalTitle');
  var contentEl = document.getElementById('policyModalContent');
  var backdrop = document.getElementById('policyModalBackdrop');
  if (titleEl) titleEl.textContent = pol.title;
  if (contentEl) contentEl.innerHTML = pol.html;
  if (backdrop) backdrop.classList.add('open');
}

function closePolicyModal() {
  var backdrop = document.getElementById('policyModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
}

function closePolicyModalOnBackdrop(e) {
  if (e.target.id === 'policyModalBackdrop') {
    closePolicyModal();
  }
}

/* =========================================================================
   7. INITIALIZATION ON DOM READY
   ========================================================================= */
document.addEventListener('DOMContentLoaded', function() {
  console.log('Meenu Label Theme Initialized with Dynamic Cart & Wishlist');

  // Initialize saved wishlist state & UI
  updateWishlistUI();

  // Refresh cart state & count from Shopify backend
  refreshCartDrawer();

  // Hero carousel auto slide
  var heroEl = document.getElementById('heroSlider');
  if (heroEl) {
    heroEl.addEventListener('mouseenter', stopAutoSlide);
    heroEl.addEventListener('mouseleave', startAutoSlide);
    startAutoSlide();
  }
});


/* =========================================================================
   8. WHATSAPP ATELIER CONCIERGE CONTROLLER
   ========================================================================= */
function toggleWaPopup(e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  var card = document.getElementById('waPopupCard');
  if (!card) return;
  var isHidden = card.style.display === 'none' || !card.style.display;
  if (isHidden) {
    card.style.display = 'flex';
    var inp = document.getElementById('waCustomMessage');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  } else {
    card.style.display = 'none';
  }
}

function sendWaPreset(text) {
  var phone = '918511616133';
  var url = 'https://wa.me/' + phone + '?text=' + encodeURIComponent(text);
  window.open(url, '_blank');
  var card = document.getElementById('waPopupCard');
  if (card) card.style.display = 'none';
}

function handleWaCustomSubmit(e) {
  if (e) e.preventDefault();
  var inp = document.getElementById('waCustomMessage');
  var msg = inp ? inp.value.trim() : '';
  if (!msg) {
    msg = 'Hi Meenu Label! I have a question about Drop 01 silhouettes and sizing.';
  }
  sendWaPreset(msg);
  if (inp) inp.value = '';
}

document.addEventListener('click', function(e) {
  var container = document.getElementById('waConciergeContainer');
  var card = document.getElementById('waPopupCard');
  if (card && card.style.display !== 'none' && container && !container.contains(e.target)) {
    card.style.display = 'none';
  }
});


/* =========================================================================
   9. DYNAMIC STICKY HEADER HEIGHT SYNCHRONIZER
   ========================================================================= */
function updateStickyHeaderHeight() {
  var header = document.getElementById('siteStickyHeaderContainer');
  if (header) {
    var h = header.offsetHeight;
    if (h > 0) {
      document.documentElement.style.setProperty('--sticky-header-height', h + 'px');
    }
  }
}
window.addEventListener('DOMContentLoaded', updateStickyHeaderHeight);
window.addEventListener('resize', updateStickyHeaderHeight);
window.addEventListener('load', updateStickyHeaderHeight);


/* =========================================================================
   10. INSTANT IN-PAGE CATEGORY FILTER CONTROLLER
   ========================================================================= */
function filterCategory(cat, btn) {
  var cards = document.querySelectorAll('#productGrid .product-card, .catalog-section .product-card');
  var matchedCount = 0;
  var normalizedCat = String(cat || 'all').toLowerCase();

  cards.forEach(function(card) {
    var cardCat = (card.getAttribute('data-category') || card.textContent || '').toLowerCase();
    var isMatch = false;

    if (normalizedCat === 'all') {
      isMatch = true;
    } else if (normalizedCat === 'coord' || normalizedCat === 'co-ord' || normalizedCat === 'co-ord-sets') {
      isMatch = cardCat.indexOf('coord') !== -1 || cardCat.indexOf('co-ord') !== -1;
    } else if (normalizedCat === 'festive' || normalizedCat === 'festive-suits') {
      isMatch = cardCat.indexOf('festive') !== -1;
    } else if (normalizedCat === 'dress' || normalizedCat === 'dresses') {
      isMatch = cardCat.indexOf('dress') !== -1;
    } else if (normalizedCat === 'top' || normalizedCat === 'tops' || normalizedCat === 'blouse') {
      isMatch = cardCat.indexOf('top') !== -1 || cardCat.indexOf('blouse') !== -1;
    } else {
      isMatch = cardCat.indexOf(normalizedCat) !== -1;
    }

    if (isMatch) {
      card.style.display = 'flex';
      matchedCount++;
    } else {
      card.style.display = 'none';
    }
  });

  document.querySelectorAll('.filter-tabs .filter-tab').forEach(function(t) {
    t.classList.remove('active');
  });
  if (btn) {
    btn.classList.add('active');
  }

  var countEl = document.getElementById('activeCategoryCount');
  if (countEl) {
    if (normalizedCat === 'all') {
      countEl.textContent = 'HANDCRAFTED EDITIONS';
    } else {
      countEl.textContent = matchedCount + ' SILHOUETTES AVAILABLE';
    }
  }
}

// Auto-trigger filter if URL has category hash (e.g. #co-ord-sets)
window.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash) {
    var h = window.location.hash.replace('#', '').toLowerCase();
    var tab = document.querySelector('.filter-tabs [data-cat*="' + h + '"]');
    if (tab) {
      tab.click();
    }
  }
});

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
    var isSaved = false;
    if (typeof isWishlisted === 'function') {
      isSaved = isWishlisted(productId);
    } else if (typeof wishlist !== 'undefined') {
      isSaved = wishlist.indexOf(productId) !== -1;
    }
    wishBtn.classList.toggle('active', isSaved);
    wishBtn.setAttribute('data-wishlist-id', productId);
    wishBtn.setAttribute('data-wishlist-title', title);
    wishBtn.setAttribute('data-wishlist-price', price);
    wishBtn.setAttribute('data-wishlist-image', img);
    wishBtn.setAttribute('data-wishlist-url', url);
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
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled sold-out' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status' + (!isAvailable ? ' sold-out-status' : '');
  if (!isAvailable) {
    statusSpan.innerHTML = '<span style="color:#25D366; font-size:12px; margin-right:4px;">&#128172;</span> NOTIFY ON WHATSAPP';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  } else {
    row.onclick = function() {
      closeSnitchSizePopup();
      var msg = 'Hi Meenu Label! Please notify me when "' + (activeSnitchProduct ? activeSnitchProduct.title : 'this silhouette') + '" in Size ' + sizeName + ' is back in stock. Please share restock timeline.';
      var waUrl = 'https://wa.me/918511616133?text=' + encodeURIComponent(msg);
      window.open(waUrl, '_blank');
      if (typeof showMeenuToast === 'function') {
        showMeenuToast('Opening WhatsApp Concierge for Size ' + sizeName + '... 💬');
      }
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
        var allBadges = document.querySelectorAll('#headerCartCount, .header-cart-pill, .cart-count-badge, .header-cart-count, #cartCountBadge, .nav-drawer-cart-count, #cartDrawerCount');
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

function toggleSnitchSizeWishlist(btn) {
  if (!activeSnitchProduct) return;
  var pId = String(activeSnitchProduct.id);

  // 1. Live Shopify theme environment (localStorage 'meenu_saved_wishlist')
  if (typeof getWishlist === 'function' && typeof saveWishlist === 'function') {
    var list = getWishlist();
    var idx = list.findIndex(function(it) { return String(it.id) === pId; });
    var willBeSaved = (idx === -1);

    if (idx >= 0) {
      list.splice(idx, 1);
      saveWishlist(list);
      if (typeof showMeenuToast === 'function') showMeenuToast('Removed from Wishlist');
    } else {
      list.push({
        id: pId,
        title: activeSnitchProduct.title || 'Atelier Silhouette',
        price: activeSnitchProduct.price || '',
        image: activeSnitchProduct.image || '',
        url: activeSnitchProduct.url || '#'
      });
      saveWishlist(list);
      if (typeof showMeenuToast === 'function') showMeenuToast('Saved to Wishlist ❤️');
    }
    btn.classList.toggle('active', willBeSaved);
    var cardBtn = document.querySelector('[data-wishlist-id="' + pId + '"]');
    if (cardBtn) cardBtn.classList.toggle('active', willBeSaved);
    return;
  }

  // 2. Standalone preview environment (index.html, global wishlist array)
  if (typeof wishlist !== 'undefined') {
    var idx = wishlist.indexOf(pId);
    var cardWishBtn = document.getElementById('wishBtn_' + pId) || document.querySelector('[data-wishlist-id="' + pId + '"]');
    if (idx === -1) {
      wishlist.push(pId);
      btn.classList.add('active');
      if (cardWishBtn) cardWishBtn.classList.add('active');
      if (typeof showToast === 'function') showToast('Added to your Wishlist!');
    } else {
      wishlist.splice(idx, 1);
      btn.classList.remove('active');
      if (cardWishBtn) cardWishBtn.classList.remove('active');
      if (typeof showToast === 'function') showToast('Removed from your Wishlist.');
    }
    if (typeof updateWishlistUI === 'function') {
      updateWishlistUI();
    }
    return;
  }

  btn.classList.toggle('active');
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


/* =========================================================================
   MEENU LABEL - SOLD OUT & LUXURY NOTIFY ME / RESTOCK WAITLIST SYSTEM
   ========================================================================= */

var activeNotifyProduct = {
  id: '',
  size: 'M',
  title: '',
  image: '',
  price: '',
  channel: 'whatsapp'
};

function openNotifyMeModal(productId, size, title, image, price) {
  var backdrop = document.getElementById('meenuNotifyBackdrop');
  if (!backdrop) return;

  activeNotifyProduct.id = productId || '';
  activeNotifyProduct.size = size || 'M';
  activeNotifyProduct.title = title || 'Atelier Silhouette';
  activeNotifyProduct.image = image || '';
  activeNotifyProduct.price = price || '';
  activeNotifyProduct.channel = 'whatsapp';

  // Set modal snapshot info
  var titleEl = document.getElementById('notifyProductTitle');
  if (titleEl) titleEl.textContent = activeNotifyProduct.title;

  var priceEl = document.getElementById('notifyProductPrice');
  if (priceEl) priceEl.textContent = activeNotifyProduct.price;

  var imgEl = document.getElementById('notifyProductImg');
  if (imgEl && activeNotifyProduct.image) {
    imgEl.src = activeNotifyProduct.image;
    imgEl.alt = activeNotifyProduct.title;
  }

  // Update size pills
  var pills = document.querySelectorAll('.notify-size-pill');
  pills.forEach(function(pill) {
    var pillSize = pill.getAttribute('data-size');
    pill.classList.toggle('active', pillSize === activeNotifyProduct.size);
  });

  // Reset channel tabs to WhatsApp
  switchNotifyTab('whatsapp');

  // Clear inputs and errors
  var phoneInput = document.getElementById('notifyPhoneInput');
  if (phoneInput) phoneInput.value = '';
  var emailInput = document.getElementById('notifyEmailInput');
  if (emailInput) emailInput.value = '';

  var phoneErr = document.getElementById('notifyPhoneError');
  if (phoneErr) phoneErr.style.display = 'none';
  var emailErr = document.getElementById('notifyEmailError');
  if (emailErr) emailErr.style.display = 'none';

  // Ensure form is visible, success is hidden
  var formView = document.getElementById('notifyFormView');
  if (formView) formView.style.display = 'block';
  var successView = document.getElementById('notifySuccessView');
  if (successView) successView.style.display = 'none';

  var submitBtn = document.getElementById('notifySubmitBtn');
  if (submitBtn) {
    submitBtn.disabled = false;
    var submitText = document.getElementById('notifySubmitText');
    if (submitText) submitText.innerHTML = 'NOTIFY ME WHEN RESTOCKED &rarr;';
  }

  // Update concierge WhatsApp link
  updateNotifyConciergeLink();

  // Show backdrop with smooth animation
  backdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeNotifyMeModal() {
  var backdrop = document.getElementById('meenuNotifyBackdrop');
  if (backdrop) backdrop.classList.remove('open');
  document.body.style.overflow = '';
}

function closeNotifyMeModalOnBackdrop(event) {
  if (event.target.id === 'meenuNotifyBackdrop') {
    closeNotifyMeModal();
  }
}

function selectNotifySize(size, btn) {
  activeNotifyProduct.size = size;
  var pills = document.querySelectorAll('.notify-size-pill');
  pills.forEach(function(pill) { pill.classList.remove('active'); });
  if (btn) btn.classList.add('active');
  updateNotifyConciergeLink();
}

function switchNotifyTab(channel) {
  activeNotifyProduct.channel = channel;
  var tabWa = document.getElementById('notifyTabWhatsApp');
  var tabEm = document.getElementById('notifyTabEmail');
  var groupWa = document.getElementById('notifyWhatsAppGroup');
  var groupEm = document.getElementById('notifyEmailGroup');

  if (channel === 'whatsapp') {
    if (tabWa) tabWa.classList.add('active');
    if (tabEm) tabEm.classList.remove('active');
    if (groupWa) groupWa.style.display = 'block';
    if (groupEm) groupEm.style.display = 'none';
  } else {
    if (tabWa) tabWa.classList.remove('active');
    if (tabEm) tabEm.classList.add('active');
    if (groupWa) groupWa.style.display = 'none';
    if (groupEm) groupEm.style.display = 'block';
  }
}

function updateNotifyConciergeLink() {
  var conciergeBtn = document.getElementById('notifyConciergeWhatsAppBtn');
  if (conciergeBtn) {
    var msg = 'Hi Meenu Label! I would like to reserve or be notified when "' + (activeNotifyProduct.title || 'this ensemble') + '" in Size ' + (activeNotifyProduct.size || 'M') + ' is crafted again. Please share restock timeline.';
    conciergeBtn.href = 'https://wa.me/918511616133?text=' + encodeURIComponent(msg);
  }
}

function submitNotifyMeRequest() {
  var channel = activeNotifyProduct.channel;
  var contactValue = '';

  if (channel === 'whatsapp') {
    var phoneInput = document.getElementById('notifyPhoneInput');
    var phoneErr = document.getElementById('notifyPhoneError');
    var rawPhone = phoneInput ? phoneInput.value.trim().replace(/\D/g, '') : '';
    if (!rawPhone || rawPhone.length !== 10) {
      if (phoneErr) phoneErr.style.display = 'block';
      if (phoneInput) phoneInput.focus();
      return;
    }
    if (phoneErr) phoneErr.style.display = 'none';
    contactValue = '+91 ' + rawPhone;
  } else {
    var emailInput = document.getElementById('notifyEmailInput');
    var emailErr = document.getElementById('notifyEmailError');
    var rawEmail = emailInput ? emailInput.value.trim() : '';
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!rawEmail || !emailRegex.test(rawEmail)) {
      if (emailErr) emailErr.style.display = 'block';
      if (emailInput) emailInput.focus();
      return;
    }
    if (emailErr) emailErr.style.display = 'none';
    contactValue = rawEmail;
  }

  // Visual submit state
  var submitBtn = document.getElementById('notifySubmitBtn');
  var submitText = document.getElementById('notifySubmitText');
  if (submitBtn) submitBtn.disabled = true;
  if (submitText) submitText.innerHTML = 'RESERVING WAITLIST...';

  // Save to localStorage
  try {
    var alerts = JSON.parse(localStorage.getItem('meenu_restock_alerts') || '[]');
    alerts.push({
      productId: activeNotifyProduct.id,
      title: activeNotifyProduct.title,
      size: activeNotifyProduct.size,
      channel: channel,
      contact: contactValue,
      timestamp: new Date().toISOString()
    });
    localStorage.setItem('meenu_restock_alerts', JSON.stringify(alerts));
  } catch(e) {}

  // Direct WhatsApp Concierge (Option A): Open WhatsApp chat directly so the merchant receives phone number & request!
  if (channel === 'whatsapp') {
    var waMsg = 'Hi Meenu Label! My contact number is ' + contactValue + '. Please notify me when "' + (activeNotifyProduct.title || 'this silhouette') + '" in Size ' + (activeNotifyProduct.size || 'M') + ' is back in stock. Please share restock timeline.';
    var waUrl = 'https://wa.me/918511616133?text=' + encodeURIComponent(waMsg);
    window.open(waUrl, '_blank');
  }

  // Also submit to Shopify native /contact endpoint in the background
  try {
    var formData = new FormData();
    formData.append('form_type', 'contact');
    formData.append('utf8', '✓');
    formData.append('contact[tags]', 'restock-waitlist, ' + (activeNotifyProduct.title || '') + ', Size ' + (activeNotifyProduct.size || ''));
    formData.append('contact[body]', 'Restock Alert Request for ' + (activeNotifyProduct.title || '') + ' (Size ' + (activeNotifyProduct.size || '') + '). Customer Contact: ' + contactValue);
    if (channel === 'email') {
      formData.append('contact[email]', contactValue);
    } else {
      var safeDigits = contactValue.replace(/\D/g, '');
      formData.append('contact[email]', 'restock-' + safeDigits + '@meenulabel.com');
      formData.append('contact[note][WhatsApp_Phone]', contactValue);
    }
    fetch('/contact', { method: 'POST', body: formData }).catch(function(){});
  } catch(e) {}

  setTimeout(function() {
    var formView = document.getElementById('notifyFormView');
    var successView = document.getElementById('notifySuccessView');
    var sizeDisplay = document.getElementById('notifySuccessSize');

    if (sizeDisplay) sizeDisplay.textContent = activeNotifyProduct.size;
    if (formView) formView.style.display = 'none';
    if (successView) successView.style.display = 'block';

    if (channel === 'whatsapp') {
      var successMsg = document.getElementById('notifySuccessMsg');
      if (successMsg) {
        successMsg.innerHTML = 'Connecting with our Chandigarh stylist via WhatsApp! We have recorded your request for Size <strong>' + activeNotifyProduct.size + '</strong> and will message you the moment it is ready.';
      }
    }

    if (typeof showMeenuToast === 'function') {
      showMeenuToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    } else if (typeof showToast === 'function') {
      showToast('Waitlist confirmed for Size ' + activeNotifyProduct.size + ' ✨');
    }
  }, 400);
}


/* =========================================================================
   TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM
   ========================================================================= */

var snitchCurrentUser = null;
var snitchOtpInterval = null;

function isSnitchLoggedIn() {
  if (snitchCurrentUser) return true;
  try {
    var stored = localStorage.getItem('meenu_vip_user');
    if (stored) {
      snitchCurrentUser = JSON.parse(stored);
      return true;
    }
  } catch(e) {}
  return false;
}

function updateAccountHeaderIcon() {
  var badge = document.getElementById('accountActiveBadge');
  if (badge) {
    if (isSnitchLoggedIn()) {
      badge.classList.add('active');
      badge.style.display = 'block';
    } else {
      badge.classList.remove('active');
      badge.style.display = 'none';
    }
  }
}

function switchAccountTab(tabName) {
  var tabTrack = document.getElementById('tabBtnTrack');
  var tabLogin = document.getElementById('tabBtnLogin');
  var viewTrack = document.getElementById('accountViewTrack');
  var viewLogin = document.getElementById('accountViewLogin');

  if (tabTrack) tabTrack.classList.toggle('active', tabName === 'track');
  if (tabLogin) tabLogin.classList.toggle('active', tabName === 'login');

  if (viewTrack) {
    viewTrack.classList.toggle('active', tabName === 'track');
    viewTrack.style.display = tabName === 'track' ? 'block' : 'none';
  }
  if (viewLogin) {
    viewLogin.classList.toggle('active', tabName === 'login');
    viewLogin.style.display = tabName === 'login' ? 'block' : 'none';
  }

  if (tabName === 'track') {
    setTimeout(function() {
      var inp = document.getElementById('orderTrackingInput');
      if (inp) inp.focus();
    }, 150);
  } else if (tabName === 'login') {
    if (isSnitchLoggedIn()) {
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      var v = document.getElementById('loginStepVip');
      if (p) p.style.display = 'none';
      if (o) o.style.display = 'none';
      if (v) v.style.display = 'block';
      var u = document.getElementById('snitchVipUserDisplay');
      if (u) u.textContent = (snitchCurrentUser && snitchCurrentUser.phone) ? snitchCurrentUser.phone : '+91 85116 16133';
    } else {
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      var v = document.getElementById('loginStepVip');
      if (p) p.style.display = 'block';
      if (o) o.style.display = 'none';
      if (v) v.style.display = 'none';
      setTimeout(function() {
        var inp = document.getElementById('snitchMobileInput');
        if (inp) inp.focus();
      }, 150);
    }
  }
}

function openAccountModal(initialTab) {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (!backdrop) return;
  backdrop.classList.add('open');
  switchAccountTab(initialTab || 'track');
  updateAccountHeaderIcon();
}

function closeAccountModalDirect() {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
  clearInterval(snitchOtpInterval);
}

function closeAccountModal(e) {
  if (e.target.id === 'accountModalBackdrop') {
    closeAccountModalDirect();
  }
}

function fillAndTrackDemo(orderId) {
  switchAccountTab('track');
  var inp = document.getElementById('orderTrackingInput');
  if (inp) inp.value = orderId;
  executeOrderTracking();
}

function executeOrderTracking() {
  var inp = document.getElementById('orderTrackingInput');
  var rawVal = inp ? inp.value.trim() : '';
  var err = document.getElementById('orderTrackingError');
  var container = document.getElementById('trackingResultContainer');

  if (!rawVal) {
    if (err) {
      err.textContent = 'Please enter an Order ID (e.g. #ML-1042) or your 10-digit mobile number.';
      err.style.display = 'block';
    }
    if (inp) inp.focus();
    return;
  }
  if (err) err.style.display = 'none';

  var cleanVal = rawVal.toUpperCase();
  var isDelivered = cleanVal.indexOf('1035') !== -1;
  var isTransit = cleanVal.indexOf('1042') !== -1 || cleanVal.indexOf('8511616133') !== -1;

  var orderNum = isDelivered ? '#ML-1035' : (isTransit ? '#ML-1042' : (cleanVal.startsWith('#') ? cleanVal : '#' + cleanVal));
  var productName = isDelivered ? 'Noor Zari Silk Anarkali Set (Size: S)' : (isTransit ? 'Gulab Organza Embroidered Kurta Set (Size: M)' : 'Atelier Drop 01 Handcrafted Silhouette');
  var awbInfo = isDelivered ? 'BlueDart Air • AWB #BD-9918231' : (isTransit ? 'Delhivery Express • AWB #DEL-85116133-TRC' : 'Assigned Upon Dispatch • Express Courier');
  var dest = isDelivered ? 'Gurugram, Haryana' : (isTransit ? 'Sector 17, Chandigarh (Tricity Express)' : 'Tricity / All India Delivery');
  var statusBadge = isDelivered ? 'Delivered' : (isTransit ? 'In Express Transit' : 'Confirmed & In Production');
  var badgeColor = isDelivered ? '#25D366' : '#C8A364';

  var step1Class = 'timeline-step completed';
  var step2Class = (isDelivered || isTransit) ? 'timeline-step completed' : 'timeline-step active';
  var step3Class = isDelivered ? 'timeline-step completed' : (isTransit ? 'timeline-step active' : 'timeline-step');
  var step4Class = isDelivered ? 'timeline-step completed' : 'timeline-step';

  var waMessage = encodeURIComponent('Hi Meenu Label! I am inquiring about my Order ' + orderNum + ' (' + productName + '). Please share latest delivery updates.');

  var html = '<div class="shipment-card">' +
    '<div class="shipment-header">' +
      '<div>' +
        '<div class="shipment-order-id">' + orderNum + '</div>' +
        '<div style="font-size: 11.5px; color: rgba(255,255,255,0.7); margin-top:2px;">' + productName + '</div>' +
      '</div>' +
      '<span class="shipment-badge" style="background: rgba(' + (isDelivered ? '37, 211, 102' : '200, 163, 100') + ', 0.15); color: ' + badgeColor + '; border-color: ' + badgeColor + ';">' + statusBadge + '</span>' +
    '</div>' +
    '<div class="shipment-timeline">' +
      '<div class="' + step1Class + '">' +
        '<div class="timeline-title">Order Confirmed &amp; Atelier Assigned</div>' +
        '<div class="timeline-desc">Handcrafted silk fabrics reserved &bull; Chandigarh Studio</div>' +
      '</div>' +
      '<div class="' + step2Class + '">' +
        '<div class="timeline-title">Handcrafted &amp; Master Quality Checked</div>' +
        '<div class="timeline-desc">' + (isDelivered || isTransit ? 'Passed 14-point artisan luxury inspection' : 'In progress at Sector 17 Atelier') + '</div>' +
      '</div>' +
      '<div class="' + step3Class + '">' +
        '<div class="timeline-title">Dispatched in Express Transit</div>' +
        '<div class="timeline-desc">' + awbInfo + '</div>' +
      '</div>' +
      '<div class="' + step4Class + '">' +
        '<div class="timeline-title">Out for Delivery &amp; VIP Handover</div>' +
        '<div class="timeline-desc">' + (isDelivered ? 'Delivered with Signature Handover' : 'Expected delivery to ' + dest) + '</div>' +
      '</div>' +
    '</div>' +
    '<div class="shipment-meta-row">' +
      '<span>Destination: <strong>' + dest + '</strong></span>' +
      '<span>ETA: <strong>' + (isDelivered ? 'Delivered' : (isTransit ? 'Today by 7:00 PM' : '24-48 Hours')) + '</strong></span>' +
    '</div>' +
    '<a href="https://wa.me/918511616133?text=' + waMessage + '" target="_blank" class="shipment-wa-btn">' +
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.073.043.419-.101.824z"/></svg>' +
      'Instant WhatsApp Inquiry with Atelier' +
    '</a>' +
  '</div>';

  if (container) {
    container.innerHTML = html;
    container.style.display = 'block';
  }
}

function onSnitchPhoneInput(el) {
  el.value = el.value.replace(/\D/g, '');
  var err = document.getElementById('snitchPhoneError');
  if (err) err.style.display = 'none';
}

function requestSnitchOtp() {
  var inp = document.getElementById('snitchMobileInput');
  var phone = inp ? inp.value.trim() : '';
  if (phone.length < 10) {
    var err = document.getElementById('snitchPhoneError');
    if (err) err.style.display = 'block';
    if (inp) inp.focus();
    return;
  }
  
  var displayEl = document.getElementById('snitchOtpPhoneDisplay');
  if (displayEl) displayEl.textContent = '+91 ' + phone;
  
  var p = document.getElementById('loginStepPhone');
  var o = document.getElementById('loginStepOtp');
  if (p) p.style.display = 'none';
  if (o) o.style.display = 'block';
  
  ['sOtp1', 'sOtp2', 'sOtp3', 'sOtp4'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.value = '';
  });
  var firstBox = document.getElementById('sOtp1');
  if (firstBox) firstBox.focus();
  
  startSnitchOtpTimer();
}

function snitchEditPhone() {
  clearInterval(snitchOtpInterval);
  var p = document.getElementById('loginStepPhone');
  var o = document.getElementById('loginStepOtp');
  if (o) o.style.display = 'none';
  if (p) p.style.display = 'block';
  var inp = document.getElementById('snitchMobileInput');
  if (inp) inp.focus();
}

function snitchOtpNext(curr, nextId) {
  curr.value = curr.value.replace(/\D/g, '');
  if (curr.value && nextId) {
    var next = document.getElementById(nextId);
    if (next) next.focus();
  }
  var code = ((document.getElementById('sOtp1') && document.getElementById('sOtp1').value) || '') +
             ((document.getElementById('sOtp2') && document.getElementById('sOtp2').value) || '') +
             ((document.getElementById('sOtp3') && document.getElementById('sOtp3').value) || '') +
             ((document.getElementById('sOtp4') && document.getElementById('sOtp4').value) || '');
  if (code.length === 4) {
    setTimeout(verifySnitchOtp, 200);
  }
}

function snitchOtpBack(e, curr, prevId) {
  if (e.key === 'Backspace' && !curr.value && prevId) {
    var prev = document.getElementById(prevId);
    if (prev) {
      prev.focus();
      prev.value = '';
    }
  }
}

function startSnitchOtpTimer() {
  var sec = 28;
  var timerTxt = document.getElementById('snitchTimerTxt');
  var countdown = document.getElementById('snitchCountdown');
  var resendBtn = document.getElementById('snitchResendBtn');
  if (timerTxt) timerTxt.style.display = 'inline';
  if (resendBtn) resendBtn.style.display = 'none';
  
  clearInterval(snitchOtpInterval);
  snitchOtpInterval = setInterval(function() {
    sec--;
    if (sec <= 0) {
      clearInterval(snitchOtpInterval);
      if (timerTxt) timerTxt.style.display = 'none';
      if (resendBtn) resendBtn.style.display = 'inline';
    } else {
      if (countdown) countdown.textContent = '0:' + (sec < 10 ? '0' : '') + sec;
    }
  }, 1000);
}

function snitchResendOtp() {
  var inp = document.getElementById('snitchMobileInput');
  var phone = inp ? inp.value.trim() : '';
  alert('New VIP OTP dispatched to +91 ' + phone + ' via SMS & WhatsApp!');
  startSnitchOtpTimer();
}

function verifySnitchOtp() {
  clearInterval(snitchOtpInterval);
  var inp = document.getElementById('snitchMobileInput');
  var phone = (inp && inp.value.trim()) ? inp.value.trim() : '8511616133';
  snitchCurrentUser = {
    phone: '+91 ' + phone,
    loggedInAt: new Date().toISOString(),
    tier: 'Atelier Privé VIP'
  };
  try {
    localStorage.setItem('meenu_vip_user', JSON.stringify(snitchCurrentUser));
  } catch(e) {}
  
  updateAccountHeaderIcon();
  
  var o = document.getElementById('loginStepOtp');
  var v = document.getElementById('loginStepVip');
  if (o) o.style.display = 'none';
  if (v) v.style.display = 'block';
  var u = document.getElementById('snitchVipUserDisplay');
  if (u) u.textContent = snitchCurrentUser.phone;
  
  if (typeof showMeenuToast === 'function') {
    showMeenuToast('Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
  } else if (typeof showToast === 'function') {
    showToast('Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
  }
}

function signOutSnitchUser() {
  snitchCurrentUser = null;
  try {
    localStorage.removeItem('meenu_vip_user');
  } catch(e) {}
  updateAccountHeaderIcon();
  
  var p = document.getElementById('loginStepPhone');
  var v = document.getElementById('loginStepVip');
  if (v) v.style.display = 'none';
  if (p) p.style.display = 'block';
  var inp = document.getElementById('snitchMobileInput');
  if (inp) {
    inp.value = '';
    inp.focus();
  }
  if (typeof showMeenuToast === 'function') {
    showMeenuToast('Signed out of VIP Atelier account.');
  } else if (typeof showToast === 'function') {
    showToast('Signed out of VIP Atelier account.');
  }
}

// Auto update header icon on load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', updateAccountHeaderIcon);
} else {
  updateAccountHeaderIcon();
}

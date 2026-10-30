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

function toggleSearchBar() {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  bar.classList.toggle('open');
  if (bar.classList.contains('open')) {
    var inp = document.getElementById('searchInput');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  }
}

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
    html: "<h3>7-Day Hassle-Free Doorstep Exchange</h3><p>At Meenu Label, we want your silhouette to fit like it was custom-tailored for you. If your piece doesn't fit exactly as desired, we offer a seamless <strong>7-Day Doorstep Size Exchange</strong>.</p><h3>How Exchange Works</h3><ol><li><strong>Initiate:</strong> Send a WhatsApp message to our Concierge Team at <strong>+91 99888 98845</strong> with your Order Number and desired replacement size (M, L, or XL).</li><li><strong>Doorstep Pickup:</strong> Our courier partner will arrive at your address to inspect and pick up the original garment.</li><li><strong>Priority Re-dispatch:</strong> Your fresh replacement piece will be dispatched immediately with zero extra delivery charges.</li></ol><h3>Eligibility Conditions</h3><ul><li>Garment must be unworn, unwashed, and undamaged with all original atelier brand tags intact.</li><li>Must be returned in the original reusable EVA zipper pouch provided.</li><li>Exchange request must be submitted within 7 calendar days of delivery.</li></ul>"
  },
  privacy: {
    title: "Privacy Policy & Terms of Service",
    html: "<h3>Your Privacy is Sacred</h3><p>Meenu Label (operating as a sole proprietorship based in Chandigarh, India) is committed to protecting your personal data in full compliance with Indian Information Technology regulations.</p><h3>Information We Collect</h3><ul><li><strong>Account Details:</strong> Name, contact phone number, and delivery address to fulfill your orders.</li><li><strong>Payment Privacy:</strong> We DO NOT store debit/credit card numbers or UPI PINs. All payments are processed through 256-Bit SSL encrypted, PCI-DSS Level 1 compliant gateways.</li><li><strong>Communication:</strong> Order confirmation, dispatch notifications, and sizing support via SMS and WhatsApp.</li></ul><h3>No Third-Party Sharing</h3><p>We strictly never rent, sell, or trade our client list with external marketing agencies or data brokers. Your information remains confidential with Meenu Label.</p>"
  },
  contact: {
    title: "Contact Us & Customer Care Concierge",
    html: "<h3>Chandigarh Atelier & Client Concierge</h3><p>We are delighted to assist you with sizing advice, custom styling recommendations, or order inquiries.</p><ul><li><strong>WhatsApp Concierge (Fastest Response):</strong> <a href='https://wa.me/919988898845' target='_blank' style='color:#25D366; font-weight:700;'>+91 99888 98845</a> (10:00 AM – 7:00 PM IST, Monday to Saturday)</li><li><strong>Official Email Support:</strong> <a href='mailto:support@meenulabel.com' style='color:#6E1A24; font-weight:700;'>support@meenulabel.com</a></li><li><strong>Atelier Headquarters:</strong> Meenu Label, Chandigarh Tricity, Punjab & Haryana, India</li><li><strong>Official Domain:</strong> <a href='https://meenulabel.com' target='_blank'>meenulabel.com</a> / <a href='https://meenulabel.in' target='_blank'>meenulabel.in</a></li></ul>"
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
  var phone = '919988898845';
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

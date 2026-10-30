import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. ADD CSS FOR UPI BANNERS & CARDS
css_target = ".announcement-bar {"
css_replacement = """/* UPI Instant Offer & Top Announcement Enhancements */
    .announcement-bar {
      background: #1E1C19;
      color: #FAF8F5;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 7px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      min-height: 35px;
      box-sizing: border-box;
    }
    .ann-left, .ann-right {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .ann-center {
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .upi-ann-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(232, 211, 185, 0.16);
      border: 1px solid rgba(232, 211, 185, 0.5);
      color: #FAF8F5;
      padding: 3px 12px;
      border-radius: 20px;
      font-size: 10.5px;
      letter-spacing: 0.06em;
      transition: all 0.25s ease;
      cursor: pointer;
    }
    .upi-ann-badge:hover {
      background: rgba(232, 211, 185, 0.28);
      border-color: #E8D3B9;
    }
    .upi-code-pill {
      background: #E8D3B9;
      color: #1E1C19;
      padding: 2px 7px;
      border-radius: 12px;
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      margin-left: 4px;
    }
    .announcement-bar a { color: #E8D3B9; text-decoration: none; margin-left: 8px; }
    .announcement-bar a:hover { text-decoration: underline; }

    @media (max-width: 991px) {
      .ann-left, .ann-right { display: none !important; }
      .announcement-bar { justify-content: center !important; padding: 7px 16px !important; }
      .upi-ann-badge { font-size: 10px !important; padding: 3px 8px !important; }
    }

    /* PDP UPI Perk Card */
    .pdp-upi-perk-card {
      margin: 16px 0 18px 0;
      background: #FBF9F5;
      border: 1px solid #E5DCCE;
      border-left: 4px solid #2E6B38;
      border-radius: 6px;
      padding: 14px 18px;
      transition: all 0.25s ease;
    }
    .pdp-upi-perk-card:hover {
      box-shadow: 0 4px 16px rgba(46, 107, 56, 0.10);
      border-color: #2E6B38;
    }
    .pdp-upi-perk-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .pdp-upi-badge-chip {
      display: inline-flex;
      align-items: center;
      background: #2E6B38;
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 4px 10px;
      border-radius: 4px;
    }
    .pdp-upi-auto-apply {
      font-size: 11px;
      color: #2E6B38;
      font-weight: 700;
      letter-spacing: 0.04em;
    }
    .pdp-upi-perk-body p {
      font-size: 12.5px;
      color: #4A4238;
      margin: 0 0 10px 0;
      line-height: 1.5;
    }
    .pdp-upi-logos {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .pdp-upi-logo-tag {
      background: #FFFFFF;
      border: 1px solid #E8E1D5;
      color: #6E6459;
      font-size: 10px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 3px;
    }

    /* Cart Drawer UPI Styles */
    .cart-upi-highlight {
      background: #F3F8F2;
      padding: 11px 24px;
      border-bottom: 1px solid #DCEADA;
      font-size: 11px;
    }
    .cart-upi-tag {
      background: #2E6B38;
      color: #FFF;
      font-size: 9px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.08em;
    }
    .cart-payment-choice {
      background: #FAF8F5;
      border: 1px solid #E8E1D5;
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 14px;
    }
    .cart-payment-choice-title {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-main);
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .cart-payment-choice-badge {
      color: #2E6B38;
      font-size: 10px;
      font-weight: 800;
      background: #E3F2E1;
      padding: 2px 6px;
      border-radius: 3px;
    }
    .cart-payment-option {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 4px;
      cursor: pointer;
      border: 1px solid transparent;
      margin-bottom: 4px;
      transition: all 0.2s ease;
    }
    .cart-payment-option.selected {
      background: #FFFFFF;
      border-color: #2E6B38;
    }
    .cart-payment-option:hover {
      background: #FFFFFF;
    }

    .announcement-bar-old {"""

if css_target in content:
    content = content.replace(css_target, css_replacement, 1)
    print("CSS updated successfully")
else:
    print("ERROR: css_target not found")

# 2. UPDATE ANNOUNCEMENT BAR HTML
html_target = """<div class="announcement-bar">
    <div>⚡ DEBUT DROP 01 LIVE &bull; 100% PURE BREATHABLE SILHOUETTES &bull; CHANDIGARH</div>
    <div>
      <span>FREE 24-HR EXPRESS TRICITY DELIVERY</span>
      <a href="javascript:void(0)" onclick="openSizeGuide()">SIZE GUIDE</a>
    </div>
  </div>"""

html_replacement = """<div class="announcement-bar">
    <div class="ann-left">
      <span>⚡ DEBUT DROP 01 LIVE &bull; CHANDIGARH ATELIER</span>
    </div>
    <div class="ann-center">
      <div class="upi-ann-badge" onclick="showToast('✨ Pay via UPI (GPay/PhonePe) at checkout to save flat ₹100 instantly!')">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px; margin-right:4px;"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
        <span>PAY VIA UPI &bull; GET INSTANT &#8377;100 OFF</span>
        <span class="upi-code-pill">CODE: UPI100</span>
      </div>
    </div>
    <div class="ann-right">
      <span>FREE PAN-INDIA EXPRESS SHIPPING</span>
      <a href="javascript:void(0)" onclick="openSizeGuide()">SIZE GUIDE</a>
    </div>
  </div>"""

if html_target in content:
    content = content.replace(html_target, html_replacement, 1)
    print("Announcement bar HTML updated successfully")
else:
    print("ERROR: html_target not found")

# 3. ADD PDP UPI PERK CARD
pdp_target = """          <!-- Scarcity Callout -->
          <div class="pdp-scarcity-banner">"""

pdp_replacement = """          <!-- Instant UPI / Prepaid Discount Offer Box -->
          <div class="pdp-upi-perk-card">
            <div class="pdp-upi-perk-header">
              <div class="pdp-upi-badge-chip">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px; margin-right:4px;"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
                <span>SPECIAL OFFER &bull; FLAT &#8377;100 OFF ON UPI</span>
              </div>
              <span class="pdp-upi-auto-apply">&#10003; Auto-Applied at Checkout</span>
            </div>
            <div class="pdp-upi-perk-body">
              <p>Pay via <strong>UPI (Google Pay, PhonePe, Paytm, QR)</strong> or Cards to save <strong>&#8377;100 instantly</strong> on your order + enjoy <strong>Priority Zero-Contact Dispatch</strong>. Zero convenience fees.</p>
            </div>
            <div class="pdp-upi-logos">
              <span class="pdp-upi-logo-tag">Google Pay</span>
              <span class="pdp-upi-logo-tag">PhonePe</span>
              <span class="pdp-upi-logo-tag">Paytm UPI</span>
              <span class="pdp-upi-logo-tag">BHIM</span>
              <span class="pdp-upi-logo-tag">Debit &amp; Credit Cards</span>
              <span class="pdp-upi-logo-tag">NetBanking</span>
            </div>
          </div>

          <!-- Scarcity Callout -->
          <div class="pdp-scarcity-banner">"""

if pdp_target in content:
    content = content.replace(pdp_target, pdp_replacement, 1)
    print("PDP UPI perk card updated successfully")
else:
    print("ERROR: pdp_target not found")

# 4. ADD CART DRAWER BANNER
cart_banner_target = """    <div style="background: #FAF8F5; padding: 10px 24px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-gold); font-weight: 700; border-bottom: 1px solid var(--border-color);">
      &#10024; Unlocked: FREE Express Shipping Across India
    </div>"""

cart_banner_replacement = """    <div style="background: #FAF8F5; padding: 10px 24px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-gold); font-weight: 700; border-bottom: 1px solid var(--border-color);">
      &#10024; Unlocked: FREE Express Shipping Across India
    </div>
    <!-- UPI Prepaid Discount Callout in Cart -->
    <div class="cart-upi-highlight">
      <div style="display:flex; align-items:center; justify-content:space-between;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="cart-upi-tag">&#8377;100 SAVED</span>
          <span style="font-weight:700; color:#1E1C19; font-size:11px; letter-spacing:0.04em;">PREPAID / UPI SPECIAL DISCOUNT</span>
        </div>
        <span style="color:#2E6B38; font-weight:800; font-size:12px;">-&#8377;100</span>
      </div>
      <div style="font-size:11px; color:#5A5145; margin-top:4px;">
        Instant <strong>&#8377;100 off</strong> auto-applied when paying via Google Pay, PhonePe, Paytm or Cards.
      </div>
    </div>"""

if cart_banner_target in content:
    content = content.replace(cart_banner_target, cart_banner_replacement, 1)
    print("Cart drawer banner updated successfully")
else:
    print("ERROR: cart_banner_target not found")

# 5. ADD PAYMENT MODE CHOICE IN CART FOOTER
cart_footer_target = """      <div style="display: flex; gap: 8px; margin-bottom: 14px;">
        <input type="text" id="couponCode" placeholder="Promo code (e.g. DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 12px; text-transform: uppercase;">
        <button onclick="applyCoupon()" style="padding: 10px 16px; background: var(--text-main); color: #FFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; text-transform: uppercase;">Apply</button>
      </div>"""

cart_footer_replacement = """      <!-- Payment Method Selector with UPI discount -->
      <div class="cart-payment-choice">
        <div class="cart-payment-choice-title">
          <span>Select Payment Mode</span>
          <span class="cart-payment-choice-badge">&#8377;100 SAVINGS</span>
        </div>
        <div class="cart-payment-option selected" id="optUpi" onclick="selectPaymentMode('upi')">
          <input type="radio" name="cartPayMode" value="upi" id="radioUpi" checked style="accent-color:#2E6B38; cursor:pointer;">
          <div style="flex:1;">
            <div style="font-weight:700; font-size:12px; color:#1E1C19;">Pay via UPI / Cards (Save &#8377;100)</div>
            <div style="font-size:10.5px; color:#6E6459;">Google Pay, PhonePe, Paytm, Cards &amp; NetBanking</div>
          </div>
          <span style="color:#2E6B38; font-weight:800; font-size:12px;">-&#8377;100</span>
        </div>
        <div class="cart-payment-option" id="optCod" onclick="selectPaymentMode('cod')">
          <input type="radio" name="cartPayMode" value="cod" id="radioCod" style="accent-color:#1E1C19; cursor:pointer;">
          <div style="flex:1;">
            <div style="font-weight:600; font-size:12px; color:#1E1C19;">Cash on Delivery (Standard Price)</div>
            <div style="font-size:10.5px; color:#8C8275;">Requires telephone OTP verification</div>
          </div>
          <span style="color:#8C8275; font-size:11px;">+&#8377;0</span>
        </div>
      </div>

      <div style="display: flex; gap: 8px; margin-bottom: 14px;">
        <input type="text" id="couponCode" placeholder="Promo code (e.g. UPI100, DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 12px; text-transform: uppercase;">
        <button onclick="applyCoupon()" style="padding: 10px 16px; background: var(--text-main); color: #FFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; text-transform: uppercase;">Apply</button>
      </div>"""

if cart_footer_target in content:
    content = content.replace(cart_footer_target, cart_footer_replacement, 1)
    print("Cart footer payment selector updated successfully")
else:
    print("ERROR: cart_footer_target not found")

# 6. ADD INSTANT UPI DISCOUNT ROW TO SUBTOTAL BREAKDOWN
subtotal_row_target = """      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: #25D366;">
        <span>Promo Discount</span>
        <span id="cartDiscount">-&#8377;0</span>
      </div>"""

subtotal_row_replacement = """      <div id="cartUpiRow" style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: #2E6B38; font-weight: 700;">
        <span>⚡ Instant UPI / Prepaid Perk</span>
        <span id="cartUpiDiscount">-&#8377;100</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: #25D366;">
        <span>Promo Discount</span>
        <span id="cartDiscount">-&#8377;0</span>
      </div>"""

if subtotal_row_target in content:
    content = content.replace(subtotal_row_target, subtotal_row_replacement, 1)
    print("Cart subtotal UPI row updated successfully")
else:
    print("ERROR: subtotal_row_target not found")

# 7. UPDATE JS CART LOGIC & COUPON LOGIC
js_vars_target = "var discountPercent = 0.0;"
js_vars_replacement = """var discountPercent = 0.0;
    var upiDiscountActive = true; // Flat ₹100 off on UPI by default"""

if js_vars_target in content:
    content = content.replace(js_vars_target, js_vars_replacement, 1)
    print("JS variables updated successfully")
else:
    print("ERROR: js_vars_target not found")

calc_target = """      var discountAmt = Math.round(subtotal * discountPercent);
      var finalTotal = subtotal - discountAmt;
      var gstAmt = Math.round(finalTotal * 0.05);

      subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
      discountEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');
      gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');
      totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');"""

calc_replacement = """      var discountAmt = Math.round(subtotal * discountPercent);
      var upiAmt = (upiDiscountActive && subtotal > 0) ? 100 : 0;
      var totalDeductions = discountAmt + upiAmt;
      var finalTotal = Math.max(0, subtotal - totalDeductions);
      var gstAmt = Math.round(finalTotal * 0.05);

      subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
      var upiRowEl = document.getElementById('cartUpiRow');
      var upiValEl = document.getElementById('cartUpiDiscount');
      if (upiRowEl && upiValEl) {
        if (upiAmt > 0) {
          upiRowEl.style.display = 'flex';
          upiValEl.textContent = '-₹' + upiAmt;
        } else {
          upiRowEl.style.display = 'none';
        }
      }
      discountEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');
      gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');
      totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');"""

if calc_target in content:
    content = content.replace(calc_target, calc_replacement, 1)
    print("Cart calculation logic updated successfully")
else:
    print("ERROR: calc_target not found")

coupon_target = """function applyCoupon() {
      var code = document.getElementById('couponCode').value.trim().toUpperCase();
      if (code === 'DEBUT10') {
        discountPercent = 0.10;
        updateCartUI();
        showToast('🎉 Promo code DEBUT10 applied! 10% discount added.');
      } else {
        showToast('❌ Invalid code. Try "DEBUT10" for 10% off.');
      }
    }"""

coupon_replacement = """function selectPaymentMode(mode) {
      var optUpi = document.getElementById('optUpi');
      var optCod = document.getElementById('optCod');
      var radioUpi = document.getElementById('radioUpi');
      var radioCod = document.getElementById('radioCod');
      if (mode === 'upi') {
        upiDiscountActive = true;
        if (optUpi) optUpi.classList.add('selected');
        if (optCod) optCod.classList.remove('selected');
        if (radioUpi) radioUpi.checked = true;
        showToast('✨ UPI Mode Active: Flat ₹100 Instant Discount applied!');
      } else {
        upiDiscountActive = false;
        if (optUpi) optUpi.classList.remove('selected');
        if (optCod) optCod.classList.add('selected');
        if (radioCod) radioCod.checked = true;
        showToast('ℹ️ Switched to Cash on Delivery (Standard Price)');
      }
      updateCartUI();
    }

    function applyCoupon() {
      var code = document.getElementById('couponCode').value.trim().toUpperCase();
      if (code === 'DEBUT10') {
        discountPercent = 0.10;
        updateCartUI();
        showToast('🎉 Promo code DEBUT10 applied! 10% discount added.');
      } else if (code === 'UPI100') {
        upiDiscountActive = true;
        selectPaymentMode('upi');
        showToast('✨ Code UPI100 verified: Flat ₹100 Instant Discount applied!');
      } else {
        showToast('❌ Invalid code. Use "UPI100" or "DEBUT10".');
      }
    }"""

if coupon_target in content:
    content = content.replace(coupon_target, coupon_replacement, 1)
    print("Coupon & selectPaymentMode functions updated successfully")
else:
    print("ERROR: coupon_target not found")

# Write updated file back
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html updated with complete UPI discounts!")

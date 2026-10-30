import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. CSS FOR DEDICATED CART PAGE AND STREAMLINED DRAWER
css_target = "/* Cart Progress Bar */"

cart_page_css = """/* ==================== DEDICATED FULL CART PAGE STYLES ==================== */
    #cartPageView {
      display: none;
      background: #FAF8F5;
      min-height: 85vh;
      padding: 36px 0 80px;
    }
    .cart-page-container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 36px;
    }
    .cart-page-breadcrumb {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    .cart-page-breadcrumb a {
      color: inherit;
      text-decoration: none;
    }
    .cart-page-breadcrumb a:hover {
      color: var(--text-main);
    }
    .cart-page-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 18px;
      margin-bottom: 32px;
    }
    .cart-continue-btn {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      padding: 10px 20px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
    }
    .cart-continue-btn:hover {
      background: #1E1C19;
      color: #FFFFFF;
      border-color: #1E1C19;
    }
    .cart-page-layout {
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 44px;
      align-items: start;
    }

    /* Left Column: Progress Card & Item Cards */
    .cart-page-progress-card {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }
    .page-progress-tag {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      background: rgba(197, 160, 89, 0.18);
      color: #8C6A28;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .page-progress-track {
      width: 100%;
      height: 8px;
      background: #EAE4DC;
      border-radius: 12px;
      overflow: hidden;
      margin: 12px 0 10px;
    }
    .page-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #C5A059 0%, #2E6B38 100%);
      border-radius: 12px;
      transition: width 0.4s ease;
    }
    .page-progress-fill.unlocked {
      background: #2E6B38;
      box-shadow: 0 0 10px rgba(46, 107, 56, 0.35);
    }
    .page-progress-milestones {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--text-muted);
    }
    .page-milestone {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .page-milestone.active {
      color: #2E6B38;
    }
    .page-ms-dot {
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background: #EAE4DC;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 9px;
      color: #5A5145;
    }
    .page-milestone.active .page-ms-dot {
      background: #2E6B38;
      color: #FFFFFF;
    }

    /* Cart Page Item Card */
    .cart-page-item {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 22px 24px;
      margin-bottom: 18px;
      display: flex;
      gap: 22px;
      align-items: flex-start;
      transition: all 0.25s ease;
    }
    .cart-page-item:hover {
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }
    .cart-page-item-img {
      width: 110px;
      height: 140px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      flex-shrink: 0;
      background: #F4EFEB;
    }
    .cart-page-item-content {
      flex: 1;
    }
    .cart-page-item-eyebrow {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }
    .cart-page-item-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 600;
      color: #1E1C19;
      margin: 0 0 6px 0;
      line-height: 1.25;
    }
    .cart-page-item-meta {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }
    .cart-page-item-meta strong {
      color: #1E1C19;
    }
    .cart-page-item-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      padding-top: 14px;
      border-top: 1px solid #F0EAE1;
    }
    .qty-stepper {
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      background: #FAF8F5;
      overflow: hidden;
    }
    .qty-step-btn {
      width: 32px;
      height: 32px;
      background: transparent;
      border: none;
      font-size: 14px;
      font-weight: 700;
      color: #1E1C19;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }
    .qty-step-btn:hover {
      background: #EAE4DC;
    }
    .qty-step-val {
      min-width: 34px;
      text-align: center;
      font-size: 13px;
      font-weight: 700;
      color: #1E1C19;
    }
    .cart-remove-link {
      background: none;
      border: none;
      color: #A0382B;
      font-size: 11.5px;
      font-weight: 600;
      letter-spacing: 0.04em;
      cursor: pointer;
      text-transform: uppercase;
      padding: 4px 8px;
    }
    .cart-remove-link:hover {
      text-decoration: underline;
    }
    .cart-page-item-prices {
      text-align: right;
    }
    .cart-page-price-main {
      font-size: 18px;
      font-weight: 700;
      color: #1E1C19;
    }
    .cart-page-price-mrp {
      font-size: 12.5px;
      color: var(--text-muted);
      text-decoration: line-through;
      margin-right: 6px;
    }

    /* Unlocked Silk Potli Page Card */
    .cart-page-gift-card {
      background: #F4F8F3;
      border: 1.5px dashed #2E6B38;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      gap: 16px;
      align-items: center;
      animation: fadeInGift 0.35s ease;
    }
    .cart-page-gift-thumb {
      width: 54px;
      height: 64px;
      background: #FFFFFF;
      border: 1px solid #D4E5D3;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      flex-shrink: 0;
    }

    /* Cross-sell row */
    .cart-page-crosssell {
      margin-top: 36px;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 24px;
    }
    .crosssell-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px solid #F0EAE1;
    }
    .crosssell-eyebrow {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-gold);
    }
    .crosssell-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 600;
      color: #1E1C19;
      margin: 2px 0 0;
    }
    .crosssell-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    .crosssell-card {
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 12px;
      background: #FAF8F5;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }
    .crosssell-card:hover {
      border-color: #1E1C19;
      background: #FFFFFF;
    }
    .crosssell-img {
      width: 100%;
      height: 140px;
      object-fit: cover;
      border-radius: 4px;
      margin-bottom: 8px;
    }
    .crosssell-card-title {
      font-size: 12px;
      font-weight: 700;
      color: #1E1C19;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .crosssell-card-price {
      font-size: 12.5px;
      font-weight: 700;
      color: #1E1C19;
      margin-bottom: 8px;
    }
    .crosssell-add-btn {
      width: 100%;
      background: #1E1C19;
      color: #FFFFFF;
      border: none;
      padding: 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      cursor: pointer;
      transition: background 0.2s;
    }
    .crosssell-add-btn:hover {
      background: #3A352F;
    }

    /* Right Column: Sticky Summary Card */
    .cart-summary-card {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 26px 26px;
      position: sticky;
      top: 90px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }
    .summary-card-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 600;
      color: #1E1C19;
      margin: 0 0 18px 0;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
    }
    .summary-payment-selector {
      background: #FAF8F5;
      border: 1px solid #EAE3D9;
      border-radius: 6px;
      padding: 12px 14px;
      margin-bottom: 18px;
    }
    .summary-payment-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-main);
      margin-bottom: 10px;
    }
    .summary-upi-save-badge {
      background: #2E6B38;
      color: #FFFFFF;
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.06em;
    }
    .summary-pay-option {
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
    .summary-pay-option.selected {
      background: #FFFFFF;
      border-color: #2E6B38;
    }
    .summary-coupon-row {
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
    }
    .summary-coupon-input {
      flex: 1;
      padding: 11px 12px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .summary-coupon-btn {
      padding: 11px 18px;
      background: #1E1C19;
      color: #FFFFFF;
      border: none;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .summary-breakdown {
      margin-bottom: 22px;
    }
    .summary-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 10px;
    }
    .summary-line.highlight-green {
      color: #2E6B38;
      font-weight: 700;
    }
    .summary-divider {
      height: 1px;
      background: var(--border-color);
      margin: 14px 0;
    }
    .summary-line.total-line {
      font-size: 17px;
      font-weight: 800;
      color: #1E1C19;
      margin-bottom: 6px;
    }
    .summary-savings-pill {
      background: #F3F8F2;
      border: 1px solid #D6E8D5;
      color: #2E6B38;
      font-size: 11px;
      font-weight: 700;
      padding: 6px 10px;
      border-radius: 4px;
      text-align: center;
      margin-top: 8px;
    }
    .summary-checkout-btn {
      width: 100%;
      background: #1E1C19;
      color: #FFFFFF;
      border: none;
      padding: 16px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      display: block;
      text-align: center;
      transition: background 0.25s ease;
      margin-bottom: 20px;
    }
    .summary-checkout-btn:hover {
      background: #3A352F;
    }
    .summary-trust-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      border-top: 1px solid #F0EAE1;
      padding-top: 16px;
    }
    .summary-trust-item {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      color: var(--text-muted);
    }
    .trust-icon {
      font-size: 13px;
      color: #1E1C19;
    }

    /* Streamlined Quick Drawer */
    .cart-drawer {
      display: flex;
      flex-direction: column;
    }
    .cart-drawer .cart-body {
      flex: 1;
      overflow-y: auto;
      padding: 16px 22px;
    }
    .cart-drawer-item {
      display: flex;
      gap: 14px;
      padding-bottom: 16px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      align-items: center;
    }
    .cart-drawer-item img {
      width: 70px;
      height: 90px;
      object-fit: cover;
      border-radius: 4px;
      border: 1px solid var(--border-color);
    }
    .drawer-view-full-btn {
      width: 100%;
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 12px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      text-align: center;
      margin-top: 8px;
      transition: all 0.2s;
    }
    .drawer-view-full-btn:hover {
      background: #FAF8F5;
      border-color: #1E1C19;
    }

    @media (max-width: 991px) {
      .cart-page-layout {
        grid-template-columns: 1fr;
        gap: 32px;
      }
      .cart-summary-card {
        position: static;
      }
      .crosssell-grid {
        grid-template-columns: 1fr;
      }
    }
    /* ==================== END DEDICATED CART PAGE STYLES ==================== */

    /* Cart Progress Bar */"""

if css_target in content:
    content = content.replace(css_target, cart_page_css, 1)
    print("CSS updated successfully")
else:
    print("ERROR: css_target not found")

# 2. INSERT DEDICATED CART PAGE HTML BEFORE FOOTER
footer_target = "  <!-- Footer -->"

cart_page_html = """  <!-- Dedicated Luxury Full Cart Page View -->
  <div id="cartPageView">
    <div class="cart-page-container">
      
      <!-- Top Breadcrumb & Header Row -->
      <div class="cart-page-breadcrumb">
        <a href="javascript:void(0)" onclick="closeCartPage()">HOME</a> &nbsp;/&nbsp;
        <span>YOUR SHOPPING BAG</span>
      </div>

      <div class="cart-page-header-row">
        <div>
          <span style="font-size: 10.5px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: #C5A059;">MEENU LABEL &bull; ATELIER SHOPPING BAG</span>
          <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 38px; font-weight: 600; color: #1E1C19; margin: 4px 0 0;">Shopping Bag (<span id="cartPageHeaderCount">0</span>)</h1>
        </div>
        <button onclick="closeCartPage()" class="cart-continue-btn">
          &larr; CONTINUE SHOPPING
        </button>
      </div>

      <!-- Empty State -->
      <div id="cartPageEmpty" style="display:none; text-align: center; padding: 80px 20px; background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px;">
        <div style="font-size: 48px; margin-bottom: 14px;">🛍️</div>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; margin: 0 0 8px; color: #1E1C19;">Your Shopping Bag is Empty</h2>
        <p style="font-size: 13px; color: var(--text-muted); max-width: 420px; margin: 0 auto 24px; line-height: 1.6;">Explore our debut 16 handcrafted silhouettes and find your perfect fit in pure breathable textiles.</p>
        <button onclick="closeCartPage()" class="btn-primary" style="padding: 14px 32px; font-size: 12px; letter-spacing: 0.1em;">EXPLORE DROP 01 COLLECTION</button>
      </div>

      <!-- Active Cart Content Grid -->
      <div id="cartPageActiveGrid" class="cart-page-layout">
        
        <!-- LEFT COLUMN: Items & Perks -->
        <div class="cart-page-left">
          
          <!-- Wide Luxury Progress Bar Card -->
          <div class="cart-page-progress-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <div style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: #1E1C19;">
                <span id="pageProgressIcon" style="font-size: 18px;">🎁</span>
                <span id="pageProgressText">Add &#8377;2,999 more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!</span>
              </div>
              <span id="pageProgressTag" class="page-progress-tag">DROP 01 PERK</span>
            </div>
            
            <div class="page-progress-track">
              <div id="pageProgressFill" class="page-progress-fill" style="width: 0%;"></div>
            </div>
            
            <div class="page-progress-milestones">
              <div class="page-milestone active">
                <span class="page-ms-dot">&#10003;</span>
                <span>Free Express Delivery (All-India)</span>
              </div>
              <div class="page-milestone" id="pageMsPotli">
                <span class="page-ms-dot" id="pageMsPotliDot">&#128274;</span>
                <span>Complimentary Jaipur Silk Potli (&#8377;2,999)</span>
              </div>
            </div>
          </div>

          <!-- Cart Items Container -->
          <div id="cartPageItemsList" class="cart-page-items">
            <!-- Dynamically populated via renderCartPage() -->
          </div>

          <!-- Cross-sell Curated Pairings -->
          <div class="cart-page-crosssell">
            <div class="crosssell-header">
              <div>
                <span class="crosssell-eyebrow">CURATED PAIRINGS</span>
                <h3 class="crosssell-title">Complete Your Drop 01 Ensemble</h3>
              </div>
              <span style="font-size: 11px; color: var(--text-muted);">Small-Batch Release</span>
            </div>
            <div class="crosssell-grid" id="cartCrosssellGrid">
              <!-- Dynamically populated -->
            </div>
          </div>

        </div>

        <!-- RIGHT COLUMN: Sticky Order Summary -->
        <div class="cart-page-right">
          <div class="cart-summary-card">
            
            <h2 class="summary-card-title">Order Summary</h2>

            <!-- Payment Selector -->
            <div class="summary-payment-selector">
              <div class="summary-payment-header">
                <span>Payment Mode</span>
                <span class="summary-upi-save-badge">SAVE &#8377;100</span>
              </div>
              
              <div class="summary-pay-option selected" id="pageOptUpi" onclick="selectPaymentMode('upi')">
                <input type="radio" name="pagePayMode" id="pageRadioUpi" value="upi" checked style="accent-color:#2E6B38; cursor:pointer;">
                <div style="flex:1;">
                  <div style="font-weight:700; font-size:12px; color:#1E1C19;">Pay via UPI / Cards (Save &#8377;100)</div>
                  <div style="font-size:10.5px; color:#6E6459;">Instant &#8377;100 auto-discount</div>
                </div>
                <span style="color:#2E6B38; font-weight:800; font-size:12px;">-&#8377;100</span>
              </div>

              <div class="summary-pay-option" id="pageOptCod" onclick="selectPaymentMode('cod')">
                <input type="radio" name="pagePayMode" id="pageRadioCod" value="cod" style="accent-color:#1E1C19; cursor:pointer;">
                <div style="flex:1;">
                  <div style="font-weight:600; font-size:12px; color:#1E1C19;">Cash on Delivery</div>
                  <div style="font-size:10.5px; color:#8C8275;">Standard price &bull; OTP verification</div>
                </div>
                <span style="color:#8C8275; font-size:11px;">+&#8377;0</span>
              </div>
            </div>

            <!-- Coupon Code Field -->
            <div class="summary-coupon-row">
              <input type="text" id="pageCouponCode" placeholder="Promo code (e.g. UPI100, DEBUT10)" class="summary-coupon-input">
              <button onclick="applyPageCoupon()" class="summary-coupon-btn">APPLY</button>
            </div>

            <!-- Breakdown Lines -->
            <div class="summary-breakdown">
              <div class="summary-line">
                <span>Bag Subtotal</span>
                <span id="pageSubtotal">&#8377;0</span>
              </div>
              
              <div class="summary-line highlight-green" id="pageUpiDiscountRow">
                <span>⚡ Instant UPI / Prepaid Perk</span>
                <span id="pageUpiDiscount">-&#8377;100</span>
              </div>

              <div class="summary-line highlight-green" id="pagePromoDiscountRow" style="display:none;">
                <span>Promo Code Discount</span>
                <span id="pagePromoDiscount">-&#8377;0</span>
              </div>

              <div class="summary-line">
                <span>Estimated GST (5% Included)</span>
                <span id="pageGst">&#8377;0</span>
              </div>

              <div class="summary-line highlight-green">
                <span>Pan-India Priority Courier</span>
                <span>FREE</span>
              </div>

              <div class="summary-divider"></div>

              <div class="summary-line total-line">
                <span>Total Payable</span>
                <span id="pageTotal">&#8377;0</span>
              </div>
              
              <div class="summary-savings-pill" id="pageSavingsNote">
                ✨ You are saving &#8377;1,500 on this order
              </div>
            </div>

            <!-- Checkout CTA Button -->
            <button onclick="proceedToCheckout()" class="summary-checkout-btn">
              PROCEED TO SECURE CHECKOUT 🔒
            </button>

            <!-- Trust Grid -->
            <div class="summary-trust-grid">
              <div class="summary-trust-item">
                <span class="trust-icon">&#128274;</span>
                <span>256-Bit SSL Encrypted Razorpay Gateway</span>
              </div>
              <div class="summary-trust-item">
                <span class="trust-icon">&#128666;</span>
                <span>Dispatched within 24 Hrs from Chandigarh</span>
              </div>
              <div class="summary-trust-item">
                <span class="trust-icon">&#128260;</span>
                <span>7-Day Hassle-Free Size Exchange</span>
              </div>
              <div class="summary-trust-item">
                <span class="trust-icon">&#128172;</span>
                <span>Stylist Support Available on WhatsApp</span>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </div>

  <!-- Footer -->"""

if footer_target in content:
    content = content.replace(footer_target, cart_page_html, 1)
    print("Inserted Cart Page HTML before footer")
else:
    print("ERROR: footer_target not found")

# 3. CLEAN UP DRAWER FOOTER: KEEP IT SLEEK WITH "VIEW FULL CART PAGE" LINK
old_drawer_footer = """    <div class="cart-footer">
      <!-- Payment Method Selector with UPI discount -->
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

new_drawer_footer = """    <div class="cart-footer" style="padding: 16px 20px; border-top: 1px solid var(--border-color); background: #FFFFFF;">
      <!-- Subtle UPI perk banner in drawer -->
      <div style="background: #F3F8F2; border: 1px solid #D6E8D5; border-radius: 4px; padding: 6px 10px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; font-size: 11px;">
        <span style="color: #2E6B38; font-weight: 700;">⚡ Instant &#8377;100 UPI discount active</span>
        <span style="color: #2E6B38; font-weight: 800;">-&#8377;100</span>
      </div>"""

if old_drawer_footer in content:
    content = content.replace(old_drawer_footer, new_drawer_footer, 1)
    print("Streamlined drawer footer")
else:
    print("ERROR: old_drawer_footer not found")

# Also add the "VIEW FULL CART PAGE" button to the bottom of the drawer footer
old_checkout_btn = """      <button class="btn-primary" style="width: 100%; padding: 16px; font-size: 12px; letter-spacing: 0.1em;" onclick="proceedToCheckout()">PROCEED TO CHECKOUT 🔒</button>
    </div>
  </div>"""

new_checkout_btn = """      <button class="btn-primary" style="width: 100%; padding: 15px; font-size: 12px; letter-spacing: 0.1em;" onclick="proceedToCheckout()">PROCEED TO CHECKOUT 🔒</button>
      <button class="drawer-view-full-btn" onclick="openCartPage()">VIEW DETAILED CART PAGE &rarr;</button>
    </div>
  </div>"""

if old_checkout_btn in content:
    content = content.replace(old_checkout_btn, new_checkout_btn, 1)
    print("Added 'VIEW DETAILED CART PAGE' button to drawer")
else:
    print("ERROR: old_checkout_btn not found")

# 4. WIRE UP HEADER SHOPPING BAG ICON TO OPEN DEDICATED CART PAGE DIRECTLY
old_header_icon = 'onclick="toggleCart()" title="Shopping Bag"'
new_header_icon = 'onclick="openCartPage()" title="Shopping Bag"'

if old_header_icon in content:
    content = content.replace(old_header_icon, new_header_icon, 1)
    print("Updated header bag icon to openCartPage()")
else:
    print("ERROR: old_header_icon not found")

# 5. ADD JS FUNCTIONS FOR CART PAGE ROUTING & RENDERING
js_target = "function proceedToCheckout() {"

cart_page_js = """function openCartPage() {
      // Close drawer if open
      var drawer = document.getElementById('cartDrawer');
      if (drawer) drawer.classList.remove('open');
      var backdrop = document.getElementById('cartBackdrop');
      if (backdrop) backdrop.classList.remove('open');

      // Hide Home and PDP, Show Cart Page
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      var cartView = document.getElementById('cartPageView');

      if (homeView) homeView.style.display = 'none';
      if (pdpView) pdpView.style.display = 'none';
      if (cartView) cartView.style.display = 'block';

      try { window.location.hash = '#cart'; } catch(e) {}
      window.scrollTo(0, 0);

      renderCartPage();
    }

    function closeCartPage() {
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      var cartView = document.getElementById('cartPageView');

      if (cartView) cartView.style.display = 'none';

      if (activePdpProductId && pdpView) {
        pdpView.style.display = 'block';
        try { window.location.hash = '#product-' + activePdpProductId; } catch(e) {}
      } else {
        if (homeView) homeView.style.display = 'block';
        try { window.location.hash = ''; } catch(e) {}
      }
      window.scrollTo(0, 0);
    }

    function changeCartItemQty(id, size, delta) {
      for (var i = 0; i < cart.length; i++) {
        if (cart[i].id === id && cart[i].size === size) {
          cart[i].qty += delta;
          if (cart[i].qty <= 0) {
            cart.splice(i, 1);
          }
          break;
        }
      }
      updateCartUI();
      renderCartPage();
    }

    function renderCartPage() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;

      var headerCountEl = document.getElementById('cartPageHeaderCount');
      if (headerCountEl) headerCountEl.textContent = totalItems;

      var emptyEl = document.getElementById('cartPageEmpty');
      var activeGridEl = document.getElementById('cartPageActiveGrid');

      if (cart.length === 0) {
        if (emptyEl) emptyEl.style.display = 'block';
        if (activeGridEl) activeGridEl.style.display = 'none';
        return;
      }

      if (emptyEl) emptyEl.style.display = 'none';
      if (activeGridEl) activeGridEl.style.display = 'grid';

      var POTLI_THRESHOLD = 2999;
      var subtotal = 0;
      var itemsHtml = '';

      for (var j = 0; j < cart.length; j++) {
        var it = cart[j];
        var itemSubtotal = it.price * it.qty;
        subtotal += itemSubtotal;

        itemsHtml += '<div class="cart-page-item">' +
          '<img src="' + it.img + '" alt="' + it.name + '" class="cart-page-item-img">' +
          '<div class="cart-page-item-content">' +
            '<div class="cart-page-item-eyebrow">DROP 01 &bull; 100% PURE BREATHABLE FABRIC</div>' +
            '<h3 class="cart-page-item-title">' + it.name + '</h3>' +
            '<div class="cart-page-item-meta">Size: <strong>' + it.size + '</strong> &bull; Free Pan-India Express Delivery</div>' +
            '<div class="cart-page-item-actions">' +
              '<div class="qty-stepper">' +
                '<button type="button" class="qty-step-btn" onclick="changeCartItemQty(\'' + it.id + '\', \'' + it.size + '\', -1)">&minus;</button>' +
                '<span class="qty-step-val">' + it.qty + '</span>' +
                '<button type="button" class="qty-step-btn" onclick="changeCartItemQty(\'' + it.id + '\', \'' + it.size + '\', 1)">&plus;</button>' +
              '</div>' +
              '<button type="button" class="cart-remove-link" onclick="removeFromCart(\'' + it.id + '\', \'' + it.size + '\'); renderCartPage();">Remove</button>' +
              '<div class="cart-page-item-prices">' +
                '<span class="cart-page-price-main">&#8377;' + itemSubtotal.toLocaleString('en-IN') + '</span>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>';
      }

      // Check if Potli is unlocked
      if (subtotal >= POTLI_THRESHOLD) {
        itemsHtml += '<div class="cart-page-gift-card">' +
          '<div class="cart-page-gift-thumb">&#129697;</div>' +
          '<div style="flex:1;">' +
            '<div style="display:flex; align-items:center; gap:8px;">' +
              '<span style="font-size:10px; font-weight:800; background:#2E6B38; color:#FFF; padding:2px 6px; border-radius:3px;">COMPLIMENTARY GIFT</span>' +
              '<strong style="font-size:13px; color:#1E1C19;">Handcrafted Jaipur Silk Potli Bag</strong>' +
            '</div>' +
            '<div style="font-size:11.5px; color:#2E6B38; margin-top:3px; font-weight:600;">Drop 01 Atelier Exclusive &bull; Automatically added to your luxury packaging</div>' +
          '</div>' +
          '<div style="text-align:right;">' +
            '<div style="font-size:11px; text-decoration:line-through; color:var(--text-muted);">&#8377;499</div>' +
            '<div style="font-size:13px; font-weight:800; color:#2E6B38;">FREE</div>' +
          '</div>' +
        '</div>';
      }

      var itemsContainer = document.getElementById('cartPageItemsList');
      if (itemsContainer) itemsContainer.innerHTML = itemsHtml;

      // Update Page Progress Bar
      var pageFill = document.getElementById('pageProgressFill');
      var pageText = document.getElementById('pageProgressText');
      var pageIcon = document.getElementById('pageProgressIcon');
      var pageMsPotli = document.getElementById('pageMsPotli');
      var pageMsPotliDot = document.getElementById('pageMsPotliDot');

      var pct = Math.min(100, Math.round((subtotal / POTLI_THRESHOLD) * 100));
      if (pageFill) pageFill.style.width = pct + '%';

      if (subtotal >= POTLI_THRESHOLD) {
        if (pageFill) pageFill.classList.add('unlocked');
        if (pageIcon) pageIcon.textContent = '🎉';
        if (pageText) pageText.innerHTML = '<strong style="color:#2E6B38;">Congratulations! You unlocked your FREE Handcrafted Silk Potli Bag!</strong>';
        if (pageMsPotli) pageMsPotli.classList.add('active');
        if (pageMsPotliDot) pageMsPotliDot.innerHTML = '&#10003;';
      } else {
        if (pageFill) pageFill.classList.remove('unlocked');
        var rem = POTLI_THRESHOLD - subtotal;
        if (pageIcon) pageIcon.textContent = '🎁';
        if (pageText) pageText.innerHTML = 'Add <strong>&#8377;' + rem.toLocaleString('en-IN') + '</strong> more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!';
        if (pageMsPotli) pageMsPotli.classList.remove('active');
        if (pageMsPotliDot) pageMsPotliDot.innerHTML = '&#128274;';
      }

      // Calculations for Right Column
      var discountAmt = Math.round(subtotal * discountPercent);
      var upiAmt = (upiDiscountActive && subtotal > 0) ? 100 : 0;
      var totalDeductions = discountAmt + upiAmt;
      var finalTotal = Math.max(0, subtotal - totalDeductions);
      var gstAmt = Math.round(finalTotal * 0.05);

      var subtotalEl = document.getElementById('pageSubtotal');
      if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');

      var upiRowEl = document.getElementById('pageUpiDiscountRow');
      var upiValEl = document.getElementById('pageUpiDiscount');
      if (upiRowEl && upiValEl) {
        if (upiAmt > 0) {
          upiRowEl.style.display = 'flex';
          upiValEl.textContent = '-₹' + upiAmt;
        } else {
          upiRowEl.style.display = 'none';
        }
      }

      var promoRowEl = document.getElementById('pagePromoDiscountRow');
      var promoValEl = document.getElementById('pagePromoDiscount');
      if (promoRowEl && promoValEl) {
        if (discountAmt > 0) {
          promoRowEl.style.display = 'flex';
          promoValEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');
        } else {
          promoRowEl.style.display = 'none';
        }
      }

      var gstEl = document.getElementById('pageGst');
      if (gstEl) gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');

      var totalEl = document.getElementById('pageTotal');
      if (totalEl) totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');

      // Populate cross-sell
      var crossGrid = document.getElementById('cartCrosssellGrid');
      if (crossGrid && productsData && productsData.length > 0) {
        var unadded = productsData.filter(function(p) {
          return !cart.some(function(c) { return c.id === p.id; });
        }).slice(0, 3);

        var crossHtml = '';
        for (var k = 0; k < unadded.length; k++) {
          var cp = unadded[k];
          crossHtml += '<div class="crosssell-card">' +
            '<img src="' + cp.b64 + '" alt="' + cp.name + '" class="crosssell-img">' +
            '<div>' +
              '<div class="crosssell-card-title">' + cp.name + '</div>' +
              '<div class="crosssell-card-price">&#8377;' + cp.price.toLocaleString('en-IN') + '</div>' +
            '</div>' +
            '<button type="button" class="crosssell-add-btn" onclick="addToCart(productsData.find(function(x){return x.id===\'' + cp.id + '\'}), \'M\'); renderCartPage();">+ ADD TO BAG</button>' +
          '</div>';
        }
        crossGrid.innerHTML = crossHtml;
      }
    }

    function applyPageCoupon() {
      var code = document.getElementById('pageCouponCode').value.trim().toUpperCase();
      if (code === 'DEBUT10') {
        discountPercent = 0.10;
        updateCartUI();
        renderCartPage();
        showToast('🎉 Promo code DEBUT10 applied! 10% discount added.');
      } else if (code === 'UPI100') {
        upiDiscountActive = true;
        selectPaymentMode('upi');
        renderCartPage();
        showToast('✨ Code UPI100 verified: Flat ₹100 Instant Discount applied!');
      } else {
        showToast('❌ Invalid code. Use "UPI100" or "DEBUT10".');
      }
    }

    """ + js_target

if js_target in content:
    content = content.replace(js_target, cart_page_js, 1)
    print("Added Cart Page JavaScript functions successfully")
else:
    print("ERROR: js_target not found")

# Also update updateCartUI() to call renderCartPage() if cartPageView is currently visible
update_cart_end_target = "totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');"
update_cart_end_replacement = """totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');
      var cartPageViewEl = document.getElementById('cartPageView');
      if (cartPageViewEl && cartPageViewEl.style.display !== 'none') {
        renderCartPage();
      }"""

if update_cart_end_target in content:
    content = content.replace(update_cart_end_target, update_cart_end_replacement, 1)
    print("Hooked updateCartUI to renderCartPage")
else:
    print("ERROR: update_cart_end_target not found")

# Write updated file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html completely updated with Dedicated Luxury Cart Page!")

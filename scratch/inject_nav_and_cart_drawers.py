import os

with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Verify if navDrawer or cartDrawer already exists in markup
has_nav = 'id="navDrawer"' in code or "id='navDrawer'" in code
has_cart = 'id="cartDrawer"' in code or "id='cartDrawer'" in code

print(f"Before injection: has_nav={has_nav}, has_cart={has_cart}")

drawers_markup = """  <!-- Navigation Drawer (Global at Root Level) -->
  <div class="nav-drawer-backdrop" id="navDrawerBackdrop" onclick="closeNavDrawer()">
    <div class="nav-drawer" id="navDrawer" onclick="event.stopPropagation()">
      <div class="nav-drawer-header">
        <img src="{logo_b64}" alt="Meenu Label" style="height: 38px; width: auto;">
        <button style="background:none; border:none; font-size:24px; cursor:pointer; color:var(--text-main); padding:4px 8px; line-height:1;" onclick="closeNavDrawer()">&times;</button>
      </div>
      <div class="nav-drawer-body">
        <ul class="nav-drawer-links">
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('all')">All Silhouettes (16)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('coord')">Co-ord Sets (4)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('festive')">Festive Suits (6)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('dress')">Midi Dresses (3)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('top')">Tops &amp; Blouses (3)</a></li>
          <li style="border-top:1px solid var(--border-color); margin-top:18px; padding-top:18px;">
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal();" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openSizeGuide();">&#128207; Size &amp; Fit Guide (M-XL)</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); closeProductPage(); var f = document.getElementById('founder'); if (f) f.scrollIntoView();">&#128081; Behind The Label (Transparency)</a>
          </li>
          <li>
            <a href="https://wa.me/919988898845" target="_blank" style="color:#25D366;">&#128172; WhatsApp Concierge (+91 99888 98845)</a>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Shopping Cart Drawer (Global at Root Level) -->
  <div class="cart-backdrop" id="cartBackdrop" onclick="toggleCart()"></div>
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-header">
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">Shopping Bag (<span id="cartCount">0</span>)</h3>
      <button style="background:none; border:none; font-size:22px; cursor:pointer; color:var(--text-main);" onclick="toggleCart()">&times;</button>
    </div>
    <div style="background: #FAF8F5; padding: 10px 24px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-gold); font-weight: 700; border-bottom: 1px solid var(--border-color);">
      &#10024; Unlocked: FREE Express Shipping Across India
    </div>
    <div class="cart-body" id="cartItemsList">
      <!-- Items dynamically populated -->
    </div>
    <div class="cart-footer">
      <div style="display: flex; gap: 8px; margin-bottom: 14px;">
        <input type="text" id="couponCode" placeholder="Promo code (e.g. DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 12px; text-transform: uppercase;">
        <button onclick="applyCoupon()" style="padding: 10px 16px; background: var(--text-main); color: #FFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; text-transform: uppercase;">Apply</button>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: var(--text-muted);">
        <span>Subtotal</span>
        <span id="cartSubtotal">&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: #25D366;">
        <span>Promo Discount</span>
        <span id="cartDiscount">-&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: var(--text-muted);">
        <span>Estimated GST (5% included)</span>
        <span id="cartGst">&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 14px; color: #25D366; font-weight: 700;">
        <span>Express Courier Dispatch</span>
        <span>FREE</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 17px; font-weight: 800; border-top: 1px solid var(--border-color); padding-top: 12px; margin-bottom: 16px;">
        <span>Total Payable</span>
        <span id="cartTotal">&#8377;0</span>
      </div>
      <button class="modal-btn-primary" onclick="proceedToCheckout()" style="width: 100%; padding: 14px; font-size: 12px; letter-spacing: 0.1em; font-weight: 700;">PROCEED TO CHECKOUT &#8250;</button>
    </div>
  </div>

  """

target = '<!-- Wishlist Drawer -->'
if target in code and not has_nav:
    code = code.replace(target, drawers_markup + target)
    print("Successfully injected navDrawer and cartDrawer before Wishlist Drawer!")
else:
    print(f"Target '{target}' not found or drawers already present!")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py!")

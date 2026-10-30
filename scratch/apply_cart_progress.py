import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. Add CSS for Cart Progress Bar
css_marker = "/* Cart Drawer UPI Styles */"
progress_css = """/* Cart Progress Bar */
    .cart-progress-container {
      background: #FAF8F5;
      padding: 14px 22px 12px 22px;
      border-bottom: 1px solid var(--border-color);
      box-sizing: border-box;
    }
    .cart-progress-msg {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--text-main);
      margin-bottom: 10px;
      line-height: 1.4;
    }
    .cart-progress-icon {
      font-size: 15px;
      flex-shrink: 0;
    }
    .cart-progress-track {
      width: 100%;
      height: 7px;
      background: #EAE3D9;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 8px;
      position: relative;
    }
    .cart-progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #C5A059 0%, #2E6B38 100%);
      border-radius: 10px;
      transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .cart-progress-fill.unlocked {
      background: #2E6B38;
      box-shadow: 0 0 10px rgba(46, 107, 56, 0.4);
    }
    .cart-progress-tiers {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--text-muted);
    }
    .cart-tier-item {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .cart-tier-item.tier-unlocked {
      color: #2E6B38;
    }
    .tier-dot {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #EAE3D9;
      font-size: 8px;
      color: #5A5145;
    }
    .cart-tier-item.tier-unlocked .tier-dot {
      background: #2E6B38;
      color: #FFFFFF;
    }

    /* Free Potli Gift Card inside Cart List when Unlocked */
    .cart-gift-card {
      display: flex;
      gap: 12px;
      align-items: center;
      background: #F3F8F2;
      border: 1px dashed #2E6B38;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 14px;
      animation: fadeInGift 0.3s ease;
    }
    @keyframes fadeInGift {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .cart-gift-icon {
      font-size: 26px;
      background: #FFFFFF;
      width: 44px;
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 4px;
      border: 1px solid #D6E8D5;
      flex-shrink: 0;
    }
    .cart-gift-info {
      flex: 1;
    }
    .cart-gift-title {
      font-size: 12px;
      font-weight: 700;
      color: #1E1C19;
      margin-bottom: 2px;
    }
    .cart-gift-sub {
      font-size: 10.5px;
      color: #2E6B38;
      font-weight: 600;
    }
    .cart-gift-badge {
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 0.08em;
      background: #2E6B38;
      color: #FFFFFF;
      padding: 3px 8px;
      border-radius: 3px;
    }

    /* Cart Drawer UPI Styles */"""

if css_marker in content:
    content = content.replace(css_marker, progress_css, 1)
    print("Added Progress Bar CSS")
else:
    print("ERROR: css_marker not found")

# 2. Update Cart Drawer HTML to replace static unlocked banner with dynamic Progress Bar
old_banner = """    <div style="background: #FAF8F5; padding: 10px 24px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-gold); font-weight: 700; border-bottom: 1px solid var(--border-color);">
      &#10024; Unlocked: FREE Express Shipping Across India
    </div>"""

progress_html = """    <!-- Dynamic 2-Tier Cart Progress Bar (Shipping + Free Silk Potli) -->
    <div class="cart-progress-container" id="cartProgressContainer">
      <div class="cart-progress-msg" id="cartProgressMsg">
        <span class="cart-progress-icon" id="cartProgressIcon">🎁</span>
        <span id="cartProgressText">Add &#8377;2,999 more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!</span>
      </div>
      <div class="cart-progress-track">
        <div class="cart-progress-fill" id="cartProgressFill" style="width: 0%;"></div>
      </div>
      <div class="cart-progress-tiers">
        <span class="cart-tier-item tier-unlocked">
          <span class="tier-dot">&#10003;</span> Free Express Shipping
        </span>
        <span class="cart-tier-item" id="tierPotli">
          <span class="tier-dot" id="potliDot">&#128274;</span> Free Silk Potli (&#8377;2,999)
        </span>
      </div>
    </div>"""

if old_banner in content:
    content = content.replace(old_banner, progress_html, 1)
    print("Added Progress Bar HTML to Cart Drawer")
else:
    print("ERROR: old_banner not found")

# 3. Update updateCartUI() to animate the progress bar and inject the gift card
target_js_block = """      if (cart.length === 0) {
        listEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 40px; margin-bottom: 12px;">🛍️</div><div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Your bag is empty</div><div style="font-size: 13px;">Explore our debut 13 silhouettes and find your fit.</div></div>';
        subtotalEl.textContent = '₹0';
        discountEl.textContent = '-₹0';
        gstEl.textContent = '₹0';
        totalEl.textContent = '₹0';
        return;
      }"""

replacement_js_block = """      // Update Cart Progress Bar
      var POTLI_THRESHOLD = 2999;
      var progressFillEl = document.getElementById('cartProgressFill');
      var progressTextEl = document.getElementById('cartProgressText');
      var progressIconEl = document.getElementById('cartProgressIcon');
      var tierPotliEl = document.getElementById('tierPotli');
      var potliDotEl = document.getElementById('potliDot');

      if (cart.length === 0) {
        listEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 40px; margin-bottom: 12px;">🛍️</div><div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Your bag is empty</div><div style="font-size: 13px;">Explore our debut 16 silhouettes and find your fit.</div></div>';
        subtotalEl.textContent = '₹0';
        discountEl.textContent = '-₹0';
        gstEl.textContent = '₹0';
        totalEl.textContent = '₹0';
        if (progressFillEl) progressFillEl.style.width = '0%';
        if (progressTextEl) progressTextEl.innerHTML = 'Add &#8377;2,999 more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!';
        if (progressIconEl) progressIconEl.textContent = '🎁';
        if (tierPotliEl) tierPotliEl.classList.remove('tier-unlocked');
        if (potliDotEl) potliDotEl.innerHTML = '&#128274;';
        return;
      }"""

if target_js_block in content:
    content = content.replace(target_js_block, replacement_js_block, 1)
    print("Updated empty cart block with progress bar reset")
else:
    print("ERROR: target_js_block not found")

# 4. Update the cart subtotal loop and add the gift card
target_loop_end = """      }
      listEl.innerHTML = html;"""

replacement_loop_end = """      }

      // Calculate Progress & Inject Free Gift if subtotal >= 2999
      var fillPercent = Math.min(100, Math.round((subtotal / POTLI_THRESHOLD) * 100));
      if (progressFillEl) {
        progressFillEl.style.width = fillPercent + '%';
        if (subtotal >= POTLI_THRESHOLD) {
          progressFillEl.classList.add('unlocked');
          if (progressIconEl) progressIconEl.textContent = '🎉';
          if (progressTextEl) {
            progressTextEl.innerHTML = '<span style="color:#2E6B38; font-weight:700;">Congratulations! You unlocked a FREE Handcrafted Silk Potli Bag!</span>';
          }
          if (tierPotliEl) tierPotliEl.classList.add('tier-unlocked');
          if (potliDotEl) potliDotEl.innerHTML = '&#10003;';

          // Append Gift Card to Cart Items
          html += '<div class="cart-gift-card">' +
            '<div class="cart-gift-icon">🪡</div>' +
            '<div class="cart-gift-info">' +
              '<div class="cart-gift-title">Handcrafted Jaipur Silk Potli Bag</div>' +
              '<div class="cart-gift-sub">Drop 01 Atelier Gift &bull; Pure Zari &amp; Silk Drape</div>' +
            '</div>' +
            '<div style="text-align:right;">' +
              '<div style="text-decoration:line-through; font-size:11px; color:#8C8275;">&#8377;499</div>' +
              '<span class="cart-gift-badge">FREE GIFT</span>' +
            '</div>' +
          '</div>';
        } else {
          progressFillEl.classList.remove('unlocked');
          var needed = POTLI_THRESHOLD - subtotal;
          if (progressIconEl) progressIconEl.textContent = '🎁';
          if (progressTextEl) {
            progressTextEl.innerHTML = 'Add <strong>&#8377;' + needed.toLocaleString('en-IN') + '</strong> more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!';
          }
          if (tierPotliEl) tierPotliEl.classList.remove('tier-unlocked');
          if (potliDotEl) potliDotEl.innerHTML = '&#128274;';
        }
      }

      listEl.innerHTML = html;"""

if target_loop_end in content:
    content = content.replace(target_loop_end, replacement_loop_end, 1)
    print("Updated cart items loop with progress bar calculation & free gift card")
else:
    print("ERROR: target_loop_end not found")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html updated with Cart Progress Bar!")

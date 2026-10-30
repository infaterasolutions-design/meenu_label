import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CART_OFFER_CONFIG at the top of <script>
config_block = """<script>
    /* ==========================================================================
       MEENU LABEL • CART OFFER CONFIGURATION (EDIT THIS BLOCK ANYTIME)
       ========================================================================== */
    var CART_OFFER_CONFIG = {
      targetAmount: 2999,                            // Spend target in Rupees (e.g. 2999, 3499, 1999)
      giftName: "Handcrafted Jaipur Silk Potli Bag", // Name of the Free Gift
      giftWorth: 499,                                // Original price (shown with strikethrough)
      giftSubtitle: "Drop 01 Atelier Exclusive • Automatically included in your package",
      badgeText: "DROP 01 PERK",                     // Tag badge in top right corner
      giftEmoji: "🪡"                                 // Icon for the gift
    };
"""

content = content.replace("<script>", config_block, 1)

# 2. Update renderCartPage() to use CART_OFFER_CONFIG dynamically
old_render_start = "var POTLI_THRESHOLD = 2999;"
new_render_start = """var cfg = CART_OFFER_CONFIG;
      var POTLI_THRESHOLD = cfg.targetAmount;
      var tagEl = document.getElementById('pageProgressTag');
      if (tagEl) tagEl.textContent = cfg.badgeText;"""

content = content.replace(old_render_start, new_render_start, 1)

# Update gift card in renderCartPage()
old_gift_card = """          itemsHtml += '<div class="cart-page-gift-card">' +
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
        '</div>';"""

new_gift_card = """          itemsHtml += '<div class="cart-page-gift-card">' +
          '<div class="cart-page-gift-thumb">' + cfg.giftEmoji + '</div>' +
          '<div style="flex:1;">' +
            '<div style="display:flex; align-items:center; gap:8px;">' +
              '<span style="font-size:10px; font-weight:800; background:#2E6B38; color:#FFF; padding:2px 6px; border-radius:3px;">COMPLIMENTARY GIFT</span>' +
              '<strong style="font-size:13px; color:#1E1C19;">' + cfg.giftName + '</strong>' +
            '</div>' +
            '<div style="font-size:11.5px; color:#2E6B38; margin-top:3px; font-weight:600;">' + cfg.giftSubtitle + '</div>' +
          '</div>' +
          '<div style="text-align:right;">' +
            '<div style="font-size:11px; text-decoration:line-through; color:var(--text-muted);">&#8377;' + cfg.giftWorth + '</div>' +
            '<div style="font-size:13px; font-weight:800; color:#2E6B38;">FREE</div>' +
          '</div>' +
        '</div>';"""

content = content.replace(old_gift_card, new_gift_card, 1)

# Update milestone labels in renderCartPage()
old_progress_msgs = """if (subtotal >= POTLI_THRESHOLD) {
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
      }"""

new_progress_msgs = """if (subtotal >= POTLI_THRESHOLD) {
        if (pageFill) pageFill.classList.add('unlocked');
        if (pageIcon) pageIcon.textContent = '🎉';
        if (pageText) pageText.innerHTML = '<strong style="color:#2E6B38;">Congratulations! You unlocked your FREE ' + cfg.giftName + '!</strong>';
        if (pageMsPotli) {
          pageMsPotli.classList.add('active');
          pageMsPotli.innerHTML = '<span class="page-ms-dot">&#10003;</span><span>Complimentary ' + cfg.giftName + ' (&#8377;' + POTLI_THRESHOLD.toLocaleString('en-IN') + ')</span>';
        }
      } else {
        if (pageFill) pageFill.classList.remove('unlocked');
        var rem = POTLI_THRESHOLD - subtotal;
        if (pageIcon) pageIcon.textContent = '🎁';
        if (pageText) pageText.innerHTML = 'Add <strong>&#8377;' + rem.toLocaleString('en-IN') + '</strong> more to unlock a <strong>FREE ' + cfg.giftName + '</strong>!';
        if (pageMsPotli) {
          pageMsPotli.classList.remove('active');
          pageMsPotli.innerHTML = '<span class="page-ms-dot">&#128274;</span><span>Complimentary ' + cfg.giftName + ' (&#8377;' + POTLI_THRESHOLD.toLocaleString('en-IN') + ')</span>';
        }
      }"""

content = content.replace(old_progress_msgs, new_progress_msgs, 1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Configurable CART_OFFER_CONFIG applied to Meenu_Label_Desktop_Storefront.html")

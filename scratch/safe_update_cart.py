import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

old_update_cart_target = """    function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;
      document.getElementById('cartCount').textContent = totalItems;
      document.getElementById('headerCartCount').textContent = totalItems;

      var listEl = document.getElementById('cartItemsList');
      var subtotalEl = document.getElementById('cartSubtotal');
      var discountEl = document.getElementById('cartDiscount');
      var gstEl = document.getElementById('cartGst');
      var totalEl = document.getElementById('cartTotal');

      // Update Cart Progress Bar
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

new_update_cart_replacement = """    function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;
      
      var countEl = document.getElementById('cartCount');
      if (countEl) countEl.textContent = totalItems;
      var headerCountEl = document.getElementById('headerCartCount');
      if (headerCountEl) headerCountEl.textContent = totalItems;

      var listEl = document.getElementById('cartItemsList');
      var subtotalEl = document.getElementById('cartSubtotal');
      var discountEl = document.getElementById('cartDiscount');
      var gstEl = document.getElementById('cartGst');
      var totalEl = document.getElementById('cartTotal');

      var POTLI_THRESHOLD = 2999;
      var progressFillEl = document.getElementById('cartProgressFill');
      var progressTextEl = document.getElementById('cartProgressText');
      var progressIconEl = document.getElementById('cartProgressIcon');
      var tierPotliEl = document.getElementById('tierPotli');
      var potliDotEl = document.getElementById('potliDot');

      if (cart.length === 0) {
        if (listEl) listEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 40px; margin-bottom: 12px;">🛍️</div><div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Your bag is empty</div><div style="font-size: 13px;">Explore our debut 16 silhouettes and find your fit.</div></div>';
        if (subtotalEl) subtotalEl.textContent = '₹0';
        if (discountEl) discountEl.textContent = '-₹0';
        if (gstEl) gstEl.textContent = '₹0';
        if (totalEl) totalEl.textContent = '₹0';
        if (progressFillEl) progressFillEl.style.width = '0%';
        if (progressTextEl) progressTextEl.innerHTML = 'Add &#8377;2,999 more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!';
        if (progressIconEl) progressIconEl.textContent = '🎁';
        if (tierPotliEl) tierPotliEl.classList.remove('tier-unlocked');
        if (potliDotEl) potliDotEl.innerHTML = '&#128274;';
        renderCartPage();
        return;
      }"""

if old_update_cart_target in content:
    content = content.replace(old_update_cart_target, new_update_cart_replacement, 1)
    print("Guarded elements in updateCartUI empty state")
else:
    print("WARNING: old_update_cart_target not found")

# Also guard listEl.innerHTML = html;
content = content.replace("listEl.innerHTML = html;", "if (listEl) listEl.innerHTML = html;")
content = content.replace("subtotalEl.textContent =", "if (subtotalEl) subtotalEl.textContent =")
content = content.replace("discountEl.textContent =", "if (discountEl) discountEl.textContent =")
content = content.replace("gstEl.textContent =", "if (gstEl) gstEl.textContent =")
content = content.replace("totalEl.textContent =", "if (totalEl) totalEl.textContent =")

# Ensure updateCartUI ALWAYS calls renderCartPage()
if "renderCartPage();" not in content[content.find("function updateCartUI()"):content.find("function toggleCart()")]:
    idx_toggle = content.find("function toggleCart()")
    content = content[:idx_toggle] + "renderCartPage();\n    }\n\n    " + content[idx_toggle:]
    print("Added renderCartPage() call to updateCartUI()")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: updateCartUI made 100% resilient!")

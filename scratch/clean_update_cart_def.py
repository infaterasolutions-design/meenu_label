import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the entire updateCartUI function with a clean, bulletproof version
start_marker = "function updateCartUI() {"
end_marker = "function toggleCart() {"

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

print("idx_start:", idx_start)
print("idx_end:", idx_end)

clean_update_cart_ui = """function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;

      var countEl = document.getElementById('cartCount');
      if (countEl) countEl.textContent = totalItems;
      var headerCountEl = document.getElementById('headerCartCount');
      if (headerCountEl) headerCountEl.textContent = totalItems;

      var subtotal = 0;
      for (var j = 0; j < cart.length; j++) {
        subtotal += cart[j].price * cart[j].qty;
      }

      var discountAmt = Math.round(subtotal * discountPercent);
      var upiAmt = (upiDiscountActive && subtotal > 0) ? 100 : 0;
      var totalDeductions = discountAmt + upiAmt;
      var finalTotal = Math.max(0, subtotal - totalDeductions);
      var gstAmt = Math.round(finalTotal * 0.05);

      var subtotalEl = document.getElementById('cartSubtotal');
      if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');

      var discountEl = document.getElementById('cartDiscount');
      if (discountEl) discountEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');

      var gstEl = document.getElementById('cartGst');
      if (gstEl) gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');

      var totalEl = document.getElementById('cartTotal');
      if (totalEl) totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');

      // Update independent Cart Page
      renderCartPage();
    }

    """

if idx_start != -1 and idx_end != -1:
    new_text = text[:idx_start] + clean_update_cart_ui + text[idx_end:]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("SUCCESS: Cleaned up updateCartUI cleanly!")
else:
    print("ERROR: could not locate markers")

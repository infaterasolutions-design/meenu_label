html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove cart-upi-highlight from drawer
upi_block_target = """    <!-- UPI Prepaid Discount Callout in Cart -->
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

if upi_block_target in content:
    content = content.replace(upi_block_target, "", 1)
    print("Removed duplicate UPI block from drawer")
else:
    print("WARNING: upi_block_target not found")

# 2. Add VIEW FULL CART PAGE button to drawer footer
checkout_btn_target = '<button class="modal-btn-primary" onclick="proceedToCheckout()" style="width: 100%; padding: 14px; font-size: 12px; letter-spacing: 0.1em; font-weight: 700;">PROCEED TO CHECKOUT &#8250;</button>'
checkout_btn_replacement = '<button class="modal-btn-primary" onclick="proceedToCheckout()" style="width: 100%; padding: 14px; font-size: 12px; letter-spacing: 0.1em; font-weight: 700; margin-bottom: 8px;">PROCEED TO CHECKOUT &#8250;</button>\n      <button type="button" class="drawer-view-full-btn" onclick="openCartPage()">VIEW DETAILED CART PAGE &rarr;</button>'

if checkout_btn_target in content:
    content = content.replace(checkout_btn_target, checkout_btn_replacement, 1)
    print("Added 'VIEW DETAILED CART PAGE' button to drawer footer")
else:
    print("WARNING: checkout_btn_target not found")

# 3. Add hash routing support for #cart
hash_target = "if (hash.indexOf('#product-') === 0) {"
hash_replacement = """if (hash === '#cart') {
        openCartPage();
      } else if (hash.indexOf('#product-') === 0) {"""

if hash_target in content:
    content = content.replace(hash_target, hash_replacement, 1)
    print("Added #cart hash routing")
else:
    print("WARNING: hash_target not found")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Drawer streamlined and full cart page connected!")

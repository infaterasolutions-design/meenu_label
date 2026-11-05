import os, re

# =========================================================================
# STEP 10: FIX MOBILE ZOOM-IN ON PINCODE SEARCH BAR
# =========================================================================

# 1. Update index.html
print("Updating index.html...")
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace PDP pincode input
old_pdp_input = '<input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" style="flex:1; padding:8px 12px; border:1px solid var(--border-color); border-radius:4px; font-size:13px; outline:none; background:#FFF;">'
new_pdp_input = '<input type="text" id="pdpPincodeInput" class="pdp-pincode-input" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" inputmode="numeric" pattern="[0-9]*" style="flex:1; padding:10px 14px; border:1px solid var(--border-color); border-radius:4px; font-size:16px; outline:none; background:#FFF; color:var(--text-main); -webkit-text-size-adjust:100%;">'

if old_pdp_input in html:
    html = html.replace(old_pdp_input, new_pdp_input, 1)
    print("Replaced pdpPincodeInput in index.html")
else:
    print("WARNING: Could not find exact old_pdp_input in index.html")

# Replace Quick View modal pincode input
old_modal_input = '<input type="text" id="pincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" style="padding: 7px 12px; border-radius: 4px; border: 1px solid var(--border-color); font-size: 12px; flex: 1;">'
new_modal_input = '<input type="text" id="pincodeInput" class="pdp-pincode-input" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" inputmode="numeric" pattern="[0-9]*" style="padding: 10px 14px; border-radius: 4px; border: 1px solid var(--border-color); font-size: 16px; flex: 1; outline:none; background:#FFF; color:var(--text-main); -webkit-text-size-adjust:100%;">'

if old_modal_input in html:
    html = html.replace(old_modal_input, new_modal_input, 1)
    print("Replaced modal pincodeInput in index.html")
else:
    print("WARNING: Could not find exact old_modal_input in index.html")

# Replace couponCode input
old_coupon = '<input type="text" id="couponCode" placeholder="Promo code (e.g. DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 12px;">'
new_coupon = '<input type="text" id="couponCode" placeholder="Promo code (e.g. DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 16px;">'
if old_coupon in html:
    html = html.replace(old_coupon, new_coupon, 1)
    print("Replaced couponCode in index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update sections/main-product.liquid & meenu-label-shopify-theme/sections/main-product.liquid
pdp_liquid_paths = [
    "sections/main-product.liquid",
    "meenu-label-shopify-theme/sections/main-product.liquid"
]

for p_path in pdp_liquid_paths:
    print(f"Updating {p_path}...")
    with open(p_path, "r", encoding="utf-8") as f:
        liq = f.read()
    
    old_liq_input = '<input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" style="flex:1; padding:8px 12px; border:1px solid var(--border-color); border-radius:4px; font-size:13px; outline:none; background:#FFF;">'
    new_liq_input = '<input type="text" id="pdpPincodeInput" class="pdp-pincode-input" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" inputmode="numeric" pattern="[0-9]*" style="flex:1; padding:10px 14px; border:1px solid var(--border-color); border-radius:4px; font-size:16px; outline:none; background:#FFF; color:var(--text-main); -webkit-text-size-adjust:100%;">'
    
    if old_liq_input in liq:
        liq = liq.replace(old_liq_input, new_liq_input, 1)
        print(f"Replaced pdpPincodeInput in {p_path}")
    else:
        print(f"WARNING: Could not find exact old_liq_input in {p_path}")
    
    # Update button padding
    old_btn = '<button type="button" onclick="checkPdpPincode()" style="padding:8px 16px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">CHECK</button>'
    new_btn = '<button type="button" onclick="checkPdpPincode()" style="padding:10px 18px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:12px; font-weight:700; cursor:pointer; letter-spacing:0.05em; touch-action:manipulation;">CHECK</button>'
    if old_btn in liq:
        liq = liq.replace(old_btn, new_btn, 1)
        print(f"Updated check button in {p_path}")
        
    with open(p_path, "w", encoding="utf-8") as f:
        f.write(liq)


# 3. Update assets/meenu-luxury.css & meenu-label-shopify-theme/assets/meenu-luxury.css
css_paths = [
    "assets/meenu-luxury.css",
    "meenu-label-shopify-theme/assets/meenu-luxury.css"
]

anti_zoom_css = """

/* =========================================================================
   MOBILE INPUT AUTO-ZOOM PREVENTION
   Prevents mobile browsers (iOS Safari, WebKit, Chrome Mobile) from zooming
   in when focusing on the pincode search bar, search fields, or form inputs.
   iOS Safari automatically zooms the page if input font-size is below 16px.
   Enforcing 16px font-size and touch-action: manipulation keeps the viewport
   stable at 1:1 scale without unwanted zoom-in.
   ========================================================================= */
html, body {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

#pdpPincodeInput,
#pincodeInput,
.pdp-pincode-input,
.pdp-pincode-input:focus {
  font-size: 16px !important;
  -webkit-text-size-adjust: 100% !important;
  touch-action: manipulation !important;
}

@media screen and (max-width: 768px) {
  input[type="text"],
  input[type="search"],
  input[type="number"],
  input[type="tel"],
  input[type="email"],
  input[type="password"],
  select,
  textarea,
  #pdpPincodeInput,
  #pincodeInput,
  .pdp-pincode-input {
    font-size: 16px !important;
    touch-action: manipulation !important;
    -webkit-text-size-adjust: 100% !important;
  }
}
"""

for c_path in css_paths:
    print(f"Updating {c_path}...")
    with open(c_path, "r", encoding="utf-8") as f:
        css = f.read()
    
    if "MOBILE INPUT AUTO-ZOOM PREVENTION" not in css:
        css += anti_zoom_css
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(css)
        print(f"Appended anti-zoom CSS to {c_path}")
    else:
        print(f"Anti-zoom CSS already present in {c_path}")

print("\nStep 10 updates successfully applied to all files!")

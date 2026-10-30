import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Target for announcement bar CSS
target_css = ".announcement-bar {"
pos_css = text.find(target_css)
print("pos_css:", pos_css)

# 2. Target for announcement bar HTML
target_html = '<div class="announcement-bar">'
pos_html = text.find(target_html)
print("pos_html:", pos_html)

# 3. Target for PDP UPI offer insertion
target_pdp = '<div class="pdp-scarcity-banner">'
pos_pdp = text.find(target_pdp)
print("pos_pdp:", pos_pdp)

# 4. Target for Cart Drawer banner insertion
target_cart_banner = '&#10024; Unlocked: FREE Express Shipping Across India'
pos_cart_banner = text.find(target_cart_banner)
print("pos_cart_banner:", pos_cart_banner)

# 5. Target for Cart footer payment choice
target_cart_footer = '<div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: var(--text-muted);">'
pos_cart_footer = text.find(target_cart_footer)
print("pos_cart_footer:", pos_cart_footer)

# 6. Target for couponCode logic
target_coupon = "if (code === 'DEBUT10') {"
pos_coupon = text.find(target_coupon)
print("pos_coupon:", pos_coupon)

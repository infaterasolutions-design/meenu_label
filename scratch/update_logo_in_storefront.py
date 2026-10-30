import os, base64, re, shutil, zipfile

downloads_dir = r"C:\Users\sande\Downloads"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
theme_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme"

# Read official logo base64
logo_png_path = os.path.join(downloads_dir, "meenu_logo_official.png")
with open(logo_png_path, "rb") as f:
    logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# 1. Update Meenu_Label_Desktop_Storefront.html
html_path = os.path.join(downloads_dir, "Meenu_Label_Desktop_Storefront.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace header logo
pattern_header = r'<div class="header-top-row">.*?</div>'
replacement_header = f'''<div class="header-top-row">
      <a href="#" style="display: inline-block;">
        <img src="{logo_b64}" alt="Meenu Label" style="height: 66px; width: auto; display: block; margin: 0 auto;">
      </a>
    </div>'''
html = re.sub(pattern_header, replacement_header, html, count=1, flags=re.DOTALL)

# Replace footer logo
old_footer = '<h4 style="font-size: 28px; letter-spacing: 0.15em;">MEENU LABEL</h4>'
new_footer = f'<img src="{logo_b64}" alt="Meenu Label" style="height: 48px; width: auto; filter: invert(1); display: block; margin-bottom: 16px;">'
html = html.replace(old_footer, new_footer)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(artifacts_dir, "Meenu_Label_Desktop_Storefront.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Updated HTML storefront with official Canva logo!")

# 2. Update Shopify Theme assets & Liquid
shutil.copy(logo_png_path, os.path.join(theme_dir, "assets", "logo.png"))

# Update header.liquid
header_liquid = """
<header>
  <div style="max-width: 1400px; margin: 0 auto; padding: 18px 40px 10px; text-align: center;">
    <a href="/" style="display: inline-block;">
      <img src="{{ 'logo.png' | asset_url }}" alt="{{ shop.name }}" style="height: 66px; width: auto; display: block; margin: 0 auto;">
    </a>
  </div>
  <div class="header-inner" style="border-top: 1px solid rgba(230, 224, 214, 0.5); padding: 10px 40px 16px;">
    <nav>
      <ul class="nav-links">
        <li><a href="/collections/all">All Silhouettes (13)</a></li>
        <li><a href="/collections/co-ord-sets">Co-ord Sets</a></li>
        <li><a href="/collections/festive-suits">Festive Suits</a></li>
        <li><a href="/collections/dresses">Dresses</a></li>
        <li><a href="/collections/tops">Tops & Blouses</a></li>
      </ul>
    </nav>
    <div></div>
    <div class="header-actions">
      <button class="header-btn" onclick="openSizeGuideModal()">📏 Guide</button>
      <button class="header-btn" onclick="toggleCartDrawer()">
        🛍️ Bag <span class="cart-badge">{{ cart.item_count }}</span>
      </button>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "header.liquid"), "w", encoding="utf-8") as f:
    f.write(header_liquid)

# Update footer.liquid
footer_liquid = """
<footer style="background: #1E1C19; color: #FAF8F5; padding: 60px 40px 24px;">
  <div style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px; padding-bottom: 40px; border-bottom: 1px solid rgba(255,255,255,0.1);">
    <div>
      <img src="{{ 'logo.png' | asset_url }}" alt="{{ shop.name }}" style="height: 48px; width: auto; filter: invert(1); display: block; margin-bottom: 16px;">
      <p style="font-size: 13px; color: #A8A095; line-height: 1.6; max-width: 400px;">
        Contemporary Indian ethnic wear & modern fusion silhouettes. Operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>, Chandigarh.
      </p>
    </div>
    <div>
      <h5 style="font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 14px;">Client Care</h5>
      <ul style="list-style: none; font-size: 13px; color: #C0B7AB; line-height: 2;">
        <li><a href="javascript:void(0)" onclick="openSizeGuideModal()" style="color: inherit; text-decoration: none;">Size Chart (M-XL)</a></li>
        <li><a href="mailto:{{ settings.contact_email }}" style="color: inherit; text-decoration: none;">{{ settings.contact_email }}</a></li>
        <li><a href="https://wa.me/{{ settings.whatsapp_number }}" style="color: inherit; text-decoration: none;">WhatsApp Concierge</a></li>
      </ul>
    </div>
    <div>
      <h5 style="font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 14px;">Tricity Guarantee</h5>
      <p style="font-size: 12px; color: #A8A095; line-height: 1.6;">
        Express 24-hr priority dispatch across Chandigarh, Mohali & Panchkula. Safe contactless delivery.
      </p>
    </div>
  </div>
  <div style="max-width: 1400px; margin: 20px auto 0; font-size: 11px; color: #7A7267; text-align: center;">
    © {{ 'now' | date: '%Y' }} Meenu Label (Infatera Software Solutions OPC Pvt. Ltd.). Official Store: meenulabel.com
  </div>
</footer>

{% schema %}
{
  "name": "Footer",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "footer.liquid"), "w", encoding="utf-8") as f:
    f.write(footer_liquid)

# Re-zip Shopify Theme
zip_path = os.path.join(downloads_dir, "Meenu_Label_Shopify_Theme.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

shutil.copy(zip_path, os.path.join(artifacts_dir, "Meenu_Label_Shopify_Theme.zip"))
print("Re-zipped Shopify theme with official logo!")

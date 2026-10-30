import zipfile
import os
import shutil

zip_path = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
extract_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch\theme_extracted"

if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

cart_snippet_path = os.path.join(extract_dir, "snippets", "cart-drawer.liquid")
with open(cart_snippet_path, "r", encoding="utf-8") as f:
    content = f.read()

target_marker = '<div class="cart-items">'

liquid_progress = """  {% assign threshold = 299900 %}
  {% assign cart_total = cart.total_price %}
  {% assign needed = threshold | minus: cart_total %}
  {% assign pct = cart_total | times: 100 | divided_by: threshold %}
  {% if pct > 100 %}{% assign pct = 100 %}{% endif %}

  <!-- Cart Progress Bar -->
  <div style="background: #FAF8F5; padding: 12px 20px 10px; border-bottom: 1px solid var(--border-color);">
    <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; margin-bottom: 8px;">
      {% if needed <= 0 %}
        <span>🎉</span>
        <strong style="color: #2E6B38;">Congratulations! You unlocked a FREE Silk Potli Gift Bag!</strong>
      {% else %}
        <span>🎁</span>
        <span>Add <strong>{{ needed | money }}</strong> more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!</span>
      {% endif %}
    </div>
    <div style="width: 100%; height: 6px; background: #EAE3D9; border-radius: 10px; overflow: hidden; margin-bottom: 6px;">
      <div style="width: {{ pct }}%; height: 100%; background: linear-gradient(90deg, #C5A059 0%, #2E6B38 100%); transition: width 0.3s ease;"></div>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 10px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">
      <span style="color: #2E6B38;">✓ Free Shipping</span>
      <span style="{% if needed <= 0 %}color: #2E6B38;{% endif %}">
        {% if needed <= 0 %}✓{% else %}🔒{% endif %} Free Silk Potli (₹2,999)
      </span>
    </div>
  </div>
"""

if target_marker in content:
    content = content.replace(target_marker, liquid_progress + "\n  " + target_marker, 1)

# Also in the items list, if unlocked, show the free potli
free_gift_liquid = """    {% if cart.item_count > 0 %}
      {% if cart.total_price >= 299900 %}
        <div style="display: flex; gap: 12px; align-items: center; background: #F3F8F2; border: 1px dashed #2E6B38; border-radius: 6px; padding: 10px 14px; margin-bottom: 14px;">
          <div style="font-size: 24px; background: #FFF; width: 44px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 4px; border: 1px solid #D6E8D5;">🪡</div>
          <div style="flex: 1;">
            <div style="font-size: 12px; font-weight: 700;">Handcrafted Jaipur Silk Potli Bag</div>
            <div style="font-size: 11px; color: #2E6B38; font-weight: 600;">Drop 01 Atelier Gift • Pure Zari &amp; Silk</div>
          </div>
          <div style="text-align: right;">
            <div style="text-decoration: line-through; font-size: 11px; color: var(--text-muted);">₹499</div>
            <span style="font-size: 9px; font-weight: 800; background: #2E6B38; color: #FFF; padding: 2px 6px; border-radius: 3px;">FREE GIFT</span>
          </div>
        </div>
      {% endif %}"""

old_items_start = "{% if cart.item_count > 0 %}"
if old_items_start in content:
    content = content.replace(old_items_start, free_gift_liquid, 1)

with open(cart_snippet_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated snippets/cart-drawer.liquid with Progress Bar & Gift Card!")

# Repack theme zip
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, extract_dir)
            z.write(full_path, rel_path)

print("SUCCESS: Meenu_Label_Shopify_Theme.zip repacked with Cart Progress Bar!")

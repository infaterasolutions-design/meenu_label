import zipfile
import os
import shutil

zip_path = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
extract_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch\theme_extracted"

if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

cart_path = os.path.join(extract_dir, "sections", "main-cart.liquid")
with open(cart_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace hardcoded threshold and strings with section.settings
old_calc = """      {% assign threshold = 299900 %}
      {% assign cart_total = cart.total_price %}
      {% assign needed = threshold | minus: cart_total %}
      {% assign pct = cart_total | times: 100 | divided_by: threshold %}
      {% if pct > 100 %}{% assign pct = 100 %}{% endif %}"""

new_calc = """      {% assign target_amt = section.settings.target_amount | default: 2999 %}
      {% assign threshold = target_amt | times: 100 %}
      {% assign cart_total = cart.total_price %}
      {% assign needed = threshold | minus: cart_total %}
      {% assign pct = cart_total | times: 100 | divided_by: threshold %}
      {% if pct > 100 %}{% assign pct = 100 %}{% endif %}
      {% assign gift_title = section.settings.gift_name | default: "Handcrafted Jaipur Silk Potli Bag" %}
      {% assign gift_val = section.settings.gift_worth | default: "499" %}
      {% assign badge_val = section.settings.badge_text | default: "DROP 01 PERK" %}"""

content = content.replace(old_calc, new_calc, 1)

# Update progress bar messages
old_pb = """            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 13px;">
              <div>
                {% if needed <= 0 %}
                  <span>🎉</span> <strong style="color: #2E6B38;">Congratulations! You unlocked your FREE Handcrafted Silk Potli Bag!</strong>
                {% else %}
                  <span>🎁</span> Add <strong>{{ needed | money }}</strong> more to unlock a <strong>FREE Handcrafted Silk Potli Bag</strong>!
                {% endif %}
              </div>
              <span style="font-size: 9.5px; font-weight: 800; background: rgba(197, 160, 89, 0.18); color: #8C6A28; padding: 3px 8px; border-radius: 4px;">DROP 01 PERK</span>
            </div>
            <div style="width: 100%; height: 8px; background: #EAE4DC; border-radius: 12px; overflow: hidden; margin-bottom: 8px;">
              <div style="width: {{ pct }}%; height: 100%; background: linear-gradient(90deg, #C5A059 0%, #2E6B38 100%);"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">
              <span style="color: #2E6B38;">✓ Free Express Delivery</span>
              <span style="{% if needed <= 0 %}color: #2E6B38;{% endif %}">
                {% if needed <= 0 %}✓{% else %}🔒{% endif %} Free Silk Potli (₹2,999)
              </span>
            </div>"""

new_pb = """            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 13px;">
              <div>
                {% if needed <= 0 %}
                  <span>🎉</span> <strong style="color: #2E6B38;">Congratulations! You unlocked your FREE {{ gift_title }}!</strong>
                {% else %}
                  <span>🎁</span> Add <strong>{{ needed | money }}</strong> more to unlock a <strong>FREE {{ gift_title }}</strong>!
                {% endif %}
              </div>
              <span style="font-size: 9.5px; font-weight: 800; background: rgba(197, 160, 89, 0.18); color: #8C6A28; padding: 3px 8px; border-radius: 4px;">{{ badge_val }}</span>
            </div>
            <div style="width: 100%; height: 8px; background: #EAE4DC; border-radius: 12px; overflow: hidden; margin-bottom: 8px;">
              <div style="width: {{ pct }}%; height: 100%; background: linear-gradient(90deg, #C5A059 0%, #2E6B38 100%);"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">
              <span style="color: #2E6B38;">✓ Free Express Delivery</span>
              <span style="{% if needed <= 0 %}color: #2E6B38;{% endif %}">
                {% if needed <= 0 %}✓{% else %}🔒{% endif %} Free {{ gift_title }} (₹{{ target_amt }})
              </span>
            </div>"""

content = content.replace(old_pb, new_pb, 1)

# Update gift card in main-cart.liquid
old_gc = """          <!-- Free Potli Gift Card if reached -->
          {% if cart.total_price >= 299900 %}
            <div style="background: #F4F8F3; border: 1.5px dashed #2E6B38; border-radius: 8px; padding: 14px 18px; margin-bottom: 20px; display: flex; gap: 14px; align-items: center;">
              <div style="width: 48px; height: 56px; background: #FFF; border: 1px solid #D4E5D3; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 24px;">🪡</div>
              <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span style="font-size: 9px; font-weight: 800; background: #2E6B38; color: #FFF; padding: 2px 6px; border-radius: 3px;">COMPLIMENTARY</span>
                  <strong style="font-size: 13px;">Handcrafted Jaipur Silk Potli Bag</strong>
                </div>
                <div style="font-size: 11px; color: #2E6B38; margin-top: 2px;">Drop 01 Atelier Exclusive • Automatically included in your package</div>
              </div>
              <div style="text-align: right;">
                <div style="font-size: 10px; text-decoration: line-through; color: var(--text-muted);">₹499</div>
                <div style="font-size: 13px; font-weight: 800; color: #2E6B38;">FREE</div>
              </div>
            </div>
          {% endif %}"""

new_gc = """          <!-- Free Gift Card if reached -->
          {% if cart.total_price >= threshold %}
            <div style="background: #F4F8F3; border: 1.5px dashed #2E6B38; border-radius: 8px; padding: 14px 18px; margin-bottom: 20px; display: flex; gap: 14px; align-items: center;">
              <div style="width: 48px; height: 56px; background: #FFF; border: 1px solid #D4E5D3; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 24px;">🪡</div>
              <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span style="font-size: 9px; font-weight: 800; background: #2E6B38; color: #FFF; padding: 2px 6px; border-radius: 3px;">COMPLIMENTARY</span>
                  <strong style="font-size: 13px;">{{ gift_title }}</strong>
                </div>
                <div style="font-size: 11px; color: #2E6B38; margin-top: 2px;">Atelier Exclusive • Automatically included in your package</div>
              </div>
              <div style="text-align: right;">
                <div style="font-size: 10px; text-decoration: line-through; color: var(--text-muted);">₹{{ gift_val }}</div>
                <div style="font-size: 13px; font-weight: 800; color: #2E6B38;">FREE</div>
              </div>
            </div>
          {% endif %}"""

content = content.replace(old_gc, new_gc, 1)

# Update schema
old_schema = """{% schema %}
{
  "name": "Main Cart",
  "settings": []
}
{% endschema %}"""

new_schema = """{% schema %}
{
  "name": "Main Cart",
  "settings": [
    {
      "type": "number",
      "id": "target_amount",
      "label": "Free Gift Target Spend (in ₹)",
      "default": 2999
    },
    {
      "type": "text",
      "id": "gift_name",
      "label": "Free Gift Name",
      "default": "Handcrafted Jaipur Silk Potli Bag"
    },
    {
      "type": "text",
      "id": "gift_worth",
      "label": "Original Gift Value (in ₹)",
      "default": "499"
    },
    {
      "type": "text",
      "id": "badge_text",
      "label": "Perk Badge Label",
      "default": "DROP 01 PERK"
    }
  ]
}
{% endschema %}"""

content = content.replace(old_schema, new_schema, 1)

with open(cart_path, "w", encoding="utf-8") as f:
    f.write(content)

# Repack zip
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, extract_dir)
            z.write(full_path, rel_path)

print("SUCCESS: Shopify Theme section settings updated for visual editing in Admin!")

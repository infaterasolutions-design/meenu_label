import zipfile
import os
import shutil

zip_path = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
extract_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch\theme_extracted"

if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

# 1. Create sections/main-cart.liquid
main_cart_liquid = """<section style="background: #FAF8F5; min-height: 80vh; padding: 40px 0 80px;">
  <div style="max-width: 1320px; margin: 0 auto; padding: 0 30px;">
    
    <!-- Breadcrumb & Header -->
    <div style="margin-bottom: 24px;">
      <div style="font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 10px;">
        <a href="/" style="color: inherit; text-decoration: none;">HOME</a> &nbsp;/&nbsp;
        <span>YOUR SHOPPING BAG</span>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;">
        <div>
          <span style="font-size: 10px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent-gold);">MEENU LABEL &bull; ATELIER SHOPPING BAG</span>
          <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 38px; font-weight: 600; color: #1E1C19; margin: 4px 0 0;">Shopping Bag ({{ cart.item_count }})</h1>
        </div>
        <a href="/collections/all" class="btn-primary" style="background: #FFFFFF; color: #1E1C19; border: 1px solid var(--border-color); padding: 10px 18px; font-size: 11px; text-decoration: none;">
          &larr; CONTINUE SHOPPING
        </a>
      </div>
    </div>

    {% if cart.item_count == 0 %}
      <div style="text-align: center; padding: 80px 20px; background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px;">
        <div style="font-size: 48px; margin-bottom: 12px;">🛍️</div>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; margin: 0 0 8px;">Your Shopping Bag is Empty</h2>
        <p style="font-size: 13px; color: var(--text-muted); max-width: 400px; margin: 0 auto 24px;">Explore our debut 16 handcrafted silhouettes and find your fit in pure breathable textiles.</p>
        <a href="/collections/all" class="btn-primary" style="padding: 14px 28px; text-decoration: none; display: inline-block;">EXPLORE COLLECTION</a>
      </div>
    {% else %}
      {% assign threshold = 299900 %}
      {% assign cart_total = cart.total_price %}
      {% assign needed = threshold | minus: cart_total %}
      {% assign pct = cart_total | times: 100 | divided_by: threshold %}
      {% if pct > 100 %}{% assign pct = 100 %}{% endif %}

      <div style="display: grid; grid-template-columns: 1fr 400px; gap: 40px; align-items: start;">
        
        <!-- Left: Items & Progress -->
        <div>
          <!-- Progress Bar Card -->
          <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px; padding: 18px 22px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 13px;">
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
            </div>
          </div>

          <!-- Items Table -->
          <form action="/cart" method="post" id="cartForm">
            {% for item in cart.items %}
              <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; display: flex; gap: 18px; align-items: flex-start;">
                <img src="{{ item.image | image_url: width: 240 }}" alt="{{ item.title }}" style="width: 90px; height: 115px; object-fit: cover; border-radius: 4px; border: 1px solid var(--border-color);">
                <div style="flex: 1;">
                  <div style="font-size: 10px; font-weight: 700; letter-spacing: 0.1em; color: var(--accent-gold); text-transform: uppercase; margin-bottom: 2px;">DROP 01 SILHOUETTE</div>
                  <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; margin: 0 0 4px;">{{ item.product.title }}</h3>
                  <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px;">Size: <strong>{{ item.variant.title }}</strong></div>
                  
                  <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #F0EAE1; padding-top: 10px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                      <label style="font-size: 11px; color: var(--text-muted);">Qty:</label>
                      <input type="number" name="updates[]" value="{{ item.quantity }}" min="1" style="width: 50px; padding: 4px 6px; border: 1px solid var(--border-color); border-radius: 4px; text-align: center;">
                      <a href="/cart/change?line={{ forloop.index }}&quantity=0" style="color: #A0382B; font-size: 11px; text-decoration: none; margin-left: 8px;">Remove</a>
                    </div>
                    <div style="font-weight: 700; font-size: 16px;">{{ item.final_line_price | money }}</div>
                  </div>
                </div>
              </div>
            {% endfor %}
            <button type="submit" name="update" class="btn-primary" style="background: #FFFFFF; color: #1E1C19; border: 1px solid var(--border-color); padding: 8px 16px; font-size: 11px; margin-bottom: 20px;">UPDATE QUANTITIES</button>
          </form>

          <!-- Free Potli Gift Card if reached -->
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
          {% endif %}
        </div>

        <!-- Right: Summary Sidebar -->
        <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: 8px; padding: 24px; position: sticky; top: 90px;">
          <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 22px; margin: 0 0 16px; padding-bottom: 10px; border-bottom: 1px solid var(--border-color);">Order Summary</h2>

          <div style="background: #F3F8F2; border: 1px solid #D6E8D5; border-radius: 6px; padding: 10px 12px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; font-size: 11px;">
            <span style="color: #2E6B38; font-weight: 700;">⚡ Instant ₹100 UPI Discount</span>
            <span style="color: #2E6B38; font-weight: 800;">AUTO-APPLIED</span>
          </div>

          <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
              <span>Subtotal</span>
              <span style="color: #1E1C19; font-weight: 700;">{{ cart.total_price | money }}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px; color: #2E6B38; font-weight: 600;">
              <span>UPI / Prepaid Perk</span>
              <span>-₹100 (At Checkout)</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
              <span>GST (5%)</span>
              <span>Included</span>
            </div>
            <div style="display: flex; justify-content: space-between; color: #2E6B38; font-weight: 700;">
              <span>Pan-India Priority Courier</span>
              <span>FREE</span>
            </div>
            <div style="height: 1px; background: var(--border-color); margin: 12px 0;"></div>
            <div style="display: flex; justify-content: space-between; font-size: 16px; font-weight: 800; color: #1E1C19;">
              <span>Estimated Total</span>
              <span>{{ cart.total_price | minus: 10000 | money }}</span>
            </div>
          </div>

          <a href="/checkout" class="btn-primary" style="width: 100%; padding: 15px; font-size: 12px; text-align: center; text-decoration: none; display: block; margin-bottom: 16px;">
            PROCEED TO CHECKOUT 🔒
          </a>

          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5;">
            <div>🔒 256-Bit SSL Encrypted Razorpay Checkout</div>
            <div>🚚 Dispatched within 24 Hours from Chandigarh</div>
            <div>🔄 7-Day Hassle-Free Size Exchange</div>
          </div>
        </div>

      </div>
    {% endif %}
  </div>
</section>

{% schema %}
{
  "name": "Main Cart",
  "settings": []
}
{% endschema %}
"""

with open(os.path.join(extract_dir, "sections", "main-cart.liquid"), "w", encoding="utf-8") as f:
    f.write(main_cart_liquid)

print("Created sections/main-cart.liquid")

# 2. Update templates/cart.json
cart_json = """{
  "sections": {
    "main": {
      "type": "main-cart",
      "settings": {}
    }
  },
  "order": [
    "main"
  ]
}"""

with open(os.path.join(extract_dir, "templates", "cart.json"), "w", encoding="utf-8") as f:
    f.write(cart_json)

print("Updated templates/cart.json")

# 3. Repack theme zip
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, extract_dir)
            z.write(full_path, rel_path)

print("SUCCESS: Meenu_Label_Shopify_Theme.zip repacked with full Cart Page template!")

import os, re

# =========================================================================
# STEP 11: FIX MOBILE COMPARE PRICE WRAP & ADD PERCENT OFF DISCOUNT
# =========================================================================

# 1. Update snippets/product-card.liquid & meenu-label-shopify-theme/snippets/product-card.liquid
product_card_files = [
    "snippets/product-card.liquid",
    "meenu-label-shopify-theme/snippets/product-card.liquid"
]

card_old_pattern = re.compile(
    r'<div class="card-price-row">\s*<div class="card-price-left">\s*<span class="price-main">\{\{\s*product\.price \| money\s*\}\}</span>\s*\{%\s*if product\.compare_at_price > product\.price\s*%\}\s*<span class="price-mrp"[^>]*>\{\{\s*product\.compare_at_price \| money\s*\}\}</span>\s*\{%\s*endif\s*%\}\s*</div>',
    re.DOTALL
)

card_new_replacement = """<div class="card-price-row">
      <div class="card-price-left">
        <span class="price-main">{{ product.price | money }}</span>
        {% if product.compare_at_price > product.price %}
          <div class="card-price-compare-wrap">
            <span class="price-mrp">{{ product.compare_at_price | money }}</span>
            {% assign savings = product.compare_at_price | minus: product.price | times: 100.0 | divided_by: product.compare_at_price | round %}
            <span class="price-discount">{{ savings }}% OFF</span>
          </div>
        {% endif %}
      </div>"""

for p_card in product_card_files:
    if os.path.exists(p_card):
        with open(p_card, "r", encoding="utf-8") as f:
            content = f.read()
        
        if card_old_pattern.search(content):
            content = card_old_pattern.sub(card_new_replacement, content, count=1)
            with open(p_card, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {p_card} with compare-wrap and % OFF discount")
        else:
            print(f"WARNING: Regex did not match in {p_card}, attempting string replace")
            # Fallback manual string replacement
            target_str = """      <div class="card-price-left">
        <span class="price-main">{{ product.price | money }}</span>
        {% if product.compare_at_price > product.price %}
          <span class="price-mrp" style="text-decoration: line-through; color: var(--text-muted); font-size: 13px; margin-left: 6px;">{{ product.compare_at_price | money }}</span>
        {% endif %}
      </div>"""
            replacement_str = """      <div class="card-price-left">
        <span class="price-main">{{ product.price | money }}</span>
        {% if product.compare_at_price > product.price %}
          <div class="card-price-compare-wrap">
            <span class="price-mrp">{{ product.compare_at_price | money }}</span>
            {% assign savings = product.compare_at_price | minus: product.price | times: 100.0 | divided_by: product.compare_at_price | round %}
            <span class="price-discount">{{ savings }}% OFF</span>
          </div>
        {% endif %}
      </div>"""
            if target_str in content:
                content = content.replace(target_str, replacement_str, 1)
                with open(p_card, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {p_card} via fallback string replace")
            else:
                print(f"ERROR: Could not find target price block in {p_card}")


# 2. Update sections/featured-collection.liquid & mirror
featured_files = [
    "sections/featured-collection.liquid",
    "meenu-label-shopify-theme/sections/featured-collection.liquid"
]

for f_file in featured_files:
    if os.path.exists(f_file):
        with open(f_file, "r", encoding="utf-8") as f:
            f_content = f.read()
            
        # Update fallback cards in featured-collection
        old_fb_pattern = re.compile(
            r'<div class="card-price-row">\s*<span class="price-main">(&#8377;\d+[\d,]*)</span>\s*<span class="price-mrp"[^>]*>(&#8377;\d+[\d,]*)</span>\s*<span class="snitch-plus-trigger">\+</span>\s*</div>',
            re.DOTALL
        )
        
        def replace_fb(m):
            p_main = m.group(1)
            p_mrp = m.group(2)
            # Estimate discount
            m_val = int(p_main.replace('&#8377;', '').replace(',', ''))
            r_val = int(p_mrp.replace('&#8377;', '').replace(',', ''))
            off = round(((r_val - m_val) / r_val) * 100)
            return f"""<div class="card-price-row">
            <div class="card-price-left">
              <span class="price-main">{p_main}</span>
              <div class="card-price-compare-wrap">
                <span class="price-mrp">{p_mrp}</span>
                <span class="price-discount">{off}% OFF</span>
              </div>
            </div>
            <span class="snitch-plus-trigger">+</span>
          </div>"""

        new_f_content = old_fb_pattern.sub(replace_fb, f_content)
        with open(f_file, "w", encoding="utf-8") as f:
            f.write(new_f_content)
        print(f"Updated fallback cards in {f_file}")


# 3. Update assets/meenu-luxury.css & mirror
css_files = [
    "assets/meenu-luxury.css",
    "meenu-label-shopify-theme/assets/meenu-luxury.css"
]

price_fix_css = """

/* ========================================================
   HYPER-CLEAN CARD PRICE & DISCOUNT PERCENTAGE
   Ensures compare price ('Rs.' and digits) NEVER break across lines.
   Displays clear discount percentage badge (e.g. 37% OFF).
   ======================================================== */
.card-price-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 6px !important;
  margin-top: 4px !important;
  padding-top: 0 !important;
}

.card-price-left {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  align-items: baseline !important;
  gap: 3px 6px !important;
  min-width: 0 !important;
  flex: 1 !important;
}

.price-main {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  color: #111111 !important;
  font-variant-numeric: lining-nums !important;
  letter-spacing: -0.02em !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
}

.card-price-compare-wrap {
  display: inline-flex !important;
  align-items: baseline !important;
  gap: 5px !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
}

.price-mrp,
.pdp-price-mrp,
.modal-price-mrp {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 12.5px !important;
  color: #8C827A !important;
  text-decoration: line-through !important;
  white-space: nowrap !important; /* CRITICAL: Never split currency and digits */
  font-variant-numeric: lining-nums !important;
  letter-spacing: -0.01em !important;
  line-height: 1.2 !important;
}

.price-discount,
.pdp-price-discount {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #B83A3A !important; /* Luxury crimson rose discount highlight */
  white-space: nowrap !important;
  letter-spacing: 0.02em !important;
  line-height: 1.2 !important;
}

/* Mobile 2-Column Responsive Layout */
@media (max-width: 768px) {
  .card-body {
    padding: 10px 10px 12px !important;
  }
  .card-price-row {
    align-items: center !important;
    gap: 4px !important;
  }
  .card-price-left {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 2px !important;
    min-width: 0 !important;
    flex: 1 !important;
  }
  .price-main {
    font-size: 13.5px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
  }
  .card-price-compare-wrap {
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
    white-space: nowrap !important;
  }
  .price-mrp {
    font-size: 11px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
  }
  .price-discount {
    font-size: 10px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
    color: #B83A3A !important;
    font-weight: 700 !important;
  }
  .snitch-plus-trigger {
    width: 28px !important;
    height: 28px !important;
    flex-shrink: 0 !important;
  }
}
"""

for c_file in css_files:
    if os.path.exists(c_file):
        with open(c_file, "r", encoding="utf-8") as f:
            c_text = f.read()
        
        if "HYPER-CLEAN CARD PRICE & DISCOUNT PERCENTAGE" not in c_text:
            c_text += price_fix_css
            with open(c_file, "w", encoding="utf-8") as f:
                f.write(c_text)
            print(f"Appended price fix CSS to {c_file}")
        else:
            print(f"Price fix CSS already present in {c_file}")


# 4. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_text = f.read()

# Update static card price rows in index.html
static_card_pattern = re.compile(
    r'<div class="card-price-row">\s*<span class="price-main">(&#8377;\d+[\d,]*)</span>\s*<span class="price-mrp">(&#8377;\d+[\d,]*)</span>\s*<span class="price-discount">(\d+%\s*OFF)</span>',
    re.DOTALL
)

def replace_static_card(m):
    p_main = m.group(1)
    p_mrp = m.group(2)
    p_off = m.group(3)
    return f"""<div class="card-price-row">
          <div class="card-price-left">
            <span class="price-main">{p_main}</span>
            <div class="card-price-compare-wrap">
              <span class="price-mrp">{p_mrp}</span>
              <span class="price-discount">{p_off}</span>
            </div>
          </div>"""

html_text_updated = static_card_pattern.sub(replace_static_card, html_text)

# Update dynamic card render in index.html line 6172
old_dyn = """        html += '<div class="card-price-row">';
        html += '<span class="price-main">&#8377;' + r.price.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-mrp">&#8377;' + r.mrp.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-discount">' + discount + '% OFF</span>';
        html += '</div>';"""

new_dyn = """        html += '<div class="card-price-row">';
        html += '<div class="card-price-left">';
        html += '<span class="price-main">&#8377;' + r.price.toLocaleString('en-IN') + '</span>';
        html += '<div class="card-price-compare-wrap">';
        html += '<span class="price-mrp">&#8377;' + r.mrp.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-discount">' + discount + '% OFF</span>';
        html += '</div>';
        html += '</div>';
        html += '</div>';"""

if old_dyn in html_text_updated:
    html_text_updated = html_text_updated.replace(old_dyn, new_dyn, 1)
    print("Updated dynamic card render in index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_text_updated)

print("\nStep 11 updates executed successfully!")

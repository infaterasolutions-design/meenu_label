import os

shopify_script = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_shopify_theme.py"
with open(shopify_script, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update header_liquid
old_header_start = code.find('header_liquid = """')
old_header_end = code.find('{% endschema %}\n"""') + len('{% endschema %}\n"""')

new_header_liquid = '''header_liquid = """
<header>
  <div class="header-inner">
    <nav>
      <ul class="nav-links">
        <li><a href="/collections/all">All Silhouettes</a></li>
        <li><a href="/collections/co-ord-sets">Co-ord Sets</a></li>
        <li><a href="/collections/festive-suits">Festive Suits</a></li>
        <li><a href="/collections/dresses">Dresses</a></li>
        <li><a href="/collections/tops">Tops</a></li>
      </ul>
    </nav>

    <div>
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>

    <!-- Snitch-Style Minimalist Outline Icons -->
    <div class="header-actions">
      <!-- 1. Search -->
      <a href="/search" class="header-icon-link" aria-label="Search" title="Search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
      </a>

      <!-- 2. Shopping Bag -->
      <button class="header-icon-btn" onclick="toggleCartDrawer()" aria-label="Shopping Bag" title="Shopping Bag">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
          <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
        </svg>
        <span class="header-badge-pill" id="cartBadgeCount">{{ cart.item_count }}</span>
      </button>

      <!-- 3. Wishlist (Heart) -->
      <a href="/pages/wishlist" class="header-icon-link" aria-label="Wishlist" title="Wishlist">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
      </a>

      <!-- 4. User Account -->
      <a href="/account" class="header-icon-link" aria-label="Account" title="Account">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
      </a>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
"""'''

if old_header_start != -1 and old_header_end != -1:
    code = code[:old_header_start] + new_header_liquid + code[old_header_end:]
    print("Replaced header_liquid successfully.")
else:
    print("WARNING: Could not find header_liquid boundaries")

# 2. Update CSS for header actions
old_css = """.header-actions { display: flex; justify-content: flex-end; align-items: center; gap: 16px; flex: 1; }
.header-btn {
  background: none;
  border: 1px solid var(--border-color);
  padding: 8px 16px;
  font-family: inherit;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
}
.header-btn:hover { background: var(--text-color); color: var(--bg-color); }
.cart-badge {
  background: var(--accent-gold);
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 10px;
}"""

new_css = """.header-actions { display: flex; justify-content: flex-end; align-items: center; gap: 18px; flex: 1; }
.header-icon-link, .header-icon-btn {
  background: none;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  padding: 0;
  text-decoration: none;
  transition: all 0.2s ease;
}
.header-icon-link:hover, .header-icon-btn:hover {
  color: var(--accent-gold);
  background: rgba(0,0,0,0.03);
  transform: translateY(-1px);
}
.header-icon-link svg, .header-icon-btn svg {
  width: 22px;
  height: 22px;
  display: block;
  stroke-width: 1.6;
}
.header-badge-pill {
  position: absolute;
  top: 4px;
  right: 2px;
  background: var(--text-color);
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 700;
  min-width: 16px;
  height: 16px;
  line-height: 16px;
  border-radius: 8px;
  text-align: center;
  padding: 0 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.18);
  pointer-events: none;
}"""

if old_css in code:
    code = code.replace(old_css, new_css)
    print("Replaced header CSS in theme.css successfully.")
else:
    # Try finding .header-actions in code
    h_pos = code.find('.header-actions {')
    if h_pos != -1:
        end_badge = code.find('border-radius: 10px;\n}', h_pos)
        if end_badge != -1:
            code = code[:h_pos] + new_css + code[end_badge + len('border-radius: 10px;\n}'):]
            print("Replaced header actions CSS via substring search.")

with open(shopify_script, 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: Updated build_shopify_theme.py with Snitch header icons!")

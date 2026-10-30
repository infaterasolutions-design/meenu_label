with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_header_liquid = '''header_liquid = """
<header>
  <div class="header-inner">
    <!-- Left: Hamburger Menu Icon -->
    <div class="header-left">
      <button class="hamburger-btn" onclick="openNavDrawer()" aria-label="Open Navigation Menu" title="Open Navigation Menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Middle: Centered Brand Logo -->
    <div class="header-center">
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>

    <!-- Right: Snitch 4 Minimalist Line Icons -->
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

pos = code.find('header_liquid = """')
end = code.find('{% endschema %}\n"""') + len('{% endschema %}\n"""')
if pos != -1 and end != -1:
    code = code[:pos] + new_header_liquid + code[end:]
    print("Replaced header_liquid in build_shopify_theme.py")

# Update CSS in theme.css
css_find = """.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 14px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}"""

css_replace = """.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 14px 36px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header-left { flex: 1; display: flex; align-items: center; justify-content: flex-start; }
.hamburger-btn { background: none; border: none; cursor: pointer; color: var(--text-color); display: inline-flex; align-items: center; padding: 6px; }
.hamburger-btn svg { width: 22px; height: 22px; display: block; }
.header-center { flex: 0 0 auto; text-align: center; }"""

if css_find in code:
    code = code.replace(css_find, css_replace)
    print("Updated header-inner CSS in build_shopify_theme.py")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_shopify_theme.py")

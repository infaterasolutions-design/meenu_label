import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update layout/theme.liquid
theme_paths = ['layout/theme.liquid', 'meenu-label-shopify-theme/layout/theme.liquid']
for p in theme_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if "{% render 'snitch-login-modal' %}" not in content:
        content = content.replace(
            "{% render 'whatsapp-concierge' %}",
            "{% render 'whatsapp-concierge' %}\n    {% render 'snitch-login-modal' %}"
        )
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added snitch-login-modal render to {p}")
    else:
        print(f"snitch-login-modal render already in {p}")

# 2. Update sections/header.liquid
header_paths = ['sections/header.liquid', 'meenu-label-shopify-theme/sections/header.liquid']
header_btn = """      <!-- 3. User Account & Order Tracking Drawer Trigger -->
      <button type="button" class="header-icon-action header-account-btn" onclick="openAccountModal()" title="Track My Order & VIP Account" aria-label="Account" style="position:relative;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
        <span class="account-active-badge" id="accountActiveBadge"></span>
      </button>"""

for p in header_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    old_target = """      <!-- 3. User Account (Direct Official Shopify Account Portal) -->
      <a href="/account" class="header-icon-action header-account-btn" title="My Account & Orders" aria-label="Account">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
      </a>"""
    if old_target in content:
        content = content.replace(old_target, header_btn)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated header account button in {p}")
    else:
        print(f"Old header link not found in {p} (checking if already updated)")

# 3. Update snippets/nav-drawer.liquid
nav_paths = ['snippets/nav-drawer.liquid', 'meenu-label-shopify-theme/snippets/nav-drawer.liquid']
nav_old = """        <li>
          <a href="/account" style="text-decoration:none; color:var(--text-color); font-size:13px; font-weight:600;">&#128100; My Account &amp; Order Tracking</a>
        </li>"""

nav_new = """        <li>
          <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('track');" style="text-decoration:none; color:var(--text-color); font-size:13px; font-weight:600;">&#128230; Track My Order</a>
        </li>
        <li>
          <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('login');" style="text-decoration:none; color:var(--text-color); font-size:13px; font-weight:600;">&#128100; VIP Account / Login</a>
        </li>"""

for p in nav_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if nav_old in content:
        content = content.replace(nav_old, nav_new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated nav drawer tracking & account in {p}")
    else:
        print(f"Nav drawer old target not found in {p}")

# 4. Update sections/footer.liquid
footer_paths = ['sections/footer.liquid', 'meenu-label-shopify-theme/sections/footer.liquid']
footer_old = """      <h4>Client Care</h4>
      <ul>
        <li><a href="javascript:void(0)" onclick="openPolicyModal('about')">About Us (Our Story)</a></li>"""

footer_new = """      <h4>Client Care</h4>
      <ul>
        <li><a href="javascript:void(0)" onclick="openAccountModal('track')">&#128230; Track My Order</a></li>
        <li><a href="javascript:void(0)" onclick="openAccountModal('login')">&#128100; VIP Atelier Account</a></li>
        <li><a href="javascript:void(0)" onclick="openPolicyModal('about')">About Us (Our Story)</a></li>"""

for p in footer_paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if footer_old in content:
        content = content.replace(footer_old, footer_new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Track My Order & VIP Account to footer in {p}")
    else:
        print(f"Footer old target not found in {p}")

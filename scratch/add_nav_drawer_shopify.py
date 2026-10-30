with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add nav-drawer snippet into theme
nav_drawer_liquid = '''# nav-drawer.liquid
nav_drawer_liquid = """
<div class="nav-drawer-backdrop" id="navDrawerBackdrop" onclick="closeNavDrawer()">
  <div class="nav-drawer" id="navDrawer" onclick="event.stopPropagation()">
    <div class="nav-drawer-header">
      <span class="brand-logo" style="font-size:20px;">{{ shop.name | default: 'MEENU LABEL' }}</span>
      <button style="background:none; border:none; font-size:24px; cursor:pointer; color:var(--text-color); padding:4px 8px; line-height:1;" onclick="closeNavDrawer()">&times;</button>
    </div>
    <div class="nav-drawer-body">
      <ul class="nav-drawer-links" style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:16px;">
        <li><a href="/collections/all" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">All Silhouettes (16)</a></li>
        <li><a href="/collections/co-ord-sets" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Co-ord Sets (4)</a></li>
        <li><a href="/collections/festive-suits" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Festive Suits (6)</a></li>
        <li><a href="/collections/dresses" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Midi Dresses (3)</a></li>
        <li><a href="/collections/tops" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Tops &amp; Blouses (3)</a></li>
        <li style="border-top:1px solid var(--border-color); margin-top:16px; padding-top:16px;">
          <a href="javascript:void(0)" onclick="closeNavDrawer(); openSizeGuideModal();" style="text-decoration:none; color:var(--text-color); font-size:13px;">&#128207; Size &amp; Fit Guide</a>
        </li>
        <li>
          <a href="https://wa.me/919988898845" target="_blank" style="text-decoration:none; color:#25D366; font-size:13px;">&#128172; WhatsApp Concierge (+91 99888 98845)</a>
        </li>
      </ul>
    </div>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "nav-drawer.liquid"), "w", encoding="utf-8") as f:
    f.write(nav_drawer_liquid)
'''

if "nav_drawer_liquid" not in code:
    pos_drawer = code.find('# cart-drawer.liquid')
    if pos_drawer != -1:
        code = code[:pos_drawer] + nav_drawer_liquid + "\n" + code[pos_drawer:]
        print("Inserted nav-drawer.liquid snippet code.")

# Also render in theme.liquid
if "{% render 'nav-drawer' %}" not in code:
    code = code.replace("{% render 'cart-drawer' %}", "{% render 'nav-drawer' %}\n  {% render 'cart-drawer' %}")
    print("Rendered nav-drawer in theme.liquid.")

# Also add openNavDrawer and closeNavDrawer in theme JS
nav_js = """function openNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.add('open');
  if (b) b.classList.add('open');
}
function closeNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.remove('open');
  if (b) b.classList.remove('open');
}"""

if "function openNavDrawer" not in code:
    code = code.replace("function toggleCartDrawer() {", nav_js + "\nfunction toggleCartDrawer() {")
    print("Added openNavDrawer and closeNavDrawer JS in build_shopify_theme.py.")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_shopify_theme.py with nav-drawer!")

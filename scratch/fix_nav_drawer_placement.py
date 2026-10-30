import os, re

build_file = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(build_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Locate and extract nav-drawer markup
nav_start_tag = '<!-- Navigation Drawer -->'
if nav_start_tag not in code:
    nav_start_tag = '<div class="nav-drawer-backdrop"'

nav_start = code.find(nav_start_tag)
# Find the end of navDrawerBackdrop (closing </div>)
nav_body_end = code.find('</ul>\n      </div>\n    </div>\n  </div>', nav_start)
if nav_body_end == -1:
    nav_body_end = code.find('</ul>\n      </div>\n    </div>\n  </div>', nav_start)
if nav_body_end == -1:
    # Substring search to <!-- Catalog Section -->
    nav_body_end = code.find('<!-- Catalog Section -->', nav_start)
else:
    nav_body_end += len('</ul>\n      </div>\n    </div>\n  </div>')

nav_drawer_html = code[nav_start:nav_body_end].strip()
print("Found navDrawer chunk of length:", len(nav_drawer_html))

# Remove from its old location inside storefrontHomeView
code = code[:nav_start] + code[nav_body_end:]
print("Removed navDrawer from inside storefrontHomeView.")

# 2. Modernize the navDrawer markup (clean close button and icons)
clean_nav_drawer = """<!-- Navigation Drawer (Global at Root Level) -->
  <div class="nav-drawer-backdrop" id="navDrawerBackdrop" onclick="closeNavDrawer()">
    <div class="nav-drawer" id="navDrawer" onclick="event.stopPropagation()">
      <div class="nav-drawer-header">
        <img src="{logo_b64}" alt="Meenu Label" style="height: 42px; width: auto;">
        <button style="background:none; border:none; font-size:24px; cursor:pointer; color:var(--text-main); padding:4px 8px; line-height:1;" onclick="closeNavDrawer()">&times;</button>
      </div>
      <div class="nav-drawer-body">
        <ul class="nav-drawer-links">
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('all')">All Silhouettes (16)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('coord')">Co-ord Sets (4)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('festive')">Festive Suits (6)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('dress')">Midi Dresses (3)</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('top')">Tops &amp; Blouses (3)</a></li>
          <li style="border-top:1px solid var(--border-color); margin-top:20px; padding-top:20px;">
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openSizeGuide()">&#128207; Size &amp; Fit Guide (M-XL)</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); closeProductPage(); document.getElementById('founder').scrollIntoView({behavior:'smooth'});">&#128081; Behind The Label (Transparency)</a>
          </li>
          <li>
            <a href="https://wa.me/919988898845" target="_blank" style="color:#25D366;">&#128172; WhatsApp Concierge (+91 99888 98845)</a>
          </li>
        </ul>
      </div>
    </div>
  </div>"""

# 3. Insert right before <!-- Cart Drawer --> or before </body>
insert_target = '<!-- Cart Drawer -->'
if insert_target in code:
    code = code.replace(insert_target, clean_nav_drawer + "\n\n  " + insert_target)
    print("Inserted global navDrawer right before Cart Drawer successfully.")
else:
    body_end = code.find('</body>')
    code = code[:body_end] + clean_nav_drawer + "\n\n" + code[body_end:]
    print("Inserted global navDrawer before </body>.")

# 4. Also ensure openProductPage scrolls to top instantly without smooth glitch
code = code.replace("window.scrollTo({{ top: 0, behavior: 'smooth' }});", "window.scrollTo(0, 0);")
code = code.replace("window.scrollTo({ top: 0, behavior: 'smooth' });", "window.scrollTo(0, 0);")

with open(build_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated build_snitch_storefront.py with global root-level navDrawer!")

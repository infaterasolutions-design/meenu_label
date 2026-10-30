with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add pointer-events: none to SVGs in buttons
svg_css_rule = """.header-icon-action svg {
      width: 22px;
      height: 22px;
      display: block;
      stroke-width: 1.6;
      pointer-events: none;
    }
    .hamburger-btn svg {
      width: 22px;
      height: 22px;
      display: block;
      pointer-events: none;
    }
    .card-wishlist-btn svg {
      width: 18px;
      height: 18px;
      display: block;
      transition: fill 0.2s ease, stroke 0.2s ease;
      pointer-events: none;
    }"""

old_svg_rule = """.header-icon-action svg {
      width: 22px;
      height: 22px;
      display: block;
      stroke-width: 1.6;
    }"""

if old_svg_rule in code:
    code = code.replace(old_svg_rule, svg_css_rule)
    print("Added pointer-events: none to SVG icons")

# 2. Defensively guard selectModalSize
old_sms = """function selectModalSize(size, el) {
      selectedSize = size;
      document.querySelectorAll('.modal-size-btn').forEach(function(b) { b.classList.remove('selected'); });
      el.classList.add('selected');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }"""

new_sms = """function selectModalSize(size, el) {
      selectedSize = size;
      document.querySelectorAll('.modal-size-btn').forEach(function(b) { b.classList.remove('selected'); });
      if (el) el.classList.add('selected');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }"""

if old_sms in code:
    code = code.replace(old_sms, new_sms)
    print("Guarded selectModalSize")

# 3. Update WhatsApp link concierge number
code = code.replace("wa.me/919876543210", "wa.me/919988898845")

# 4. Guard navDrawer functions
old_nav = """function openNavDrawer() {
      document.getElementById('navDrawer').classList.add('open');
      document.getElementById('navDrawerBackdrop').classList.add('open');
    }
    function closeNavDrawer() {
      document.getElementById('navDrawer').classList.remove('open');
      document.getElementById('navDrawerBackdrop').classList.remove('open');
    }"""

new_nav = """function openNavDrawer() {
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

if old_nav in code:
    code = code.replace(old_nav, new_nav)
    print("Guarded navDrawer functions")

# 5. Guard sizeGuide functions
old_sg = """function openSizeGuide() {
      document.getElementById('sizeGuideBackdrop').classList.add('open');
    }
    function closeSizeGuideDirect() {
      document.getElementById('sizeGuideBackdrop').classList.remove('open');
    }"""

new_sg = """function openSizeGuide() {
      var b = document.getElementById('sizeGuideBackdrop');
      if (b) b.classList.add('open');
    }
    function closeSizeGuideDirect() {
      var b = document.getElementById('sizeGuideBackdrop');
      if (b) b.classList.remove('open');
    }"""

if old_sg in code:
    code = code.replace(old_sg, new_sg)
    print("Guarded sizeGuide functions")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py")

import os

# 1. Update build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add CSS for whatsapp-benefit-box
wa_box_css = """    /* WhatsApp Benefit Hint Box */
    .whatsapp-benefit-box {{
      background: #F4FAF6;
      border: 1px solid rgba(37, 211, 102, 0.35);
      border-radius: 8px;
      padding: 11px 14px;
      margin-top: 10px;
      font-size: 12px;
      line-height: 1.55;
      color: #1B4D30;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      text-align: left;
    }}
    .whatsapp-benefit-box strong {{
      color: #0F3820;
      font-weight: 700;
    }}
    .whatsapp-benefit-box .wa-icon {{
      font-size: 16px;
      line-height: 1.2;
      flex-shrink: 0;
      margin-top: 2px;
    }}
"""

if "whatsapp-benefit-box" not in code:
    code = code.replace("</style>", wa_box_css + "\n  </style>")
    print("Added whatsapp-benefit-box CSS to build_snitch_storefront.py")

# Add benefit box below pdpWhatsAppBtn
pdp_target = """            <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="#" target="_blank">
              <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
            </a>"""

pdp_repl = pdp_target + """\n            <div class="whatsapp-benefit-box">
              <span class="wa-icon">&#128172;</span>
              <div>
                <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
                Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
              </div>
            </div>"""

if pdp_target in code:
    code = code.replace(pdp_target, pdp_repl)
    print("Added WhatsApp benefit box below pdpWhatsAppBtn in build_snitch_storefront.py")
else:
    print("WARNING: pdp_target not found in build_snitch_storefront.py")

# Add benefit box below modalWhatsAppBtn
modal_target = """        <a id="modalWhatsAppBtn" class="modal-btn-whatsapp" href="#" target="_blank">
          <span>&#128172;</span> DIRECT ORDER VIA WHATSAPP CONCIERGE
        </a>"""

if modal_target not in code:
    # Try finding whatever span is inside modalWhatsAppBtn
    import re
    m = re.search(r'(<a id="modalWhatsAppBtn" class="modal-btn-whatsapp" href="#" target="_blank">[\s\S]*?</a>)', code)
    if m:
        modal_target = m.group(1)
        print("Found dynamic modal_target:", modal_target[:60])

modal_repl = modal_target + """\n        <div class="whatsapp-benefit-box">
          <span class="wa-icon">&#128172;</span>
          <div>
            <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
            Chat directly with our Chandigarh stylist to confirm sizing, request custom alterations, or view unedited fabric videos.
          </div>
        </div>"""

if modal_target in code:
    code = code.replace(modal_target, modal_repl)
    print("Added WhatsApp benefit box below modalWhatsAppBtn in build_snitch_storefront.py")
else:
    print("WARNING: modal_target not found in build_snitch_storefront.py")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated build_snitch_storefront.py!")

# 2. Update build_shopify_theme.py
with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    shopify_code = f.read()

# Add CSS in theme CSS
wa_shopify_css = """
/* WhatsApp Benefit Hint */
.whatsapp-benefit-box {
  background: #F4FAF6;
  border: 1px solid rgba(37, 211, 102, 0.35);
  border-radius: 8px;
  padding: 11px 14px;
  margin-top: 10px;
  font-size: 12px;
  line-height: 1.55;
  color: #1B4D30;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  text-align: left;
}
.whatsapp-benefit-box strong {
  color: #0F3820;
  font-weight: 700;
}
.whatsapp-benefit-box .wa-icon {
  font-size: 16px;
  line-height: 1.2;
  flex-shrink: 0;
  margin-top: 2px;
}
"""

if "whatsapp-benefit-box" not in shopify_code:
    shopify_code = shopify_code.replace("/* Cart Drawer */", wa_shopify_css + "\n/* Cart Drawer */")
    print("Added whatsapp-benefit-box CSS in build_shopify_theme.py")

sh_target = """    <a href="https://wa.me/{{ settings.whatsapp_number }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20(SKU:%20{{ product.selected_or_first_available_variant.sku }})" target="_blank" style="display: block; width: 100%; text-align: center; background: #25D366; color: #FFF; padding: 14px 24px; border-radius: 6px; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 0.05em; font-size: 14px;">
      Order Directly via WhatsApp
    </a>"""

sh_repl = sh_target + """\n    <div class="whatsapp-benefit-box">
      <span class="wa-icon">&#128172;</span>
      <div>
        <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
        Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
      </div>
    </div>"""

if sh_target in shopify_code:
    shopify_code = shopify_code.replace(sh_target, sh_repl)
    print("Added WhatsApp benefit box to product.liquid in build_shopify_theme.py")
else:
    print("WARNING: sh_target not found in build_shopify_theme.py")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(shopify_code)

print("Saved updated build_shopify_theme.py!")

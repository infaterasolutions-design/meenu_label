# 1. Update build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Match 1: Founder paragraph
text = text.replace(
    'Operating proudly out of Chandigarh under <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>, we set out to bridge this gap.',
    'Operating proudly as an independent luxury ethnic label out of Chandigarh, we set out to bridge this gap.'
)

# Match 2: Stat row in Founder section
text = text.replace(
    '<span class="stat-label">Operating Entity</span>\n        <span class="stat-val">Infatera Software Solutions OPC Pvt. Ltd.</span>',
    '<span class="stat-label">Brand Ownership</span>\n        <span class="stat-val">Meenu Label (Independent Atelier)</span>'
)
# Also check single line variant
text = text.replace(
    '<span class="stat-label">Operating Entity</span> <span class="stat-val">Infatera Software Solutions OPC Pvt. Ltd.</span>',
    '<span class="stat-label">Brand Ownership</span> <span class="stat-val">Meenu Label (Independent Atelier)</span>'
)

# Match 3: Footer paragraph
text = text.replace(
    'Operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong><br>\n          Chandigarh, India &bull; Official Domain: <strong>meenulabel.com</strong>',
    '<strong>Meenu Label &bull; Independent Luxury Label</strong><br>\n          Chandigarh, India &bull; Official Domain: <strong>meenulabel.com</strong>'
)
text = text.replace(
    'Operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong><br>           Chandigarh, India &bull; Official Domain: <strong>meenulabel.com</strong>',
    '<strong>Meenu Label &bull; Independent Luxury Label</strong><br>           Chandigarh, India &bull; Official Domain: <strong>meenulabel.com</strong>'
)

# Match 4: Copyright line
text = text.replace(
    '&copy; 2026 Meenu Label (Infatera Software Solutions OPC Pvt. Ltd.). All rights reserved.',
    '&copy; 2026 Meenu Label. All rights reserved.'
)

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned Infatera references in build_snitch_storefront.py!")

# 2. Update build_shopify_theme.py
with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    sh_text = f.read()

sh_text = sh_text.replace(
    'Meenu Label was born out of Chandigarh under <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>',
    'Meenu Label was born out of Chandigarh as an independent luxury ethnic atelier.'
)

sh_text = sh_text.replace(
    '<span>Operating Entity</span><strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>',
    '<span>Brand Ownership</span><strong>Meenu Label (Independent Atelier)</strong>'
)

sh_text = sh_text.replace(
    'Operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>, Chandigarh.',
    'Independent Luxury Ethnic Label, Chandigarh.'
)

sh_text = sh_text.replace(
    'Meenu Label (Infatera Software Solutions OPC Pvt. Ltd.). Official Store: meenulabel.com',
    'Meenu Label. Official Store: meenulabel.com'
)

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(sh_text)

print("Cleaned Infatera references in build_shopify_theme.py!")

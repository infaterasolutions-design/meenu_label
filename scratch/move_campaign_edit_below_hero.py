import os

with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Extract The Campaign Edit block
camp_start_tag = '<!-- ========================================================\n       THE CAMPAIGN EDIT'
pos_camp_start = code.find(camp_start_tag)
pos_camp_end = code.find('</section>', pos_camp_start) + len('</section>')

if pos_camp_start == -1 or pos_camp_end == -1:
    print("ERROR: Could not locate Campaign Edit block!")
    exit(1)

campaign_html = code[pos_camp_start:pos_camp_end].strip()
print(f"Extracted Campaign Edit block of length {len(campaign_html)}")

# Remove from current location below catalog
code_without_camp = code[:pos_camp_start] + code[pos_camp_end:]

# Target right above <!-- Catalog Section -->
target_catalog = '<!-- Catalog Section -->'
pos_catalog = code_without_camp.find(target_catalog)

if pos_catalog == -1:
    print("ERROR: Could not locate target_catalog!")
    exit(1)

# Insert right above Catalog Section
new_code = code_without_camp[:pos_catalog] + campaign_html + "\n\n  " + code_without_camp[pos_catalog:]

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Successfully moved The Campaign Edit right below the Hero Banner in build_snitch_storefront.py!")

# 2. Also ensure Shopify theme has campaign_edit right after hero in templates/index.json
with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    sh_code = f.read()

sh_old_order = '"order": ["hero", "collection", "campaign_edit", "values", "founder"]'
sh_new_order = '"order": ["hero", "campaign_edit", "collection", "values", "founder"]'

if sh_old_order in sh_code:
    sh_code = sh_code.replace(sh_old_order, sh_new_order)
    with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
        f.write(sh_code)
    print("Updated Shopify templates/index.json order to place campaign_edit right below hero!")
else:
    print("Shopify order already matches or pattern not found.")

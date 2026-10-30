with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections\campaign-edit.html', 'r', encoding='utf-8') as f:
    camp_html = f.read()

with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\campaign-edit.liquid', 'r', encoding='utf-8') as f:
    camp_liq = f.read()

print("=== CAMPAIGN HTML FROM STOREFRONT ===")
print(camp_html[:1500])
print("\n=== CAMPAIGN LIQUID ===")
print(camp_liq[:1500])

import os

theme_pdp = 'sections/main-product.liquid'
mirror_pdp = 'meenu-label-shopify-theme/sections/main-product.liquid'
index_pdp = 'index.html'

with open(theme_pdp, 'r', encoding='utf-8') as f:
    c1 = f.read()

with open(mirror_pdp, 'r', encoding='utf-8') as f:
    c2 = f.read()

with open(index_pdp, 'r', encoding='utf-8') as f:
    c3 = f.read()

print("Sections match exactly:", c1 == c2)
print("pdpNotifyWhatsAppBtn in theme:", 'pdpNotifyWhatsAppBtn' in c1)
print("pdpNotifyWaitlistBtn in theme:", 'pdpNotifyWaitlistBtn' in c1)
print("pdpNotifyWhatsAppBtn in index:", 'pdpNotifyWhatsAppBtn' in c3)
print("pdpNotifyWaitlistBtn in index:", 'pdpNotifyWaitlistBtn' in c3)
print("8511616133 in theme:", '8511616133' in c1)
print("8511616133 in index:", '8511616133' in c3)

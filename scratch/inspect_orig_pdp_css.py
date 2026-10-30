import re

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.backup_size_fix.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.pdp-grid {')
if idx != -1:
    print("Found .pdp-grid in backup_size_fix:\n")
    print(text[idx:idx+1200])
else:
    print("Not found .pdp-grid")

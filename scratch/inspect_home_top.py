import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

home_idx = text.find('id="storefrontHomeView"')
sub = text[home_idx:home_idx+4000]
print(sub[:2500])

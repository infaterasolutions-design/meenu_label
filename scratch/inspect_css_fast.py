with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_start = text.find('<style>')
s_end = text.find('</style>')
css = text[s_start:s_end]
print("CSS length:", len(css))

import re
for m in re.finditer(r'hamburger[^{]*\{[^}]*\}', css):
    print("Match:", m.group(0))

for m in re.finditer(r'header-left[^{]*\{[^}]*\}', css):
    print("Match:", m.group(0))

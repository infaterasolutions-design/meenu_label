with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(re.escape('quickAddCartFromPage'), html)]
print("Occurrences of quickAddCartFromPage:", len(matches))
for idx in matches:
    print(html[max(0, idx-50):min(len(html), idx+100)].replace('\n', ' '))

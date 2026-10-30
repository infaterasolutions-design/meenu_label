with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.search(r'(\/\* ===+ CAMPAIGN EDIT[\s\S]*?)(?=\/\* ===+|\Z)', css)
if m:
    print(m.group(1)[:2000].encode('ascii', 'replace').decode('ascii'))
else:
    # search for .campaign-edit-section
    idx = css.find('.campaign-edit-section')
    if idx != -1:
        print(css[idx:idx+2500].encode('ascii', 'replace').decode('ascii'))

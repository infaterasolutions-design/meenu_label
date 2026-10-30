with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<style>')
s_end = html.find('</style>')
css = html[s_start:s_end]

import re
lines = css.split('\n')
for i, line in enumerate(lines):
    if 'overflow' in line or 'pdp-section' in line or 'pdp-grid' in line or 'pdp-gallery-col' in line or 'pdp-info-col' in line:
        context = '\n'.join(lines[max(0, i-3):min(len(lines), i+8)])
        print(f"--- line {i} ---")
        print(context)

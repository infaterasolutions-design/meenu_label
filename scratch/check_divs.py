import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
open_divs = len(re.findall(r'<div\b', html, re.IGNORECASE))
close_divs = len(re.findall(r'</div>', html, re.IGNORECASE))
print(f"Open divs: {open_divs}, Close divs: {close_divs}, Diff: {open_divs - close_divs}")

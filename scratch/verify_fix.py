import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Div balance
open_divs = len(re.findall(r'<div\b', html, re.IGNORECASE))
close_divs = len(re.findall(r'</div>', html, re.IGNORECASE))
print(f"Div balance: Open={open_divs}, Close={close_divs}, Diff={open_divs - close_divs}")

# 2. Check selected class
matches = re.findall(r'<[^>]*class="[^"]*\bselected\b[^"]*"[^>]*>', html)
print(f"Elements with 'selected' class ({len(matches)}):")
for m in matches:
    print(" ", m)

# 3. Extract all <script> blocks and test syntax with node
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} script tags")
for i, s in enumerate(scripts):
    # test syntax using node
    res = subprocess.run(['node', '--check', '-'], input=s, text=True, capture_output=True, encoding='utf-8', errors='ignore')
    if res.returncode != 0:
        print(f"Script #{i} syntax ERROR: {res.stderr}")
    else:
        print(f"Script #{i} syntax OK")

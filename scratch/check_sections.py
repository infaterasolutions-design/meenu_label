import os
import re

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print('HTML length:', len(html))
sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', html)
print('Section classes in standalone HTML:')
for s in sections:
    print('  -', s)

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
sections_dir = os.path.join(theme_dir, 'sections')

print('\nTheme sections:')
for fname in os.listdir(sections_dir):
    fpath = os.path.join(sections_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    classes = set(re.findall(r'class=["\']([^"\']+)["\']', content))
    print(f'=== {fname} ===')
    sec_tags = re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', content)
    print('  section tag classes:', sec_tags)

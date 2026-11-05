with open('scratch/apply_pdp_mobile_fix.py', 'r', encoding='utf-8') as f:
    script_text = f.read()

# Extract mobile_css
start = script_text.find("mobile_css = '''") + len("mobile_css = '''")
end = script_text.find("'''\n\n# 1. Update")
mobile_css = script_text[start:end]

# Update assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
for path in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'MOBILE RESPONSIVENESS & OVERFLOW ELIMINATION' not in content:
        content += '\n' + mobile_css + '\n'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Already updated {path}")

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '</style>' in html and 'MOBILE RESPONSIVENESS & OVERFLOW ELIMINATION' not in html:
    html = html.replace('</style>', mobile_css + '\n</style>', 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html")

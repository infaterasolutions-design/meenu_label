import os
import re

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
sections_dir = os.path.join(theme_dir, 'sections')
extracted_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections'

for fname in os.listdir(extracted_dir):
    ex_path = os.path.join(extracted_dir, fname)
    with open(ex_path, 'r', encoding='utf-8') as f:
        ex_content = f.read()
    
    liq_fname = fname.replace('.html', '.liquid')
    liq_path = os.path.join(sections_dir, liq_fname)
    if os.path.exists(liq_path):
        with open(liq_path, 'r', encoding='utf-8') as f:
            liq_content = f.read()
        
        ex_classes = set(re.findall(r'class=["\']([^"\']+)["\']', ex_content))
        liq_classes = set(re.findall(r'class=["\']([^"\']+)["\']', liq_content))
        
        # Flatten class lists
        ex_set = set(c for line in ex_classes for c in line.split())
        liq_set = set(c for line in liq_classes for c in line.split())
        
        print(f"=== {fname} vs {liq_fname} ===")
        in_ex_not_liq = ex_set - liq_set
        in_liq_not_ex = liq_set - ex_set
        print(f"  Classes in HTML but not Liquid: {len(in_ex_not_liq)}")
        if in_ex_not_liq:
            print(f"    {sorted(list(in_ex_not_liq))[:10]}")
        print(f"  Classes in Liquid but not HTML: {len(in_liq_not_ex)}")
        if in_liq_not_ex:
            print(f"    {sorted(list(in_liq_not_ex))[:10]}")
        print()

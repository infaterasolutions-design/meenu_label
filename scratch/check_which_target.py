with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

import sys
sys.path.append('scratch')
import update_liquid_pdp_option_a as m
print("target_html in c:", m.target_html in c)
print("target_js in c:", m.target_js in c)

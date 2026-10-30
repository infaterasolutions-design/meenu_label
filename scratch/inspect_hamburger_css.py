with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('hamburger')
while pos != -1:
    print(text[pos-40:pos+150].replace('\n', ' '))
    print('---')
    pos = text.find('hamburger', pos+40)

import re

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up duplicate rules in @media (min-width: 993px)
target = """      .pdp-main-image-wrap {
        width: 100%;
        border-radius: 12px;
        overflow: hidden;
        background: #F4EFEB;
        border: 1px solid var(--border-color);
        box-shadow: 0 12px 30px rgba(0,0,0,0.04);
      }
      .pdp-main-image {
        width: 100%;
        aspect-ratio: 4 / 5;
        object-fit: cover;
        object-position: top center;
        display: block;
        max-height: none !important;
      }"""

if target in content:
    content = content.replace(target, "", 1)
    print("Removed redundant override; native 4/5 portrait rules now active!")

# Also ensure .pdp-main-image base rule has aspect-ratio: 4 / 5
idx = content.find('.pdp-main-image {')
print("Base .pdp-main-image rule:")
print(content[idx:idx+250])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Meenu_Label_Desktop_Storefront.html updated successfully!")

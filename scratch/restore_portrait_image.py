import os
import re

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the desktop max-height override with clean portrait styling
target_override = """      .pdp-main-image-wrap {
        max-height: calc(100vh - 220px);
        display: flex;
        align-items: center;
        justify-content: center;
        background: #F4EFEB;
      }
      .pdp-main-image {
        max-height: calc(100vh - 220px);
        object-fit: cover;
      }"""

replacement_override = """      .pdp-main-image-wrap {
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

if target_override in content:
    content = content.replace(target_override, replacement_override, 1)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Restored full 4:5 portrait image shape on desktop!")
else:
    print("target_override not found, checking...")
    idx = content.find('.pdp-main-image-wrap {')
    print(content[idx:idx+400])

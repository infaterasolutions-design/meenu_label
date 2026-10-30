import os

# 1. Read preview_minimal_flow.html to get the exact PDP block
with open('scratch/preview_minimal_flow.html', 'r', encoding='utf-8') as f:
    source = f.read()

idx_pdp_start = source.find('<!-- DEDICATED FULL PRODUCT DETAIL VIEW (PDP) -->')
idx_pdp_end = source.find('<!-- Footer -->', idx_pdp_start)
pdp_block = source[idx_pdp_start:idx_pdp_end].strip()

# In build_snitch_storefront.py, curly braces inside f-strings must be escaped as {{ and }} if any!
# Let's check if there are single curly braces in pdp_block
# Let's see: pdp_block has style="display:none;" etc.
# In Python f-string: { must be {{ unless it's a variable reference.
# Let's check what variables are inside pdp_block in source
print("Found PDP block of length:", len(pdp_block))

# Check for curly braces in pdp_block
import re
curly_matches = re.findall(r'\{[^{}]*\}', pdp_block)
print("Curly matches in PDP block:", curly_matches[:10])

# Escape curly braces for Python f-string
pdp_block_escaped = pdp_block.replace('{', '{{').replace('}', '}}')

# 2. Update build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    target = f.read()

idx_founder_end = target.find('</section>', target.find('class="founder-section"')) + 10
idx_footer = target.find('<!-- Footer -->')

# Insert: closing </div> for storefrontHomeView, then pdp_block_escaped, then newline
new_middle = f"""
  </div>

  {pdp_block_escaped}

  """

target_updated = target[:idx_founder_end] + new_middle + target[idx_footer:]

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(target_updated)

print("Restored productDetailView into scratch/build_snitch_storefront.py successfully!")

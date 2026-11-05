# Update index.html to ensure no size is pre-selected globally or in quick view modal

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update var selectedSize = 'M'; -> var selectedSize = null;
old1 = "    var selectedSize = 'M';"
new1 = "    var selectedSize = null;"
if old1 in content:
    content = content.replace(old1, new1, 1)
    print("Replaced selectedSize = 'M'")
else:
    print("Could not find selectedSize = 'M'")

# 2. Update var pdpSelectedSize = 'M'; -> var pdpSelectedSize = null;
old2 = "    var pdpSelectedSize = 'M';"
new2 = "    var pdpSelectedSize = null;"
if old2 in content:
    content = content.replace(old2, new2, 1)
    print("Replaced pdpSelectedSize = 'M'")
else:
    print("Could not find pdpSelectedSize = 'M'")

# 3. In addCurrentProductToCart(), check if selectedSize is set
old3 = """    function addCurrentProductToCart() {
      if (!activeModalProduct) return;
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }"""

new3 = """    function addCurrentProductToCart() {
      if (!activeModalProduct) return;
      if (!selectedSize) {
        if (typeof showToast === 'function') {
          showToast('⚠️ Please select a size (M, L, or XL) first.');
        }
        return;
      }
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }"""

if old3 in content:
    content = content.replace(old3, new3, 1)
    print("Updated addCurrentProductToCart with size check")
else:
    print("Could not find exact addCurrentProductToCart")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html update complete!")

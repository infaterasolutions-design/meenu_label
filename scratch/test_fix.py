with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "r", encoding="utf-8") as f:
    js = f.read()

# Fix 1: changeCartItemQty
js = js.replace(
    'onclick="changeCartItemQty(\'\' + it.id + \'\', \'\' + it.size + \'\', -1)"',
    'onclick="changeCartItemQty(\\\'\' + it.id + \'\\\', \\\'\' + it.size + \'\\\', -1)"'
)
js = js.replace(
    'onclick="changeCartItemQty(\'\' + it.id + \'\', \'\' + it.size + \'\', 1)"',
    'onclick="changeCartItemQty(\\\'\' + it.id + \'\\\', \\\'\' + it.size + \'\\\', 1)"'
)

# Fix 2: removeFromCart
js = js.replace(
    'onclick="removeFromCart(\'\' + it.id + \'\', \'\' + it.size + \'\'); renderCartPage();"',
    'onclick="removeCartItemFromPage(\\\'\' + it.id + \'\\\', \\\'\' + it.size + \'\\\')"'
)

# Fix 3: cross-sell button
js = js.replace(
    'onclick="addToCart(productsData.find(function(x){return x.id===\'\' + cp.id + \'\'}), \'M\'); renderCartPage();"',
    'onclick="quickAddCartFromPage(\\\'\' + cp.id + \'\\\')"'
)

# Add helper functions if not present
helpers = """
    function quickAddCartFromPage(prodId) {
      var p = productsData.find(function(x) { return x.id === prodId; });
      if (p) {
        addToCart(p, 'M');
        renderCartPage();
      }
    }
    function removeCartItemFromPage(id, size) {
      removeFromCart(id, size);
      renderCartPage();
    }
"""
if "function quickAddCartFromPage" not in js:
    js = helpers + "\n" + js

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Updated scratch/extracted.js, now let's verify with node --check")

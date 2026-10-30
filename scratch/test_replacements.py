import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Test 1: Check modal JS
p1 = html.find("var activeModalProduct = null;\n    var selectedSize = 'M';")
print("Target 1 found:", p1 != -1)

# Test 2: Check openProductModal
p2 = html.find("activeModalProduct = p;\n      selectedSize = 'M';")
print("Target 2 found:", p2 != -1)

# Test 3: Check modal size btn loop in openProductModal
p3 = html.find("var btns = document.querySelectorAll('.modal-size-btn');\n      btns.forEach(function(b, idx) {\n        if (idx === 0) b.classList.add('selected');\n        else b.classList.remove('selected');\n      });\n\n      updateWhatsAppLink(p, 'M');")
print("Target 3 found:", p3 != -1)

# Test 4: Check pdp variables
p4 = html.find("var activePdpProductId = null;\n    var pdpSelectedSize = 'M';")
print("Target 4 found:", p4 != -1)

# Test 5: Check openProductPage
p5 = html.find("activePdpProductId = prodId;\n      pdpSelectedSize = 'M';")
print("Target 5 found:", p5 != -1)

# Test 6: Check size buttons reset in openProductPage
p6 = html.find("// Size buttons\n      selectPdpSize('M', document.getElementById('pdpSizeBtn_M'));\n\n      // WhatsApp concierge link\n      updatePdpWhatsAppLink(p, 'M');")
print("Target 6 found:", p6 != -1)

# Test 7: Check selectPdpSize & updatePdpWhatsAppLink & addPdpProductToCart & buyPdpProductNow
p7 = html.find("function selectPdpSize(size, btn)")
print("Target 7 found:", p7 != -1)

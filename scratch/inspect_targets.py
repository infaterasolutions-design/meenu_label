with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check pdp-grid CSS
idx1 = html.find('.pdp-grid {')
print("=== pdp-grid CSS ===")
print(html[idx1:idx1+800])

# 2. Check pdp-gallery-col HTML
idx2 = html.find('<!-- Left: Visual Gallery -->')
print("=== Left Gallery HTML ===")
print(html[idx2:idx2+1400])

# 3. Check html, body overflow
idx3 = html.find('html, body {')
print("=== html, body CSS ===")
print(html[idx3:idx3+300])

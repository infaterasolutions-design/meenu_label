with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Trace ancestors of pdp-gallery-col
idx = html.find('class="pdp-gallery-col"')
# print the 2000 chars before this
print("=== Markup before pdp-gallery-col ===")
print(html[idx-1000:idx+100])

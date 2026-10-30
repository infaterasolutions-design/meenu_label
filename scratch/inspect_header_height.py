with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Look for header / navbar height and sticky position
idx = html.find('header')
while idx != -1:
    snippet = html[idx:idx+300]
    if 'position' in snippet or 'top' in snippet or 'height' in snippet:
        print("HEADER SNIPPET:")
        print(snippet)
        print("-" * 30)
    idx = html.find('header', idx+1)
    if idx > 100000: break

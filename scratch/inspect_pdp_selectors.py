with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<style>')
s_end = html.find('</style>')
css = html[s_start:s_end]

for line in css.split('\n'):
    if any(k in line for k in ['productDetailView', 'pdp-section', 'pdp-grid', 'pdp-gallery-col', 'pdp-info-col']):
        print(line)

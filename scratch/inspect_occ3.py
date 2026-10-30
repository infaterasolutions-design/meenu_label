with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<style>')
s_end = html.find('</style>')
css = html[s_start:s_end]

idx = 104030
print(css[idx-300:idx+200])

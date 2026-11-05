with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="productDetailView"')
if start != -1:
    print('Found productDetailView at:', start)
    end = html.find('id="productDetailView"', start + 1)
    # Let's inspect the section
    print(html[start-30:start+2500])

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('class="pdp-grid"')
if idx != -1:
    idx_end = html.find('</section>', idx)
    if idx_end == -1:
        idx_end = html.find('</div>\n    </div>', idx)
    print(html[idx:idx+4000])

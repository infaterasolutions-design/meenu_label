with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<style>')
s_end = html.find('</style>')
css = html[s_start:s_end]

idx = 0
count = 0
while True:
    idx = css.find('.pdp-gallery-col', idx)
    if idx == -1: break
    count += 1
    print(f"=== Occurrence {count} at index {idx} ===")
    print(css[max(0, idx-100):min(len(css), idx+400)])
    print("=" * 40)
    idx += 16

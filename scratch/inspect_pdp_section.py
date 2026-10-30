p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.backup_size_fix.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.pdp-section {')
if idx != -1:
    print(text[idx:idx+400])

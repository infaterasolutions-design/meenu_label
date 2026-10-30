p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront_backup.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.pdp-main-image')
if idx != -1:
    print(text[idx:idx+400])
else:
    print("Not found")

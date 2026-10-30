with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('productDetailView')
print('First occurrence at:', idx)
print(text[idx-50:idx+600])

idx2 = text.find('productDetailView', idx + 20)
print('\nSecond occurrence at:', idx2)
print(text[idx2-50:idx2+600])

idx3 = text.find('productDetailView', idx2 + 20)
print('\nThird occurrence at:', idx3)
if idx3 != -1:
    print(text[idx3-50:idx3+600])

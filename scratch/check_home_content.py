with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_home = text.find('id="storefrontHomeView"')
pos_home_close = text.find('</div>', pos_home)

print("storefrontHomeView starts at:", pos_home)
print("Content right before storefrontHomeView:")
print(text[pos_home-400:pos_home])

print("Content right after storefrontHomeView starts:")
print(text[pos_home:pos_home+400])

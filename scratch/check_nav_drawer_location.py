with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_home = text.find('id="storefrontHomeView"')
pos_home_end = text.find('id="productDetailView"')
pos_nav = text.find('id="navDrawer"')
pos_nav_backdrop = text.find('id="navDrawerBackdrop"')

print("storefrontHomeView start:", pos_home)
print("storefrontHomeView end / PDP start:", pos_home_end)
print("navDrawer pos:", pos_nav)
print("navDrawerBackdrop pos:", pos_nav_backdrop)

if pos_home < pos_nav < pos_home_end:
    print("CRITICAL FINDING: navDrawer IS INSIDE storefrontHomeView!")
else:
    print("navDrawer is outside storefrontHomeView")

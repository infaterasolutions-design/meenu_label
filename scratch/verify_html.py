with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Total HTML length:', len(html))
print('Search icon count:', html.count('header-icon-action'))
print('Wishlist drawer present:', 'wishlistDrawer' in html)
print('Account modal present:', 'accountModalBackdrop' in html)
print('Search overlay present:', 'searchOverlayBar' in html)
print('Wishlist buttons in cards:', html.count('card-wishlist-btn'))
print('Product cards count:', html.count('class="product-card"'))

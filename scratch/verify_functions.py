import re

with open('scratch/storefront_script_0_fixed.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = [
    'addAllWishlistToCart',
    'addCurrentProductToCart',
    'applyCoupon',
    'checkPincode',
    'clearSearch',
    'closeAccountModal',
    'closeAccountModalDirect',
    'closeModal',
    'closeModalOnBackdrop',
    'closeNavDrawer',
    'closeSizeGuide',
    'closeSizeGuideDirect',
    'filterCategory',
    'goToSlide',
    'nextSlide',
    'openAccountModal',
    'openNavDrawer',
    'openProductModal',
    'openSizeGuide',
    'prevSlide',
    'proceedToCheckout',
    'quickAddCart',
    'quickSearch',
    'removeFromCart',
    'selectModalSize',
    'showToast',
    'toggleCart',
    'toggleSearchBar',
    'toggleWishlistDrawer',
    'toggleWishlistProduct',
    'trackOrderSubmit'
]

missing = []
for fn in funcs:
    pattern = rf'function\s+{fn}\s*\('
    if not re.search(pattern, js):
        missing.append(fn)

print('Missing functions count:', len(missing))
if missing:
    print('MISSING FUNCTIONS:', missing)
else:
    print('ALL onclick functions are defined in the script!')

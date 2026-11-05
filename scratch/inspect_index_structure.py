with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        ls = line.strip()
        for tag in ['<section', '<header', '<footer', 'id="pdp', 'id="cart', 'id="wishlist', 'id="snitch']:
            if tag in ls:
                print(f'{i+1}: {ls[:90]}')
                break

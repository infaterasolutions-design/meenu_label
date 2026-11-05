with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('var productsData = [')
print(text[idx:idx+600])

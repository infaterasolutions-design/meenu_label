with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function quickAddCart')
print(text[idx:idx+1500].encode('ascii', errors='replace').decode('ascii'))

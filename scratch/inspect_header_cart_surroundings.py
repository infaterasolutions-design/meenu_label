with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="headerCartCount"')
print(text[idx-300:idx+400].encode('ascii', errors='replace').decode('ascii'))

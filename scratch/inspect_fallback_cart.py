with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function snitchFallbackCartAdd')
print(text[idx:idx+800].encode('ascii', errors='replace').decode('ascii'))

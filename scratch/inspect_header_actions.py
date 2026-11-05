with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="header-actions"')
print(text[idx-50:idx+900].encode('ascii', errors='replace').decode('ascii'))

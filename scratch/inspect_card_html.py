with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="card-info"')
if idx == -1:
    idx = text.find('class="card-body"')
if idx != -1:
    print(text[idx:idx+800].encode('ascii', errors='replace').decode('ascii'))

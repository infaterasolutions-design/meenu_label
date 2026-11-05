with open('index.html', 'r', encoding='utf-8') as f:
    text_index = f.read()

idx = text_index.find('headerCartCount')
while idx != -1:
    print(text_index[max(0, idx-100):min(len(text_index), idx+200)].replace('\n', ' '))
    print('='*40)
    idx = text_index.find('headerCartCount', idx+15)

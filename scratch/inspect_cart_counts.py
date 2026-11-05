with open('sections/header.liquid', 'r', encoding='utf-8') as f:
    text_header = f.read()

idx = text_header.find('headerCartCount')
print("--- sections/header.liquid ---")
print(text_header[max(0, idx-100):min(len(text_header), idx+200)])

with open('index.html', 'r', encoding='utf-8') as f:
    text_index = f.read()

idx2 = text_index.find('cartCount')
print("--- index.html ---")
while idx2 != -1:
    print(text_index[max(0, idx2-60):min(len(text_index), idx2+100)].replace('\n', ' '))
    idx2 = text_index.find('cartCount', idx2+10)

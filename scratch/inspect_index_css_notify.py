with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '/* Mobile responsive drawer feel */'
idx = c.find(target)
if idx != -1:
    print('Found target in index.html at', idx)
    print(c[idx:idx+300])
else:
    print('Target not found')

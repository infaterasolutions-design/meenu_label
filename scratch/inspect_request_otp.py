with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function requestSnitchOtp')
if idx != -1:
    print("Found in index.html at", idx)
    print(c[idx:idx+800])
else:
    print("Not in index.html")

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

line4605 = lines[4604]
pos = 142625
print("Exact 142625:", repr(line4605[pos-100:pos+100]))

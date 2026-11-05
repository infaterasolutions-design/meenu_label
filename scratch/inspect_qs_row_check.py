import sys
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function createSnitchSizeRow')
sys.stdout.buffer.write(c[idx+700:idx+1500].encode('utf-8'))

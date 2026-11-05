import sys
with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function createSnitchSizeRow')
sys.stdout.buffer.write(c[idx:idx+900].encode('utf-8'))

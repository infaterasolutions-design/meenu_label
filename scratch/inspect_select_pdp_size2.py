import sys
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function selectPdpSize')
sys.stdout.buffer.write(c[idx+800:idx+1800].encode('utf-8'))

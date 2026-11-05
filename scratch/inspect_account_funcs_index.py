import sys
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function verifySnitchOtp')
sys.stdout.buffer.write(c[idx:idx+2500].encode('utf-8'))

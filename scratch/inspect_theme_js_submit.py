import sys
with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function submitNotifyMeRequest')
sys.stdout.buffer.write(c[idx+1200:idx+2500].encode('utf-8'))

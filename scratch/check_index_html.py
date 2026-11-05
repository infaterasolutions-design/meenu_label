with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
print('index.html length:', len(html))
print('Has heroSlider?', 'heroSlider' in html)

idx = html.find('id="heroSlider"')
if idx != -1:
    print(html[idx:idx+1500].encode('ascii', 'replace').decode('ascii'))

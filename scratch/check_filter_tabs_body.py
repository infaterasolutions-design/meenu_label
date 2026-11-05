with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

idx = html.find('class="filter-tabs"')
if idx != -1:
    print(html[idx:idx+1500].encode('ascii', 'replace').decode('ascii'))

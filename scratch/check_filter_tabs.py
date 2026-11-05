with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

idx = html.find('filter-tabs')
if idx != -1:
    print(html[idx-100:idx+1200].encode('ascii', 'replace').decode('ascii'))

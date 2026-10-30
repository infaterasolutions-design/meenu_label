with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections\campaign-edit.html', 'r', encoding='utf-8') as f:
    camp = f.read()

print(camp.encode('ascii', 'replace').decode('ascii'))

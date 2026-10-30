with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections\footer.html', 'r', encoding='utf-8') as f:
    foot = f.read()

print("=== footer.html from standalone ===")
print(foot.encode('ascii', 'replace').decode('ascii'))

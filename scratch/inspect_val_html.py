with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections\value-props.html', 'r', encoding='utf-8') as f:
    val = f.read()

print("=== value-props.html from standalone ===")
print(val.encode('ascii', 'replace').decode('ascii'))

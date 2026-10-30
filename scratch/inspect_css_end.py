with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print("Last 30 lines:")
for l in lines[-30:]:
    print(l.rstrip().encode('ascii', 'replace').decode('ascii'))

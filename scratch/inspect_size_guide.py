with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\snippets\size-guide-modal.liquid', 'r', encoding='utf-8') as f:
    sg = f.read()

print("=== snippets/size-guide-modal.liquid ===")
print(sg.encode('ascii', 'replace').decode('ascii'))

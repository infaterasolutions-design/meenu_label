theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/layout/theme.liquid"
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

print("theme.liquid length:", len(content))
# print without base64 or huge blobs
print(content[:3000].encode('ascii', 'replace').decode('ascii'))
print("...\n--- END OF THEME.LIQUID PREVIEW ---")

with open('sections/footer.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

print("Footer track order mentions:")
for line in c.splitlines():
    if 'track' in line.lower() or 'order' in line.lower():
        print("  ", line.strip())

with open('snippets/nav-drawer.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

print("\nNav drawer track order mentions:")
for line in c.splitlines():
    if 'track' in line.lower() or 'order' in line.lower() or 'account' in line.lower():
        print("  ", line.strip())

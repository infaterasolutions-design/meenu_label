with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    content = f.read()

print("File length:", len(content))
lines = content.splitlines()
for i, l in enumerate(lines[:30]):
    print(f"{i+1}: {l}")

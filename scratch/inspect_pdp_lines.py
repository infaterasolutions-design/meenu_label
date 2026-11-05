with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[2350:2470]):
    print(f"{i+2351}: {line.rstrip()}")

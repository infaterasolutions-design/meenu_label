with open('scratch/render_ultimate_hero_preview.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(70, 105):
    if i < len(lines):
        clean = lines[i].rstrip().encode('ascii', errors='replace').decode('ascii')
        print(f'{i+1}: {clean[:100]}')

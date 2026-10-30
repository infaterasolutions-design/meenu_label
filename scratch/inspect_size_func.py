with open('scratch/generated_check.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(295, 320):
    if i < len(lines):
        print(f'{i+1}: {lines[i].rstrip()[:100]}')

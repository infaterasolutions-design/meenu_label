import os

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
old_nums = ['9988898845', '8511616133']

matches = []
for root, dirs, files in os.walk(workspace):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.zip') or f.endswith('.jpg') or f.endswith('.png') or f.endswith('.pyc'):
            continue
        filepath = os.path.join(root, f)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                for num in old_nums:
                    if num in content:
                        count = content.count(num)
                        matches.append((os.path.relpath(filepath, workspace), num, count))
        except Exception:
            pass

for m in sorted(matches):
    print(f"{m[0]}: found {m[1]} ({m[2]} times)")

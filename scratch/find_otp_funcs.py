import os

for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for f in files:
        if f.endswith('.js') or f.endswith('.html') or f.endswith('.liquid'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fl:
                c = fl.read()
                if 'requestSnitchOtp' in c:
                    print(f"Found in {p}")

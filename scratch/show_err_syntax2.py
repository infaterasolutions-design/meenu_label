with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\syntax_check2.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(855, 875):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}")

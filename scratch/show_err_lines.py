with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1085, 1115):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}")

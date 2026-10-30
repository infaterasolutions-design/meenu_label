import sys

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1180, 1220):
    if i < len(lines):
        sys.stdout.buffer.write(f"{i+1}: {lines[i]}".encode('utf-8'))

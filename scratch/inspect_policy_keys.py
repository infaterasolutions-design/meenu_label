with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_policies.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
keys = re.findall(r'(\w+):\s*\{[\s\n]*title:\s*["\']([^"\']+)["\']', js)
print("Policy keys found:")
for k, t in keys:
    print(f" - {k}: {t}")

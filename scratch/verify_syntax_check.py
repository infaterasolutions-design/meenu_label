import re
import subprocess

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r"<script[^>]*>(.*?)</script>", text, flags=re.DOTALL | re.IGNORECASE)
with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\syntax_check.js", "w", encoding="utf-8") as f:
    f.write(scripts[0])

result = subprocess.run(["node", "--check", r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\syntax_check.js"], capture_output=True, text=True)
print("Node check exit code:", result.returncode)
if result.returncode == 0:
    print("VERIFIED: 100% Valid JavaScript Syntax! No errors!")
else:
    print("STDERR:", result.stderr)

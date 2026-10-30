import re
import os

files_to_check = [
    r"C:\Users\sande\Downloads\Meenu_Label_Official_Policies.md",
    r"C:\Users\sande\Downloads\Meenu_Label_Policies_Shopify_Ready.html",
    r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
]

for fpath in files_to_check:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r".{0,50}(?:Infatera|OPC\s*Pvt|Pvt\.?\s*Ltd).{0,50}", content, re.IGNORECASE)
        print(f"=== {os.path.basename(fpath)}: {len(matches)} matches ===")
        for m in matches[:5]:
            print("   ", m.strip())

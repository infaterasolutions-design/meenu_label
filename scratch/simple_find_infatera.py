import os

files_to_check = [
    r"C:\Users\sande\Downloads\Meenu_Label_Official_Policies.md",
    r"C:\Users\sande\Downloads\Meenu_Label_Policies_Shopify_Ready.html",
    r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
]

for fpath in files_to_check:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        count = 0
        print(f"=== {os.path.basename(fpath)} ===")
        for i, line in enumerate(lines):
            if any(k in line for k in ["Infatera", "OPC", "Pvt. Ltd"]):
                count += 1
                if count <= 6:
                    print(f"  Line {i+1}: {line.strip()[:100]}")
        print(f"Total matching lines: {count}\n")

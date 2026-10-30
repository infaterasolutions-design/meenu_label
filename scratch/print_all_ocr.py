import os, json

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
ocr_file = os.path.join(scratch_dir, "ocr_results.json")

with open(ocr_file, "r", encoding="utf-8") as f:
    ocr_data = json.load(f)

for item in ocr_data:
    p = item.get("page")
    texts = item.get("raw_texts", [])
    print(f"=== Page {p} ===")
    for t in texts:
        print("  ", t)

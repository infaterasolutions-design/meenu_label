import json

with open(r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\ocr_results.json", encoding="utf-8") as f:
    data = json.load(f)

target_pages = [1, 4, 5, 9, 10, 16, 17, 24, 25, 28, 41, 44, 47]

for item in data:
    p = item["page"]
    if p in target_pages:
        print(f"=== Page {p} ===")
        for t in item["raw_texts"]:
            print(f"  {t}")

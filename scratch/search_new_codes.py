import os, json

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
ocr_file = os.path.join(scratch_dir, "ocr_results.json")

with open(ocr_file, "r", encoding="utf-8") as f:
    ocr_data = json.load(f)

targets = ["5740", "2661", "5754", "574", "266", "575"]

print("--- SEARCH RESULTS ---")
for item in ocr_data:
    texts = item.get("raw_texts", [])
    for t in texts:
        for tgt in targets:
            if tgt in t:
                print(f"Page {item.get('page')}: {t}")

print("\n--- ALL CODES IN OCR ---")
all_codes = []
for item in ocr_data:
    p = item.get("page")
    for t in item.get("raw_texts", []):
        if any(t.startswith(prefix) for prefix in ["JA", "JE", "SET", "TX", "ZA", "SL", "JN"]):
            all_codes.append((p, t))

for p, c in all_codes[:50]:
    print(f"P{p}: {c}")

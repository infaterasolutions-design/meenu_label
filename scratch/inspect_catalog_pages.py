import pymupdf, json, os

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)
print(f"Total pages in Selected catalog .pdf: {len(doc)}")

targets = ["5740", "2661", "5754", "05740", "02661", "05754", "JAB26SS", "JAB25ST", "JAB26ST"]

# Let's inspect ocr_results.json again, printing all lines from all pages
ocr_file = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\ocr_results.json"
with open(ocr_file, "r", encoding="utf-8") as f:
    ocr_results = json.load(f)

print(f"Loaded {len(ocr_results)} pages from ocr_results.json")
for item in ocr_results:
    p = item["page"]
    lines = item["raw_texts"]
    for l in lines:
        for t in ["5740", "2661", "5754", "574", "266", "575", "0574", "0266", "0575"]:
            if t in l:
                print(f"Page {p}: {l}")

print("\nLet's check 2 Piece or Coord set.pdf:")
coord_pdf = r"C:\Users\sande\Downloads\2 Piece or Coord set.pdf"
if os.path.exists(coord_pdf):
    cdoc = pymupdf.open(coord_pdf)
    print(f"Total pages in Coord set: {len(cdoc)}")
    for i in range(len(cdoc)):
        txt = cdoc[i].get_text()
        if txt.strip():
            print(f"Coord P{i+1}: {txt[:100]}")

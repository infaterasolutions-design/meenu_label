import pymupdf
import os
import io
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

results = []

for page_idx in range(len(doc)):
    page = doc[page_idx]
    images = doc.get_page_images(page_idx)
    if not images:
        continue
    xref = images[0][0]
    base_img = doc.extract_image(xref)
    img_bytes = base_img["image"]
    
    # Run OCR on image
    res, _ = ocr(img_bytes)
    texts = [item[1] for item in res] if res else []
    
    # Filter for relevant tags
    page_summary = {
        "page": page_idx + 1,
        "raw_texts": texts
    }
    results.append(page_summary)
    print(f"--- Page {page_idx + 1} ---")
    for t in texts:
        print("  ", t)

# Save results to a file for easy inspection
import json
with open(r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\ocr_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDone extracting all pages!")

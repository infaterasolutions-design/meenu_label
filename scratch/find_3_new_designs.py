import pymupdf
from rapidocr_onnxruntime import RapidOCR
import io
from PIL import Image

ocr = RapidOCR()
pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

targets = ["5740", "2661", "5754", "05740", "02661", "05754", "SS05740", "ST02661", "ST05754"]

print("Scanning all 47 pages of Selected catalog .pdf...")

for page_idx in range(len(doc)):
    page = doc[page_idx]
    # Render page at 2x resolution (144 dpi) for super crisp OCR
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    
    res, _ = ocr(img_bytes)
    if res:
        page_texts = [item[1] for item in res]
        full_page_str = " ".join(page_texts)
        for t in targets:
            if t.lower() in full_page_str.lower():
                print(f"*** FOUND TARGET '{t}' on Page {page_idx + 1}! ***")
                for item in res:
                    print("   ", item[1])
                print("---------------------------------------------")

print("Finished scanning.")

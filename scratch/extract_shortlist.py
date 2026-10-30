import pymupdf
import io
import os
from PIL import Image

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)
out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\shortlist"
os.makedirs(out_dir, exist_ok=True)

target_pages = [1, 4, 5, 9, 15, 16, 17, 21]

for p in target_pages:
    page_idx = p - 1
    images = doc.get_page_images(page_idx)
    if images:
        xref = images[0][0]
        base_img = doc.extract_image(xref)
        img = Image.open(io.BytesIO(base_img["image"]))
        img.thumbnail((700, 1500))
        img.save(os.path.join(out_dir, f"page_{p}.jpg"), quality=85)
        print(f"Saved page_{p}.jpg")

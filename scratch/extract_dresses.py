import pymupdf
import io
import os
from PIL import Image

doc = pymupdf.open(r"C:\Users\sande\Downloads\Selected catalog .pdf")
out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\dresses"
os.makedirs(out_dir, exist_ok=True)

dress_pages = [20, 22, 23, 24, 25, 39, 40]

for p in dress_pages:
    page_idx = p - 1
    images = doc.get_page_images(page_idx)
    if images:
        xref = images[0][0]
        base_img = doc.extract_image(xref)
        img = Image.open(io.BytesIO(base_img["image"]))
        img.thumbnail((700, 1500))
        img.save(os.path.join(out_dir, f"dress_page_{p}.jpg"), quality=85)
        print(f"Saved dress_page_{p}.jpg")

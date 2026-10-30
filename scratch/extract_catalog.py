import pymupdf
import os
from PIL import Image
import io

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)
print(f"Total pages: {len(doc)}")

out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\catalog_pages"
os.makedirs(out_dir, exist_ok=True)

# Let's extract first 5 pages and inspect
for i in range(min(5, len(doc))):
    page = doc[i]
    images = doc.get_page_images(i)
    if images:
        xref = images[0][0]
        base_img = doc.extract_image(xref)
        img_bytes = base_img["image"]
        img = Image.open(io.BytesIO(img_bytes))
        out_path = os.path.join(out_dir, f"page_{i+1}.jpg")
        # Save a scaled down version or inspect
        print(f"Page {i+1}: size={img.size}, mode={img.mode}")
        # Crop top left (where Design No / Fabric / Rate are)
        # Usually top left is 0 to 45% width, 0 to 45% height
        w, h = img.size
        crop_box = (0, 0, int(w * 0.45), int(h * 0.45))
        crop_img = img.crop(crop_box)
        crop_path = os.path.join(out_dir, f"crop_{i+1}.jpg")
        crop_img.save(crop_path, quality=85)

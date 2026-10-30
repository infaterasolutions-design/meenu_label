import pymupdf, io, os
from PIL import Image

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

highres_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\highres_products"
os.makedirs(highres_dir, exist_ok=True)

new_designs = [
    ("JAB26SS05740", 7, 0.21, 0.67), # Page 7: Festive Chanderi Sharara / Silk Set
    ("JAB25ST02661", 6, 0.21, 0.67), # Page 6: Festive Chanderi Straight Kurta Suit
    ("JAB26ST05754", 2, 0.21, 0.67), # Page 2: Royal Chanderi Straight Kurta Set with Organza Dupatta
]

for code, pno, y1, y2 in new_designs:
    imgs = doc.get_page_images(pno - 1)
    base = doc.extract_image(imgs[0][0])
    im = Image.open(io.BytesIO(base['image']))
    w, h = im.size
    crop_box = (int(w * 0.03), int(h * y1), int(w * 0.97), int(h * y2))
    cropped = im.crop(crop_box)
    target_path = os.path.join(highres_dir, f"{code}.jpg")
    cropped.save(target_path, "JPEG", quality=95)
    print(f"Saved {code}.jpg to highres_products -> Size: {cropped.size}")

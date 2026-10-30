import pymupdf, io, os
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\clean_crops"

candidates = [
    ('Page2_JAB26ST05104', 2, 0.21, 0.67),
    ('Page3_JAB26ST05278', 3, 0.21, 0.67),
    ('Page8_JAC26ST05086', 8, 0.21, 0.67),
]

for name, pno, y1, y2 in candidates:
    imgs = doc.get_page_images(pno - 1)
    base = doc.extract_image(imgs[0][0])
    im = Image.open(io.BytesIO(base['image']))
    w, h = im.size
    crop_box = (int(w * 0.03), int(h * y1), int(w * 0.97), int(h * y2))
    cropped = im.crop(crop_box)
    save_path = os.path.join(out_dir, f"{name}.jpg")
    cropped.save(save_path, "JPEG", quality=92)
    res, _ = ocr(save_path)
    ocr_texts = [item[1] for item in res] if res else []
    print(f"{name} -> Size: {cropped.size}, OCR Texts: {ocr_texts}")

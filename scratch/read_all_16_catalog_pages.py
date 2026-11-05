import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
pdf_path = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\.user_uploaded\media_1793397414118_5ae084ef.pdf'
doc = pymupdf.open(pdf_path)

print("=== ALL 16 PAGES OF THE OFFICIAL CATALOG ===")
for p_num in range(len(doc)):
    page = doc[p_num]
    xref = page.get_images()[0][0]
    base = doc.extract_image(xref)
    res, _ = ocr(base['image'])
    texts = [r[1] for r in res] if res else []
    print(f"Page {p_num+1:2d}: {' | '.join(texts)}")

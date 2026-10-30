import pymupdf
import os

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

for pno in [0, 1, 2, 5, 6, 7, 8, 9, 10]:
    imgs = doc.get_page_images(pno)
    print(f"Page {pno+1}: {len(imgs)} images")
    for img in imgs:
        xref = img[0]
        base = doc.extract_image(xref)
        w, h = base["width"], base["height"]
        print(f"   xref {xref}: {w}x{h}, format: {base['ext']}")

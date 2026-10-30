import os
import fitz # PyMuPDF

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = fitz.open(pdf_path)
print(f"Total Pages: {len(doc)}")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text().strip()
    if text:
        # Print first few lines of text
        clean_text = " | ".join(text.splitlines())
        print(f"Page {i+1}: {clean_text[:120]}")
    else:
        # Check images
        images = page.get_images()
        print(f"Page {i+1}: [Scanned/Image] {len(images)} images")

import pymupdf, os
from PIL import Image

pdf_path = r"C:\Users\sande\Downloads\Selected catalog .pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\inspect_new_candidates"
os.makedirs(out_dir, exist_ok=True)

# Let's render all pages from 1 to 47 to inspect them
for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    pix.save(os.path.join(out_dir, f"page_{i+1}.jpg"))

print(f"Rendered all {len(doc)} pages to {out_dir}")

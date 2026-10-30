import os, fitz # PyMuPDF

downloads = r"C:\Users\sande\Downloads"
targets = ["JAB26SS05740", "JAB25ST02661", "JAB26ST05754", "05740", "02661", "05754", "5740", "2661", "5754"]

pdf_files = [os.path.join(downloads, f) for f in os.listdir(downloads) if f.lower().endswith(".pdf")]

print(f"Scanning {len(pdf_files)} PDFs in Downloads...")

for pdf_path in pdf_files:
    try:
        doc = fitz.open(pdf_path)
        found = False
        for pno in range(len(doc)):
            page = doc[pno]
            text = page.get_text()
            for t in targets:
                if t.lower() in text.lower():
                    print(f"MATCH: '{t}' in '{os.path.basename(pdf_path)}' Page {pno+1}")
                    print(f"   Excerpt: {text.strip().replace(chr(10), ' ')[:160]}")
                    found = True
        if found:
            print("---")
    except Exception as e:
        pass

print("Scan complete.")

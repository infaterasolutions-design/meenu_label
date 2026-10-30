import os
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
img_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\inspect_new_candidates"

targets = ["5740", "2661", "5754", "05740", "02661", "05754", "JAB26SS", "JAB25ST", "JAB26ST"]

print("Analyzing all 47 rendered page images...")
all_labels = []

for pno in range(1, 48):
    fname = f"page_{pno}.jpg"
    p = os.path.join(img_dir, fname)
    if not os.path.exists(p):
        continue
    im = Image.open(p)
    W, H = im.size
    
    # We can run OCR on the whole image
    res, _ = ocr(p)
    if res:
        texts = [item[1] for item in res]
        for t in texts:
            # check if code-like
            if any(t.startswith(prefix) for prefix in ["JA", "JE", "SET", "TX", "ZA", "SL", "JN", "HD", "FU", "WSP"]):
                all_labels.append((pno, t))
            for tgt in ["5740", "2661", "5754", "574", "266", "575"]:
                if tgt in t:
                    print(f"Target match on Page {pno}: {t}")

print(f"\nTotal labels found: {len(all_labels)}")
for pno, l in all_labels:
    print(f"P{pno:2d}: {l}")

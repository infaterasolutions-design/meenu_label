import os
from PIL import Image

img_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\inspect_new_candidates"
out_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\inspect_labels"
os.makedirs(out_dir, exist_ok=True)

# For pages 1 to 15, let's crop the bottom 25% where the codes and tables are
for pno in range(1, 16):
    p = os.path.join(img_dir, f"page_{pno}.jpg")
    if os.path.exists(p):
        im = Image.open(p)
        w, h = im.size
        # crop bottom 30%
        bot = im.crop((0, int(h * 0.70), w, h))
        bot.save(os.path.join(out_dir, f"page_{pno}_bottom.jpg"))

print("Saved bottom crops for pages 1-15")

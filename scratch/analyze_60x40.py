import os
from PIL import Image, ImageDraw, ImageFont

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
user_photo_path = os.path.join(artifacts_dir, ".user_uploaded", "media_1793654201438_3a4af83f.jpg")
real_photo = Image.open(user_photo_path).convert("RGBA")

# Card coordinates in real photo:
# Card Left = 200, Right = 525 (Width = 325 px = 50.8 mm) -> 1 mm = 6.4 px
# Card Top = 268, Bottom = 815 (Height = 547 px = 88.9 mm) -> 1 mm = 6.15 px
# Hole bottom = y: 320
# Wash care line = y: 715

# Case 1: 60mm Wide x 40mm Tall (Overhang)
w1 = int(60 * 6.4)  # 384 px (wider than 325px card by 59px!)
h1 = int(40 * 6.15) # 246 px
x1 = 200 - (w1 - 325) // 2 # hangs off left by 30px!
y1 = 380

img1 = real_photo.copy()
d1 = ImageDraw.Draw(img1)
# Draw overhanging red outline box
d1.rectangle([x1, y1, x1 + w1, y1 + h1], outline=(239, 68, 68), width=3, fill=(255, 255, 255, 210))
d1.text((x1 + 15, y1 + 10), "60 mm Width is TOO WIDE!", fill=(220, 38, 38))
d1.text((x1 + 15, y1 + 35), "Overhangs card by 4.6 mm", fill=(180, 20, 20))

# Case 2: 40mm Wide x 60mm Tall (Tight Height)
w2 = int(40 * 6.4)  # 256 px
h2 = int(60 * 6.15) # 369 px
x2 = 200 + (325 - w2) // 2
y2 = 330 # starts right below hole, reaches y=699 (right at line!)

img2 = real_photo.copy()
d2 = ImageDraw.Draw(img2)
d2.rectangle([x2, y2, x2 + w2, y2 + h2], outline=(234, 179, 8), width=3, fill=(255, 255, 255, 210))
d2.text((x2 + 10, y2 + 10), "40 mm Wide x 60 mm Tall", fill=(161, 98, 7))
d2.text((x2 + 10, y2 + 35), "Height is tight (60 mm)", fill=(161, 98, 7))
d2.text((x2 + 10, y2 + 60), "Zero error margin!", fill=(200, 50, 0))

# Combine into comparison graphic
font_dir = r"C:\Windows\Fonts"
f_title = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 30)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 16)
f_col = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 20)

board = Image.new("RGB", (768 * 2 + 40, 1024 + 110), (20, 20, 23))
bdraw = ImageDraw.Draw(board)

bdraw.text((30, 20), "AMAZON 60×40 MM STICKER FIT ANALYSIS ON 2\"×3.5\" TAG", font=f_title, fill=(255, 255, 255))
bdraw.text((32, 60), "Check the roll orientation: 60 mm Width will hang off the edges; 40 mm Width x 60 mm Height is very tight vertically.", font=f_sub, fill=(180, 180, 180))

board.paste(img1.convert("RGB"), (15, 95))
bdraw.text((15 + 384, 1024 + 75), "IF 60 MM WIDE × 40 MM TALL (TOO WIDE - FAILS)", font=f_col, fill=(248, 113, 113), anchor="mt")

board.paste(img2.convert("RGB"), (768 + 25, 95))
bdraw.text((768 + 25 + 384, 1024 + 75), "IF 40 MM WIDE × 60 MM TALL (VERY TIGHT VERTICAL)", font=f_col, fill=(250, 204, 21), anchor="mt")

out_comp = os.path.join(artifacts_dir, "Meenu_60x40_Amazon_Analysis.png")
board.save(out_comp, "PNG")
board.save(r"C:\Users\sande\Downloads\Meenu_60x40_Amazon_Analysis.png", "PNG")
print("Saved Amazon 60x40 analysis to:", out_comp)

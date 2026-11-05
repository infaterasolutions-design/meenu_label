import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 1. Barcode Code 128 B encoder
CODE128_PATTERNS = [
    '212222', '222122', '222221', '121223', '121322', '131222', '122213', '122312', '132212', '221213',
    '221312', '231212', '112232', '122132', '122231', '113222', '123122', '123221', '223211', '221132',
    '221231', '213212', '223112', '312131', '311222', '321122', '321221', '312212', '322112', '322211',
    '212123', '212321', '232121', '111323', '131123', '131321', '112313', '132113', '132311', '211313',
    '231113', '231311', '112133', '112331', '132131', '113123', '113321', '133121', '313121', '211331',
    '231131', '213113', '213311', '213131', '311123', '311321', '331121', '312113', '312311', '332111',
    '314111', '221411', '431111', '111224', '111422', '121124', '121421', '141122', '141221', '112214',
    '112412', '122114', '122411', '142112', '142211', '241211', '221114', '413111', '241112', '134111',
    '111242', '121142', '121241', '114212', '124112', '124211', '411212', '421112', '421211', '212141',
    '214121', '412121', '111143', '111341', '131141', '114113', '114311', '411113', '411311', '113141',
    '114131', '311141', '411131', '211412', '211214', '211232', '2331112'
]

def draw_code128(draw, text, x_center, y_top, bar_height=44, module_width=2.1, font=None):
    indices = [ord(c) - 32 for c in text]
    checksum = (104 + sum((i + 1) * idx for i, idx in enumerate(indices))) % 103
    pattern_indices = [104] + indices + [checksum, 106]
    pattern = ''.join(CODE128_PATTERNS[idx] for idx in pattern_indices)
    
    total_modules = sum(int(digit) for digit in pattern)
    total_width = total_modules * module_width
    curr_x = x_center - (total_width / 2.0)
    
    is_bar = True
    for digit in pattern:
        w = int(digit) * module_width
        if is_bar:
            draw.rectangle([curr_x, y_top, curr_x + w, y_top + bar_height], fill=(0, 0, 0))
        curr_x += w
        is_bar = not is_bar
        
    if font:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text((x_center - tw // 2, y_top + bar_height + 4), text, font=font, fill=(30, 30, 30))
    return total_width, bar_height + (20 if font else 0)

# 2. Dimensions at 300 DPI
# 45 mm width x 52 mm height
DPI = 300
MM_TO_INCH = 1.0 / 25.4
LABEL_W = int(45 * MM_TO_INCH * DPI)  # 531 px
LABEL_H = int(52 * MM_TO_INCH * DPI)  # 614 px

font_dir = r"C:\Windows\Fonts"
f_regular = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 18)
f_semibold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 18)
f_mrp = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 30)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 14)
f_bc_text = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 16)
f_tiny = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 11)

def create_real_sticker():
    img = Image.new("RGBA", (LABEL_W, LABEL_H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer die-cut outline
    draw.rounded_rectangle([2, 2, LABEL_W-3, LABEL_H-3], radius=12, outline=(220, 220, 220), width=1)
    
    pad_x = 32
    y = 26
    
    specs = [
        ("PRODUCT", "KURTA SET"),
        ("STYLE NO.", "JAB26ST05010"),
        ("SIZE", "M  (Bust 96 cm)"),
        ("COLOR", "ROYAL WINE"),
        ("MATERIAL", "PURE CHANDERI SILK"),
        ("NET QTY", "1 SET (3 PCS)")
    ]
    
    col1_x = pad_x
    col2_x = pad_x + 120
    val_x = col2_x + 16
    
    for label, val in specs:
        draw.text((col1_x, y), label, font=f_regular, fill=(60, 60, 60))
        draw.text((col2_x, y), ":", font=f_semibold, fill=(60, 60, 60))
        draw.text((val_x, y), val, font=f_semibold, fill=(10, 10, 10))
        y += 28
        
    y += 8
    # Divider line 1
    draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 18
    
    # MRP
    mrp_str = "MRP : ₹ 2,799.00"
    bbox = draw.textbbox((0, 0), mrp_str, font=f_mrp)
    mrp_w = bbox[2] - bbox[0]
    draw.text(((LABEL_W - mrp_w) // 2, y), mrp_str, font=f_mrp, fill=(0, 0, 0))
    y += 36
    
    tax_str = "(Inclusive of all taxes)"
    bbox = draw.textbbox((0, 0), tax_str, font=f_sub)
    tax_w = bbox[2] - bbox[0]
    draw.text(((LABEL_W - tax_w) // 2, y), tax_str, font=f_sub, fill=(90, 90, 90))
    y += 24
    
    # Barcode
    sku_str = "JAB26ST05010-M"
    draw_code128(draw, sku_str, LABEL_W // 2, y, bar_height=48, module_width=2.1, font=f_bc_text)
    y += 82
    
    # Divider line 2
    draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 12
    
    # Legal microprint (cleanly fits in base)
    legal_lines = [
        "MFD & MKTD BY: MEENU LABEL, SECTOR 17, CHANDIGARH",
        "CUSTOMER CARE: care@meenulabel.com | +91 99888 98845",
        "COUNTRY OF ORIGIN: INDIA | PKD: 11/2026"
    ]
    for l in legal_lines:
        bbox = draw.textbbox((0, 0), l, font=f_tiny)
        lw = bbox[2] - bbox[0]
        draw.text(((LABEL_W - lw) // 2, y), l, font=f_tiny, fill=(110, 110, 110))
        y += 16
        
    return img

sticker = create_real_sticker()

# Save standalone sticker
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
out_sticker = os.path.join(artifacts_dir, "Meenu_Label_Real_Sticker_45x52mm.png")
sticker.save(out_sticker, "PNG", dpi=(300, 300))
sticker.save(r"C:\Users\sande\Downloads\Meenu_Label_Real_Sticker_45x52mm.png", "PNG", dpi=(300, 300))
print("Saved 45x52mm sticker to artifacts and Downloads!")

# 3. Paste onto User's Real Photo
user_photo_path = os.path.join(artifacts_dir, ".user_uploaded", "media_1793654201438_3a4af83f.jpg")
real_photo = Image.open(user_photo_path).convert("RGBA")

# Card coordinates in real photo:
# Card Left = 200, Right = 525 (Width = 325 px)
# Empty area top = below hole (y = 340)
# Empty area bottom = above wash care line (y = 698)
# Empty area height = 358 px
# Sticker aspect ratio = 531 / 614 = 0.865
# Sticker width on card = 325 * (45 mm / 50.8 mm) = 288 px
# Sticker height on card = 288 / 0.865 = 333 px

paste_w = 288
paste_h = 334
sticker_resized = sticker.resize((paste_w, paste_h), Image.Resampling.LANCZOS)

paste_x = 200 + (325 - paste_w) // 2  # centered on card: 218
paste_y = 345 # leaves 25px below hole, and 20px above wash care line!

# Apply soft shadow behind sticker
shadow = Image.new("RGBA", (paste_w + 12, paste_h + 12), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(shadow)
sdraw.rounded_rectangle([3, 3, paste_w + 9, paste_h + 9], radius=10, fill=(0, 0, 0, 30))
shadow = shadow.filter(ImageFilter.GaussianBlur(3))

# Composite onto photo
applied_photo = real_photo.copy()
applied_photo.paste(shadow, (paste_x - 6, paste_y - 6), shadow)
applied_photo.paste(sticker_resized, (paste_x, paste_y), sticker_resized)

# 4. Create Side-by-Side Comparison Board
# Left: Original photo (Before)
# Right: Photo with sticker applied (After)
orig_w, orig_h = real_photo.size
board_w = orig_w * 2 + 60
board_h = orig_h + 120

board = Image.new("RGB", (board_w, board_h), (24, 24, 27))
bdraw = ImageDraw.Draw(board)

f_bh = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 32)
f_bs = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 16)
f_col_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 22)

bdraw.text((30, 25), "MEENU LABEL  |  PHYSICAL HANG TAG CUSTOM LABEL FIT", font=f_bh, fill=(255, 255, 255))
bdraw.text((32, 68), "Custom 45 × 52 mm Barcode & Price Sticker Fits Perfectly Above Pre-Printed Wash Care Symbols", font=f_bs, fill=(180, 180, 180))

# Paste Original
board.paste(real_photo.convert("RGB"), (20, 100))
bdraw.text((20 + orig_w // 2, board_h - 15), "1. YOUR PHYSICAL TAG (EMPTY MIDDLE AREA)", font=f_col_title, fill=(200, 200, 200), anchor="mb")

# Paste Applied
board.paste(applied_photo.convert("RGB"), (orig_w + 40, 100))
bdraw.text((orig_w + 40 + orig_w // 2, board_h - 15), "2. WITH 45 × 52 MM STICKER APPLIED (100% RETAIL READY)", font=f_col_title, fill=(74, 222, 128), anchor="mb")

out_board = os.path.join(artifacts_dir, "Meenu_Real_HangTag_Fit_Comparison.png")
board.save(out_board, "PNG")
board.save(r"C:\Users\sande\Downloads\Meenu_Real_HangTag_Fit_Comparison.png", "PNG")
print(f"Saved comparison board to {out_board}")

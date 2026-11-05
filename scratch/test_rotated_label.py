import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Code 128 encoder
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

def draw_code128(draw, text, x_center, y_top, bar_height=48, module_width=1.9, font=None):
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

# Dimensions for 40 mm Wide x 60 mm Tall at 300 DPI
DPI = 300
MM_TO_INCH = 1.0 / 25.4
W_PX = int(40 * MM_TO_INCH * DPI)  # 472 px
H_PX = int(60 * MM_TO_INCH * DPI)  # 708 px

font_dir = r"C:\Windows\Fonts"
f_regular = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 17)
f_semibold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 17)
f_mrp = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 28)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 13)
f_bc_text = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 15)
f_tiny = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 10)

def create_40x60_label():
    img = Image.new("RGBA", (W_PX, H_PX), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rounded_rectangle([2, 2, W_PX-3, H_PX-3], radius=12, outline=(220, 220, 220), width=1)
    
    pad_x = 24
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
    col2_x = pad_x + 105
    val_x = col2_x + 14
    
    for label, val in specs:
        draw.text((col1_x, y), label, font=f_regular, fill=(60, 60, 60))
        draw.text((col2_x, y), ":", font=f_semibold, fill=(60, 60, 60))
        draw.text((val_x, y), val, font=f_semibold, fill=(10, 10, 10))
        y += 28
        
    y += 10
    draw.line([(pad_x, y), (W_PX - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 20
    
    # MRP
    mrp_str = "MRP : ₹ 2,799.00"
    bbox = draw.textbbox((0, 0), mrp_str, font=f_mrp)
    mrp_w = bbox[2] - bbox[0]
    draw.text(((W_PX - mrp_w) // 2, y), mrp_str, font=f_mrp, fill=(0, 0, 0))
    y += 36
    
    tax_str = "(Inclusive of all taxes)"
    bbox = draw.textbbox((0, 0), tax_str, font=f_sub)
    tax_w = bbox[2] - bbox[0]
    draw.text(((W_PX - tax_w) // 2, y), tax_str, font=f_sub, fill=(90, 90, 90))
    y += 26
    
    # Barcode
    sku_str = "JAB26ST05010-M"
    draw_code128(draw, sku_str, W_PX // 2, y, bar_height=52, module_width=1.9, font=f_bc_text)
    y += 88
    
    draw.line([(pad_x, y), (W_PX - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 14
    
    legal_lines = [
        "MFD & MKTD BY: MEENU LABEL, SECTOR 17, CHANDIGARH",
        "CUSTOMER CARE: care@meenulabel.com | +91 99888 98845",
        "COUNTRY OF ORIGIN: INDIA | PKD: 11/2026"
    ]
    for l in legal_lines:
        bbox = draw.textbbox((0, 0), l, font=f_tiny)
        lw = bbox[2] - bbox[0]
        draw.text(((W_PX - lw) // 2, y), l, font=f_tiny, fill=(110, 110, 110))
        y += 15
        
    return img

label_40x60 = create_40x60_label()

# Save upright 40x60
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
label_40x60.save(os.path.join(artifacts_dir, "Meenu_Label_40x60mm_Upright.png"), "PNG", dpi=(300, 300))
label_40x60.save(r"C:\Users\sande\Downloads\Meenu_Label_40x60mm_Upright.png", "PNG", dpi=(300, 300))

# Rotate 90 degrees clockwise for printing onto a 60mm (W) x 40mm (H) roll
label_rotated_60x40 = label_40x60.rotate(270, expand=True)
label_rotated_60x40.save(os.path.join(artifacts_dir, "Meenu_Label_60x40mm_Rotated_For_Print.png"), "PNG", dpi=(300, 300))
label_rotated_60x40.save(r"C:\Users\sande\Downloads\Meenu_Label_60x40mm_Rotated_For_Print.png", "PNG", dpi=(300, 300))
print("Saved both upright and 90-degree rotated print files!")

# Now paste the upright 40x60 sticker onto the user's REAL tag photo to verify the real fit!
user_photo_path = os.path.join(artifacts_dir, ".user_uploaded", "media_1793654201438_3a4af83f.jpg")
real_photo = Image.open(user_photo_path).convert("RGBA")

# In photo: Card width = 325 px = 50.8 mm -> 1 mm = 6.4 px
# 40 mm width on photo = 40 * 6.4 = 256 px
# 60 mm height on photo = 60 * 6.15 = 369 px

paste_w = 256
paste_h = 369
sticker_res = label_40x60.resize((paste_w, paste_h), Image.Resampling.LANCZOS)

paste_x = 200 + (325 - paste_w) // 2  # 234 (leaves 34px = 5.3mm on left and right!)
paste_y = 336 # starts 18px below hole, ends at 336+369 = 705 (leaves 10px above wash line!)

shadow = Image.new("RGBA", (paste_w + 12, paste_h + 12), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(shadow)
sdraw.rounded_rectangle([3, 3, paste_w + 9, paste_h + 9], radius=10, fill=(0, 0, 0, 30))
shadow = shadow.filter(ImageFilter.GaussianBlur(3))

applied_photo = real_photo.copy()
applied_photo.paste(shadow, (paste_x - 6, paste_y - 6), shadow)
applied_photo.paste(sticker_res, (paste_x, paste_y), sticker_res)

# Create 3-panel presentation:
# 1. Physical 60x40 roll printing (rotated)
# 2. Peeled & rotated into portrait (40x60)
# 3. Applied to user's real card
f_title = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 30)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 16)
f_col = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 20)
f_note = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 14)

board_w = 1750
board_h = 1180
board = Image.new("RGB", (board_w, board_h), (24, 24, 27))
bdraw = ImageDraw.Draw(board)

bdraw.text((40, 25), "ROTATE 90° STRATEGY: HOW 60×40 MM ROLL BECOMES A 40×60 MM TAG STICKER", font=f_title, fill=(255, 255, 255))
bdraw.text((42, 68), "By rotating the design 90 degrees before printing, the 60mm dimension becomes the height, and 40mm becomes the width!", font=f_sub, fill=(200, 200, 200))

# Left Box: The rotated print on 60x40 roll
bdraw.rectangle([40, 110, 850, 1120], fill=(35, 35, 40), outline=(50, 50, 55), width=1)
bdraw.text((70, 140), "STEP 1 & 2: PRINT ROTATED 90° ON 60×40 ROLL", font=f_col, fill=(250, 204, 21))
bdraw.text((70, 175), "Your printer feeds 60 mm wide x 40 mm tall paper. We print sideways:", font=f_note, fill=(180, 180, 180))

# Paste rotated label
rot_w, rot_h = label_rotated_60x40.size
scale = 0.8
rot_preview = label_rotated_60x40.resize((int(rot_w * scale), int(rot_h * scale)), Image.Resampling.LANCZOS)
board.paste(rot_preview, (90, 220))

bdraw.text((70, 650), "STEP 3: PEEL & APPLY VERTICALLY (40 MM W × 60 MM H)", font=f_col, fill=(96, 165, 250))
bdraw.text((70, 685), "Turn it upright in your hand before sticking onto the tag:", font=f_note, fill=(180, 180, 180))

upright_scale = 0.55
upright_preview = label_40x60.resize((int(W_PX * upright_scale), int(H_PX * upright_scale)), Image.Resampling.LANCZOS)
board.paste(upright_preview, (90, 725))

bdraw.text((380, 760), "Width on tag: 40 mm", font=f_col, fill=(255, 255, 255))
bdraw.text((380, 790), "• Leaves 5.4 mm safe borders on left/right", font=f_note, fill=(160, 160, 160))
bdraw.text((380, 815), "• 100% eliminates the 60 mm overhang!", font=f_note, fill=(74, 222, 128))

bdraw.text((380, 860), "Height on tag: 60 mm", font=f_col, fill=(255, 255, 255))
bdraw.text((380, 890), "• Starts right below punch hole", font=f_note, fill=(160, 160, 160))
bdraw.text((380, 915), "• Stops right above pre-printed wash care line", font=f_note, fill=(160, 160, 160))

# Right Box: Applied to user's real photo
bdraw.rectangle([880, 110, 1710, 1120], fill=(35, 35, 40), outline=(50, 50, 55), width=1)
bdraw.text((910, 140), "RESULT ON YOUR REAL PHYSICAL HANG TAG", font=f_col, fill=(74, 222, 128))
bdraw.text((910, 175), "Simulated using your exact photo in your hand:", font=f_note, fill=(180, 180, 180))

photo_scale = 0.86
photo_preview = applied_photo.convert("RGB").resize((int(768 * photo_scale), int(1024 * photo_scale)), Image.Resampling.LANCZOS)
board.paste(photo_preview, (940, 220))

out_rot_board = os.path.join(artifacts_dir, "Meenu_60x40_Rotate90_Real_Proof.png")
board.save(out_rot_board, "PNG")
board.save(r"C:\Users\sande\Downloads\Meenu_60x40_Rotate90_Real_Proof.png", "PNG")
print("Saved Rotated Strategy Proof board to:", out_rot_board)

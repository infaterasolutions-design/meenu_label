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

def draw_code128(draw, text, x_center, y_top, bar_height=42, module_width=2.2, font=None):
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
DPI = 300
MM_TO_INCH = 1.0 / 25.4
LABEL_W = int(45 * MM_TO_INCH * DPI)  # 531 px
LABEL_H = int(65 * MM_TO_INCH * DPI)  # 768 px

# Fonts
font_dir = r"C:\Windows\Fonts"
f_regular = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 17)
f_semibold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 17)
f_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 20)
f_mrp = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 28)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 13)
f_sub_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 13)
f_bc_text = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 15)
f_tiny = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 11)
f_icon_label = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 10)

def create_sticker_image():
    img = Image.new("RGBA", (LABEL_W, LABEL_H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Border (subtle die-cut line)
    draw.rounded_rectangle([2, 2, LABEL_W-3, LABEL_H-3], radius=14, outline=(215, 215, 215), width=1)
    
    pad_x = 32
    y = 26
    
    # Header specs
    specs = [
        ("PRODUCT", "KURTA SET"),
        ("STYLE NO.", "JAB26ST05010"),
        ("SIZE", "M  (Bust 96 cm)"),
        ("COLOR", "ROYAL WINE"),
        ("MATERIAL", "PURE CHANDERI SILK"),
        ("NET QTY", "1 SET (3 PCS)")
    ]
    
    col1_x = pad_x
    col2_x = pad_x + 115
    val_x = col2_x + 14
    
    for label, val in specs:
        draw.text((col1_x, y), label, font=f_regular, fill=(60, 60, 60))
        draw.text((col2_x, y), ":", font=f_semibold, fill=(60, 60, 60))
        draw.text((val_x, y), val, font=f_semibold, fill=(10, 10, 10))
        y += 27
        
    y += 6
    # Divider line 1
    draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 16
    
    # MRP
    mrp_str = "MRP : ₹ 2,799.00"
    bbox = draw.textbbox((0, 0), mrp_str, font=f_mrp)
    mrp_w = bbox[2] - bbox[0]
    draw.text(((LABEL_W - mrp_w) // 2, y), mrp_str, font=f_mrp, fill=(0, 0, 0))
    y += 34
    
    tax_str = "(Inclusive of all taxes)"
    bbox = draw.textbbox((0, 0), tax_str, font=f_sub)
    tax_w = bbox[2] - bbox[0]
    draw.text(((LABEL_W - tax_w) // 2, y), tax_str, font=f_sub, fill=(90, 90, 90))
    y += 24
    
    # Barcode
    sku_str = "JAB26ST05010-M"
    draw_code128(draw, sku_str, LABEL_W // 2, y, bar_height=42, module_width=2.1, font=f_bc_text)
    y += 72
    
    # Divider line 2
    draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 14
    
    # Wash care symbols
    icon_spacing = (LABEL_W - 2 * pad_x) // 4
    y_top = y
    
    # 1. Hand Wash
    ix1 = pad_x + icon_spacing // 2
    draw.polygon([(ix1-13, y_top+5), (ix1-9, y_top+18), (ix1+9, y_top+18), (ix1+13, y_top+5)], outline=(50, 50, 50), width=1)
    draw.line([(ix1-11, y_top+9), (ix1+11, y_top+9)], fill=(50, 50, 50), width=1)
    draw.line([(ix1+4, y_top-1), (ix1-1, y_top+8)], fill=(50, 50, 50), width=1)
    draw.text((ix1, y_top + 22), "HAND WASH", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # 2. Do Not Bleach
    ix2 = ix1 + icon_spacing
    draw.polygon([(ix2, y_top+1), (ix2-11, y_top+18), (ix2+11, y_top+18)], outline=(50, 50, 50), width=1)
    draw.line([(ix2-7, y_top+5), (ix2+7, y_top+17)], fill=(50, 50, 50), width=1)
    draw.line([(ix2+7, y_top+5), (ix2-7, y_top+17)], fill=(50, 50, 50), width=1)
    draw.text((ix2, y_top + 22), "DO NOT BLEACH", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # 3. Warm Iron
    ix3 = ix2 + icon_spacing
    draw.arc([(ix3-13, y_top+6), (ix3+13, y_top+20)], start=0, end=180, fill=(50, 50, 50), width=1)
    draw.line([(ix3-13, y_top+13), (ix3+11, y_top+13)], fill=(50, 50, 50), width=1)
    draw.line([(ix3-9, y_top+6), (ix3+4, y_top+6)], fill=(50, 50, 50), width=1)
    draw.ellipse([(ix3-4, y_top+9), (ix3-2, y_top+11)], fill=(50, 50, 50))
    draw.ellipse([(ix3+1, y_top+9), (ix3+3, y_top+11)], fill=(50, 50, 50))
    draw.text((ix3, y_top + 22), "WARM IRON", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # 4. Dry Clean
    ix4 = ix3 + icon_spacing
    draw.ellipse([(ix4-10, y_top+1), (ix4+10, y_top+19)], outline=(50, 50, 50), width=1)
    draw.text((ix4, y_top+4), "P", font=f_sub_bold, fill=(50, 50, 50), anchor="mt")
    draw.text((ix4, y_top + 22), "DRY CLEAN", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    y += 42
    # Divider line 3
    draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
    y += 10
    
    # Micro legal details
    legal_lines = [
        "MFD & MKTD BY: MEENU LABEL, SECTOR 17, CHANDIGARH",
        "CUSTOMER CARE: care@meenulabel.com | +91 99888 98845",
        "COUNTRY OF ORIGIN: INDIA | PKD: 11/2026"
    ]
    for l in legal_lines:
        bbox = draw.textbbox((0, 0), l, font=f_tiny)
        lw = bbox[2] - bbox[0]
        draw.text(((LABEL_W - lw) // 2, y), l, font=f_tiny, fill=(110, 110, 110))
        y += 15
        
    return img

sticker_img = create_sticker_image()

# Save sticker image
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
out_label = os.path.join(artifacts_dir, "Meenu_Label_45x65mm_Sticker.png")
sticker_img.save(out_label, "PNG", dpi=(300, 300))
sticker_img.save(r"C:\Users\sande\Downloads\Meenu_Label_45x65mm_Sticker.png", "PNG", dpi=(300, 300))
print("Saved 45x65mm sticker to artifacts and Downloads!")

# 3. Create Realistic 3D Mockup on 2" x 3.5" Hang Tag
TAG_W = int(2.0 * DPI)  # 600 px
TAG_H = int(3.5 * DPI)  # 1050 px

def create_tag_canvas():
    tag = Image.new("RGBA", (TAG_W, TAG_H), (252, 252, 252, 255))
    tdraw = ImageDraw.Draw(tag)
    # Card bevel / border
    tdraw.rectangle([0, 0, TAG_W-1, TAG_H-1], outline=(225, 225, 225), width=2)
    # Eyelet hole at top center
    hole_cx = TAG_W // 2
    hole_cy = 65
    hole_r = 16
    # Silver grommet ring
    tdraw.ellipse([hole_cx - hole_r - 6, hole_cy - hole_r - 6, hole_cx + hole_r + 6, hole_cy + hole_r + 6], outline=(170, 170, 170), width=4)
    # Hole center
    tdraw.ellipse([hole_cx - hole_r, hole_cy - hole_r, hole_cx + hole_r, hole_cy + hole_r], fill=(230, 230, 230))
    # String / black cord
    tdraw.line([(hole_cx, 0), (hole_cx, hole_cy)], fill=(30, 30, 30), width=8)
    return tag

# Tag Front
tag_front = create_tag_canvas()
fdraw = ImageDraw.Draw(tag_front)
# MEENU LABEL Logo on Front
f_logo = ImageFont.truetype(os.path.join(font_dir, "georgia.ttf"), 48)
f_logo_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 20)
f_tm = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 14)

logo_str = "MEENU"
bbox = fdraw.textbbox((0, 0), logo_str, font=f_logo)
lw = bbox[2] - bbox[0]
lx = (TAG_W - lw) // 2
ly = TAG_H // 2 - 30
fdraw.text((lx, ly), logo_str, font=f_logo, fill=(15, 15, 15))
fdraw.text((lx + lw + 4, ly + 2), "TM", font=f_tm, fill=(60, 60, 60))

sub_str = "L  A  B  E  L"
bbox = fdraw.textbbox((0, 0), sub_str, font=f_logo_sub)
sw = bbox[2] - bbox[0]
fdraw.text(((TAG_W - sw) // 2, ly + 62), sub_str, font=f_logo_sub, fill=(50, 50, 50))

# Tag Back (With 45x65mm sticker pasted on it)
tag_back = create_tag_canvas()
# Paste sticker on tag back
# Position: centered horizontally, placed 140px from top (leaving clearance for eyelet)
sticker_x = (TAG_W - LABEL_W) // 2
sticker_y = 150

# Subtle drop shadow for sticker on card
shadow = Image.new("RGBA", (LABEL_W + 16, LABEL_H + 16), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(shadow)
sdraw.rounded_rectangle([4, 4, LABEL_W + 12, LABEL_H + 12], radius=16, fill=(0, 0, 0, 25))
shadow = shadow.filter(ImageFilter.GaussianBlur(4))
tag_back.paste(shadow, (sticker_x - 8, sticker_y - 8), shadow)

# Paste the sticker
tag_back.paste(sticker_img, (sticker_x, sticker_y))

# 4. Compose Side-by-Side Presentation Board
CANVAS_W = 1600
CANVAS_H = 1250
board = Image.new("RGB", (CANVAS_W, CANVAS_H), (247, 246, 242)) # Warm luxury studio background
bdraw = ImageDraw.Draw(board)

# Header typography
f_header = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 38)
f_hsub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 18)
f_label_tag = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 20)
f_dim_label = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 15)

header_title = "MEENU LABEL  |  PHYSICAL HANG TAG SPECIFICATION"
bdraw.text((70, 50), header_title, font=f_header, fill=(25, 25, 25))
bdraw.text((72, 100), "Hang Tag Size: 2.0\" × 3.5\" (50.8 × 88.9 mm)   •   Back Sticker Label Size: 45 × 65 mm (1.77\" × 2.56\")", font=f_hsub, fill=(100, 100, 100))
bdraw.line([(70, 135), (CANVAS_W - 70, 135)], fill=(220, 218, 212), width=1)

# Place Front of Tag
# Add soft drop shadow behind tags
def paste_with_shadow(bg, fg, pos):
    fw, fh = fg.size
    sh = Image.new("RGBA", (fw + 40, fh + 40), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh)
    sdraw.rectangle([10, 10, fw + 30, fh + 30], fill=(0, 0, 0, 35))
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    bg.paste(sh, (pos[0] - 15, pos[1] - 15), sh)
    bg.paste(fg, pos)

# Positions
tag1_x = 130
tag1_y = 175
paste_with_shadow(board, tag_front, (tag1_x, tag1_y))

bdraw.text((tag1_x + TAG_W // 2, tag1_y + TAG_H + 20), "FRONT OF HANG TAG", font=f_label_tag, fill=(40, 40, 40), anchor="mt")
bdraw.text((tag1_x + TAG_W // 2, tag1_y + TAG_H + 46), "350 GSM Matte Laminated Card with Black Eyelet", font=f_dim_label, fill=(120, 120, 120), anchor="mt")

tag2_x = 870
tag2_y = 175
paste_with_shadow(board, tag_back, (tag2_x, tag2_y))

bdraw.text((tag2_x + TAG_W // 2, tag2_y + TAG_H + 20), "BACK OF HANG TAG (WITH 45×65 MM STICKER)", font=f_label_tag, fill=(40, 40, 40), anchor="mt")
bdraw.text((tag2_x + TAG_W // 2, tag2_y + TAG_H + 46), "Perfect 3 mm outer border margin • Leaves eyelet clearance", font=f_dim_label, fill=(120, 120, 120), anchor="mt")

# Annotations & Dimension lines
# Show 45mm width arrow
label_left = tag2_x + sticker_x
label_right = label_left + LABEL_W
annot_y = tag2_y + sticker_y + LABEL_H + 15
bdraw.line([(label_left, annot_y), (label_right, annot_y)], fill=(180, 100, 50), width=2)
bdraw.line([(label_left, annot_y - 6), (label_left, annot_y + 6)], fill=(180, 100, 50), width=2)
bdraw.line([(label_right, annot_y - 6), (label_right, annot_y + 6)], fill=(180, 100, 50), width=2)
bdraw.text(((label_left + label_right) // 2, annot_y + 12), "Sticker Width: 45 mm", font=f_dim_label, fill=(180, 100, 50), anchor="mt")

# Show 65mm height arrow
annot_x = label_right + 15
label_top = tag2_y + sticker_y
label_bottom = label_top + LABEL_H
bdraw.line([(annot_x, label_top), (annot_x, label_bottom)], fill=(180, 100, 50), width=2)
bdraw.line([(annot_x - 6, label_top), (annot_x + 6, label_top)], fill=(180, 100, 50), width=2)
bdraw.line([(annot_x - 6, label_bottom), (annot_x + 6, label_bottom)], fill=(180, 100, 50), width=2)
bdraw.text((annot_x + 10, (label_top + label_bottom) // 2), "65 mm", font=f_dim_label, fill=(180, 100, 50), anchor="lm")

out_mockup = os.path.join(artifacts_dir, "Meenu_HangTag_45x65mm_Mockup.png")
board.save(out_mockup, "PNG")
board.save(r"C:\Users\sande\Downloads\Meenu_HangTag_45x65mm_Mockup.png", "PNG")
print("Saved 3D Mockup board to artifacts and Downloads!")

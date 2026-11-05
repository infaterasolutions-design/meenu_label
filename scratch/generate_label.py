import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.graphics import renderPM

# Dimensions at 300 DPI
# 45 mm x 65 mm
DPI = 300
MM_TO_INCH = 1.0 / 25.4
LABEL_W = int(45 * MM_TO_INCH * DPI)  # 531 px
LABEL_H = int(65 * MM_TO_INCH * DPI)  # 768 px

print(f"Label Dimensions: {LABEL_W} x {LABEL_H} px at {DPI} DPI")

# Fonts
font_dir = r"C:\Windows\Fonts"
f_regular = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 18)
f_semibold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 18)
f_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 22)
f_mrp_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 30)
f_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 14)
f_sub_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 14)
f_tiny = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 12)
f_icon_label = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 11)

# Create crisp white canvas with subtle rounded corner boundary (like a die-cut sticker)
img = Image.new("RGBA", (LABEL_W, LABEL_H), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# Outer sticker border (very subtle hairline for cutting/peel preview)
draw.rounded_rectangle([1, 1, LABEL_W-2, LABEL_H-2], radius=12, outline=(220, 220, 220), width=1)

# Margins
pad_x = 32
y = 28

# 1. Product Spec Grid
specs = [
    ("PRODUCT", "3-PIECE FESTIVE SUIT"),
    ("STYLE NO.", "JAB26ST05010"),
    ("SIZE", "M  (Bust 96 cm)"),
    ("COLOR", "ROYAL WINE / MAROON"),
    ("FABRIC", "PURE CHANDERI SILK"),
    ("NET QTY", "1 SET (3 PCS)")
]

col1_x = pad_x
col2_x = pad_x + 130
val_x = col2_x + 16

for label, val in specs:
    draw.text((col1_x, y), label, font=f_regular, fill=(40, 40, 40))
    draw.text((col2_x, y), ":", font=f_semibold, fill=(40, 40, 40))
    draw.text((val_x, y), val, font=f_semibold, fill=(15, 15, 15))
    y += 28

y += 8
# Divider line
draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
y += 18

# 2. MRP Section (Centered or Bold Left)
mrp_text = "MRP : ₹ 2,799.00"
# Measure width of mrp text
bbox = draw.textbbox((0, 0), mrp_text, font=f_mrp_bold)
mrp_w = bbox[2] - bbox[0]
draw.text(((LABEL_W - mrp_w) // 2, y), mrp_text, font=f_mrp_bold, fill=(0, 0, 0))
y += 36

tax_text = "(Inclusive of all taxes)"
bbox = draw.textbbox((0, 0), tax_text, font=f_sub)
tax_w = bbox[2] - bbox[0]
draw.text(((LABEL_W - tax_w) // 2, y), tax_text, font=f_sub, fill=(100, 100, 100))
y += 24

# 3. Barcode (Code-128 via ReportLab rendered to image)
bc = code128.Code128("JAB26ST05010-M", barWidth=0.38*mm, barHeight=14*mm, humanReadable=True)
bc.fontName = 'Helvetica'
bc.fontSize = 8
bc_d = renderPM.drawToPIL(bc)
# Resize or crop bc_d cleanly
bc_w, bc_h = bc_d.size
bc_x = (LABEL_W - bc_w) // 2
img.paste(bc_d, (bc_x, y))
y += bc_h + 10

# Divider line
draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
y += 14

# 4. Wash Care Icons Section (Hand Drawn Vector Symbols)
def draw_wash_care(draw, x_center, y_top):
    # 4 icons: Hand Wash, Do Not Bleach, Warm Iron, Dry Clean
    icon_spacing = (LABEL_W - 2 * pad_x) // 4
    
    # Icon 1: Hand Wash
    ix1 = pad_x + icon_spacing // 2
    # Tub outline
    draw.polygon([(ix1-14, y_top+6), (ix1-10, y_top+20), (ix1+10, y_top+20), (ix1+14, y_top+6)], outline=(50, 50, 50), width=1)
    # Water line
    draw.line([(ix1-12, y_top+11), (ix1+12, y_top+11)], fill=(50, 50, 50), width=1)
    # Hand
    draw.line([(ix1+4, y_top-2), (ix1-1, y_top+10)], fill=(50, 50, 50), width=1)
    draw.text((ix1, y_top + 24), "HAND WASH", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # Icon 2: Do Not Bleach (Triangle with X)
    ix2 = ix1 + icon_spacing
    draw.polygon([(ix2, y_top+1), (ix2-12, y_top+20), (ix2+12, y_top+20)], outline=(50, 50, 50), width=1)
    draw.line([(ix2-8, y_top+5), (ix2+8, y_top+19)], fill=(50, 50, 50), width=1)
    draw.line([(ix2+8, y_top+5), (ix2-8, y_top+19)], fill=(50, 50, 50), width=1)
    draw.text((ix2, y_top + 24), "DO NOT BLEACH", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # Icon 3: Warm Iron
    ix3 = ix2 + icon_spacing
    # Iron shape
    draw.arc([(ix3-14, y_top+8), (ix3+14, y_top+22)], start=0, end=180, fill=(50, 50, 50), width=1)
    draw.line([(ix3-14, y_top+15), (ix3+12, y_top+15)], fill=(50, 50, 50), width=1)
    draw.line([(ix3-10, y_top+8), (ix3+4, y_top+8)], fill=(50, 50, 50), width=1)
    # 2 dots for warm iron
    draw.ellipse([(ix3-4, y_top+11), (ix3-2, y_top+13)], fill=(50, 50, 50))
    draw.ellipse([(ix3+1, y_top+11), (ix3+3, y_top+13)], fill=(50, 50, 50))
    draw.text((ix3, y_top + 24), "WARM IRON", font=f_icon_label, fill=(70, 70, 70), anchor="mt")
    
    # Icon 4: Dry Clean (P in circle)
    ix4 = ix3 + icon_spacing
    draw.ellipse([(ix4-11, y_top+2), (ix4+11, y_top+22)], outline=(50, 50, 50), width=1)
    draw.text((ix4, y_top+5), "P", font=f_sub_bold, fill=(50, 50, 50), anchor="mt")
    draw.text((ix4, y_top + 24), "DRY CLEAN", font=f_icon_label, fill=(70, 70, 70), anchor="mt")

draw_wash_care(draw, LABEL_W // 2, y)
y += 46

# Divider line
draw.line([(pad_x, y), (LABEL_W - pad_x, y)], fill=(200, 200, 200), width=1)
y += 12

# 5. Mandatory Indian Legal Metrology Details (Microprint at bottom)
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

# Save standalone high-res label
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
out_label = os.path.join(artifacts_dir, "Meenu_Label_45x65mm_Sticker.png")
img.save(out_label, "PNG", dpi=(300, 300))
print(f"Saved standalone label to {out_label}")

# Also copy to Downloads for user
dl_label = r"C:\Users\sande\Downloads\Meenu_Label_45x65mm_Sticker.png"
img.save(dl_label, "PNG", dpi=(300, 300))
print(f"Saved to Downloads: {dl_label}")

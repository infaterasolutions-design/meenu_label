import os
import io
import pymupdf
from PIL import Image, ImageDraw, ImageFont

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
os.makedirs(scratch_dir, exist_ok=True)
downloads_dir = r"C:\Users\sande\Downloads"

W, H = 1080, 1350
BG_COLOR = (250, 248, 245)      # Warm porcelain/ivory
BORDER_COLOR = (222, 214, 203)  # Soft taupe border
BORDER_INNER = (240, 235, 228)  # Subtle double border
TEXT_DARK = (30, 28, 25)        # Soft charcoal black
TEXT_MUTED = (135, 125, 112)    # Taupe bronze
TEXT_ACCENT = (80, 74, 66)      # Warm deep bronze
LINE_COLOR = (205, 195, 183)    # Accent line

# Fonts
font_brand = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 40)
font_title_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 36)
font_title_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 30)
font_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 28)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 26)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 22)
font_label = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 22)
font_label_bold = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 22)
font_card_title = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 20)
font_card_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 20)

def draw_tracked_caps(draw, text, y, font, fill, tracking=12):
    char_widths = [draw.textbbox((0, 0), c, font=font)[2] - draw.textbbox((0, 0), c, font=font)[0] for c in text]
    total_w = sum(char_widths) + (len(text) - 1) * tracking
    cur_x = (W - total_w) // 2
    for i, c in enumerate(text):
        draw.text((cur_x, y), c, font=font, fill=fill)
        cur_x += char_widths[i] + tracking

def draw_centered_text(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    cur_x = (W - text_w) // 2
    draw.text((cur_x, y), text, font=font, fill=fill)

doc = pymupdf.open(r"C:\Users\sande\Downloads\Selected catalog .pdf")

target_w, target_h = 920, 960

# =========================================================================
# 1. SOLO HERO: MUSTARD ANGRAKHA SET (SET974)
# =========================================================================
imgs4 = doc.get_page_images(3)
img4 = Image.open(io.BytesIO(doc.extract_image(imgs4[0][0])['image']))
crop_angrakha = img4.crop((15, 640, 1070, 1750)).resize((target_w, target_h), Image.Resampling.LANCZOS)

img_solo1 = Image.new("RGB", (W, H), BG_COLOR)
d_solo1 = ImageDraw.Draw(img_solo1)
d_solo1.rectangle([48, 48, W - 48, H - 48], outline=BORDER_COLOR, width=2)
d_solo1.rectangle([58, 58, W - 58, H - 58], outline=BORDER_INNER, width=1)

draw_tracked_caps(d_solo1, "M E E N U   L A B E L", 95, font_brand, TEXT_DARK, tracking=10)
draw_tracked_caps(d_solo1, "D R O P   0 1   •   D E B U T   C O L L E C T I O N", 148, font_label, TEXT_MUTED, tracking=6)

img_solo1.paste(crop_angrakha, (80, 195))
d_solo1.rectangle([80, 195, 80 + target_w, 195 + target_h], outline=BORDER_COLOR, width=2)

draw_centered_text(d_solo1, "The Mustard Angrakha Co-ord Set", 1175, font_title_huge, TEXT_DARK)
draw_centered_text(d_solo1, "Fluid Crepe Silk  •  Gold Gota Patti Wrap  •  Side Latkan Tassels", 1222, font_sub, TEXT_ACCENT)

badge_box = [(W//2 - 380, 1255), (W//2 + 380, 1298)]
d_solo1.rounded_rectangle(badge_box, radius=6, fill=(244, 240, 233), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d_solo1, "SIZES: M (38)  •  L (40)  •  XL (42)    |    MEENULABEL.COM", 1267, font_label_bold, TEXT_DARK, tracking=3)

img_solo1.save(os.path.join(scratch_dir, "post_solo_angrakha.png"), "PNG")
img_solo1.save(os.path.join(downloads_dir, "Meenu_Label_Post_Solo_Angrakha.png"), "PNG")

# =========================================================================
# 2. SOLO HERO: FESTIVE CHANDERI SUIT (JAB26ST05010)
# =========================================================================
imgs1 = doc.get_page_images(0)
img1 = Image.open(io.BytesIO(doc.extract_image(imgs1[0][0])['image']))
crop_chanderi = img1.crop((45, 655, 1125, 1775)).resize((target_w, target_h), Image.Resampling.LANCZOS)

img_solo2 = Image.new("RGB", (W, H), BG_COLOR)
d_solo2 = ImageDraw.Draw(img_solo2)
d_solo2.rectangle([48, 48, W - 48, H - 48], outline=BORDER_COLOR, width=2)
d_solo2.rectangle([58, 58, W - 58, H - 58], outline=BORDER_INNER, width=1)

draw_tracked_caps(d_solo2, "M E E N U   L A B E L", 95, font_brand, TEXT_DARK, tracking=10)
draw_tracked_caps(d_solo2, "T H E   F E S T I V E   E D I T   •   D R O P   0 1", 148, font_label, TEXT_MUTED, tracking=6)

img_solo2.paste(crop_chanderi, (80, 195))
d_solo2.rectangle([80, 195, 80 + target_w, 195 + target_h], outline=BORDER_COLOR, width=2)

draw_centered_text(d_solo2, "The Jaipur Chanderi Silk Suit", 1175, font_title_huge, TEXT_DARK)
draw_centered_text(d_solo2, "Delicate Zari V-Neck  •  Fuchsia Organza Dupatta  •  3-Piece Set", 1222, font_sub, TEXT_ACCENT)

d_solo2.rounded_rectangle(badge_box, radius=6, fill=(244, 240, 233), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d_solo2, "SIZES: M (38)  •  L (40)  •  XL (42)    |    MEENULABEL.COM", 1267, font_label_bold, TEXT_DARK, tracking=3)

img_solo2.save(os.path.join(scratch_dir, "post_solo_chanderi.png"), "PNG")
img_solo2.save(os.path.join(downloads_dir, "Meenu_Label_Post_Solo_Chanderi.png"), "PNG")

# =========================================================================
# 3. 3-IN-1 COLLECTION POST (All 3 Co-ords on ONE Screen, No Swipe!)
# =========================================================================
img_grid = Image.new("RGB", (W, H), BG_COLOR)
d_grid = ImageDraw.Draw(img_grid)

d_grid.rectangle([48, 48, W - 48, H - 48], outline=BORDER_COLOR, width=2)
d_grid.rectangle([58, 58, W - 58, H - 58], outline=BORDER_INNER, width=1)

draw_tracked_caps(d_grid, "M E E N U   L A B E L", 90, font_brand, TEXT_DARK, tracking=10)
draw_tracked_caps(d_grid, "T H E   C O - O R D   E D I T   •   D R O P   0 1", 142, font_label, TEXT_MUTED, tracking=6)

card_w3, card_h3 = 280, 730
y3_img = 195
xs3 = [74, 400, 726]

crop_g1 = img4.crop((181, 650, 879, 1760)).resize((card_w3, card_h3), Image.Resampling.LANCZOS)

imgs16 = doc.get_page_images(15)
img16 = Image.open(io.BytesIO(doc.extract_image(imgs16[0][0])['image']))
crop_g2 = img16.crop((243, 640, 927, 1730)).resize((card_w3, card_h3), Image.Resampling.LANCZOS)

imgs17 = doc.get_page_images(16)
img17 = Image.open(io.BytesIO(doc.extract_image(imgs17[0][0])['image']))
crop_g3 = img17.crop((243, 590, 927, 1680)).resize((card_w3, card_h3), Image.Resampling.LANCZOS)

grid_items = [
    (crop_g1, "THE ANGRAKHA", "Crepe Silk 2-Pc", "Warm Mustard"),
    (crop_g2, "THE HALTER", "Dobby Chiffon 2-Pc", "Lime Chartreuse"),
    (crop_g3, "THE TUNIC SET", "Cotton Blend 2-Pc", "Porcelain Ivory"),
]

for idx, (img_c, title, cat_txt, col_txt) in enumerate(grid_items):
    cx = xs3[idx]
    img_grid.paste(img_c, (cx, y3_img))
    d_grid.rectangle([cx, y3_img, cx + card_w3, y3_img + card_h3], outline=BORDER_COLOR, width=2)
    
    ty = y3_img + card_h3 + 18
    tb = d_grid.textbbox((0, 0), title, font=font_card_title)
    d_grid.text((cx + (card_w3 - (tb[2]-tb[0]))//2, ty), title, font=font_card_title, fill=TEXT_DARK)
    
    cb = d_grid.textbbox((0, 0), cat_txt, font=font_card_sub)
    d_grid.text((cx + (card_w3 - (cb[2]-cb[0]))//2, ty + 26), cat_txt, font=font_card_sub, fill=TEXT_ACCENT)

    clb = d_grid.textbbox((0, 0), col_txt, font=font_sub)
    d_grid.text((cx + (card_w3 - (clb[2]-clb[0]))//2, ty + 50), col_txt, font=font_sub, fill=TEXT_MUTED)

d_grid.line([(W//2 - 60, 1070), (W//2 + 60, 1070)], fill=LINE_COLOR, width=2)
draw_centered_text(d_grid, "Zero-Effort Dressing for Work, Travel & Festive Brunches", 1105, font_italic, TEXT_ACCENT)

badge_box2 = [(W//2 - 380, 1170), (W//2 + 380, 1220)]
d_grid.rounded_rectangle(badge_box2, radius=6, fill=(244, 240, 233), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d_grid, "SIZES: M (38)  •  L (40)  •  XL (42)  |  ONLY 3 PCS PER SIZE", 1184, font_label_bold, TEXT_DARK, tracking=2)

draw_tracked_caps(d_grid, "E X C L U S I V E L Y   A T   M E E N U L A B E L . C O M", 1260, font_label_bold, TEXT_DARK, tracking=4)

img_grid.save(os.path.join(scratch_dir, "post_3in1_lookbook.png"), "PNG")
img_grid.save(os.path.join(downloads_dir, "Meenu_Label_Post_3in1_Lookbook.png"), "PNG")

print("SUCCESS: Generated Solo Angrakha, Solo Chanderi, and 3-in-1 Lookbook with meenulabel.com!")

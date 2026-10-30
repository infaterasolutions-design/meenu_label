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
font_serif_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 62)
font_serif_medium = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 46)
font_serif_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 34)
font_serif_italic_small = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 26)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 28)
font_body_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 30)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 24)
font_sub_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 24)
font_label = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 22)
font_card_title = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 20)
font_card_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 22)

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

def draw_base_frame(draw, slide_num_str):
    draw.rectangle([56, 56, W - 56, H - 56], outline=BORDER_COLOR, width=2)
    draw.rectangle([68, 68, W - 68, H - 68], outline=BORDER_INNER, width=1)
    draw_tracked_caps(draw, slide_num_str, 1220, font_label, TEXT_MUTED, tracking=6)

# ==================== SLIDE 1: Cover ====================
img1 = Image.new("RGB", (W, H), BG_COLOR)
d1 = ImageDraw.Draw(img1)
draw_base_frame(d1, "01 / 03  —  SWIPE  →")
draw_tracked_caps(d1, "M E E N U   L A B E L   •   D R O P   0 1", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d1, "ANNOUNCING OUR DEBUT CAPSULE", 420, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d1, "13 Silhouettes.", 480, font_serif_huge, TEXT_DARK)
draw_centered_text(d1, "Endless Elegance.", 555, font_serif_italic, TEXT_ACCENT)

d1.line([(W//2 - 60, 640), (W//2 + 60, 640)], fill=LINE_COLOR, width=2)

draw_centered_text(d1, "From featherlight festive Chanderi to effortless", 700, font_serif_italic_small, TEXT_ACCENT)
draw_centered_text(d1, "georgette wrap dresses and modern co-ords.", 740, font_serif_italic_small, TEXT_ACCENT)

draw_centered_text(d1, "Hand-curated for the woman who values timeless grace.", 810, font_body, TEXT_MUTED)

draw_tracked_caps(d1, "STRICTLY LIMITED BATCH  •  SIZES M, L, XL", 1060, font_sub_bold, TEXT_DARK, tracking=6)

img1.save(os.path.join(scratch_dir, "post4_slide1.png"), "PNG")
img1.save(os.path.join(downloads_dir, "Meenu_Label_Post4_Slide_1.png"), "PNG")

# ==================== SLIDE 2: Lineup Lookbook ====================
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_base_frame(d2, "02 / 03  —  SWIPE  →")
draw_tracked_caps(d2, "M E E N U   L A B E L   •   T H E   L I N E U P", 140, font_label, TEXT_MUTED, tracking=6)
draw_centered_text(d2, "Three Signature Moods", 200, font_serif_medium, TEXT_DARK)
draw_centered_text(d2, "A first look into our 13 debut silhouettes", 260, font_serif_italic_small, TEXT_MUTED)

# Load 3 exact authentic catalog photos with full heads and natural proportions
path_c1 = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\final_clean_1.jpg"
path_c2 = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\final_clean_2.jpg"
path_c3 = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\final_clean_3.jpg"

crop1 = Image.open(path_c1)
crop2 = Image.open(path_c2)
crop3 = Image.open(path_c3)

card_w, card_h = 264, 420
y_img = 330
card_xs = [96, 408, 720]

cards = [
    (crop1, "THE FESTIVE SUIT", "Chanderi Silk 3-Pc", "Yellow & Rose Gold"),
    (crop2, "THE MODERN SET", "Crepe Angrakha 2-Pc", "Warm Mustard Silk"),
    (crop3, "THE WRAP DRESS", "Georgette Midi", "White Porcelain Blue"),
]

for idx, (img_c, title, cat_txt, col_txt) in enumerate(cards):
    cx = card_xs[idx]
    
    # Paste natural aspect ratio authentic catalog image
    img2.paste(img_c, (cx, y_img))
    
    # Elegant border around image
    d2.rectangle([cx, y_img, cx + card_w, y_img + card_h], outline=BORDER_COLOR, width=2)
    
    # Text below image
    ty = y_img + card_h + 24
    
    # Center title in card column
    tb = d2.textbbox((0, 0), title, font=font_card_title)
    d2.text((cx + (card_w - (tb[2]-tb[0]))//2, ty), title, font=font_card_title, fill=TEXT_DARK)
    
    cb = d2.textbbox((0, 0), cat_txt, font=font_card_sub)
    d2.text((cx + (card_w - (cb[2]-cb[0]))//2, ty + 28), cat_txt, font=font_card_sub, fill=TEXT_ACCENT)

    clb = d2.textbbox((0, 0), col_txt, font=font_sub)
    d2.text((cx + (card_w - (clb[2]-clb[0]))//2, ty + 56), col_txt, font=font_sub, fill=TEXT_MUTED)

# Line below cards
d2.line([(W//2 - 60, 920), (W//2 + 60, 920)], fill=LINE_COLOR, width=2)

draw_centered_text(d2, "Plus 10 more curated silhouettes in lightweight cottons, crepes & chiffons.", 960, font_body, TEXT_ACCENT)
draw_tracked_caps(d2, "EXPLORE OUR CAPSULE PHILOSOPHY", 1060, font_label, TEXT_MUTED, tracking=6)

img2.save(os.path.join(scratch_dir, "post4_slide2.png"), "PNG")
img2.save(os.path.join(downloads_dir, "Meenu_Label_Post4_Slide_2.png"), "PNG")

# ==================== SLIDE 3: Limited Edition & CTA ====================
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_base_frame(d3, "03 / 03  •  MEENULABEL.IN")
draw_tracked_caps(d3, "M E E N U   L A B E L   •   T H E   D R O P", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d3, "A NOTE ON OUR PRODUCTION", 380, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d3, "Curated for Quality,", 440, font_serif_huge, TEXT_DARK)
draw_centered_text(d3, "Not Mass Production.", 515, font_serif_italic, TEXT_ACCENT)

d3.line([(W//2 - 60, 600), (W//2 + 60, 600)], fill=LINE_COLOR, width=2)

draw_centered_text(d3, "To honor thoughtful craftsmanship and ensure zero excess waste,", 660, font_body, TEXT_DARK)
draw_centered_text(d3, "each design in Drop 01 is created in an ultra-limited batch of", 705, font_body, TEXT_DARK)
draw_centered_text(d3, "just 3 pieces per size across Medium, Large, and XL.", 750, font_body_bold, TEXT_ACCENT)
draw_centered_text(d3, "Once a silhouette finds its home, it will not be restocked.", 810, font_serif_italic_small, TEXT_MUTED)

# Size badge (widened and centered)
badge_box = [(W//2 - 340, 890), (W//2 + 340, 950)]
d3.rounded_rectangle(badge_box, radius=8, fill=(244, 240, 233), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d3, "AVAILABLE IN SIZES:  M (38)   •   L (40)   •   XL (42)", 912, font_label, TEXT_DARK, tracking=3)

# CTA button
pill_box = [(W//2 - 240, 990), (W//2 + 240, 1060)]
d3.rounded_rectangle(pill_box, radius=8, fill=TEXT_DARK)
draw_tracked_caps(d3, "TURN ON POST NOTIFICATIONS", 1014, font_label, (250, 248, 245), tracking=4)

draw_centered_text(d3, "Dropping Soon on meenulabel.in  •  Chandigarh, India", 1110, font_sub, TEXT_MUTED)

img3.save(os.path.join(scratch_dir, "post4_slide3.png"), "PNG")
img3.save(os.path.join(downloads_dir, "Meenu_Label_Post4_Slide_3.png"), "PNG")

print("SUCCESS: Post 4 Carousel Generated!")

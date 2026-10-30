import os
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
font_serif_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 58)
font_serif_medium = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 44)
font_serif_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 36)
font_serif_italic_small = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 26)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 28)
font_body_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 28)
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
draw_tracked_caps(d1, "M E E N U   L A B E L   •   T H E   C O - O R D   E D I T", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d1, "AUTUMN / FESTIVE '26", 420, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d1, "Zero-Effort Dressing.", 480, font_serif_huge, TEXT_DARK)
draw_centered_text(d1, "The Modern Co-ord Collection", 555, font_serif_italic, TEXT_ACCENT)

d1.line([(W//2 - 60, 640), (W//2 + 60, 640)], fill=LINE_COLOR, width=2)

draw_centered_text(d1, "Tailored matching sets designed to take you from", 700, font_serif_italic_small, TEXT_ACCENT)
draw_centered_text(d1, "morning meetings to intimate festive dinners with effortless ease.", 740, font_serif_italic_small, TEXT_ACCENT)

draw_centered_text(d1, "No styling guesswork. Just pure comfort and timeless drape.", 810, font_body, TEXT_MUTED)

draw_tracked_caps(d1, "EXPLORE THE 3 SIGNATURE SILHOUETTES", 1060, font_sub_bold, TEXT_DARK, tracking=6)

img1.save(os.path.join(scratch_dir, "post5_slide1.png"), "PNG")
img1.save(os.path.join(downloads_dir, "Meenu_Label_Post5_Slide_1.png"), "PNG")

# ==================== SLIDE 2: The 3 Co-ord Sets ====================
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_base_frame(d2, "02 / 03  —  SWIPE  →")
draw_tracked_caps(d2, "M E E N U   L A B E L   •   T H R E E   S E T S", 140, font_label, TEXT_MUTED, tracking=6)
draw_centered_text(d2, "Matching Sets for Every Mood", 200, font_serif_medium, TEXT_DARK)
draw_centered_text(d2, "Breathable fabrics, flattering drapes, zero fuss", 260, font_serif_italic_small, TEXT_MUTED)

# Load the 3 authentic catalog crops
c1 = Image.open(os.path.join(scratch_dir, "coord_card_1.jpg"))
c2 = Image.open(os.path.join(scratch_dir, "coord_card_2.jpg"))
c3 = Image.open(os.path.join(scratch_dir, "coord_card_3.jpg"))

card_w, card_h = 264, 420
y_img = 330
card_xs = [96, 408, 720]

cards = [
    (c1, "THE WRAP ANGRAKHA", "Crepe Silk 2-Pc", "Warm Mustard"),
    (c2, "THE PLEATED HALTER", "Dobby Chiffon 2-Pc", "Lime Chartreuse"),
    (c3, "THE GEOMETRIC TUNIC", "Cotton Blend 2-Pc", "Porcelain Ivory"),
]

for idx, (img_c, title, cat_txt, col_txt) in enumerate(cards):
    cx = card_xs[idx]
    img2.paste(img_c, (cx, y_img))
    d2.rectangle([cx, y_img, cx + card_w, y_img + card_h], outline=BORDER_COLOR, width=2)
    
    ty = y_img + card_h + 24
    tb = d2.textbbox((0, 0), title, font=font_card_title)
    d2.text((cx + (card_w - (tb[2]-tb[0]))//2, ty), title, font=font_card_title, fill=TEXT_DARK)
    
    cb = d2.textbbox((0, 0), cat_txt, font=font_card_sub)
    d2.text((cx + (card_w - (cb[2]-cb[0]))//2, ty + 28), cat_txt, font=font_card_sub, fill=TEXT_ACCENT)

    clb = d2.textbbox((0, 0), col_txt, font=font_sub)
    d2.text((cx + (card_w - (clb[2]-clb[0]))//2, ty + 56), col_txt, font=font_sub, fill=TEXT_MUTED)

d2.line([(W//2 - 60, 920), (W//2 + 60, 920)], fill=LINE_COLOR, width=2)

draw_centered_text(d2, "Tailored in fluid crepes, textured chiffons & breathable cotton blends.", 960, font_body, TEXT_ACCENT)
draw_tracked_caps(d2, "HOW TO STYLE YOUR CO-ORDS", 1060, font_label, TEXT_MUTED, tracking=6)

img2.save(os.path.join(scratch_dir, "post5_slide2.png"), "PNG")
img2.save(os.path.join(downloads_dir, "Meenu_Label_Post5_Slide_2.png"), "PNG")

# ==================== SLIDE 3: Versatility & Sizes ====================
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_base_frame(d3, "03 / 03  •  MEENULABEL.IN")
draw_tracked_caps(d3, "M E E N U   L A B E L   •   T H E   V E R S A T I L I T Y", 140, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d3, "HOW TO WEAR THEM", 230, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d3, "One Set. Endless Occasions.", 280, font_serif_medium, TEXT_DARK)

d3.line([(W//2 - 60, 360), (W//2 + 60, 360)], fill=LINE_COLOR, width=2)

# 3 Styling Benefits
benefits = [
    ("01. WEAR TOGETHER", "Instant, head-to-toe elegance for cafe brunches, festive poojas, or workdays. Zero decision fatigue."),
    ("02. SEPARATE & REMIX", "Pair the tunics with classic denim or cigarette trousers; style the palazzos with a crisp white shirt."),
    ("03. TAILORED FOR BREATHABILITY", "Lightweight fabrics crafted specifically for Indian climates with relaxed, flattering cuts that move with you."),
]

y_ben = 420
for b_title, b_desc in benefits:
    d3.text((120, y_ben), b_title, font=font_body_bold, fill=TEXT_DARK)
    
    # Simple word wrap for description
    words = b_desc.split()
    line = ""
    lines = []
    for w in words:
        test = line + (" " if line else "") + w
        if d3.textbbox((0, 0), test, font=font_sub)[2] < 840:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    
    y_l = y_ben + 36
    for l in lines:
        d3.text((120, y_l), l, font=font_sub, fill=TEXT_ACCENT)
        y_l += 28
    
    d3.line([(120, y_l + 16), (W - 120, y_l + 16)], fill=(235, 230, 222), width=1)
    y_ben = y_l + 38

# Size Badge
badge_box = [(W//2 - 340, 890), (W//2 + 340, 950)]
d3.rounded_rectangle(badge_box, radius=8, fill=(244, 240, 233), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d3, "AVAILABLE IN SIZES:  M (38)   •   L (40)   •   XL (42)", 912, font_label, TEXT_DARK, tracking=3)

# CTA button
pill_box = [(W//2 - 240, 985), (W//2 + 240, 1055)]
d3.rounded_rectangle(pill_box, radius=8, fill=TEXT_DARK)
draw_tracked_caps(d3, "SAVE & TURN ON NOTIFICATIONS", 1009, font_label, (250, 248, 245), tracking=4)

draw_centered_text(d3, "Strictly Limited Edition  •  Only 3 pieces per size", 1090, font_sub_bold, TEXT_ACCENT)
draw_centered_text(d3, "meenulabel.in  •  Chandigarh, India", 1125, font_sub, TEXT_MUTED)

img3.save(os.path.join(scratch_dir, "post5_slide3.png"), "PNG")
img3.save(os.path.join(downloads_dir, "Meenu_Label_Post5_Slide_3.png"), "PNG")

print("SUCCESS: Post 5 Carousel Generated!")

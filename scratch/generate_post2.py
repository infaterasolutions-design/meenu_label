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
font_serif_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 62)
font_serif_medium = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 46)
font_serif_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 34)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 28)
font_body_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 30)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 26)
font_label = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 22)

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

# ==================== SLIDE 1 ====================
img1 = Image.new("RGB", (W, H), BG_COLOR)
d1 = ImageDraw.Draw(img1)
draw_base_frame(d1, "01 / 03  —  SWIPE  →")
draw_tracked_caps(d1, "M E E N U   L A B E L   •   D E S I G N   N O T E S", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d1, "THE ANATOMY OF", 460, font_label, TEXT_MUTED, tracking=10)
draw_centered_text(d1, "A Modern Co-ord", 520, font_serif_huge, TEXT_DARK)

d1.line([(W//2 - 60, 630), (W//2 + 60, 630)], fill=LINE_COLOR, width=2)

draw_centered_text(d1, "Designed for all-day comfort.", 680, font_serif_italic, TEXT_ACCENT)
draw_centered_text(d1, "Tailored with effortless grace.", 735, font_serif_italic, TEXT_ACCENT)

draw_tracked_caps(d1, "WHAT MAKES OUR PIECES DIFFERENT", 1080, font_sub, TEXT_DARK, tracking=8)

img1.save(os.path.join(scratch_dir, "post2_slide1.png"), "PNG")
img1.save(os.path.join(downloads_dir, "Meenu_Label_Post2_Slide_1.png"), "PNG")

# ==================== SLIDE 2 ====================
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_base_frame(d2, "02 / 03  —  SWIPE  →")
draw_tracked_caps(d2, "MEENU LABEL  •  CRAFT & DETAILS", 160, font_label, TEXT_MUTED, tracking=6)

# Pillar 1
draw_centered_text(d2, "01. PURE BREATHABLE TEXTILES", 380, font_body_bold, TEXT_DARK)
draw_centered_text(d2, "Rich khadi cottons & soft muslins that breathe.", 425, font_body, TEXT_ACCENT)
draw_centered_text(d2, "Zero synthetic friction. All-day featherlight wear.", 465, font_sub, TEXT_MUTED)

d2.line([(W//2 - 40, 530), (W//2 + 40, 530)], fill=LINE_COLOR, width=1)

# Pillar 2
draw_centered_text(d2, "02. THOUGHTFUL TAILORING", 590, font_body_bold, TEXT_DARK)
draw_centered_text(d2, "Deep functional pockets on every bottom.", 635, font_body, TEXT_ACCENT)
draw_centered_text(d2, "Modest tunic hemlines with relaxed comfort waistbands.", 675, font_sub, TEXT_MUTED)

d2.line([(W//2 - 40, 740), (W//2 + 40, 740)], fill=LINE_COLOR, width=1)

# Pillar 3
draw_centered_text(d2, "03. DAY-TO-EVENING VERSATILITY", 800, font_body_bold, TEXT_DARK)
draw_centered_text(d2, "From morning cafe work to intimate festive dinners.", 845, font_body, TEXT_ACCENT)
draw_centered_text(d2, "Pairs seamlessly with flat juttis or elevated heels.", 885, font_sub, TEXT_MUTED)

img2.save(os.path.join(scratch_dir, "post2_slide2.png"), "PNG")
img2.save(os.path.join(downloads_dir, "Meenu_Label_Post2_Slide_2.png"), "PNG")

# ==================== SLIDE 3 ====================
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_base_frame(d3, "03 / 03  •  MEENULABEL.IN")
draw_tracked_caps(d3, "MEENU LABEL  •  FIRST DROP", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d3, "EXCLUSIVELY LAUNCHING", 420, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d3, "OCTOBER 31", 485, font_serif_huge, TEXT_DARK)

d3.line([(W//2 - 60, 600), (W//2 + 60, 600)], fill=LINE_COLOR, width=2)

draw_centered_text(d3, "Our first small-batch drop is limited in units.", 660, font_serif_italic, TEXT_ACCENT)
draw_tracked_caps(d3, "CHANDIGARH  •  DELIVERING ACROSS INDIA", 725, font_label, TEXT_MUTED, tracking=4)

# CTA button/pill
pill_box = [(W//2 - 250, 860), (W//2 + 250, 935)]
d3.rounded_rectangle(pill_box, radius=8, fill=(242, 237, 230), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d3, "TAP LINK IN BIO FOR VIP ACCESS", 882, font_label, TEXT_DARK, tracking=4)

draw_centered_text(d3, "Turn on notifications to be first when the drop goes live", 975, font_sub, TEXT_MUTED)

img3.save(os.path.join(scratch_dir, "post2_slide3.png"), "PNG")
img3.save(os.path.join(downloads_dir, "Meenu_Label_Post2_Slide_3.png"), "PNG")

print("SUCCESS: Post 2 slides created!")

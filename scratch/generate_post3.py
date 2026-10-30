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

# Swatch colors
COLOR_IVORY = (238, 232, 220)   # Porcelain Ivory
COLOR_SAGE = (128, 138, 112)    # Botanical Sage
COLOR_RUST = (166, 92, 70)      # Warm Terracotta/Rust

# Fonts
font_serif_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 60)
font_serif_date = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 52)
font_serif_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 34)
font_body_bold = ImageFont.truetype(r"C:\Windows\Fonts\GARABD.TTF", 30)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 26)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 24)
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
draw_tracked_caps(d1, "M E E N U   L A B E L   •   C O L O R   S T O R Y", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d1, "AUTUMN / FESTIVE '26", 450, font_label, TEXT_MUTED, tracking=10)
draw_centered_text(d1, "The Palette of Drop 01", 515, font_serif_huge, TEXT_DARK)

d1.line([(W//2 - 60, 625), (W//2 + 60, 625)], fill=LINE_COLOR, width=2)

draw_centered_text(d1, "Earthy botanicals, sunlit ivories,", 675, font_serif_italic, TEXT_ACCENT)
draw_centered_text(d1, "and timeless festive neutrals.", 725, font_serif_italic, TEXT_ACCENT)

# Swatch row preview
swatch_w, swatch_h = 44, 44
gap = 24
total_swatch_w = (3 * swatch_w) + (2 * gap)
start_x = (W - total_swatch_w) // 2
colors = [COLOR_IVORY, COLOR_SAGE, COLOR_RUST]
for i, col in enumerate(colors):
    sx = start_x + i * (swatch_w + gap)
    d1.rounded_rectangle([sx, 840, sx + swatch_w, 840 + swatch_h], radius=6, fill=col, outline=BORDER_COLOR, width=1)

draw_tracked_caps(d1, "EXPLORE THE THREE COLOR STORIES", 1080, font_sub, TEXT_DARK, tracking=8)

img1.save(os.path.join(scratch_dir, "post3_slide1.png"), "PNG")
img1.save(os.path.join(downloads_dir, "Meenu_Label_Post3_Slide_1.png"), "PNG")

# ==================== SLIDE 2 ====================
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_base_frame(d2, "02 / 03  —  SWIPE  →")
draw_tracked_caps(d2, "MEENU LABEL  •  THE SHADES", 160, font_label, TEXT_MUTED, tracking=6)

# Swatch 1: Porcelain Ivory
d2.rounded_rectangle([110, 360, 160, 410], radius=8, fill=COLOR_IVORY, outline=BORDER_COLOR, width=1)
d2.text((185, 360), "01. PORCELAIN IVORY & BOTANICALS", font=font_body_bold, fill=TEXT_DARK)
d2.text((185, 395), "Clean sunlit neutrals paired with delicate earth-tone florals.", font=font_body, fill=TEXT_ACCENT)
d2.text((185, 430), "Effortless, fresh, and flattering for every skin tone.", font=font_sub, fill=TEXT_MUTED)

d2.line([(W//2 - 40, 505), (W//2 + 40, 505)], fill=LINE_COLOR, width=1)

# Swatch 2: Botanical Sage
d2.rounded_rectangle([110, 560, 160, 610], radius=8, fill=COLOR_SAGE, outline=BORDER_COLOR, width=1)
d2.text((185, 560), "02. BOTANICAL SAGE & OLIVE", font=font_body_bold, fill=TEXT_DARK)
d2.text((185, 595), "Grounding earthy tones inspired by morning nature.", font=font_body, fill=TEXT_ACCENT)
d2.text((185, 630), "Smart elegance for cafe brunches and work meetings.", font=font_sub, fill=TEXT_MUTED)

d2.line([(W//2 - 40, 705), (W//2 + 40, 705)], fill=LINE_COLOR, width=1)

# Swatch 3: Warm Terracotta
d2.rounded_rectangle([110, 760, 160, 810], radius=8, fill=COLOR_RUST, outline=BORDER_COLOR, width=1)
d2.text((185, 760), "03. WARM TERRACOTTA & RUST", font=font_body_bold, fill=TEXT_DARK)
d2.text((185, 795), "Rich, festive warmth crafted for sunset celebrations.", font=font_body, fill=TEXT_ACCENT)
d2.text((185, 830), "Deep, cozy tones with subtle artisanal embroidery.", font=font_sub, fill=TEXT_MUTED)

img2.save(os.path.join(scratch_dir, "post3_slide2.png"), "PNG")
img2.save(os.path.join(downloads_dir, "Meenu_Label_Post3_Slide_2.png"), "PNG")

# ==================== SLIDE 3 ====================
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_base_frame(d3, "03 / 03  •  MEENULABEL.IN")
draw_tracked_caps(d3, "MEENU LABEL  •  YOUR CHOICE", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d3, "TELL US IN THE COMMENTS", 410, font_label, TEXT_MUTED, tracking=8)
draw_centered_text(d3, "Which shade calls to you?", 475, font_serif_date, TEXT_DARK)

d3.line([(W//2 - 60, 580), (W//2 + 60, 580)], fill=LINE_COLOR, width=2)

draw_centered_text(d3, "01. Porcelain Ivory   •   02. Botanical Sage   •   03. Warm Rust", 635, font_body_bold, TEXT_ACCENT)
draw_centered_text(d3, "Drop your favorite number below.", 685, font_serif_italic, TEXT_MUTED)

# CTA button/pill
pill_box = [(W//2 - 250, 850), (W//2 + 250, 925)]
d3.rounded_rectangle(pill_box, radius=8, fill=(242, 237, 230), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d3, "TAP LINK IN BIO FOR VIP ACCESS", 872, font_label, TEXT_DARK, tracking=4)

draw_centered_text(d3, "Drop 01 launches October 31st in limited quantities.", 965, font_sub, TEXT_MUTED)

img3.save(os.path.join(scratch_dir, "post3_slide3.png"), "PNG")
img3.save(os.path.join(downloads_dir, "Meenu_Label_Post3_Slide_3.png"), "PNG")

print("SUCCESS: Post 3 slides created!")

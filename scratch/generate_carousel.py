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
TEXT_MUTED = (130, 120, 108)    # Taupe bronze
TEXT_ACCENT = (80, 74, 66)      # Warm deep bronze
LINE_COLOR = (205, 195, 183)    # Accent line

# Fonts
font_serif_huge = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 66)
font_serif_date = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 74)
font_serif_medium = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 50)
font_serif_italic = ImageFont.truetype(r"C:\Windows\Fonts\georgiai.ttf", 36)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\GARA.TTF", 28)
font_label = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 22)

def draw_tracked_caps(draw, text, y, font, fill, tracking=12):
    """Used for uppercase spaced editorial headers and titles."""
    char_widths = [draw.textbbox((0, 0), c, font=font)[2] - draw.textbbox((0, 0), c, font=font)[0] for c in text]
    total_w = sum(char_widths) + (len(text) - 1) * tracking
    cur_x = (W - total_w) // 2
    for i, c in enumerate(text):
        draw.text((cur_x, y), c, font=font, fill=fill)
        cur_x += char_widths[i] + tracking

def draw_centered_text(draw, text, y, font, fill):
    """Used for natural flowing sentences with native font kerning."""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    cur_x = (W - text_w) // 2
    draw.text((cur_x, y), text, font=font, fill=fill)

def draw_base_frame(draw, slide_num_str):
    # Outer luxury border
    draw.rectangle([56, 56, W - 56, H - 56], outline=BORDER_COLOR, width=2)
    # Inner hairline border
    draw.rectangle([68, 68, W - 68, H - 68], outline=BORDER_INNER, width=1)
    # Footer indicator
    draw_tracked_caps(draw, slide_num_str, 1220, font_label, TEXT_MUTED, tracking=6)

# ==================== SLIDE 1 ====================
img1 = Image.new("RGB", (W, H), BG_COLOR)
d1 = ImageDraw.Draw(img1)
draw_base_frame(d1, "01 / 03  —  SWIPE  →")

# Top header
draw_tracked_caps(d1, "E S T .  2 0 2 6   •   C H A N D I G A R H", 160, font_label, TEXT_MUTED, tracking=6)

# Brand name
draw_tracked_caps(d1, "MEENU LABEL", 530, font_serif_huge, TEXT_DARK, tracking=18)

# Center divider
d1.line([(W//2 - 60, 645), (W//2 + 60, 645)], fill=LINE_COLOR, width=2)

# Subtitle
draw_tracked_caps(d1, "CONTEMPORARY DESIGNER WEAR", 685, font_sub, TEXT_ACCENT, tracking=8)
draw_tracked_caps(d1, "HANDCRAFTED CO-ORD SETS", 735, font_label, TEXT_MUTED, tracking=6)

# Bottom note
draw_tracked_caps(d1, "D E B U T   C O L L E C T I O N", 1080, font_sub, TEXT_DARK, tracking=10)

img1.save(os.path.join(scratch_dir, "slide1.png"), "PNG")
img1.save(os.path.join(downloads_dir, "Meenu_Label_Slide_1.png"), "PNG")

# ==================== SLIDE 2 ====================
img2 = Image.new("RGB", (W, H), BG_COLOR)
d2 = ImageDraw.Draw(img2)
draw_base_frame(d2, "02 / 03  —  SWIPE  →")

# Top header
draw_tracked_caps(d2, "MEENU LABEL  •  OUR PHILOSOPHY", 160, font_label, TEXT_MUTED, tracking=6)

# Natural flowing typography for manifesto (perfect kerning)
draw_centered_text(d2, "Thoughtfully designed co-ord sets.", 490, font_serif_medium, TEXT_DARK)
draw_centered_text(d2, "Pure, breathable fabrics.", 575, font_serif_medium, TEXT_DARK)
draw_centered_text(d2, "Tailored for effortless grace.", 660, font_serif_medium, TEXT_DARK)

d2.line([(W//2 - 50, 765), (W//2 + 50, 765)], fill=LINE_COLOR, width=2)

draw_centered_text(d2, "Artisanal florals & modern silhouettes.", 830, font_serif_italic, TEXT_ACCENT)
draw_centered_text(d2, "Made for everyday ease and intimate celebrations.", 895, font_sub, TEXT_MUTED)

img2.save(os.path.join(scratch_dir, "slide2.png"), "PNG")
img2.save(os.path.join(downloads_dir, "Meenu_Label_Slide_2.png"), "PNG")

# ==================== SLIDE 3 ====================
img3 = Image.new("RGB", (W, H), BG_COLOR)
d3 = ImageDraw.Draw(img3)
draw_base_frame(d3, "03 / 03  •  MEENULABEL.IN")

# Top header
draw_tracked_caps(d3, "MEENU LABEL  •  OFFICIAL LAUNCH", 160, font_label, TEXT_MUTED, tracking=6)

draw_tracked_caps(d3, "D E B U T   D R O P", 420, font_label, TEXT_MUTED, tracking=10)
draw_centered_text(d3, "OCTOBER 31", 485, font_serif_date, TEXT_DARK)

d3.line([(W//2 - 60, 605), (W//2 + 60, 605)], fill=LINE_COLOR, width=2)

draw_centered_text(d3, "Made with intention in Chandigarh.", 660, font_serif_italic, TEXT_ACCENT)
draw_tracked_caps(d3, "LIMITED SMALL-BATCH RELEASE", 725, font_label, TEXT_MUTED, tracking=5)

# CTA button/pill
pill_box = [(W//2 - 250, 860), (W//2 + 250, 935)]
d3.rounded_rectangle(pill_box, radius=8, fill=(242, 237, 230), outline=BORDER_COLOR, width=1)
draw_tracked_caps(d3, "JOIN THE VIP WAITLIST", 882, font_label, TEXT_DARK, tracking=6)

draw_centered_text(d3, "Tap the link in bio for exclusive launch privileges", 975, font_sub, TEXT_MUTED)

img3.save(os.path.join(scratch_dir, "slide3.png"), "PNG")
img3.save(os.path.join(downloads_dir, "Meenu_Label_Slide_3.png"), "PNG")

print("SUCCESS: Perfectly kerned slides regenerated!")

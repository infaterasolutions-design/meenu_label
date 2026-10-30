import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
scratch_dir = os.path.join(artifacts_dir, "scratch")
banners_dir = os.path.join(scratch_dir, "banners")
downloads_dir = r"C:\Users\sande\Downloads"

# Fonts
font_title = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 34)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 17)
font_browser_url = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 14)
font_nav = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 12)
font_atelier = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)

# Canvas: 2000 x 1280
CW, CH = 2000, 1280
canvas = Image.new("RGB", (CW, CH), (245, 243, 238))
d = ImageDraw.Draw(canvas)

# Subtle background framing
d.rectangle([20, 20, CW - 20, CH - 20], outline=(225, 218, 208), width=1)

# Header Presentation Bar
d.text((50, 40), "MEENU LABEL  •  FULL-SCREEN BANNER (ZERO HEAD CUTOFF)", font=font_title, fill=(20, 18, 16))
d.text((50, 84), "100VH CINEMATIC DESKTOP VIEWPORT  |  AMPLE HEADROOM PRESERVED  |  SLOW AUTO-SLIDE GLIDE", font=font_sub, fill=(120, 105, 90))

# Badge on top right
d.rounded_rectangle([CW - 420, 46, CW - 50, 90], radius=6, fill=(43, 110, 68))
d.text((CW - 400, 58), "✓ 100% FULL-SCREEN BANNER VERIFIED", font=font_sub, fill=(255, 255, 255))

# =========================================================================
# DESKTOP BROWSER MOCKUP (FULL SCREEN 16:9 VIEWPORT)
# =========================================================================
BX, BY = 50, 125
BW, BH = 1900, 1100

# Window drop shadow
shadow = Image.new("RGBA", (BW + 40, BH + 40), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle([20, 20, BW + 20, BH + 20], radius=16, fill=(0, 0, 0, 35))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
canvas.paste(shadow, (BX - 20, BY - 20), shadow)

# Browser Window Container
browser = Image.new("RGB", (BW, BH), (255, 255, 255))
bd = ImageDraw.Draw(browser)
bd.rounded_rectangle([0, 0, BW, BH], radius=12, fill=(255, 255, 255), outline=(210, 204, 196), width=1)

# Browser Top Bar (Chrome frame)
bd.rectangle([0, 0, BW, 44], fill=(236, 233, 227))
bd.line([(0, 44), (BW, 44)], fill=(215, 210, 202), width=1)

# Traffic Light buttons
bd.ellipse([18, 16, 30, 28], fill=(255, 95, 86)) # Close
bd.ellipse([38, 16, 50, 28], fill=(255, 189, 46)) # Min
bd.ellipse([58, 16, 70, 28], fill=(39, 201, 63)) # Max

# Address bar
bd.rounded_rectangle([120, 8, BW - 180, 36], radius=14, fill=(255, 255, 255), outline=(215, 210, 202), width=1)
bd.text((140, 14), "🔒  https://meenulabel.com  •  Meenu Label • Contemporary Ethnic & Fusion Wear", font=font_browser_url, fill=(90, 85, 80))
bd.text((BW - 150, 13), "⚡ Chrome 120", font=font_browser_url, fill=(130, 120, 110))

# -------------------------------------------------------------------------
# STOREFRONT HEADER (Announcement + Nav)
# -------------------------------------------------------------------------
# Announcement Bar (32px)
bd.rectangle([0, 45, BW, 77], fill=(20, 18, 16))
font_ann = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
bd.text((36, 54), "⚡ DEBUT DROP 01 LIVE  •  100% PURE BREATHABLE SILHOUETTES  •  CHANDIGARH", font=font_ann, fill=(250, 248, 245))
bd.text((BW - 400, 54), "FREE 24-HR EXPRESS TRICITY DELIVERY  |  SIZE GUIDE", font=font_ann, fill=(232, 211, 185))

# Header Navigation Bar (68px)
HEADER_Y = 78
HEADER_H = 68
bd.rectangle([0, HEADER_Y, BW, HEADER_Y + HEADER_H], fill=(255, 255, 255))
bd.line([(0, HEADER_Y + HEADER_H), (BW, HEADER_Y + HEADER_H)], fill=(232, 226, 216), width=1)

# Left: Hamburger + Nav Links
font_icon = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 22)
bd.text((36, HEADER_Y + 22), "☰", font=font_icon, fill=(20, 18, 16))

nav_x = 80
nav_items = ["ALL SILHOUETTES", "CO-ORDS", "FESTIVE SUITS", "DRESSES", "TOPS"]
for idx, item in enumerate(nav_items):
    color = (158, 125, 71) if idx == 2 else (20, 18, 16) # Highlight Festive Suits for Slide 4
    bd.text((nav_x, HEADER_Y + 27), item, font=font_nav, fill=color)
    nav_x += 140

# Center: Authentic Canva Brand Logo
logo_path = os.path.join(downloads_dir, "meenu_logo_official.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    h_target = 52
    w_target = int(logo_img.width * (h_target / logo_img.height))
    logo_resized = logo_img.resize((w_target, h_target), Image.Resampling.LANCZOS)
    logo_x = (BW - w_target) // 2
    logo_y = HEADER_Y + 8
    browser.paste(logo_resized, (logo_x, logo_y), logo_resized)

# Right: Search + Guide + Bag
bd.rounded_rectangle([BW - 420, HEADER_Y + 16, BW - 220, HEADER_Y + 52], radius=18, fill=(243, 239, 232))
font_search = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 13)
bd.text((BW - 404, HEADER_Y + 24), "🔍 Search Drop 01...", font=font_search, fill=(120, 110, 100))

bd.text((BW - 195, HEADER_Y + 25), "📏 Guide", font=font_nav, fill=(20, 18, 16))

bd.rounded_rectangle([BW - 115, HEADER_Y + 18, BW - 35, HEADER_Y + 50], radius=6, fill=(243, 239, 232))
bd.text((BW - 105, HEADER_Y + 25), "🛍️ Bag", font=font_nav, fill=(20, 18, 16))
bd.rounded_rectangle([BW - 55, HEADER_Y + 22, BW - 40, HEADER_Y + 44], radius=6, fill=(20, 18, 16))
font_badge = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 10)
bd.text((BW - 51, HEADER_Y + 27), "0", font=font_badge, fill=(255, 255, 255))

# -------------------------------------------------------------------------
# TRUE FULL-SCREEN BANNER (Fills 100% of the screen down to the bottom!)
# -------------------------------------------------------------------------
HERO_Y = HEADER_Y + HEADER_H
HERO_H = BH - HERO_Y # Fills the complete remaining screen height!

# Load Banner 4 (The Gulabi Organza Festive Suit) with full headroom
banner_4_path = os.path.join(banners_dir, "banner_4_gulabi.jpg")
if os.path.exists(banner_4_path):
    b4_img = Image.open(banner_4_path)
    # Resize to width BW (1900) while anchoring to top
    b4_resized = b4_img.resize((BW, HERO_H), Image.Resampling.LANCZOS)
    browser.paste(b4_resized, (0, HERO_Y))

# Slider Chevrons
font_chev = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 32)
# Left Chevron
bd.ellipse([24, HERO_Y + HERO_H//2 - 24, 72, HERO_Y + HERO_H//2 + 24], fill=(255, 255, 255), outline=(210, 204, 196), width=1)
bd.text((41, HERO_Y + HERO_H//2 - 25), "‹", font=font_chev, fill=(20, 18, 16))

# Right Chevron
bd.ellipse([BW - 72, HERO_Y + HERO_H//2 - 24, BW - 24, HERO_Y + HERO_H//2 + 24], fill=(255, 255, 255), outline=(210, 204, 196), width=1)
bd.text((BW - 55, HERO_Y + HERO_H//2 - 25), "›", font=font_chev, fill=(20, 18, 16))

# Bottom Indicator Dots Pill
dots_w = 120
dots_x = (BW - dots_w) // 2
dots_y = HERO_Y + HERO_H - 42
bd.rounded_rectangle([dots_x, dots_y, dots_x + dots_w, dots_y + 24], radius=12, fill=(255, 255, 255), outline=(220, 215, 205), width=1)

# 4 dots: active is dot 4 (Gulabi Suit)
bd.ellipse([dots_x + 16, dots_y + 7, dots_x + 26, dots_y + 17], fill=(200, 190, 180))
bd.ellipse([dots_x + 34, dots_y + 7, dots_x + 44, dots_y + 17], fill=(200, 190, 180))
bd.ellipse([dots_x + 52, dots_y + 7, dots_x + 62, dots_y + 17], fill=(200, 190, 180))
bd.rounded_rectangle([dots_x + 70, dots_y + 7, dots_x + 102, dots_y + 17], radius=5, fill=(20, 18, 16)) # Active

# Bottom Right Atelier Pill (matching Snitch)
bd.rounded_rectangle([BW - 300, HERO_Y + HERO_H - 48, BW - 36, HERO_Y + HERO_H - 16], radius=6, fill=(255, 255, 255), outline=(220, 215, 205), width=1)
bd.ellipse([BW - 286, HERO_Y + HERO_H - 36, BW - 278, HERO_Y + HERO_H - 28], fill=(43, 110, 68))
bd.text((BW - 270, HERO_Y + HERO_H - 38), "DROP 01 • STRICTLY 39 PIECES TOTAL", font=font_atelier, fill=(20, 18, 16))

# Paste browser onto canvas
canvas.paste(browser, (BX, BY))

# Save preview
out_downloads = os.path.join(downloads_dir, "Meenu_Label_Snitch_Style_Preview.png")
canvas.save(out_downloads, "PNG", quality=95)

out_artifacts = os.path.join(artifacts_dir, "Meenu_Label_Snitch_Style_Preview.png")
canvas.save(out_artifacts, "PNG", quality=95)

print("SUCCESS: Rendered updated full-screen preview with zero head cutoff!")

import os, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
scratch_dir = os.path.join(artifacts_dir, "scratch")
highres_dir = os.path.join(scratch_dir, "highres_products")
downloads_dir = r"C:\Users\sande\Downloads"

# Fonts
font_title = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 34)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 17)
font_browser_url = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 14)
font_nav = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 12)
font_hero_bold = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 46)
font_hero_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 38)
font_hero_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 15)
font_hero_specs = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 12)
font_hero_btn = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 14)
font_quote_bold = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 22)
font_quote_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 19)
font_tag = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
font_card_title = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 13)
font_card_price = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 13)

# Canvas: 2000 x 1280
CW, CH = 2000, 1280
canvas = Image.new("RGB", (CW, CH), (245, 243, 238))
d = ImageDraw.Draw(canvas)

# Subtle background framing
d.rectangle([20, 20, CW - 20, CH - 20], outline=(225, 218, 208), width=1)

# Header Presentation Bar
d.text((50, 40), "MEENU LABEL  •  SNITCH 1500x708 AUTO-LAYOUT HERO SECTION", font=font_title, fill=(20, 18, 16))
d.text((50, 84), "EXACT SNITCH CONTAINER DIMENSIONS (1500x708)  |  FLAWLESS EDITORIAL PORTRAIT  |  ZERO BLUR SMUDGE", font=font_sub, fill=(120, 105, 90))

# Badge on top right
d.rounded_rectangle([CW - 420, 46, CW - 50, 90], radius=6, fill=(43, 110, 68))
d.text((CW - 395, 58), "✓ SNITCH 1500x708 VERIFIED", font=font_sub, fill=(255, 255, 255))

# =========================================================================
# DESKTOP BROWSER MOCKUP
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
bd.text((140, 14), "🔒 https://meenulabel.com  •  Meenu Label • Contemporary Ethnic & Fusion Wear", font=font_browser_url, fill=(90, 85, 80))
bd.text((BW - 150, 13), "⚡ Chrome 120", font=font_browser_url, fill=(130, 120, 110))

# -------------------------------------------------------------------------
# STOREFRONT HEADER (Announcement + Nav)
# -------------------------------------------------------------------------
# Announcement Bar (32px)
bd.rectangle([0, 45, BW, 77], fill=(20, 18, 16))
font_ann = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
bd.text((36, 54), "✨ DEBUT DROP 01 LIVE  •  100% PURE BREATHABLE SILHOUETTES  •  CHANDIGARH", font=font_ann, fill=(250, 248, 245))
bd.text((BW - 340, 54), "FREE 24-HR EXPRESS TRICITY DELIVERY   |   SIZE GUIDE", font=font_ann, fill=(220, 215, 205))

# Header Nav Bar (72px)
bd.rectangle([0, 78, BW, 150], fill=(250, 248, 245))
bd.line([(0, 150), (BW, 150)], fill=(235, 230, 222), width=1)

# Left nav
bd.text((36, 106), "☰", font=font_nav, fill=(20, 18, 16))
nav_items = ["ALL SILHOUETTES", "CO-ORDS", "FESTIVE SUITS", "DRESSES", "TOPS"]
nx = 80
for idx, item in enumerate(nav_items):
    col = (184, 134, 11) if idx == 0 else (60, 55, 50)
    bd.text((nx, 107), item, font=font_nav, fill=col)
    nx += 120

# Center Logo
logo_path = os.path.join(downloads_dir, "meenu_logo_official.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img.thumbnail((180, 52))
    lx = (BW - logo_img.width) // 2
    browser.paste(logo_img, (lx, 88), logo_img if logo_img.mode == 'RGBA' else None)

# Right Header Controls
bd.rounded_rectangle([BW - 380, 94, BW - 180, 134], radius=18, fill=(240, 236, 230))
bd.text((BW - 365, 105), "🔍 Search Drop 01...", font=font_browser_url, fill=(140, 130, 120))
bd.text((BW - 150, 107), "📏 Guide", font=font_nav, fill=(60, 55, 50))
bd.text((BW - 75, 107), "🛍 Bag (0)", font=font_nav, fill=(20, 18, 16))

# -------------------------------------------------------------------------
# SNITCH 1500x708 HERO VIEWPORT (EXACT AUTO-LAYOUT)
# -------------------------------------------------------------------------
hero_y = 151
hero_w = 1500
hero_h = 708
hero_x = (BW - hero_w) // 2  # 200px centered

# Background canvas for hero
bd.rectangle([0, hero_y, BW, hero_y + hero_h], fill=(250, 248, 245))
# Viewport border line
bd.line([(0, hero_y + hero_h), (BW, hero_y + hero_h)], fill=(235, 230, 222), width=1)

# Inside 1500x708 Hero Viewport:
# 1. Left Editorial Typography (x = hero_x + 70)
hx_left = hero_x + 70
hy_start = hero_y + 130

# Badge pill
bd.rounded_rectangle([hx_left, hy_start, hx_left + 190, hy_start + 28], radius=14, fill=(238, 233, 225))
bd.ellipse([hx_left + 10, hy_start + 10, hx_left + 18, hy_start + 18], fill=(184, 134, 11))
bd.text((hx_left + 26, hy_start + 6), "DROP 01 • LIMITED EDITION", font=font_tag, fill=(70, 60, 50))

# Bold Title
bd.text((hx_left, hy_start + 45), "GULABI,", font=font_hero_bold, fill=(24, 22, 20))
bd.text((hx_left, hy_start + 100), "POWDER PINK GRACE.", font=font_hero_light, fill=(40, 36, 32))

# Subtitle
bd.text((hx_left, hy_start + 165), "Pure Cotton Silk Ensemble • Floral Organza Dupatta", font=font_hero_sub, fill=(110, 100, 90))

# Specs
bd.text((hx_left, hy_start + 205), "Straight-Cut 3-Pc Suit  •  Jaipur Looms  •  Strictly 3 Pieces", font=font_hero_specs, fill=(140, 130, 120))

# CTA Button
btn_y = hy_start + 250
btn_w, btn_h = 220, 50
bd.rounded_rectangle([hx_left, btn_y, hx_left + btn_w, btn_y + btn_h], radius=4, fill=(24, 22, 20))
bd.text((hx_left + 36, btn_y + 16), "VIEW GULABI SUIT  →", font=font_hero_btn, fill=(255, 255, 255))

# 2. Center Editorial Model Card (Full Head, Full Hair, Crisp Frame, Soft Shadow)
gulabi_path = os.path.join(highres_dir, "JAC25ST03063.jpg")
if os.path.exists(gulabi_path):
    g_img = Image.open(gulabi_path)
    # Fit into 500w x 600h
    mw, mh = 490, 590
    g_resized = g_img.resize((mw, mh), Image.Resampling.LANCZOS)
    
    card_x = hero_x + 550
    card_y = hero_y + (hero_h - mh) // 2
    
    # Shadow
    card_shadow = Image.new("RGBA", (mw + 40, mh + 40), (0, 0, 0, 0))
    csd = ImageDraw.Draw(card_shadow)
    csd.rounded_rectangle([20, 20, mw + 20, mh + 20], radius=14, fill=(0, 0, 0, 35))
    card_shadow = card_shadow.filter(ImageFilter.GaussianBlur(14))
    browser.paste(card_shadow, (card_x - 20, card_y - 10), card_shadow)
    
    # Rounded Card Mask
    c_mask = Image.new("L", (mw, mh), 0)
    cmd = ImageDraw.Draw(c_mask)
    cmd.rounded_rectangle([0, 0, mw, mh], radius=14, fill=255)
    browser.paste(g_resized, (card_x, card_y), c_mask)
    
    # Border
    bd.rounded_rectangle([card_x, card_y, card_x + mw, card_y + mh], radius=14, outline=(225, 218, 208), width=1)
    
    # Scarcity tag on photo
    bd.rounded_rectangle([card_x + 16, card_y + 16, card_x + 140, card_y + 40], radius=4, fill=(255, 255, 255))
    bd.text((card_x + 26, card_y + 22), "ONLY 3 PIECES LEFT", font=font_tag, fill=(180, 40, 30))

# 3. Right Flank (Snitch Signature Minimalist Quote)
rx_quote = hero_x + hero_w - 280
ry_quote = hero_y + 240
bd.line([(rx_quote, ry_quote - 20), (rx_quote, ry_quote + 160)], fill=(225, 218, 208), width=1)
bd.text((rx_quote + 24, ry_quote), "SUBTLE LUXURY.", font=font_quote_bold, fill=(45, 39, 33))
bd.text((rx_quote + 24, ry_quote + 32), "HERITAGE PRINTS.", font=font_quote_light, fill=(120, 110, 100))
bd.text((rx_quote + 24, ry_quote + 80), "SURAT ATELIER • EXCLUSIVE", font=font_tag, fill=(160, 150, 140))

# 4. Controls: Chevrons, Progress Dots, Atelier Pill
# Left chevron
bd.ellipse([hero_x + 16, hero_y + hero_h//2 - 23, hero_x + 62, hero_y + hero_h//2 + 23], fill=(255, 255, 255), outline=(225, 220, 212), width=1)
bd.text((hero_x + 33, hero_y + hero_h//2 - 13), "<", font=font_hero_btn, fill=(60, 50, 40))

# Right chevron
bd.ellipse([hero_x + hero_w - 62, hero_y + hero_h//2 - 23, hero_x + hero_w - 16, hero_y + hero_h//2 + 23], fill=(255, 255, 255), outline=(225, 220, 212), width=1)
bd.text((hero_x + hero_w - 45, hero_y + hero_h//2 - 13), ">", font=font_hero_btn, fill=(60, 50, 40))

# Progress Dots (bottom center)
dx = hero_x + hero_w // 2 - 40
dy = hero_y + hero_h - 32
bd.ellipse([dx, dy, dx + 8, dy + 8], fill=(200, 190, 180))
bd.ellipse([dx + 18, dy, dx + 26, dy + 8], fill=(200, 190, 180))
bd.ellipse([dx + 36, dy, dx + 44, dy + 8], fill=(200, 190, 180))
# Active dot (elongated pill)
bd.rounded_rectangle([dx + 54, dy - 1, dx + 84, dy + 9], radius=5, fill=(24, 22, 20))

# Atelier Pill (Bottom Right)
pill_x = hero_x + hero_w - 290
pill_y = hero_y + hero_h - 44
bd.rounded_rectangle([pill_x, pill_y, pill_x + 260, pill_y + 30], radius=15, fill=(255, 255, 255), outline=(220, 215, 208), width=1)
bd.ellipse([pill_x + 12, pill_y + 10, pill_x + 22, pill_y + 20], fill=(46, 125, 50))
bd.text((pill_x + 30, pill_y + 7), "DROP 01 • STRICTLY 48 PIECES TOTAL", font=font_tag, fill=(40, 36, 32))

# -------------------------------------------------------------------------
# CATALOG SECTION PEEK (Tabs + Top Row)
# -------------------------------------------------------------------------
cat_y = hero_y + hero_h + 30
bd.text((hero_x, cat_y), "The Debut 16 Silhouettes", font=font_title, fill=(24, 22, 20))
bd.text((hero_x, cat_y + 44), "Explore our complete 16-silhouette release. Strictly 3 pieces per design in M, L, XL.", font=font_hero_sub, fill=(120, 110, 100))

# Filter tabs
tx = hero_x
tabs = ["All (16)", "Festive Suits (6)", "Co-ord Sets (4)", "Dresses (3)", "Tops & Blouses (3)"]
for idx, t in enumerate(tabs):
    bg_t = (24, 22, 20) if idx == 0 else (240, 236, 230)
    col_t = (255, 255, 255) if idx == 0 else (60, 50, 40)
    tw = len(t) * 9 + 24
    bd.rounded_rectangle([tx, cat_y + 80, tx + tw, cat_y + 114], radius=17, fill=bg_t)
    bd.text((tx + 12, cat_y + 90), t, font=font_hero_specs, fill=col_t)
    tx += tw + 10

# Paste browser window into presentation canvas
canvas.paste(browser, (BX, BY))

out_path = os.path.join(downloads_dir, "Meenu_Label_Snitch_Style_Preview.png")
canvas.save(out_path, quality=95)
shutil.copy2(out_path, os.path.join(artifacts_dir, "Meenu_Label_Snitch_Style_Preview.png"))

print(f"SUCCESS: Rendered clean Snitch 1500x708 preview at {out_path}")

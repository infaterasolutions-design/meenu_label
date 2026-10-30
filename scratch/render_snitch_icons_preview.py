import os, shutil
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
font_hero_btn = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 14)
font_tag = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
font_hero_specs = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 12)
font_hero_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 15)
font_ann = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
font_badge = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 10)

# Canvas: 2000 x 1280
CW, CH = 2000, 1280
canvas = Image.new("RGB", (CW, CH), (245, 243, 238))
d = ImageDraw.Draw(canvas)

# Top Bar Announcement
d.rectangle([0, 0, CW, 50], fill=(24, 22, 20))
d.text((50, 16), "MEENU LABEL  •  AUTUMN/WINTER 2026 DEBUT  •  CHANDIGARH", font=font_sub, fill=(220, 215, 205))
d.text((CW - 420, 16), "SNITCH-STYLE MINIMALIST LUXURY STOREFRONT", font=font_sub, fill=(184, 134, 11))

# Browser Window Dimensions (1900 x 1150)
BW, BH = 1900, 1150
BX, BY = (CW - BW) // 2, 80

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
bd.ellipse([18, 16, 30, 28], fill=(255, 95, 86))
bd.ellipse([38, 16, 50, 28], fill=(255, 189, 46))
bd.ellipse([58, 16, 70, 28], fill=(39, 201, 63))

# Address bar
bd.rounded_rectangle([120, 8, BW - 180, 36], radius=14, fill=(255, 255, 255), outline=(215, 210, 202), width=1)
bd.text((140, 16), "https://meenulabel.com  •  Meenu Label Official Store | Chandigarh Luxury Pret", font=font_browser_url, fill=(100, 95, 90))

# Top Announcement Bar (34px)
bd.rectangle([0, 44, BW, 78], fill=(24, 22, 20))
bd.text((40, 54), "AUTUMN/WINTER 2026 DEBUT: EXCLUSIVE 16-SILHOUETTE DROP (STRICTLY 3 PIECES PER DESIGN)", font=font_ann, fill=(220, 215, 205))
bd.text((BW - 340, 54), "FREE 24-HR EXPRESS TRICITY DELIVERY   |   SIZE GUIDE", font=font_ann, fill=(220, 215, 205))

# Header Nav Bar (72px) - Ultra-Clean, Hamburger on Left, Centered Logo, 4 Icons on Right
bd.rectangle([0, 78, BW, 150], fill=(255, 255, 255))
bd.line([(0, 150), (BW, 150)], fill=(235, 230, 222), width=1)

# 1. Left Hamburger Menu Icon (Kept in place)
hy = 114
hx = 40
for off in [-6, 0, 6]:
    bd.line([(hx, hy + off), (hx + 20, hy + off)], fill=(20, 18, 16), width=2)

# 2. Middle Centered Brand Logo
logo_path = os.path.join(downloads_dir, "meenu_logo_official.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img.thumbnail((190, 54))
    lx = (BW - logo_img.width) // 2
    browser.paste(logo_img, (lx, 87), logo_img if logo_img.mode == 'RGBA' else None)

# 3. Right Header: EXACT SNITCH MINIMALIST LINE ICONS (Search, Bag, Wishlist, User)
icon_centers = [BW - 220, BW - 165, BW - 110, BW - 55]
for i, cx in enumerate(icon_centers):
    icon_path = f"scratch/snitch_clean_{i}.png"
    if os.path.exists(icon_path):
        ic = Image.open(icon_path)
        w, h = ic.size
        scale = 22.0 / max(w, h)
        nw, nh = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
        ic_resized = ic.resize((nw, nh), Image.LANCZOS)
        
        px = cx - nw // 2
        py = 114 - nh // 2
        browser.paste(ic_resized, (px, py), ic_resized)

# Draw Pill Badges for Bag (Icon 1) and Wishlist (Icon 2)
bag_cx = icon_centers[1]
bd.rounded_rectangle([bag_cx + 4, 102, bag_cx + 18, 116], radius=7, fill=(24, 22, 20))
bd.text((bag_cx + 8, 103), "0", font=font_badge, fill=(255, 255, 255))

wish_cx = icon_centers[2]
bd.rounded_rectangle([wish_cx + 5, 102, wish_cx + 19, 116], radius=7, fill=(184, 134, 11))
bd.text((wish_cx + 9, 103), "0", font=font_badge, fill=(255, 255, 255))

# -------------------------------------------------------------------------
# SNITCH 1500x708 FULL-BLEED EDITORIAL HERO VIEWPORT
# -------------------------------------------------------------------------
hero_y = 151
hero_w = 1500
hero_h = 708
hero_x = (BW - hero_w) // 2  # centered

bd.rectangle([0, hero_y, BW, hero_y + hero_h], fill=(248, 246, 242))

banner_path = os.path.join(banners_dir, "hero_1_marigold.jpg")
if os.path.exists(banner_path):
    b_img = Image.open(banner_path)
    browser.paste(b_img, (hero_x, hero_y))

bd.line([(0, hero_y + hero_h), (BW, hero_y + hero_h)], fill=(235, 230, 222), width=1)

# Floating Luxury CTA Pill & Action on the Left Wall
hx_left = hero_x + 85
hy_cta = hero_y + hero_h - 145

bd.rounded_rectangle([hx_left, hy_cta, hx_left + 240, hy_cta + 28], radius=14, fill=(255, 255, 255))
bd.ellipse([hx_left + 10, hy_cta + 10, hx_left + 18, hy_cta + 18], fill=(184, 134, 11))
bd.text((hx_left + 26, hy_cta + 6), "DROP 01 • 100% PURE CHANDERI SILK", font=font_tag, fill=(70, 60, 50))

bd.text((hx_left, hy_cta + 36), "Jaipur Heritage Looms  •  Strictly 3 Pieces (M, L, XL)  •  Rs. 2,299", font=font_hero_specs, fill=(60, 50, 40))

btn_y = hy_cta + 60
btn_w, btn_h = 240, 50
bd.rounded_rectangle([hx_left, btn_y, hx_left + btn_w, btn_y + btn_h], radius=4, fill=(24, 22, 20))
bd.text((hx_left + 45, btn_y + 16), "SHOP FESTIVE SUIT  ->", font=font_hero_btn, fill=(255, 255, 255))

# Chevrons
bd.ellipse([hero_x + 24, hero_y + hero_h // 2 - 22, hero_x + 68, hero_y + hero_h // 2 + 22], fill=(255, 255, 255), outline=(220, 215, 205), width=1)
bd.text((hero_x + 40, hero_y + hero_h // 2 - 11), "<", font=font_title, fill=(30, 28, 25))

bd.ellipse([hero_x + hero_w - 68, hero_y + hero_h // 2 - 22, hero_x + hero_w - 24, hero_y + hero_h // 2 + 22], fill=(255, 255, 255), outline=(220, 215, 205), width=1)
bd.text((hero_x + hero_w - 53, hero_y + hero_h // 2 - 11), ">", font=font_title, fill=(30, 28, 25))

# Dots
dot_cx = hero_x + hero_w // 2
dot_y = hero_y + hero_h - 26
dot_spacing = 28
dot_start = dot_cx - (3 * dot_spacing) // 2
for i in range(4):
    dx = dot_start + i * dot_spacing
    if i == 0:
        bd.rounded_rectangle([dx - 14, dot_y - 4, dx + 14, dot_y + 4], radius=4, fill=(184, 134, 11))
    else:
        bd.ellipse([dx - 4, dot_y - 4, dx + 4, dot_y + 4], fill=(210, 205, 195))

# Floating Atelier Pill
bd.rounded_rectangle([hero_x + hero_w - 245, hero_y + hero_h - 48, hero_x + hero_w - 25, hero_y + hero_h - 20], radius=14, fill=(255, 255, 255))
bd.ellipse([hero_x + hero_w - 233, hero_y + hero_h - 37, hero_x + hero_w - 227, hero_y + hero_h - 31], fill=(39, 174, 96))
bd.text((hero_x + hero_w - 220, hero_y + hero_h - 40), "AUTO-SLIDING • 6S INTERVAL", font=font_tag, fill=(70, 60, 50))

# -------------------------------------------------------------------------
# CATALOG SECTION BELOW HERO
# -------------------------------------------------------------------------
cat_y = hero_y + hero_h + 30
bd.text((80, cat_y), "DISCOVER DROP 01  •  16 EXCLUSIVE SILHOUETTES", font=font_sub, fill=(24, 22, 20))
bd.text((80, cat_y + 24), "Limited Atelier Run: Strictly 1 Piece per Size (M, L, XL)  |  Crafted in Chandigarh & Jaipur", font=font_tag, fill=(130, 120, 110))

# Paste browser onto canvas
canvas.paste(browser, (BX, BY))

# Save preview
out_downloads = os.path.join(downloads_dir, "Meenu_Label_Snitch_Style_Preview.png")
canvas.save(out_downloads, quality=95)

out_artifacts = os.path.join(artifacts_dir, "Meenu_Label_Snitch_Style_Preview.png")
canvas.save(out_artifacts, quality=95)

shutil.copyfile("scratch/render_snitch_icons_preview.py", "scratch/render_ultimate_hero_preview.py")

print("SUCCESS: Rendered Meenu Label preview with hamburger on left, centered logo, and 4 icons on right!")

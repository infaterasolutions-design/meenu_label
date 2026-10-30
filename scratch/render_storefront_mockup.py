import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
highres_dir = os.path.join(scratch_dir, "highres_products")
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
downloads_dir = r"C:\Users\sande\Downloads"

# Fonts
font_studio_title = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 46)
font_studio_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 22)
font_phone_brand = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 24)
font_phone_h1 = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 20)
font_phone_h2 = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 17)
font_phone_body = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 14)
font_phone_bold = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 14)
font_phone_sm = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 12)
font_phone_sm_bold = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 12)
font_tag = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 11)
font_badge = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 13)
font_anno_title = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 16)
font_anno_desc = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 13)

# Canvas
CW, CH = 2200, 1420
canvas = Image.new("RGB", (CW, CH), (247, 245, 240))
d = ImageDraw.Draw(canvas)

# Studio borders
d.rectangle([30, 30, CW - 30, CH - 30], outline=(225, 218, 208), width=2)
d.rectangle([40, 40, CW - 40, CH - 40], outline=(240, 235, 226), width=1)

# Studio Header
title_text = "M E E N U   L A B E L"
tb = d.textbbox((0, 0), title_text, font=font_studio_title)
d.text(((CW - (tb[2]-tb[0])) // 2, 60), title_text, font=font_studio_title, fill=(30, 28, 25))

sub_text = "SHOPIFY LUXURY STOREFRONT ARCHITECTURE  •  MOBILE-FIRST DESIGN  •  MEENULABEL.COM"
sb = d.textbbox((0, 0), sub_text, font=font_studio_sub)
d.text(((CW - (sb[2]-sb[0])) // 2, 120), sub_text, font=font_studio_sub, fill=(130, 120, 108))

d.line([(CW//2 - 250, 155), (CW//2 + 250, 155)], fill=(210, 200, 188), width=1)

# Helper to draw phone device
PW, PH = 520, 1100
CORNER = 42

def create_phone_base():
    p_img = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
    pd = ImageDraw.Draw(p_img)
    # Phone body (sleek matte dark titanium chassis)
    pd.rounded_rectangle([0, 0, PW, PH], radius=CORNER, fill=(24, 24, 27), outline=(60, 60, 65), width=3)
    # Screen area
    screen_rect = [12, 12, PW - 12, PH - 12]
    pd.rounded_rectangle(screen_rect, radius=CORNER - 8, fill=(250, 248, 245))
    return p_img

# =========================================================================
# PHONE 1: HOMEPAGE (DROP 01 SHOWCASE)
# =========================================================================
p1 = create_phone_base()
d1 = ImageDraw.Draw(p1)

# Dynamic island / camera notch
d1.rounded_rectangle([PW//2 - 60, 22, PW//2 + 60, 44], radius=11, fill=(24, 24, 27))
# Status bar
d1.text((36, 26), "9:41", font=font_phone_sm_bold, fill=(30, 28, 25))
d1.text((PW - 70, 26), "5G  100%", font=font_phone_sm_bold, fill=(30, 28, 25))

# Top Announcement Bar
d1.rectangle([12, 54, PW - 12, 82], fill=(30, 28, 25))
ann1 = "✨ DROP 01 LIVE • FREE SHIPPING IN TRICITY • LIMITED PIECES"
ab1 = d1.textbbox((0, 0), ann1, font=font_tag)
d1.text(((PW - (ab1[2]-ab1[0]))//2, 62), ann1, font=font_tag, fill=(245, 240, 230))

# Header
d1.rectangle([12, 82, PW - 12, 136], fill=(250, 248, 245), outline=(230, 224, 215), width=1)
# Hamburger
d1.line([(32, 102), (52, 102)], fill=(30, 28, 25), width=2)
d1.line([(32, 109), (52, 109)], fill=(30, 28, 25), width=2)
d1.line([(32, 116), (46, 116)], fill=(30, 28, 25), width=2)
# Logo
logo_txt = "MEENU LABEL"
lb = d1.textbbox((0, 0), logo_txt, font=font_phone_brand)
d1.text(((PW - (lb[2]-lb[0]))//2, 97), logo_txt, font=font_phone_brand, fill=(30, 28, 25))
# Bag icon
d1.rectangle([PW - 56, 100, PW - 38, 120], outline=(30, 28, 25), width=2)
d1.text((PW - 50, 102), "0", font=font_phone_sm_bold, fill=(30, 28, 25))

# Hero Banner
hero_src = Image.open(os.path.join(highres_dir, "JAB26ST05010.jpg"))
hero_img = hero_src.crop((50, 80, 1050, 850)).resize((PW - 24, 290), Image.Resampling.LANCZOS)
p1.paste(hero_img, (12, 136))

# Dark gradient overlay on hero bottom
overlay = Image.new("RGBA", (PW - 24, 110), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for y in range(110):
    alpha = int(180 * (y / 110)**1.2)
    od.line([(0, y), (PW - 24, y)], fill=(20, 18, 16, alpha))
p1.paste(overlay, (12, 136 + 290 - 110), overlay)

d1.text((32, 335), "THE DEBUT COLLECTION", font=font_phone_sm_bold, fill=(240, 225, 205))
d1.text((32, 355), "Effortless Everyday Luxury", font=font_phone_h1, fill=(255, 255, 255))
d1.text((32, 385), "Pure Breathable Silhouettes  •  Drop 01", font=font_phone_sm, fill=(220, 215, 208))

# Hero CTA Button
d1.rounded_rectangle([PW - 160, 365, PW - 32, 405], radius=6, fill=(250, 248, 245))
d1.text((PW - 148, 376), "EXPLORE  →", font=font_phone_sm_bold, fill=(30, 28, 25))

# Category Filter Pills
y_cat = 438
d1.rectangle([12, y_cat, PW - 12, y_cat + 46], fill=(250, 248, 245), outline=(238, 232, 224), width=1)
cats = [("All (13)", True), ("Co-ord Sets", False), ("Festive Suits", False), ("Dresses", False)]
cx = 26
for cname, is_sel in cats:
    if is_sel:
        d1.rounded_rectangle([cx, y_cat + 8, cx + 70, y_cat + 36], radius=14, fill=(30, 28, 25))
        d1.text((cx + 14, y_cat + 14), cname, font=font_phone_sm_bold, fill=(250, 248, 245))
        cx += 80
    else:
        cb = d1.textbbox((0, 0), cname, font=font_phone_sm)[2] - d1.textbbox((0, 0), cname, font=font_phone_sm)[0]
        d1.rounded_rectangle([cx, y_cat + 8, cx + cb + 24, y_cat + 36], radius=14, fill=(244, 240, 233), outline=(225, 218, 208))
        d1.text((cx + 12, y_cat + 14), cname, font=font_phone_sm, fill=(60, 55, 50))
        cx += cb + 34

# 2-Column Product Grid
card_w = (PW - 24 - 24 - 14) // 2
grid_y = 496

# Item 1: Polka Dress
p1_src = Image.open(os.path.join(highres_dir, "JAA26DR03942.jpg"))
p1_crop = p1_src.crop((60, 20, 1040, 1170)).resize((card_w, 240), Image.Resampling.LANCZOS)
p1.paste(p1_crop, (24, grid_y))
d1.rectangle([24, grid_y, 24 + card_w, grid_y + 240], outline=(228, 220, 210), width=1)

# Scarcity tag on Item 1
d1.rounded_rectangle([32, grid_y + 8, 116, grid_y + 28], radius=4, fill=(200, 50, 40))
d1.text((38, grid_y + 11), "ONLY 3 LEFT", font=font_tag, fill=(255, 255, 255))

d1.text((24, grid_y + 248), "Retro Polka Wrap Dress", font=font_phone_bold, fill=(30, 28, 25))
d1.text((24, grid_y + 268), "Pure Breathable Cotton", font=font_phone_sm, fill=(120, 110, 100))
d1.text((24, grid_y + 288), "₹1,499", font=font_phone_bold, fill=(30, 28, 25))
d1.text((80, grid_y + 290), "₹2,499", font=font_phone_sm, fill=(150, 140, 130))
d1.line([(78, grid_y + 297), (120, grid_y + 297)], fill=(150, 140, 130), width=1)
d1.text((24, grid_y + 312), "Sizes: M (38) • L (40) • XL (42)", font=font_tag, fill=(80, 75, 70))

# Item 2: Gulabi Festive Suit
p2_src = Image.open(os.path.join(highres_dir, "JAC25ST03063.jpg"))
p2_crop = p2_src.crop((60, 20, 1040, 1170)).resize((card_w, 240), Image.Resampling.LANCZOS)
p1.paste(p2_crop, (24 + card_w + 14, grid_y))
d1.rectangle([24 + card_w + 14, grid_y, 24 + card_w + 14 + card_w, grid_y + 240], outline=(228, 220, 210), width=1)

# Badge on Item 2
d1.rounded_rectangle([24 + card_w + 22, grid_y + 8, 24 + card_w + 116, grid_y + 28], radius=4, fill=(40, 90, 70))
d1.text((24 + card_w + 28, grid_y + 11), "LIMITED RUN", font=font_tag, fill=(255, 255, 255))

d1.text((24 + card_w + 14, grid_y + 248), "Gulabi Organza Suit", font=font_phone_bold, fill=(30, 28, 25))
d1.text((24 + card_w + 14, grid_y + 268), "Cotton Silk 3-Piece Set", font=font_phone_sm, fill=(120, 110, 100))
d1.text((24 + card_w + 14, grid_y + 288), "₹2,199", font=font_phone_bold, fill=(30, 28, 25))
d1.text((24 + card_w + 70, grid_y + 290), "₹3,499", font=font_phone_sm, fill=(150, 140, 130))
d1.line([(24 + card_w + 68, grid_y + 297), (24 + card_w + 110, grid_y + 297)], fill=(150, 140, 130), width=1)
d1.text((24 + card_w + 14, grid_y + 312), "Sizes: M (38) • L (40) • XL (42)", font=font_tag, fill=(80, 75, 70))

# Tricity Trust Strip
trust_y = 850
d1.rectangle([12, trust_y, PW - 12, trust_y + 70], fill=(244, 240, 233), outline=(230, 224, 215), width=1)
d1.text((28, trust_y + 14), "⚡ Chandigarh • Mohali • Panchkula Priority Delivery", font=font_phone_sm_bold, fill=(30, 28, 25))
d1.text((28, trust_y + 36), "Order today, arrives tomorrow  •  7-Day Easy Size Exchange", font=font_phone_sm, fill=(110, 100, 90))

# Bottom Nav Bar
nav_y = PH - 74
d1.rectangle([12, nav_y, PW - 12, PH - 12], fill=(250, 248, 245), outline=(225, 218, 208), width=1)
nav_items = [("Home", True), ("Shop", False), ("Search", False), ("Bag (0)", False)]
nx = 44
for n_txt, is_sel in nav_items:
    color = (30, 28, 25) if is_sel else (140, 130, 120)
    d1.text((nx, nav_y + 18), n_txt, font=font_phone_bold if is_sel else font_phone_body, fill=color)
    if is_sel:
        d1.line([(nx, nav_y + 40), (nx + 38, nav_y + 40)], fill=(30, 28, 25), width=2)
    nx += 120

# =========================================================================
# PHONE 2: PRODUCT DETAIL PAGE (PDP & 1-CLICK CHECKOUT)
# =========================================================================
p2 = create_phone_base()
d2 = ImageDraw.Draw(p2)

# Dynamic island / notch
d2.rounded_rectangle([PW//2 - 60, 22, PW//2 + 60, 44], radius=11, fill=(24, 24, 27))
# Status bar
d2.text((36, 26), "9:41", font=font_phone_sm_bold, fill=(30, 28, 25))
d2.text((PW - 70, 26), "5G  100%", font=font_phone_sm_bold, fill=(30, 28, 25))

# Top Announcement Bar
d2.rectangle([12, 54, PW - 12, 82], fill=(30, 28, 25))
ann2 = "✨ 1-CLICK UPI CHECKOUT • MEENULABEL.COM"
ab2 = d2.textbbox((0, 0), ann2, font=font_tag)
d2.text(((PW - (ab2[2]-ab2[0]))//2, 62), ann2, font=font_tag, fill=(245, 240, 230))

# Header with back arrow
d2.rectangle([12, 82, PW - 12, 136], fill=(250, 248, 245), outline=(230, 224, 215), width=1)
d2.text((32, 98), "←", font=font_phone_h1, fill=(30, 28, 25))
logo_txt2 = "MEENU LABEL"
lb2 = d2.textbbox((0, 0), logo_txt2, font=font_phone_brand)
d2.text(((PW - (lb2[2]-lb2[0]))//2, 97), logo_txt2, font=font_phone_brand, fill=(30, 28, 25))
d2.rectangle([PW - 56, 100, PW - 38, 120], outline=(30, 28, 25), width=2)
d2.text((PW - 50, 102), "1", font=font_phone_sm_bold, fill=(30, 28, 25))

# PDP Main Image
pdp_src = Image.open(os.path.join(highres_dir, "JAA26DR03942.jpg"))
pdp_img = pdp_src.crop((60, 20, 1040, 1170)).resize((PW - 24, 380), Image.Resampling.LANCZOS)
p2.paste(pdp_img, (12, 136))
d2.rectangle([12, 136, PW - 12, 136 + 380], outline=(230, 222, 212), width=1)

# Image carousel indicator
dots_x = PW // 2 - 24
for i in range(4):
    col = (30, 28, 25) if i == 0 else (180, 175, 168)
    d2.ellipse([dots_x + i*14, 136 + 360, dots_x + i*14 + 8, 136 + 368], fill=col)

# Breadcrumbs
pdp_y = 528
d2.text((28, pdp_y), "Home / Dresses / Drop 01", font=font_tag, fill=(130, 120, 110))

# Title & Price
d2.text((28, pdp_y + 18), "The Retro Polka Dot Wrap Dress", font=font_phone_h1, fill=(30, 28, 25))
d2.text((28, pdp_y + 46), "₹1,499", font=font_phone_h1, fill=(30, 28, 25))
d2.text((105, pdp_y + 50), "₹2,499", font=font_phone_bold, fill=(140, 130, 120))
d2.line([(103, pdp_y + 59), (155, pdp_y + 59)], fill=(140, 130, 120), width=1)
d2.rounded_rectangle([165, pdp_y + 48, 230, pdp_y + 68], radius=4, fill=(235, 245, 238))
d2.text((172, pdp_y + 51), "40% OFF", font=font_tag, fill=(35, 115, 65))
d2.text((28, pdp_y + 74), "Inclusive of all taxes  •  Free Shipping", font=font_tag, fill=(120, 110, 100))

# Size Selector
sz_y = pdp_y + 102
d2.text((28, sz_y), "SELECT SIZE", font=font_phone_sm_bold, fill=(30, 28, 25))
d2.text((PW - 120, sz_y), "📏 Size Guide", font=font_phone_sm_bold, fill=(110, 85, 55))

sizes = [("M (38\")", True, "Only 1 Left!"), ("L (40\")", False, "Only 1 Left!"), ("XL (42\")", False, "Only 1 Left!")]
sx = 28
for s_txt, is_sel, note in sizes:
    if is_sel:
        d2.rounded_rectangle([sx, sz_y + 20, sx + 140, sz_y + 64], radius=6, fill=(244, 240, 233), outline=(30, 28, 25), width=2)
        d2.text((sx + 14, sz_y + 26), s_txt, font=font_phone_sm_bold, fill=(30, 28, 25))
        d2.text((sx + 14, sz_y + 44), note, font=font_tag, fill=(180, 45, 35))
    else:
        d2.rounded_rectangle([sx, sz_y + 20, sx + 140, sz_y + 64], radius=6, fill=(250, 248, 245), outline=(225, 218, 208), width=1)
        d2.text((sx + 14, sz_y + 26), s_txt, font=font_phone_sm_bold, fill=(80, 75, 70))
        d2.text((sx + 14, sz_y + 44), note, font=font_tag, fill=(120, 110, 100))
    sx += 152

# Pincode Box
pin_y = sz_y + 82
d2.rounded_rectangle([28, pin_y, PW - 28, pin_y + 46], radius=6, fill=(245, 248, 244), outline=(200, 220, 205), width=1)
d2.text((40, pin_y + 8), "📍 Deliver to: 160017 (Chandigarh)", font=font_phone_sm_bold, fill=(30, 80, 45))
d2.text((40, pin_y + 26), "✓ Priority Dispatch: Arrives Tomorrow by 2 PM", font=font_tag, fill=(45, 110, 65))

# CTAs
cta_y = pin_y + 60
# Primary Add to Bag
d2.rounded_rectangle([28, cta_y, PW - 28, cta_y + 46], radius=6, fill=(30, 28, 25))
d2.text((PW//2 - 45, cta_y + 14), "ADD TO BAG", font=font_phone_sm_bold, fill=(255, 255, 255))

# Instant UPI Button
upi_y = cta_y + 54
d2.rounded_rectangle([28, upi_y, PW - 28, upi_y + 46], radius=6, fill=(225, 185, 125))
d2.text((PW//2 - 80, upi_y + 14), "⚡ BUY WITH UPI / GPAY", font=font_phone_sm_bold, fill=(30, 28, 25))

# WhatsApp 1-Click Order
wa_y = upi_y + 54
d2.rounded_rectangle([28, wa_y, PW - 28, wa_y + 42], radius=6, fill=(236, 248, 241), outline=(100, 185, 130), width=1)
d2.text((PW//2 - 85, wa_y + 13), "💬 Order via WhatsApp (Direct)", font=font_phone_sm_bold, fill=(25, 120, 60))

# =========================================================================
# PASTE PHONES ONTO CANVAS WITH SUBTLE SHADOWS
# =========================================================================
x_p1 = 180
x_p2 = 780
y_phones = 200

shadow = Image.new("RGBA", (PW + 40, PH + 40), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle([20, 20, PW + 20, PH + 20], radius=CORNER + 4, fill=(0, 0, 0, 70))
shadow_blur = shadow.filter(ImageFilter.GaussianBlur(18))

canvas.paste(shadow_blur, (x_p1 - 20, y_phones - 10), shadow_blur)
canvas.paste(p1, (x_p1, y_phones), p1)

canvas.paste(shadow_blur, (x_p2 - 20, y_phones - 10), shadow_blur)
canvas.paste(p2, (x_p2, y_phones), p2)

# =========================================================================
# RIGHT PANEL: DESIGN SYSTEM & ARCHITECTURAL HIGHLIGHTS
# =========================================================================
x_panel = 1380
y_p = 200

d.rounded_rectangle([x_panel, y_p, CW - 60, y_p + 1100], radius=16, fill=(252, 250, 246), outline=(225, 218, 208), width=1)

d.text((x_panel + 36, y_p + 40), "THE MEENU LABEL DESIGN SYSTEM", font=font_phone_h1, fill=(30, 28, 25))
d.text((x_panel + 36, y_p + 70), "Engineered for High-Converting Indian D2C Fashion", font=font_phone_sm, fill=(120, 110, 100))
d.line([(x_panel + 36, y_p + 100), (CW - 96, y_p + 100)], fill=(225, 218, 208), width=1)

features = [
    ("1. Visual-First Editorial Layout",
     "Zero bounce intro slides. High-res authentic catalog photos fill 75%+ of the screen so shoppers fall in love with the silhouette in under 0.5s.",
     (40, 40, 45)),
    ("2. Genuine Drop 01 Scarcity Badges",
     "Subtle 'Only 1 Left in M' tags trigger immediate buying behavior without tacky countdown timers. Tailored to your exact 3-piece inventory per design.",
     (180, 50, 40)),
    ("3. Tricity Same-Day / 24-Hr Delivery Perk",
     "Pin-code intelligence highlights 24-hr priority delivery for Chandigarh, Mohali & Panchkula (Pincodes 160xxx, 140xxx, 134xxx) creating unmatched local trust.",
     (35, 115, 65)),
    ("4. Instant 1-Click UPI & WhatsApp Checkout",
     "No 10-step checkout friction. Indian shoppers pay in 2 taps using Google Pay, PhonePe, Paytm or direct WhatsApp confirmation.",
     (175, 125, 45)),
    ("5. Clean Size Guide (Bust 38\" • 40\" • 42\")",
     "Prominent chest measurement sizing prevents size uncertainty and slashes return/exchange rates by up to 80%.",
     (60, 55, 50)),
    ("6. Warm Porcelain Ivory Palette",
     "#FAF8F5 canvas + #1E1C19 charcoal text + taupe accents creates an understated luxury aesthetic comparable to Zara, Buna & Raw Mango.",
     (120, 95, 70))
]

cur_y = y_p + 125
for title, desc, tag_col in features:
    d.rounded_rectangle([x_panel + 36, cur_y, x_panel + 44, cur_y + 50], radius=4, fill=tag_col)
    d.text((x_panel + 56, cur_y), title, font=font_anno_title, fill=(30, 28, 25))
    
    words = desc.split()
    line1, line2, line3 = "", "", ""
    for w in words:
        if len(line1) + len(w) < 48:
            line1 += w + " "
        elif len(line2) + len(w) < 48:
            line2 += w + " "
        else:
            line3 += w + " "
    d.text((x_panel + 56, cur_y + 24), line1.strip(), font=font_anno_desc, fill=(100, 95, 88))
    if line2:
        d.text((x_panel + 56, cur_y + 44), line2.strip(), font=font_anno_desc, fill=(100, 95, 88))
    if line3:
        d.text((x_panel + 56, cur_y + 64), line3.strip(), font=font_anno_desc, fill=(100, 95, 88))
    
    cur_y += 105

# Bottom tech badge
tech_y = y_p + 880
d.rounded_rectangle([x_panel + 36, tech_y, CW - 96, tech_y + 170], radius=10, fill=(244, 240, 233), outline=(215, 205, 195), width=1)
d.text((x_panel + 56, tech_y + 20), "TECH STACK & INTEGRATIONS", font=font_phone_sm_bold, fill=(30, 28, 25))
d.text((x_panel + 56, tech_y + 48), "• Shopify Online Store 2.0 (Custom Liquid & CSS Tokens)", font=font_phone_sm, fill=(80, 75, 70))
d.text((x_panel + 56, tech_y + 72), "• Razorpay / Cashfree 1-Click UPI & Card Payments", font=font_phone_sm, fill=(80, 75, 70))
d.text((x_panel + 56, tech_y + 96), "• Shiprocket Direct API (Instant 4x6 Thermal Label Printing)", font=font_phone_sm, fill=(80, 75, 70))
d.text((x_panel + 56, tech_y + 120), "• Official Custom Domain: meenulabel.com", font=font_phone_sm_bold, fill=(30, 28, 25))

# Save outputs
out_png = os.path.join(scratch_dir, "Meenu_Label_Website_Design_Mockup.png")
canvas.save(out_png, "PNG")

out_downloads = os.path.join(downloads_dir, "Meenu_Label_Website_Design_Mockup.png")
canvas.save(out_downloads, "PNG")

out_artifacts = os.path.join(artifacts_dir, "Meenu_Label_Website_Design_Mockup.png")
canvas.save(out_artifacts, "PNG")

print("Generated Meenu_Label_Website_Design_Mockup.png successfully!")

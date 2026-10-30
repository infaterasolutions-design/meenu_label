import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
highres_dir = os.path.join(scratch_dir, "highres_products")
banners_dir = os.path.join(scratch_dir, "banners")
os.makedirs(banners_dir, exist_ok=True)

BW, BH = 1800, 720

font_bold = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 60)
font_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 52)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 16)
font_quote = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 26)
font_btn = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 15)

def make_banner_1():
    # Polka Dress Banner
    # Studio color sampled from JAA26DR03942: ~ (238, 219, 192)
    bg_color = (238, 220, 194)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAA26DR03942.jpg"))
    # Crop model and plants: w=900, h=1050
    model = src.crop((60, 40, 1040, 1150)).resize((660, 720), Image.Resampling.LANCZOS)
    
    # Create soft horizontal gradient alpha mask on left and right edges so it blends seamlessly
    mask = Image.new("L", (660, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(70):
        a = int(255 * (x / 70.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(660 - 1 - x, 0), (660 - 1 - x, 720)], fill=a)
        
    banner.paste(model, (620, 0), mask)
    
    d = ImageDraw.Draw(banner)
    
    # Left typography (Snitch style: large, clean, bold/thin mix)
    x_left = 120
    d.text((x_left, 180), "RETRO,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "BREATHABLE, BETTER.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 335), "100% PURE COTTON  •  CINCHED WAIST  •  DROP 01", font=font_sub, fill=(110, 95, 80))
    
    # CTA button
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 36, 396), "EXPLORE DROP 01  →", font=font_btn, fill=(255, 255, 255))
    
    # Right secondary quote (Snitch style)
    d.text((BW - 420, 560), "MORE BREEZE.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 420, 595), "MORE ATTITUDE.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_1_polka.jpg")
    banner.save(out_path, "JPEG", quality=92)
    print("Saved banner_1_polka.jpg")

def make_banner_2():
    # Chanderi Festive Suit Banner
    # Studio color sampled from JAB26ST05010: ~ (244, 238, 228)
    bg_color = (244, 238, 228)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAB26ST05010.jpg"))
    model = src.crop((60, 40, 1040, 1150)).resize((660, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (660, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(70):
        a = int(255 * (x / 70.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(660 - 1 - x, 0), (660 - 1 - x, 720)], fill=a)
        
    banner.paste(model, (620, 0), mask)
    
    d = ImageDraw.Draw(banner)
    
    x_left = 120
    d.text((x_left, 180), "REGAL,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "AIRY, FESTIVE.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 335), "PURE JAIPUR CHANDERI SILK  •  HANDCRAFTED ZARI", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 40, 396), "SHOP FESTIVE SUIT  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 440, 560), "LIGHTWEIGHT SILK.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 440, 595), "ROYAL CELEBRATION.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_2_chanderi.jpg")
    banner.save(out_path, "JPEG", quality=92)
    print("Saved banner_2_chanderi.jpg")

def make_banner_3():
    # Gulabi Organza Suit Banner
    bg_color = (235, 225, 218)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAC25ST03063.jpg"))
    model = src.crop((60, 40, 1040, 1150)).resize((660, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (660, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(70):
        a = int(255 * (x / 70.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(660 - 1 - x, 0), (660 - 1 - x, 720)], fill=a)
        
    banner.paste(model, (620, 0), mask)
    
    d = ImageDraw.Draw(banner)
    
    x_left = 120
    d.text((x_left, 180), "GULABI,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "POWDER PINK GRACE.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 335), "COTTON SILK ENSEMBLE  •  FLORAL ORGANZA DUPATTA", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 38, 396), "VIEW GULABI SUIT  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 420, 560), "SUBTLE LUXURY.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 420, 595), "LIMITED 3 PIECES.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_3_gulabi.jpg")
    banner.save(out_path, "JPEG", quality=92)
    print("Saved banner_3_gulabi.jpg")

make_banner_1()
make_banner_2()
make_banner_3()

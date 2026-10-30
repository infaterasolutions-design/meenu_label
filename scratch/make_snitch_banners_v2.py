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
    bg_color = (238, 220, 194)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAA26DR03942.jpg"))
    model = src.crop((60, 40, 1040, 1150)).resize((660, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (660, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(80):
        a = int(255 * (x / 80.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(660 - 1 - x, 0), (660 - 1 - x, 720)], fill=a)
        
    banner.paste(model, (620, 0), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 120
    d.text((x_left, 180), "RETRO,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "BREATHABLE, BETTER.", font=font_light, fill=(20, 18, 16))
    d.text((x_left, 335), "100% PURE COTTON  •  CINCHED WAIST  •  DROP 01", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 36, 396), "EXPLORE DROP 01  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 420, 560), "MORE BREEZE.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 420, 595), "MORE ATTITUDE.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_1_polka.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_1_polka.jpg")

def make_banner_2():
    # Chanderi Festive Suit Banner
    bg_color = (244, 238, 228)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAB26ST05010.jpg"))
    model = src.crop((60, 40, 1040, 1150)).resize((660, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (660, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(80):
        a = int(255 * (x / 80.0))
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
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_2_chanderi.jpg")

def make_banner_3():
    # SET916 Pleated Halter Co-ord Banner
    bg_color = (236, 224, 210)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "SET916.jpg"))
    # Crop: x from 90 to 1030, y from 40 to 1090 (excludes left "916" and bottom black table)
    model = src.crop((90, 40, 1030, 1090)).resize((650, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (650, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(80):
        a = int(255 * (x / 80.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(650 - 1 - x, 0), (650 - 1 - x, 720)], fill=a)
    # subtle feather on bottom
    for y in range(20):
        a = int(255 * (y / 20.0))
        for x in range(650):
            current = mask.getpixel((x, 719 - y))
            mask.putpixel((x, 719 - y), min(current, a))
        
    banner.paste(model, (620, 0), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 120
    d.text((x_left, 180), "EFFORTLESS,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "FLOWING, CHIC.", font=font_light, fill=(20, 18, 16))
    d.text((x_left, 335), "PLEATED HALTER TOP  •  WIDE-LEG SILHOUETTE  •  LIME", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 42, 396), "SHOP CO-ORD SET  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 420, 560), "MINIMAL CUT.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 420, 595), "TIMELESS COMFORT.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_3_coord.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_3_coord.jpg")

def make_banner_4():
    # Gulabi Organza Suit Banner (clean crop, y=105 to 1150)
    bg_color = (226, 214, 204)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAC25ST03063.jpg"))
    # Clean crop strictly below top black line (y=105 to 1150)
    model = src.crop((100, 105, 1000, 1155)).resize((620, 720), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (620, 720), 255)
    md = ImageDraw.Draw(mask)
    for x in range(90):
        a = int(255 * (x / 90.0))
        md.line([(x, 0), (x, 720)], fill=a)
        md.line([(620 - 1 - x, 0), (620 - 1 - x, 720)], fill=a)
    for y in range(40):
        a = int(255 * (y / 40.0))
        for x in range(620):
            current = mask.getpixel((x, y))
            mask.putpixel((x, y), min(current, a))
            current_b = mask.getpixel((x, 719 - y))
            mask.putpixel((x, 719 - y), min(current_b, a))
        
    banner.paste(model, (640, 0), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 120
    d.text((x_left, 180), "GULABI,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 246), "POWDER PINK GRACE.", font=font_light, fill=(20, 18, 16))
    d.text((x_left, 335), "COTTON SILK ENSEMBLE  •  FLORAL ORGANZA DUPATTA", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 380, x_left + 220, 432], radius=4, fill=(20, 18, 16))
    d.text((x_left + 38, 396), "VIEW GULABI SUIT  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 420, 560), "SUBTLE LUXURY.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 420, 595), "HERITAGE PRINTS.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_4_gulabi.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_4_gulabi.jpg")

if __name__ == "__main__":
    make_banner_1()
    make_banner_2()
    make_banner_3()
    make_banner_4()

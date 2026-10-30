import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
highres_dir = os.path.join(scratch_dir, "highres_products")
banners_dir = os.path.join(scratch_dir, "banners")
os.makedirs(banners_dir, exist_ok=True)

# Full HD Desktop Cinematic Banner Dimensions: 1920 x 960
BW, BH = 1920, 960

font_bold = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 72)
font_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 62)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 18)
font_quote = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 28)
font_btn = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 16)

def extend_seamless_headroom(model_crop, pad_top, hair_x_left, hair_x_right, bg_color):
    """
    Extends the natural background above the model crop without dragging hair pixels upwards.
    Uses the wall on the left of the head and the wall/curtain on the right.
    """
    mw, mh = model_crop.size
    ext = Image.new("RGB", (mw, mh + pad_top), bg_color)
    
    # Left background slice
    left_slice = model_crop.crop((0, 0, max(hair_x_left, 10), 2)).resize((mw // 2, pad_top + 10))
    # Right background slice
    right_slice = model_crop.crop((min(hair_x_right, mw - 10), 0, mw, 2)).resize((mw - mw // 2, pad_top + 10))
    
    ext.paste(left_slice, (0, 0))
    ext.paste(right_slice, (mw // 2, 0))
    
    top_blurred = ext.crop((0, 0, mw, pad_top + 10)).filter(ImageFilter.GaussianBlur(4))
    ext.paste(top_blurred, (0, 0))
    ext.paste(model_crop, (0, pad_top))
    return ext

def make_banner_1():
    # Polka Dress Banner
    bg_color = (238, 220, 194)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAA26DR03942.jpg"))
    raw_model = src.crop((60, 40, 1040, 1150))
    # Hair is between x=400 and x=560 in this crop
    ext_model = extend_seamless_headroom(raw_model, 160, 380, 580, bg_color)
    
    model = ext_model.resize((720, 860), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (720, 860), 255)
    md = ImageDraw.Draw(mask)
    for x in range(90):
        a = int(255 * (x / 90.0))
        md.line([(x, 0), (x, 860)], fill=a)
        md.line([(720 - 1 - x, 0), (720 - 1 - x, 860)], fill=a)
        
    banner.paste(model, (620, 50), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 140
    d.text((x_left, 260), "RETRO,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 338), "BREATHABLE, BETTER.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 440), "100% PURE COTTON  •  CINCHED WAIST  •  DROP 01", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 495, x_left + 240, 555], radius=4, fill=(20, 18, 16))
    d.text((x_left + 42, 514), "EXPLORE DROP 01  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 440, 720), "MORE BREEZE.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 440, 760), "MORE ATTITUDE.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_1_polka.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_1_polka.jpg (1920x960)")

def make_banner_2():
    # Chanderi Festive Suit Banner
    bg_color = (244, 238, 228)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAB26ST05010.jpg"))
    raw_model = src.crop((60, 40, 1040, 1150))
    ext_model = extend_seamless_headroom(raw_model, 160, 400, 580, bg_color)
    
    model = ext_model.resize((720, 860), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (720, 860), 255)
    md = ImageDraw.Draw(mask)
    for x in range(90):
        a = int(255 * (x / 90.0))
        md.line([(x, 0), (x, 860)], fill=a)
        md.line([(720 - 1 - x, 0), (720 - 1 - x, 860)], fill=a)
        
    banner.paste(model, (620, 50), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 140
    d.text((x_left, 260), "REGAL,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 338), "AIRY, FESTIVE.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 440), "PURE JAIPUR CHANDERI SILK  •  HANDCRAFTED ZARI", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 495, x_left + 240, 555], radius=4, fill=(20, 18, 16))
    d.text((x_left + 44, 514), "SHOP FESTIVE SUIT  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 460, 720), "LIGHTWEIGHT SILK.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 460, 760), "ROYAL CELEBRATION.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_2_chanderi.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_2_chanderi.jpg (1920x960)")

def make_banner_3():
    # SET916 Pleated Halter Co-ord Banner
    bg_color = (236, 224, 210)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "SET916.jpg"))
    raw_model = src.crop((90, 25, 1030, 1090))
    ext_model = extend_seamless_headroom(raw_model, 160, 390, 570, bg_color)
    
    model = ext_model.resize((720, 860), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (720, 860), 255)
    md = ImageDraw.Draw(mask)
    for x in range(90):
        a = int(255 * (x / 90.0))
        md.line([(x, 0), (x, 860)], fill=a)
        md.line([(720 - 1 - x, 0), (720 - 1 - x, 860)], fill=a)
        
    banner.paste(model, (620, 50), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 140
    d.text((x_left, 260), "EFFORTLESS,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 338), "FLOWING, CHIC.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 440), "PLEATED HALTER TOP  •  WIDE-LEG PALAZZO  •  LIME", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 495, x_left + 240, 555], radius=4, fill=(20, 18, 16))
    d.text((x_left + 46, 514), "SHOP CO-ORD SET  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 440, 720), "MINIMAL CUT.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 440, 760), "TIMELESS COMFORT.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_3_coord.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_3_coord.jpg (1920x960)")

def make_banner_4():
    # Gulabi Organza Suit Banner
    bg_color = (226, 214, 204)
    banner = Image.new("RGB", (BW, BH), bg_color)
    
    src = Image.open(os.path.join(highres_dir, "JAC25ST03063.jpg"))
    raw_model = src.crop((80, 108, 1020, 1150))
    
    pad_top = 160
    ext = Image.new("RGB", (raw_model.width, raw_model.height + pad_top), bg_color)
    wall_slice = raw_model.crop((0, 0, 380, 2)).resize((440, pad_top + 10))
    curtain_slice = raw_model.crop((560, 0, raw_model.width, 2)).resize((raw_model.width - 440, pad_top + 10))
    ext.paste(wall_slice, (0, 0))
    ext.paste(curtain_slice, (440, 0))
    top_bg = ext.crop((0, 0, raw_model.width, pad_top + 10)).filter(ImageFilter.GaussianBlur(3))
    ext.paste(top_bg, (0, 0))
    ext.paste(raw_model, (0, pad_top))
    
    model = ext.resize((700, 860), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (700, 860), 255)
    md = ImageDraw.Draw(mask)
    for x in range(95):
        a = int(255 * (x / 95.0))
        md.line([(x, 0), (x, 860)], fill=a)
        md.line([(700 - 1 - x, 0), (700 - 1 - x, 860)], fill=a)
        
    banner.paste(model, (630, 50), mask)
    
    d = ImageDraw.Draw(banner)
    x_left = 140
    d.text((x_left, 260), "GULABI,", font=font_bold, fill=(20, 18, 16))
    d.text((x_left, 338), "POWDER PINK GRACE.", font=font_light, fill=(20, 18, 16))
    
    d.text((x_left, 440), "COTTON SILK ENSEMBLE  •  FLORAL ORGANZA DUPATTA", font=font_sub, fill=(110, 95, 80))
    
    d.rounded_rectangle([x_left, 495, x_left + 240, 555], radius=4, fill=(20, 18, 16))
    d.text((x_left + 42, 514), "VIEW GULABI SUIT  →", font=font_btn, fill=(255, 255, 255))
    
    d.text((BW - 440, 720), "SUBTLE LUXURY.", font=font_quote, fill=(70, 60, 50))
    d.text((BW - 440, 760), "HERITAGE PRINTS.", font=font_quote, fill=(70, 60, 50))
    
    out_path = os.path.join(banners_dir, "banner_4_gulabi.jpg")
    banner.save(out_path, "JPEG", quality=95)
    print("Saved banner_4_gulabi.jpg (1920x960)")

if __name__ == "__main__":
    make_banner_1()
    make_banner_2()
    make_banner_3()
    make_banner_4()

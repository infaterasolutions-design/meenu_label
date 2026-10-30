import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
highres_dir = os.path.join(scratch_dir, "highres_products")

# Snitch exact dimensions
BW, BH = 1500, 708

# Fonts
font_tag = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 13)
font_bold = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 52)
font_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 46)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\calibri.ttf", 16)
font_specs = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 13)
font_btn = ImageFont.truetype(r"C:\Windows\Fonts\calibrib.ttf", 14)
font_quote = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 22)
font_quote_light = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 20)

def render_editorial_slide_gulabi():
    # Canvas
    canvas = Image.new("RGB", (BW, BH), (247, 245, 240))
    d = ImageDraw.Draw(canvas)
    
    # 1. Subtle background grid / architectural line
    d.line([(60, 60), (BW - 60, 60)], fill=(235, 230, 222), width=1)
    d.line([(60, BH - 60), (BW - 60, BH - 60)], fill=(235, 230, 222), width=1)
    
    # 2. Left Typography Section
    x_left = 90
    y_start = 140
    
    # Season / Drop Tag
    d.rounded_rectangle([x_left, y_start, x_left + 190, y_start + 28], radius=14, fill=(238, 233, 225))
    d.ellipse([x_left + 10, y_start + 10, x_left + 18, y_start + 18], fill=(184, 134, 11))
    d.text((x_left + 26, y_start + 6), "DROP 01 ? LIMITED RUN", font=font_tag, fill=(70, 60, 50))
    
    # Main Headline
    d.text((x_left, y_start + 45), "GULABI,", font=font_bold, fill=(24, 22, 20))
    d.text((x_left, y_start + 105), "POWDER PINK GRACE.", font=font_light, fill=(40, 36, 32))
    
    # Subtitle
    d.text((x_left, y_start + 180), "Cotton Silk Ensemble ? Handcrafted Floral Organza Dupatta", font=font_sub, fill=(110, 100, 90))
    
    # Specs line
    d.text((x_left, y_start + 220), "Fit: Straight-Cut Festive  ?  Surat Looms  ?  Strictly 3 Pieces", font=font_specs, fill=(140, 130, 120))
    
    # CTA Button (Snitch style)
    btn_y = y_start + 270
    btn_w, btn_h = 220, 50
    d.rounded_rectangle([x_left, btn_y, x_left + btn_w, btn_y + btn_h], radius=4, fill=(24, 22, 20))
    d.text((x_left + 36, btn_y + 16), "VIEW GULABI SUIT  +'", font=font_btn, fill=(255, 255, 255))
    
    # 3. Model Editorial Portrait Card (Center/Right)
    model_src = Image.open(os.path.join(highres_dir, "JAC25ST03063.jpg"))
    # Clean crop preserving full head and drape: 520 wide x 600 high
    mw, mh = 500, 580
    model_resized = model_src.resize((mw, mh), Image.Resampling.LANCZOS)
    
    card_x = 650
    card_y = (BH - mh) // 2
    
    # Soft drop shadow for editorial card
    shadow = Image.new("RGBA", (mw + 40, mh + 40), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([20, 20, mw + 20, mh + 20], radius=12, fill=(0, 0, 0, 35))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    canvas.paste(shadow, (card_x - 20, card_y - 10), shadow)
    
    # Paste model
    # Create mask for rounded corners
    card_mask = Image.new("L", (mw, mh), 0)
    cmd = ImageDraw.Draw(card_mask)
    cmd.rounded_rectangle([0, 0, mw, mh], radius=12, fill=255)
    canvas.paste(model_resized, (card_x, card_y), card_mask)
    
    # Subtle card border
    d.rounded_rectangle([card_x, card_y, card_x + mw, card_y + mh], radius=12, outline=(220, 210, 200), width=1)
    
    # Floating tag on card
    tag_x, tag_y = card_x + 20, card_y + 20
    d.rounded_rectangle([tag_x, tag_y, tag_x + 130, tag_y + 26], radius=4, fill=(255, 255, 255, 220))
    d.text((tag_x + 12, tag_y + 6), "Only 3 Pieces Left", font=font_tag, fill=(180, 50, 40))
    
    # 4. Right Typographic Statement (Snitch style, safely inside 1500px boundary)
    d.text((BW - 280, 260), "SUBTLE LUXURY.", font=font_quote, fill=(60, 50, 42))
    d.text((BW - 280, 292), "HERITAGE PRINTS.", font=font_quote_light, fill=(100, 90, 80))
    d.line([(BW - 280, 335), (BW - 120, 335)], fill=(210, 200, 190), width=1)
    d.text((BW - 280, 350), "SURAT ATELIER", font=font_tag, fill=(140, 130, 120))
    
    # 5. Snitch Navigation Elements
    # Chevrons
    d.ellipse([24, BH//2 - 22, 68, BH//2 + 22], fill=(255, 255, 255), outline=(230, 225, 218), width=1)
    d.text((40, BH//2 - 14), "<", font=font_btn, fill=(60, 50, 40))
    
    d.ellipse([BW - 68, BH//2 - 22, BW - 24, BH//2 + 22], fill=(255, 255, 255), outline=(230, 225, 218), width=1)
    d.text((BW - 52, BH//2 - 14), ">", font=font_btn, fill=(60, 50, 40))
    
    # Progress Dots at Bottom Center
    dots_x = BW // 2 - 50
    dots_y = BH - 38
    d.ellipse([dots_x, dots_y, dots_x + 8, dots_y + 8], fill=(190, 180, 170))
    d.ellipse([dots_x + 20, dots_y, dots_x + 28, dots_y + 8], fill=(190, 180, 170))
    d.ellipse([dots_x + 40, dots_y, dots_x + 48, dots_y + 8], fill=(190, 180, 170))
    # Active dot (elongated pill like Snitch)
    d.rounded_rectangle([dots_x + 60, dots_y - 1, dots_x + 92, dots_y + 9], radius=5, fill=(24, 22, 20))
    
    # Atelier Pill (Bottom Right)
    pill_w = 270
    pill_x = BW - pill_w - 40
    pill_y = BH - 48
    d.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + 32], radius=16, fill=(255, 255, 255), outline=(220, 215, 208), width=1)
    d.ellipse([pill_x + 14, pill_y + 11, pill_x + 24, pill_y + 21], fill=(46, 125, 50))
    d.text((pill_x + 32, pill_y + 8), "DROP 01 ? STRICTLY 48 PIECES TOTAL", font=font_tag, fill=(40, 36, 32))
    
    out_path = os.path.join(scratch_dir, "test_snitch_clean_slide.jpg")
    canvas.save(out_path, quality=95)
    print("SUCCESS: Rendered test_snitch_clean_slide.jpg (1500x708)")

if __name__ == "__main__":
    render_editorial_slide_gulabi()

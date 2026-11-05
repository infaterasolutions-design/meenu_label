from PIL import Image

p = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(p)
w, h = im.size

# Let's check aspect ratio and dimensions
print(f"Original size: {w}x{h}")

# In the theme, hero banners are typically 1500x708 or 1500x600, or standard JPEG/PNG
# Let's save a preview thumbnail to inspect
thumb = im.copy()
thumb.thumbnail((800, 320))
thumb.save(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\maroon_thumb.jpg', 'JPEG', quality=85)
print("Saved thumbnail")

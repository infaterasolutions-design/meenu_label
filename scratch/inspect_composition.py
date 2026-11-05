from PIL import Image

p = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(p)
w, h = im.size

# Check left 1/3, center 1/3, right 1/3
left = im.crop((0, 0, w//3, h))
center = im.crop((w//3, 0, 2*w//3, h))
right = im.crop((2*w//3, 0, w, h))

# Save crops to scratch to inspect
left.thumbnail((400, 200))
center.thumbnail((400, 200))
right.thumbnail((400, 200))

left.save(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\crop_left.jpg', 'JPEG')
center.save(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\crop_center.jpg', 'JPEG')
right.save(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\crop_right.jpg', 'JPEG')

print(f"Original size: {w}x{h}")
print("Saved left, center, right crops to inspect composition.")

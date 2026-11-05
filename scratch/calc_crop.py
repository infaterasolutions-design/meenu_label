from PIL import Image

src_path = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(src_path)
w, h = im.size
print(f"Original: {w}x{h}")

# Desktop 1500x708:
# Target aspect: 1500/708 = 2.1186
# Source aspect: 1983/793 = 2.5006
# To fit 2.1186 without distortion, we crop horizontally or resize.
# If height is 793, target width for 2.1186 is 793 * 1500 / 708 = 1680 px.
# We have 1983 px width. That means we have 1983 - 1680 = 303 px extra width.
# Where is the extra width?
# Left side has the text. Right side has the model and arch.
# Let's see: if we keep the full image or crop slightly from left/right:
print(f"Excess width for 1500x708 aspect: {w - int(h * 1500 / 708)}px")

# Also, what if we keep 1983x793 as the asset directly?
# In CSS: background-size: cover; background-position: center center;
# On a 1500px wide container, height 708:
# image rendered at height 708 will be width = 708 * (1983/793) = 1770px.
# It overflows container by 270px (135px left, 135px right).
# Does 135px crop cut off the text "MEENU LABEL" on the left?
# Let's measure where "MEENU LABEL" starts from x=0!

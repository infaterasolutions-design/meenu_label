import base64

# Convert banner_festive_maroon.jpg to base64
with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\banner_festive_maroon.jpg', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

data_uri = f"data:image/jpeg;base64,{b64_data}"

with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find Slide 1 in index.html
start = html.find('<!-- Slide 1:')
end = html.find('<!-- Slide 2:', start)

if start != -1 and end != -1:
    old_slide1 = html[start:end]
    new_slide1 = f"""<!-- Slide 1: Festive Maroon Elegance in Bloom (Flagship Festive Suit) -->
        <div class="snitch-slide snitch-slide-maroon" style="background-image: url('{data_uri}'); cursor: pointer;" onclick="window.location.href='#festive-suits'" title="Shop Festive Maroon Elegance in Bloom">
        </div>

        """
    html = html[:start] + new_slide1 + html[end:]
    with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html Slide 1 with Festive Maroon Elegance base64 banner!")
else:
    print("Could not find Slide 1 boundaries in index.html")

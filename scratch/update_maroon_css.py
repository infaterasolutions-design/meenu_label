import os

css_paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-luxury.css',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css'
]

# We need to make sure the root meenu-luxury.css has the clean rules for snitch-slide-maroon
with open(css_paths[0], 'r', encoding='utf-8') as f:
    css = f.read()

maroon_styles = """
/* =========================================================================
   FESTIVE MAROON ELEGANCE IN BLOOM - HERO BANNER 1
   ========================================================================= */
.snitch-slide-maroon {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  cursor: pointer !important;
}
.snitch-slide.snitch-slide-maroon::after {
  display: none !important;
  content: none !important;
}
@media (max-width: 768px) {
  .snitch-slide.snitch-slide-maroon {
    background-position: 72% center !important; /* Perfectly frames the model in festive maroon on mobile */
  }
}
"""

if 'snitch-slide-maroon' not in css:
    css += maroon_styles
    print("Added snitch-slide-maroon styles to root meenu-luxury.css")

with open(css_paths[0], 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved root meenu-luxury.css")

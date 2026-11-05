# Test SVG render
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <line x1="12" y1="4" x2="12" y2="16"></line>
  <line x1="6" y1="10" x2="18" y2="10"></line>
  <line x1="4" y1="20" x2="20" y2="20"></line>
</svg>"""

with open("scratch/test_plus_icon.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
print("Saved scratch/test_plus_icon.svg")

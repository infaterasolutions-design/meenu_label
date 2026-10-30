with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the duplicate functions block at the bottom
dup_marker = "// --- Navigation & Search Bar Controls ---"
if dup_marker in js:
    # We only want to keep toggleSearchBar and the DOMContentLoaded listener
    parts = js.split(dup_marker)
    base = parts[0]
    
    clean_tail = """// --- Navigation & Search Bar Controls ---
function toggleSearchBar() {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  if (bar.style.display === 'block') {
    bar.style.display = 'none';
  } else {
    bar.style.display = 'block';
    var inp = document.getElementById('searchInput');
    if (inp) inp.focus();
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var heroEl = document.getElementById('heroSlider');
  if (heroEl) {
    heroEl.addEventListener('mouseenter', stopAutoSlide);
    heroEl.addEventListener('mouseleave', startAutoSlide);
    startAutoSlide();
  }
});
"""
    new_js = base + clean_tail
    with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("meenu-theme.js cleaned successfully! New length:", len(new_js))

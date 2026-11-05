import os

def update_file(path, old_sub, new_sub, label=""):
    if not os.path.exists(path):
        print(f"Skipping {path} (does not exist)")
        return False
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_sub not in content:
        print(f"WARNING: Target not found in {path} [{label}]")
        return False
    new_content = content.replace(old_sub, new_sub, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated {path} [{label}]")
    return True

print("=== APPLYING SEARCH CLOSE BUTTON FIX ===")

# 1. Update meenu-luxury.css in both assets and meenu-label-shopify-theme/assets
css_paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-luxury.css',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css'
]

css_old_override = """/* Search Overlay Bar Clickability & Layering Fix */
.search-overlay-bar {
  z-index: 250 !important;
}
.search-overlay-bar.open {
  display: block !important;
  opacity: 1 !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
  visibility: visible !important;
}
.search-input-box {
  position: relative !important;
  z-index: 260 !important;
}
.search-input-box input {
  pointer-events: auto !important;
}"""

css_new_override = """/* Search Overlay Bar Clickability & Layering Fix */
.search-overlay-bar {
  z-index: 250 !important;
}
.search-overlay-bar.open {
  display: block !important;
  opacity: 1 !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
  visibility: visible !important;
}
.search-input-box {
  position: relative !important;
  z-index: 260 !important;
  padding-right: 84px !important;
}
.search-input-box input {
  pointer-events: auto !important;
}
.search-close-action {
  position: absolute !important;
  top: 0 !important;
  right: 0 !important;
  z-index: 280 !important;
  pointer-events: auto !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 6px 12px !important;
  min-height: 36px !important;
  min-width: 65px !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: var(--text-muted) !important;
  background: transparent !important;
  border: none !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  transition: color 0.18s ease, transform 0.18s ease !important;
}
.search-close-action:hover {
  color: var(--text-main) !important;
  transform: scale(1.05) !important;
}"""

for p in css_paths:
    update_file(p, css_old_override, css_new_override, "CSS override")

# 2. Update meenu-theme.js in both assets and meenu-label-shopify-theme/assets
js_paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-theme.js',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js'
]

js_old = """function toggleSearchBar() {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  bar.classList.toggle('open');
  if (bar.classList.contains('open')) {
    var inp = document.getElementById('searchInput');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  }
}"""

js_new = """function closeSearchBar(e) {
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  var bar = document.getElementById('searchOverlayBar');
  if (bar) bar.classList.remove('open');
}

function toggleSearchBar(e) {
  if (e) {
    if (typeof e.preventDefault === 'function') e.preventDefault();
    if (typeof e.stopPropagation === 'function') e.stopPropagation();
  }
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  var willOpen = !bar.classList.contains('open');
  bar.classList.toggle('open');
  if (willOpen) {
    var inp = document.getElementById('searchInput');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  }
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
    closeSearchBar();
  }
});

document.addEventListener('click', function(e) {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar || !bar.classList.contains('open')) return;
  var isSearchTrigger = e.target.closest && e.target.closest('.header-search-btn, .search-close-action, [onclick*="toggleSearchBar"], [onclick*="closeSearchBar"]');
  var isInsideBar = bar.contains(e.target);
  if (!isInsideBar && !isSearchTrigger) {
    closeSearchBar();
  }
});"""

for p in js_paths:
    update_file(p, js_old, js_new, "JS functions")

# 3. Update sections/header.liquid in both root and meenu-label-shopify-theme
header_paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\sections\header.liquid',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\header.liquid'
]

header_old_btn = '<button class="header-icon-action header-search-btn" onclick="toggleSearchBar()"'
header_new_btn = '<button class="header-icon-action header-search-btn" onclick="toggleSearchBar(event)"'

header_old_close = '<button type="button" class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>'
header_new_close = '<button type="button" class="search-close-action" id="searchCloseBtn" onclick="closeSearchBar(event)" title="Close Search" aria-label="Close Search">Close &times;</button>'

for p in header_paths:
    update_file(p, header_old_btn, header_new_btn, "Header search trigger")
    update_file(p, header_old_close, header_new_close, "Header close action")

# 4. Update index.html
index_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html'

# Index CSS
index_old_input = """.search-input-box {
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
    }"""

index_new_input = """.search-input-box {
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
      padding-right: 84px;
      position: relative;
    }"""

index_old_close_css = """.search-close-action {
      position: absolute;
      top: 0;
      right: 0;
      background: none;
      border: none;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      padding: 4px 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .search-close-action:hover { color: var(--text-main); }"""

index_new_close_css = """.search-close-action {
      position: absolute;
      top: 0;
      right: 0;
      z-index: 280;
      pointer-events: auto;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 12px;
      min-height: 36px;
      min-width: 65px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      background: none;
      border: none;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      transition: color 0.18s ease, transform 0.18s ease;
    }
    .search-close-action:hover {
      color: var(--text-main);
      transform: scale(1.05);
    }"""

index_old_search_btn = '<button class="header-icon-action" onclick="toggleSearchBar()" title="Search Drop 01"'
index_new_search_btn = '<button class="header-icon-action" onclick="toggleSearchBar(event)" title="Search Drop 01"'

index_old_search_close = '<button class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>'
index_new_search_close = '<button type="button" class="search-close-action" id="searchCloseBtn" onclick="closeSearchBar(event)" title="Close Search" aria-label="Close Search">Close &times;</button>'

index_old_js = """    /* Search Bar Overlay Logic */
    function toggleSearchBar() {
      var bar = document.getElementById('searchOverlayBar');
      bar.classList.toggle('open');
      if (bar.classList.contains('open')) {
        setTimeout(function() {
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }, 120);
      }
    }"""

index_new_js = """    function closeSearchBar(e) {
      if (e) {
        if (typeof e.preventDefault === 'function') e.preventDefault();
        if (typeof e.stopPropagation === 'function') e.stopPropagation();
      }
      var bar = document.getElementById('searchOverlayBar');
      if (bar) bar.classList.remove('open');
    }

    /* Search Bar Overlay Logic */
    function toggleSearchBar(e) {
      if (e) {
        if (typeof e.preventDefault === 'function') e.preventDefault();
        if (typeof e.stopPropagation === 'function') e.stopPropagation();
      }
      var bar = document.getElementById('searchOverlayBar');
      if (!bar) return;
      var willOpen = !bar.classList.contains('open');
      bar.classList.toggle('open');
      if (willOpen) {
        setTimeout(function() {
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }, 120);
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
        closeSearchBar();
      }
    });

    document.addEventListener('click', function(e) {
      var bar = document.getElementById('searchOverlayBar');
      if (!bar || !bar.classList.contains('open')) return;
      var isSearchTrigger = e.target.closest && e.target.closest('.header-search-btn, .search-close-action, [onclick*="toggleSearchBar"], [onclick*="closeSearchBar"]');
      var isInsideBar = bar.contains(e.target);
      if (!isInsideBar && !isSearchTrigger) {
        closeSearchBar();
      }
    });"""

update_file(index_path, index_old_input, index_new_input, "Index search input CSS")
update_file(index_path, index_old_close_css, index_new_close_css, "Index search close CSS")
update_file(index_path, index_old_search_btn, index_new_search_btn, "Index header search trigger")
update_file(index_path, index_old_search_close, index_new_search_close, "Index search close action")
update_file(index_path, index_old_js, index_new_js, "Index JS logic")

print("All updates applied!")

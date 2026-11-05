import os

css_paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-luxury.css',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css'
]

old_base_input = """.search-input-box {
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
    }"""

new_base_input = """.search-input-box {
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
      padding-right: 84px;
      position: relative;
    }"""

old_base_close = """.search-close-action {
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

new_base_close = """.search-close-action {
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

for p in css_paths:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if old_base_input in c:
        c = c.replace(old_base_input, new_base_input, 1)
        print(f"Updated base input in {p}")
    if old_base_close in c:
        c = c.replace(old_base_close, new_base_close, 1)
        print(f"Updated base close in {p}")
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

print("Base CSS updated successfully!")

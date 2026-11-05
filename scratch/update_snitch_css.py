def update_snitch_css(file_path):
    print(f"Updating CSS in {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    old_css = """.snitch-size-backdrop {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(0, 0, 0, 0.45) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  z-index: 999999 !important;
  display: flex !important;
  align-items: flex-end !important;
  justify-content: center !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.snitch-size-backdrop.open {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}
.snitch-size-drawer {
  width: 100% !important;
  max-width: 540px !important;
  background: #FFFFFF !important;
  border-radius: 14px 14px 0 0 !important;
  box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.16) !important;
  transform: translateY(100%) !important;
  transition: transform 0.26s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
  padding-bottom: max(16px, env(safe-area-inset-bottom)) !important;
}
.snitch-size-backdrop.open .snitch-size-drawer {
  transform: translateY(0) !important;
}"""

    new_css = """.snitch-size-backdrop {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  max-width: 100vw !important;
  height: 100% !important;
  background: rgba(0, 0, 0, 0.45) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  z-index: 999999 !important;
  display: flex !important;
  align-items: flex-end !important;
  justify-content: center !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  box-sizing: border-box !important;
  transition: opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.snitch-size-backdrop.open {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}
.snitch-size-drawer {
  width: 100% !important;
  max-width: min(540px, 100vw) !important;
  background: #FFFFFF !important;
  border-radius: 14px 14px 0 0 !important;
  box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.16) !important;
  transform: translateY(100%) !important;
  transition: transform 0.26s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
  padding-bottom: max(16px, env(safe-area-inset-bottom)) !important;
}
.snitch-size-backdrop.open .snitch-size-drawer {
  transform: translateY(0) !important;
}"""

    if old_css in content:
        content = content.replace(old_css, new_css, 1)
        print("  -> Updated drawer and backdrop CSS successfully!")
    else:
        print("  -> old_css not found! Checking partial match...")

    # Also ensure active heart fill is ultra robust
    old_heart_active = """.snitch-size-wishlist-btn.active {
  color: #E53935 !important;
}
.snitch-size-wishlist-btn.active svg {
  fill: #E53935 !important;
  stroke: #E53935 !important;
}"""

    new_heart_active = """.snitch-size-wishlist-btn.active {
  color: #E53935 !important;
}
.snitch-size-wishlist-btn.active svg,
.snitch-size-wishlist-btn.active svg path {
  fill: #E53935 !important;
  stroke: #E53935 !important;
}"""

    if old_heart_active in content:
        content = content.replace(old_heart_active, new_heart_active, 1)
        print("  -> Updated heart active SVG path fill successfully!")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path}.")

update_snitch_css("assets/meenu-luxury.css")
update_snitch_css("meenu-label-shopify-theme/assets/meenu-luxury.css")
update_snitch_css("index.html")

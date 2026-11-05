with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove previous quick size CSS
idx = css.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE")
if idx != -1:
    css = css[:idx].rstrip()

snitch_drawer_css = """
/* ========================================================
   EXACT SNITCH-STYLE QUICK SIZE POPUP DRAWER
   ======================================================== */
.snitch-size-backdrop {
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
}

/* Header Row: CHOOSE YOUR SIZE + Heart */
.snitch-size-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  height: 64px !important;
  padding: 0 24px !important;
  border-bottom: 1px solid #EEEEEE !important;
  box-sizing: border-box !important;
}
.snitch-size-header-title {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Plus Jakarta Sans", sans-serif !important;
  font-size: 15px !important;
  font-weight: 500 !important;
  letter-spacing: 0.05em !important;
  color: #111111 !important;
  text-transform: uppercase !important;
}
.snitch-size-wishlist-btn {
  background: none !important;
  border: none !important;
  padding: 0 !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: #111111 !important;
  transition: transform 0.2s ease, color 0.2s ease !important;
}
.snitch-size-wishlist-btn:hover {
  transform: scale(1.15) !important;
  color: #E53935 !important;
}
.snitch-size-wishlist-btn.active {
  color: #E53935 !important;
}
.snitch-size-wishlist-btn.active svg {
  fill: #E53935 !important;
  stroke: #E53935 !important;
}

/* Size List */
.snitch-size-list {
  display: flex !important;
  flex-direction: column !important;
  margin: 0 !important;
  padding: 0 !important;
  list-style: none !important;
}
.snitch-size-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  height: 55px !important;
  padding: 0 24px !important;
  background: #FFFFFF !important;
  border: none !important;
  border-bottom: 1px solid #EEEEEE !important;
  cursor: pointer !important;
  box-sizing: border-box !important;
  text-align: left !important;
  transition: background 0.15s ease, color 0.15s ease !important;
}
.snitch-size-row:hover {
  background: #F8F8F8 !important;
}
.snitch-size-row:active {
  background: #EFEFEF !important;
}
.snitch-size-name {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Plus Jakarta Sans", sans-serif !important;
  font-size: 15px !important;
  font-weight: 400 !important;
  color: #111111 !important;
  letter-spacing: 0.02em !important;
}
.snitch-size-status {
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #2E7D32 !important;
  letter-spacing: 0.04em !important;
}
.snitch-size-row.disabled {
  opacity: 0.45 !important;
  cursor: not-allowed !important;
  background: #FAFAFA !important;
}
.snitch-size-row.disabled .snitch-size-name {
  text-decoration: line-through !important;
  color: #888888 !important;
}
.snitch-size-row.disabled .snitch-size-status {
  color: #888888 !important;
  font-size: 11px !important;
  text-transform: uppercase !important;
}
"""

css = css + "\n" + snitch_drawer_css

with open('assets/meenu-luxury.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/meenu-luxury.css successfully with Snitch drawer styling!")

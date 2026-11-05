with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace old .snitch-plus-trigger rule
import re
css = re.sub(
    r'\.snitch-plus-trigger\s*\{[^}]*\}',
    '''.snitch-plus-trigger {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 32px !important;
  height: 32px !important;
  background: transparent !important;
  border: none !important;
  color: #1A1A1A !important;
  cursor: pointer !important;
  padding: 0 !important;
  margin-left: auto !important;
  border-radius: 6px !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}''',
    css,
    count=1
)

quick_size_css = """
/* ========================================================
   QUICK SIZE POPUP INTERFACE (LUXURY MODAL & BOTTOM SHEET)
   ======================================================== */
.quick-size-backdrop {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(18, 16, 14, 0.68) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  z-index: 99999 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 20px !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
.quick-size-backdrop.open {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}
.quick-size-modal {
  position: relative !important;
  width: 100% !important;
  max-width: 440px !important;
  background: #FFFFFF !important;
  border-radius: 16px !important;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.25) !important;
  border: 1px solid rgba(218, 203, 186, 0.6) !important;
  padding: 24px 22px 20px !important;
  box-sizing: border-box !important;
  transform: scale(0.92) translateY(16px) !important;
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
  overflow: hidden !important;
}
.quick-size-backdrop.open .quick-size-modal {
  transform: scale(1) translateY(0) !important;
}
.quick-size-close-btn {
  position: absolute !important;
  top: 14px !important;
  right: 14px !important;
  width: 32px !important;
  height: 32px !important;
  border-radius: 50% !important;
  border: 1px solid rgba(0, 0, 0, 0.08) !important;
  background: #FAF7F2 !important;
  color: #1A1A1A !important;
  font-size: 20px !important;
  line-height: 1 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  z-index: 2 !important;
}
.quick-size-close-btn:hover {
  background: #EFE9E0 !important;
  color: var(--accent-burgundy, #6E1A24) !important;
  transform: rotate(90deg) !important;
}
.quick-size-product-row {
  display: flex !important;
  gap: 16px !important;
  align-items: center !important;
  padding-right: 28px !important;
}
.quick-size-thumb {
  width: 64px !important;
  height: 96px !important;
  aspect-ratio: 2 / 3 !important;
  border-radius: 8px !important;
  overflow: hidden !important;
  background: #F4EFEB !important;
  flex-shrink: 0 !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
}
.quick-size-thumb img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: top center !important;
  display: block !important;
}
.quick-size-meta {
  display: flex !important;
  flex-direction: column !important;
  gap: 4px !important;
  min-width: 0 !important;
}
.quick-size-tag {
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--accent-gold, #C5A059) !important;
}
.quick-size-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 19px !important;
  font-weight: 600 !important;
  color: #1A1A1A !important;
  margin: 0 !important;
  line-height: 1.25 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}
.quick-size-price-row {
  display: flex !important;
  align-items: baseline !important;
  gap: 8px !important;
  margin-top: 2px !important;
}
.quick-size-price {
  font-size: 17px !important;
  font-weight: 700 !important;
  color: #1A1A1A !important;
}
.quick-size-mrp {
  font-size: 13px !important;
  color: #8C827A !important;
  text-decoration: line-through !important;
}
.quick-size-discount {
  font-size: 10.5px !important;
  font-weight: 700 !important;
  color: #2E7D32 !important;
  background: #E8F5E9 !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  letter-spacing: 0.04em !important;
}
.quick-size-divider {
  height: 1px !important;
  background: #EAE3D9 !important;
  margin: 16px 0 !important;
}
.quick-size-header-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-bottom: 12px !important;
}
.quick-size-label {
  font-size: 11.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #1A1A1A !important;
}
.quick-size-chart-link {
  background: none !important;
  border: none !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  color: var(--accent-burgundy, #6E1A24) !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 4px !important;
  padding: 0 !important;
  text-decoration: underline !important;
  transition: opacity 0.2s ease !important;
}
.quick-size-chart-link:hover {
  opacity: 0.75 !important;
}
.quick-size-tiles {
  display: grid !important;
  grid-template-columns: repeat(5, 1fr) !important;
  gap: 8px !important;
  margin-bottom: 14px !important;
}
.qs-size-tile {
  background: #FAF7F2 !important;
  border: 1.5px solid #E5DED4 !important;
  border-radius: 8px !important;
  padding: 10px 4px 8px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  cursor: pointer !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-sizing: border-box !important;
}
.qs-size-tile:hover {
  border-color: rgba(110, 26, 36, 0.45) !important;
  background: #F4EFEB !important;
  transform: translateY(-2px) !important;
}
.qs-size-tile.active {
  background: #FFFFFF !important;
  border-color: var(--accent-burgundy, #6E1A24) !important;
  box-shadow: 0 4px 14px rgba(110, 26, 36, 0.18) !important;
  transform: translateY(-2px) !important;
}
.qs-size-tile.disabled {
  opacity: 0.4 !important;
  cursor: not-allowed !important;
  background: #F1ECE6 !important;
  border-color: #E0D9D0 !important;
  text-decoration: line-through !important;
}
.qs-tile-name {
  font-size: 14px !important;
  font-weight: 700 !important;
  color: #1A1A1A !important;
  line-height: 1 !important;
}
.qs-size-tile.active .qs-tile-name {
  color: var(--accent-burgundy, #6E1A24) !important;
}
.qs-tile-sub {
  font-size: 9.5px !important;
  color: #8C827A !important;
  margin-top: 4px !important;
  line-height: 1 !important;
}
.qs-tile-stock {
  font-size: 8px !important;
  font-weight: 700 !important;
  color: var(--accent-gold, #C5A059) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  margin-top: 4px !important;
  line-height: 1 !important;
}
.quick-size-scarcity-note {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  font-size: 10.5px !important;
  color: #8C827A !important;
  margin-bottom: 14px !important;
}
.qs-scarcity-dot {
  width: 6px !important;
  height: 6px !important;
  border-radius: 50 !important;
  border-radius: 50% !important;
  background: #D97706 !important;
  flex-shrink: 0 !important;
  animation: qsPulse 2s infinite !important;
}
@keyframes qsPulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}
.quick-size-add-btn {
  width: 100% !important;
  height: 48px !important;
  background: var(--accent-burgundy, #6E1A24) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 8px !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  cursor: pointer !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 4px 16px rgba(110, 26, 36, 0.25) !important;
}
.quick-size-add-btn:hover {
  background: #50131B !important;
  box-shadow: 0 6px 20px rgba(110, 26, 36, 0.35) !important;
  transform: translateY(-1px) !important;
}
.quick-size-add-btn:active {
  transform: translateY(1px) !important;
}
.quick-size-footer {
  text-align: center !important;
  margin-top: 12px !important;
}
.quick-size-view-full {
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #55504A !important;
  text-decoration: none !important;
  transition: color 0.2s ease !important;
}
.quick-size-view-full:hover {
  color: var(--accent-burgundy, #6E1A24) !important;
  text-decoration: underline !important;
}

@media (max-width: 600px) {
  .quick-size-backdrop {
    align-items: flex-end !important;
    padding: 0 !important;
  }
  .quick-size-modal {
    max-width: 100% !important;
    border-radius: 20px 20px 0 0 !important;
    padding: 20px 16px 26px !important;
    box-shadow: 0 -8px 30px rgba(0, 0, 0, 0.25) !important;
    transform: translateY(100%) !important;
  }
  .quick-size-backdrop.open .quick-size-modal {
    transform: translateY(0) !important;
  }
  .quick-size-tiles {
    grid-template-columns: repeat(5, 1fr) !important;
    gap: 6px !important;
  }
  .qs-size-tile {
    padding: 8px 2px 6px !important;
  }
  .qs-tile-name {
    font-size: 13px !important;
  }
  .qs-tile-sub {
    font-size: 8.5px !important;
  }
  .qs-tile-stock {
    font-size: 7.5px !important;
  }
}
"""

if ".quick-size-backdrop" not in css:
    css = css + "\n" + quick_size_css

with open('assets/meenu-luxury.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/meenu-luxury.css successfully!")

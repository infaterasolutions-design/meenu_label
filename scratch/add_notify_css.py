css_to_add = """
/* =========================================================================
   MEENU LABEL - SOLD OUT & LUXURY NOTIFY ME / RESTOCK WAITLIST SYSTEM
   ========================================================================= */

/* Product Card Sold Out Badge */
.card-badge.badge-sold-out {
  background: #1A1816 !important;
  color: #F8F5EE !important;
  border: 1px solid rgba(200, 163, 100, 0.6) !important;
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25) !important;
}

.product-card.is-sold-out .card-img-primary,
.product-card.is-sold-out .card-img-secondary {
  opacity: 0.88;
}

/* Card Price Row Notify Me Trigger Button */
.snitch-notify-trigger {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #1C1917;
  color: #E6C894;
  border: 1px solid #C8A364;
  border-radius: 4px;
  font-family: inherit;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.snitch-notify-trigger:hover {
  background: #C8A364;
  color: #1C1917;
  border-color: #C8A364;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(200, 163, 100, 0.3);
}

.snitch-notify-trigger svg {
  stroke: currentColor;
  flex-shrink: 0;
}

/* Quick Size Popup: Sold Out Size Rows */
.snitch-size-row.sold-out,
.snitch-size-row.disabled.sold-out {
  opacity: 0.95 !important;
  cursor: pointer !important;
  background: #FCFBF9 !important;
  border-color: #E7E2DA !important;
}

.snitch-size-row.sold-out:hover,
.snitch-size-row.disabled.sold-out:hover {
  background: #FDF9F2 !important;
  border-color: #C8A364 !important;
}

.snitch-size-row.sold-out .snitch-size-name,
.snitch-size-row.disabled.sold-out .snitch-size-name {
  text-decoration: line-through !important;
  color: #78716C !important;
}

.snitch-size-row.sold-out .snitch-size-status,
.snitch-size-row.disabled.sold-out .snitch-size-status {
  color: #B45309 !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.05em !important;
  text-decoration: none !important;
}

/* PDP Size Buttons Sold Out State */
.pdp-size-btn.sold-out {
  background: #FBF9F5 !important;
  border-color: #E7E2DA !important;
  cursor: pointer !important;
}

.pdp-size-btn.sold-out .pdp-size-name {
  text-decoration: line-through !important;
  color: #8C827A !important;
}

.pdp-size-btn.sold-out .pdp-size-stock {
  color: #DC2626 !important;
  font-weight: 700 !important;
}

.pdp-size-btn.sold-out.selected {
  border-color: #B45309 !important;
  background: #FEF3C7 !important;
}

/* PDP Primary Notify Me Button */
.pdp-btn-notify {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  padding: 16px 24px;
  background: #1C1917;
  color: #F5EBE1;
  border: 1.5px solid #C8A364;
  border-radius: 4px;
  font-family: inherit;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
}

.pdp-btn-notify:hover {
  background: #C8A364;
  color: #1C1917;
  border-color: #C8A364;
  box-shadow: 0 6px 20px rgba(200, 163, 100, 0.35);
  transform: translateY(-1px);
}

.pdp-btn-notify svg {
  stroke: currentColor;
  flex-shrink: 0;
}

/* =========================================================================
   LUXURY NOTIFY ME MODAL / ATELIER WAITLIST DIALOG
   ========================================================================= */

.meenu-notify-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(18, 16, 14, 0.72);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.35s;
}

.meenu-notify-backdrop.open {
  opacity: 1;
  visibility: visible;
}

.meenu-notify-modal {
  background: #FFFFFF;
  width: 100%;
  max-width: 480px;
  border-radius: 12px;
  padding: 28px 26px;
  position: relative;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(200, 163, 100, 0.25);
  transform: translateY(20px) scale(0.97);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  max-height: 90vh;
  overflow-y: auto;
  box-sizing: border-box;
}

.meenu-notify-backdrop.open .meenu-notify-modal {
  transform: translateY(0) scale(1);
}

.meenu-notify-close {
  position: absolute;
  top: 16px;
  right: 18px;
  background: none;
  border: none;
  font-size: 28px;
  line-height: 1;
  color: #78716C;
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s;
  z-index: 10;
}

.meenu-notify-close:hover {
  color: #1C1917;
}

.meenu-notify-header {
  text-align: center;
  margin-bottom: 20px;
  padding-right: 20px;
  padding-left: 20px;
}

.notify-atelier-tag {
  display: inline-block;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #B45309;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.notify-title {
  font-family: "Cormorant Garamond", Georgia, serif;
  font-size: 26px;
  font-weight: 700;
  color: #1C1917;
  margin: 0 0 8px 0;
  line-height: 1.15;
  letter-spacing: 0.01em;
}

.notify-subtitle {
  font-size: 12.5px;
  color: #78716C;
  margin: 0;
  line-height: 1.45;
}

/* Product Preview in Modal */
.notify-product-preview {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #FAF7F2;
  border: 1px solid #EFEAE1;
  border-radius: 8px;
  padding: 12px 14px;
  margin-bottom: 20px;
}

.notify-thumb {
  width: 54px;
  height: 68px;
  object-fit: cover;
  border-radius: 4px;
  background: #EAE5DC;
  flex-shrink: 0;
}

.notify-product-meta {
  flex: 1;
  min-width: 0;
}

.notify-prod-title {
  font-size: 13.5px;
  font-weight: 600;
  color: #1C1917;
  margin: 0 0 4px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.notify-prod-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.notify-prod-price {
  font-size: 13.5px;
  font-weight: 700;
  color: #1C1917;
}

.notify-stock-status {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #DC2626;
  background: #FEE2E2;
  padding: 2px 7px;
  border-radius: 3px;
  text-transform: uppercase;
}

/* Size Picker */
.notify-size-picker {
  margin-bottom: 18px;
}

.notify-label {
  display: block;
  font-size: 11.5px;
  font-weight: 600;
  color: #44403C;
  letter-spacing: 0.04em;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.notify-size-pills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.notify-size-pill {
  flex: 1;
  min-width: 48px;
  padding: 8px 10px;
  background: #FFFFFF;
  border: 1.5px solid #E7E2DA;
  border-radius: 4px;
  font-family: inherit;
  font-size: 12.5px;
  font-weight: 600;
  color: #292524;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.notify-size-pill:hover {
  border-color: #C8A364;
  background: #FAF7F2;
}

.notify-size-pill.active {
  background: #1C1917;
  color: #F5EBE1;
  border-color: #1C1917;
}

/* Channels & Tabs */
.notify-channels-wrap {
  margin-bottom: 20px;
}

.notify-tabs {
  display: flex;
  gap: 6px;
  margin-bottom: 12px;
  background: #F5F2EB;
  padding: 4px;
  border-radius: 6px;
}

.notify-tab {
  flex: 1;
  padding: 8px 12px;
  border: none;
  background: transparent;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  color: #78716C;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.notify-tab.active {
  background: #FFFFFF;
  color: #1C1917;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.notify-phone-row {
  display: flex;
  align-items: center;
  border: 1.5px solid #D6D3D1;
  border-radius: 6px;
  overflow: hidden;
  background: #FFFFFF;
  transition: border-color 0.2s ease;
}

.notify-phone-row:focus-within {
  border-color: #C8A364;
  box-shadow: 0 0 0 2px rgba(200, 163, 100, 0.2);
}

.notify-country-code {
  padding: 10px 14px;
  background: #F5F2EB;
  font-size: 13.5px;
  font-weight: 600;
  color: #44403C;
  border-right: 1px solid #E7E2DA;
}

#notifyPhoneInput,
.notify-email-input {
  flex: 1;
  width: 100%;
  padding: 10px 14px;
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 13.5px;
  color: #1C1917;
  background: transparent;
  box-sizing: border-box;
}

.notify-email-input {
  border: 1.5px solid #D6D3D1;
  border-radius: 6px;
  background: #FFFFFF;
}

.notify-email-input:focus {
  border-color: #C8A364;
  box-shadow: 0 0 0 2px rgba(200, 163, 100, 0.2);
}

.notify-error {
  color: #DC2626;
  font-size: 11.5px;
  font-weight: 500;
  margin-top: 5px;
}

/* Primary Modal Submit Button */
.notify-submit-btn {
  width: 100%;
  padding: 14px 20px;
  background: #1C1917;
  color: #F5EBE1;
  border: none;
  border-radius: 6px;
  font-family: inherit;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
}

.notify-submit-btn:hover {
  background: #C8A364;
  color: #1C1917;
}

/* Concierge WhatsApp Link */
.notify-concierge-divider {
  display: flex;
  align-items: center;
  text-align: center;
  margin: 16px 0 12px 0;
  color: #A8A29E;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
}

.notify-concierge-divider::before,
.notify-concierge-divider::after {
  content: "";
  flex: 1;
  border-bottom: 1px solid #E7E2DA;
}

.notify-concierge-divider span {
  padding: 0 10px;
}

.notify-concierge-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 16px;
  background: #F0FDF4;
  color: #166534;
  border: 1px solid #BBF7D0;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.notify-concierge-btn:hover {
  background: #DCFCE7;
  border-color: #86EFAC;
}

/* Success View */
.notify-success-view {
  text-align: center;
  padding: 24px 10px;
}

.notify-success-check {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #DCFCE7;
  color: #166534;
  font-size: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px auto;
  box-shadow: 0 0 0 8px rgba(220, 252, 231, 0.4);
}

.notify-success-title {
  font-family: "Cormorant Garamond", Georgia, serif;
  font-size: 26px;
  font-weight: 700;
  color: #1C1917;
  margin: 0 0 8px 0;
}

.notify-success-msg {
  font-size: 13px;
  color: #57534E;
  line-height: 1.5;
  margin: 0 0 24px 0;
}

.notify-done-btn {
  padding: 12px 28px;
  background: #1C1917;
  color: #F5EBE1;
  border: none;
  border-radius: 4px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s ease;
}

.notify-done-btn:hover {
  background: #C8A364;
  color: #1C1917;
}

/* Mobile responsive drawer feel */
@media (max-width: 600px) {
  .meenu-notify-modal {
    padding: 24px 18px;
    max-height: 94vh;
  }
  .notify-title {
    font-size: 23px;
  }
}
"""

for path in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'MEENU LABEL - SOLD OUT & LUXURY NOTIFY ME' not in content:
        content += '\n' + css_to_add
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Appended notify me CSS to {path}')
    else:
        print(f'Already present in {path}')

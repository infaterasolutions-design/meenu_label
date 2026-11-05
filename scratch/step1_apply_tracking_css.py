import sys
sys.stdout.reconfigure(encoding='utf-8')

css_content = """
/* =========================================================================
   TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM
   ========================================================================= */

.account-modal-tabs {
  display: flex;
  gap: 8px;
  background: rgba(255, 255, 255, 0.05);
  padding: 4px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 22px;
}

.account-modal-tab {
  flex: 1;
  padding: 10px 14px;
  background: transparent;
  color: rgba(255, 255, 255, 0.6);
  border: none;
  border-radius: 6px;
  font-family: inherit;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.account-modal-tab:hover {
  color: #FFFFFF;
}

.account-modal-tab.active {
  background: #C8A364;
  color: #12100E;
  box-shadow: 0 2px 8px rgba(200, 163, 100, 0.3);
}

.account-view {
  display: none;
  animation: fadeInModal 0.25s ease forwards;
}

.account-view.active {
  display: block;
}

/* Order Tracking View */
.tracking-input-wrap {
  margin-bottom: 16px;
}

.tracking-input-field {
  width: 100%;
  padding: 14px 16px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 6px;
  color: #FFFFFF;
  font-family: inherit;
  font-size: 13px;
  letter-spacing: 0.04em;
  transition: border-color 0.2s ease;
  box-sizing: border-box;
}

.tracking-input-field:focus {
  outline: none;
  border-color: #C8A364;
  background: rgba(255, 255, 255, 0.09);
}

.tracking-demo-chips {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.45);
  flex-wrap: wrap;
}

.tracking-demo-chip {
  background: rgba(200, 163, 100, 0.12);
  color: #E6C894;
  border: 1px solid rgba(200, 163, 100, 0.3);
  border-radius: 4px;
  padding: 3px 8px;
  font-size: 10.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tracking-demo-chip:hover {
  background: #C8A364;
  color: #12100E;
}

/* Shipment Status Card & Timeline */
.shipment-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  padding: 18px 16px;
  margin-top: 18px;
  text-align: left;
}

.shipment-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 12px;
  margin-bottom: 14px;
}

.shipment-order-id {
  font-size: 14px;
  font-weight: 700;
  color: #FAF8F5;
  letter-spacing: 0.04em;
}

.shipment-badge {
  display: inline-block;
  padding: 3px 8px;
  background: rgba(37, 211, 102, 0.15);
  color: #25D366;
  border: 1px solid rgba(37, 211, 102, 0.3);
  border-radius: 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.shipment-timeline {
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
  padding-left: 24px;
  margin: 16px 0;
}

.shipment-timeline::before {
  content: '';
  position: absolute;
  top: 6px;
  bottom: 6px;
  left: 6px;
  width: 2px;
  background: rgba(255, 255, 255, 0.12);
}

.timeline-step {
  position: relative;
}

.timeline-step::before {
  content: '';
  position: absolute;
  left: -24px;
  top: 3px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #292524;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-sizing: border-box;
}

.timeline-step.completed::before {
  background: #25D366;
  border-color: #25D366;
  box-shadow: 0 0 8px rgba(37, 211, 102, 0.5);
}

.timeline-step.active::before {
  background: #C8A364;
  border-color: #C8A364;
  box-shadow: 0 0 10px rgba(200, 163, 100, 0.6);
}

.timeline-title {
  font-size: 12.5px;
  font-weight: 700;
  color: #FAF8F5;
  line-height: 1.3;
}

.timeline-desc {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.5);
  margin-top: 2px;
}

.shipment-meta-row {
  display: flex;
  justify-content: space-between;
  padding-top: 10px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 11.5px;
  color: rgba(255, 255, 255, 0.6);
}

.shipment-wa-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 12px 16px;
  background: #25D366;
  color: #FFFFFF !important;
  border-radius: 6px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-decoration: none !important;
  margin-top: 14px;
  transition: all 0.2s ease;
}

.shipment-wa-btn:hover {
  background: #1EBE5D;
  transform: translateY(-1px);
}

.account-active-badge {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 7px;
  height: 7px;
  background: #25D366;
  border-radius: 50%;
  border: 1px solid #000;
  display: none;
}
.account-active-badge.active {
  display: block;
}

.vip-recent-orders-block {
  margin-top: 16px;
  text-align: left;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 14px;
}

.vip-recent-orders-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #C8A364;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.vip-order-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  margin-bottom: 8px;
  gap: 10px;
}

.vip-order-info {
  font-size: 12px;
  color: #FAF8F5;
  line-height: 1.4;
}

.vip-order-date {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.5);
}

.vip-order-track-btn {
  padding: 6px 12px;
  background: rgba(200, 163, 100, 0.15);
  border: 1px solid #C8A364;
  color: #E6C894;
  font-size: 10.5px;
  font-weight: 700;
  border-radius: 4px;
  cursor: pointer;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.vip-order-track-btn:hover {
  background: #C8A364;
  color: #12100E;
}
"""

targets = [
    'assets/meenu-luxury.css',
    'meenu-label-shopify-theme/assets/meenu-luxury.css'
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        existing = f.read()
    if 'TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM' not in existing:
        with open(t, 'a', encoding='utf-8') as f:
            f.write("\n" + css_content)
        print(f"Appended tracking CSS to {t}")
    else:
        print(f"Tracking CSS already present in {t}")

# Also update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

if 'TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM' not in html_content:
    # insert before </style>
    pos = html_content.find('</style>')
    if pos != -1:
        new_html = html_content[:pos] + "\n" + css_content + "\n" + html_content[pos:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Inserted tracking CSS into index.html <style>")
    else:
        print("Could not find </style> in index.html")
else:
    print("Tracking CSS already present in index.html")

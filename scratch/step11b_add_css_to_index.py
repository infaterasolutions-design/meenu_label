import os

price_fix_css = """

/* ========================================================
   HYPER-CLEAN CARD PRICE & DISCOUNT PERCENTAGE
   Ensures compare price ('Rs.' and digits) NEVER break across lines.
   Displays clear discount percentage badge (e.g. 37% OFF).
   ======================================================== */
.card-price-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 6px !important;
  margin-top: 4px !important;
  padding-top: 0 !important;
}

.card-price-left {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  align-items: baseline !important;
  gap: 3px 6px !important;
  min-width: 0 !important;
  flex: 1 !important;
}

.price-main {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  color: #111111 !important;
  font-variant-numeric: lining-nums !important;
  letter-spacing: -0.02em !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
}

.card-price-compare-wrap {
  display: inline-flex !important;
  align-items: baseline !important;
  gap: 5px !important;
  white-space: nowrap !important;
  line-height: 1.2 !important;
}

.price-mrp,
.pdp-price-mrp,
.modal-price-mrp {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 12.5px !important;
  color: #8C827A !important;
  text-decoration: line-through !important;
  white-space: nowrap !important; /* CRITICAL: Never split currency and digits */
  font-variant-numeric: lining-nums !important;
  letter-spacing: -0.01em !important;
  line-height: 1.2 !important;
}

.price-discount,
.pdp-price-discount {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  color: #B83A3A !important; /* Luxury crimson rose discount highlight */
  white-space: nowrap !important;
  letter-spacing: 0.02em !important;
  line-height: 1.2 !important;
}

/* Mobile 2-Column Responsive Layout */
@media (max-width: 768px) {
  .card-body {
    padding: 10px 10px 12px !important;
  }
  .card-price-row {
    align-items: center !important;
    gap: 4px !important;
  }
  .card-price-left {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 2px !important;
    min-width: 0 !important;
    flex: 1 !important;
  }
  .price-main {
    font-size: 13.5px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
  }
  .card-price-compare-wrap {
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
    white-space: nowrap !important;
  }
  .price-mrp {
    font-size: 11px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
  }
  .price-discount {
    font-size: 10px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
    color: #B83A3A !important;
    font-weight: 700 !important;
  }
  .snitch-plus-trigger {
    width: 28px !important;
    height: 28px !important;
    flex-shrink: 0 !important;
  }
}
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

target = ".vip-order-track-btn:hover {\n  background: #C8A364;\n  color: #12100E;\n}"
if target in html:
    html = html.replace(target, target + "\n" + price_fix_css, 1)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Added price_fix_css to index.html successfully!")
else:
    print("WARNING: Could not find target in index.html")

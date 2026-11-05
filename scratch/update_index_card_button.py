# scratch/update_index_card_button.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                  <button type="button" class="snitch-plus-trigger" data-product-id="JAB25ST02661" onclick="event.preventDefault(); event.stopPropagation(); openQuickSizePopup(this)" title="Select Size & Add to Bag" aria-label="Select Size & Add to Bag">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="3" x2="12" y2="15"></line>
              <line x1="6" y1="9" x2="18" y2="9"></line>
              <line x1="4" y1="19" x2="20" y2="19"></line>
            </svg>
          </button>
</div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('JAB25ST02661', 'M')">M (38)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('JAB25ST02661', 'L')">L (40)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('JAB25ST02661', 'XL')">XL (42)</span>
          </div>
          <span class="stock-chip">Only 3 Left</span>"""

replacement = """          <button type="button" class="snitch-notify-trigger" data-product-id="JAB25ST02661" onclick="event.preventDefault(); event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'M', 'The Noor Petrol Teal Chanderi Suit', '', '&#8377;2,999')" title="Sold Out - Notify Me When Available" aria-label="Notify Me When Available">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span class="notify-btn-text">NOTIFY ME</span>
          </button>
        </div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" style="text-decoration: line-through; opacity: 0.6;" onclick="event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'M', 'The Noor Petrol Teal Chanderi Suit', '', '&#8377;2,999')">M (38)</span>
            <span class="size-chip" style="text-decoration: line-through; opacity: 0.6;" onclick="event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'L', 'The Noor Petrol Teal Chanderi Suit', '', '&#8377;2,999')">L (40)</span>
            <span class="size-chip" style="text-decoration: line-through; opacity: 0.6;" onclick="event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'XL', 'The Noor Petrol Teal Chanderi Suit', '', '&#8377;2,999')">XL (42)</span>
          </div>
          <span class="stock-chip" style="color: #DC2626; font-weight: 700;">Sold Out</span>"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: index.html updated for JAB25ST02661 card button and chips!")
else:
    print("ERROR: Target block not found in index.html")

import os

filter_js = '''

/* =========================================================================
   10. INSTANT IN-PAGE CATEGORY FILTER CONTROLLER
   ========================================================================= */
function filterCategory(cat, btn) {
  var cards = document.querySelectorAll('#productGrid .product-card, .catalog-section .product-card');
  var matchedCount = 0;
  var normalizedCat = String(cat || 'all').toLowerCase();

  cards.forEach(function(card) {
    var cardCat = (card.getAttribute('data-category') || card.textContent || '').toLowerCase();
    if (normalizedCat === 'all' || cardCat.indexOf(normalizedCat) !== -1) {
      card.style.display = 'flex';
      matchedCount++;
    } else {
      card.style.display = 'none';
    }
  });

  document.querySelectorAll('.filter-tabs .filter-tab').forEach(function(t) {
    t.classList.remove('active');
  });
  if (btn) {
    btn.classList.add('active');
  }

  var countEl = document.getElementById('activeCategoryCount');
  if (countEl) {
    if (normalizedCat === 'all') {
      countEl.textContent = 'HANDCRAFTED EDITIONS';
    } else {
      countEl.textContent = matchedCount + ' SILHOUETTES AVAILABLE';
    }
  }
}

// Auto-trigger filter if URL has category hash (e.g. #co-ord-sets)
window.addEventListener('DOMContentLoaded', function() {
  if (window.location.hash) {
    var h = window.location.hash.replace('#', '').toLowerCase();
    var tab = document.querySelector('.filter-tabs [data-cat*="' + h + '"]');
    if (tab) {
      tab.click();
    }
  }
});
'''

paths = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-theme.js',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js'
]

for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'function filterCategory(' not in content:
        content += filter_js
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added filterCategory to {p}")
    else:
        print(f"filterCategory already in {p}")

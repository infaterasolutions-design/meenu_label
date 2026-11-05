path = r'assets/meenu-theme.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """function filterCategory(cat, btn) {
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
  });"""

new_block = """function filterCategory(cat, btn) {
  var cards = document.querySelectorAll('#productGrid .product-card, .catalog-section .product-card');
  var matchedCount = 0;
  var normalizedCat = String(cat || 'all').toLowerCase();

  cards.forEach(function(card) {
    var cardCat = (card.getAttribute('data-category') || card.textContent || '').toLowerCase();
    var isMatch = false;

    if (normalizedCat === 'all') {
      isMatch = true;
    } else if (normalizedCat === 'coord' || normalizedCat === 'co-ord' || normalizedCat === 'co-ord-sets') {
      isMatch = cardCat.indexOf('coord') !== -1 || cardCat.indexOf('co-ord') !== -1;
    } else if (normalizedCat === 'festive' || normalizedCat === 'festive-suits') {
      isMatch = cardCat.indexOf('festive') !== -1;
    } else if (normalizedCat === 'dress' || normalizedCat === 'dresses') {
      isMatch = cardCat.indexOf('dress') !== -1;
    } else if (normalizedCat === 'top' || normalizedCat === 'tops' || normalizedCat === 'blouse') {
      isMatch = cardCat.indexOf('top') !== -1 || cardCat.indexOf('blouse') !== -1;
    } else {
      isMatch = cardCat.indexOf(normalizedCat) !== -1;
    }

    if (isMatch) {
      card.style.display = 'flex';
      matchedCount++;
    } else {
      card.style.display = 'none';
    }
  });"""

# normalize line endings in matching
content_normalized = content.replace('\r\n', '\n')
if old_block in content_normalized:
    content_normalized = content_normalized.replace(old_block, new_block)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_normalized)
    print("Successfully updated assets/meenu-theme.js")
else:
    print("Block not found!")

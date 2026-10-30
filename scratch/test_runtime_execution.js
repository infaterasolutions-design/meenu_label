const fs = require('fs');

// Create a DOM mock
const elements = {};

function createElementMock(id, tag = 'div') {
  const el = {
    id: id,
    tagName: tag.toUpperCase(),
    value: '',
    textContent: '',
    innerHTML: '',
    style: {},
    classList: {
      _classes: new Set(),
      add: function(c) { this._classes.add(c); },
      remove: function(c) { this._classes.delete(c); },
      contains: function(c) { return this._classes.has(c); },
      toggle: function(c) {
        if (this._classes.has(c)) { this._classes.delete(c); return false; }
        else { this._classes.add(c); return true; }
      }
    },
    getAttribute: function(attr) { return this[attr] || ''; },
    setAttribute: function(attr, val) { this[attr] = val; },
    querySelectorAll: function(sel) { return []; },
    querySelector: function(sel) { return createElementMock('sub'); },
    scrollIntoView: function() {},
    focus: function() {},
    addEventListener: function(event, handler) {}
  };
  return el;
}

const mockDoc = {
  getElementById: function(id) {
    if (!elements[id]) {
      elements[id] = createElementMock(id);
    }
    return elements[id];
  },
  querySelectorAll: function(sel) {
    return [createElementMock('mock_card'), createElementMock('mock_tab')];
  },
  querySelector: function(sel) {
    return createElementMock('single_' + sel);
  }
};

global.document = mockDoc;
global.window = global;
global.alert = function(msg) { console.log('ALERT:', msg); };
global.setTimeout = function(fn, ms) { fn(); return 1; };
global.setInterval = function(fn, ms) { return 1; };
global.clearInterval = function() {};

// Load and evaluate the script
const code = fs.readFileSync('scratch/generated_check.js', 'utf-8');
eval(code);

console.log('Script evaluated successfully into global scope!');

// Now test calling all major interactive functions:
console.log('--- Testing interactive functions ---');

// 1. Search
toggleSearchBar();
console.log('toggleSearchBar: OK');
mockDoc.getElementById('searchInput').value = 'Festive';
searchProducts();
console.log('searchProducts: OK');
clearSearch();
console.log('clearSearch: OK');
quickSearch('Chanderi');
console.log('quickSearch: OK');

// 2. Wishlist
toggleWishlistProduct('JAB26ST05010');
console.log('toggleWishlistProduct: OK, wishlist length:', wishlist.length);
toggleWishlistDrawer();
console.log('toggleWishlistDrawer: OK');

// 3. Cart
quickAddCart('JAB26ST05010', 'M');
console.log('quickAddCart: OK, cart length:', cart.length);
toggleCart();
console.log('toggleCart: OK');

// 4. Move Wishlist To Cart
moveWishlistToCart('JAB26ST05010');
console.log('moveWishlistToCart: OK');

// 5. Account
openAccountModal();
console.log('openAccountModal: OK');
mockDoc.getElementById('trackOrderInput').value = 'ML-84920';
trackOrderSubmit();
console.log('trackOrderSubmit: OK, result:', mockDoc.getElementById('trackOrderResult')?.textContent);
closeAccountModalDirect();
console.log('closeAccountModalDirect: OK');

// 6. Product Modal
openProductModal('JAB26ST05010');
console.log('openProductModal: OK, active modal:', activeModalProduct?.id);
selectModalSize('XL');
console.log('selectModalSize: OK, selected size:', selectedSize);
addCurrentProductToCart();
console.log('addCurrentProductToCart: OK, cart length:', cart.length);
closeModal();
console.log('closeModal: OK');

// 7. Filters
filterCategory('coord', null);
console.log('filterCategory: OK');

// 8. Slider
nextSlide();
console.log('nextSlide: OK, currentSlide:', currentSlide);
prevSlide();
console.log('prevSlide: OK, currentSlide:', currentSlide);
goToSlide(3);
console.log('goToSlide: OK, currentSlide:', currentSlide);

// 9. Size Guide
openSizeGuide();
console.log('openSizeGuide: OK');
closeSizeGuideDirect();
console.log('closeSizeGuideDirect: OK');

// 10. Nav Drawer
openNavDrawer();
console.log('openNavDrawer: OK');
closeNavDrawer();
console.log('closeNavDrawer: OK');

console.log('=== ALL 10 INTERACTIVE SUBSYSTEMS RUN FLAWLESSLY WITH 0 ERRORS! ===');

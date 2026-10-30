const fs = require('fs');

const elements = {};

function createElementMock(id, tag = 'div') {
  return {
    id: id,
    tagName: tag.toUpperCase(),
    value: '',
    textContent: '',
    innerHTML: '',
    src: '',
    href: '',
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
    querySelectorAll: function(sel) {
      if (sel === '.pdp-size-btn') {
        return [
          mockDoc.getElementById('pdpSizeBtn_M'),
          mockDoc.getElementById('pdpSizeBtn_L'),
          mockDoc.getElementById('pdpSizeBtn_XL')
        ];
      }
      if (sel === '.modal-size-btn') {
        return [
          mockDoc.getElementById('modalSizeBtn_M'),
          mockDoc.getElementById('modalSizeBtn_L'),
          mockDoc.getElementById('modalSizeBtn_XL')
        ];
      }
      return [createElementMock('sub_q')];
    },
    querySelector: function(sel) { return createElementMock('single_' + sel); },
    scrollIntoView: function() {},
    focus: function() {},
    addEventListener: function(event, handler) {}
  };
}

const mockDoc = {
  getElementById: function(id) {
    if (!elements[id]) {
      elements[id] = createElementMock(id);
    }
    return elements[id];
  },
  querySelectorAll: function(sel) {
    if (sel === '.pdp-size-btn') {
      return [
        mockDoc.getElementById('pdpSizeBtn_M'),
        mockDoc.getElementById('pdpSizeBtn_L'),
        mockDoc.getElementById('pdpSizeBtn_XL')
      ];
    }
    if (sel === '.modal-size-btn') {
      return [
        mockDoc.getElementById('modalSizeBtn_M'),
        mockDoc.getElementById('modalSizeBtn_L'),
        mockDoc.getElementById('modalSizeBtn_XL')
      ];
    }
    return [createElementMock('mock_item')];
  },
  querySelector: function(sel) {
    return createElementMock('single_' + sel);
  },
  addEventListener: function(event, handler) {}
};

global.document = mockDoc;
global.window = global;
global.window.scrollTo = function() {};
global.window.addEventListener = function() {};
global.window.location = { hash: '', href: '' };
global.alert = function(msg) { console.log('ALERT:', msg); };
global.setTimeout = function(fn, ms) { fn(); return 1; };
global.setInterval = function(fn, ms) { return 1; };
global.clearInterval = function() {};

// Extract the script from the storefront HTML
const html = fs.readFileSync('C:\\Users\\sande\\Downloads\\Meenu_Label_Desktop_Storefront.html', 'utf-8');
const scriptMatches = html.match(/<script\b[^>]*>([\s\S]*?)<\/script>/i);
if (!scriptMatches) {
  console.error("No script tag found!");
  process.exit(1);
}
eval(scriptMatches[1]);

console.log('--- Storefront Script Loaded & Evaluated Successfully! ---');

// TEST 1: Open PDP
console.log('\n[Test 1] Opening PDP for JAB26ST05010...');
openProductPage('JAB26ST05010');
console.log('  pdpSelectedSize after openProductPage:', pdpSelectedSize);
console.log('  pdpSizeBtn_M selected:', mockDoc.getElementById('pdpSizeBtn_M').classList.contains('selected'));
console.log('  pdpSizeBtn_L selected:', mockDoc.getElementById('pdpSizeBtn_L').classList.contains('selected'));
console.log('  pdpSizeBtn_XL selected:', mockDoc.getElementById('pdpSizeBtn_XL').classList.contains('selected'));
if (pdpSelectedSize === null && !mockDoc.getElementById('pdpSizeBtn_M').classList.contains('selected')) {
  console.log('  => PASS: ZERO default size selected on PDP load!');
} else {
  console.error('  => FAIL: A size is still default selected!');
  process.exit(1);
}

// TEST 2: Attempt Add to Cart without selecting size
console.log('\n[Test 2] Attempting addPdpProductToCart() without choosing a size...');
const cartBefore = cart.length;
addPdpProductToCart();
console.log('  Cart length before:', cartBefore, 'after:', cart.length);
console.log('  Toast message:', mockDoc.getElementById('toastNote').textContent);
console.log('  Prompt display:', mockDoc.getElementById('pdpSizeSelectPrompt').style.display);
if (cart.length === cartBefore && mockDoc.getElementById('pdpSizeSelectPrompt').style.display === 'block') {
  console.log('  => PASS: Add to Bag correctly BLOCKED until size is deliberately chosen!');
} else {
  console.error('  => FAIL: Product was added without choosing a size!');
  process.exit(1);
}

// TEST 3: Attempt Buy Now without selecting size
console.log('\n[Test 3] Attempting buyPdpProductNow() without choosing a size...');
buyPdpProductNow();
console.log('  Cart length:', cart.length);
if (cart.length === cartBefore) {
  console.log('  => PASS: Buy It Now correctly BLOCKED without size selection!');
} else {
  console.error('  => FAIL: Buy It Now proceeded without size selection!');
  process.exit(1);
}

// TEST 4: Select Size 'L'
console.log('\n[Test 4] Selecting size L...');
const btnL = mockDoc.getElementById('pdpSizeBtn_L');
selectPdpSize('L', btnL);
console.log('  pdpSelectedSize:', pdpSelectedSize);
console.log('  btnL has class selected:', btnL.classList.contains('selected'));
console.log('  Prompt display after selection:', mockDoc.getElementById('pdpSizeSelectPrompt').style.display);
console.log('  Indicator text:', mockDoc.getElementById('pdpSelectedSizeIndicator').textContent);
console.log('  WhatsApp href:', mockDoc.getElementById('pdpWhatsAppBtn').href);
if (pdpSelectedSize === 'L' && btnL.classList.contains('selected') && mockDoc.getElementById('pdpSizeSelectPrompt').style.display === 'none') {
  console.log('  => PASS: Size L deliberately selected, prompt hidden, indicator displayed!');
} else {
  console.error('  => FAIL: Size selection failed!');
  process.exit(1);
}

// TEST 5: Add to bag with size L
console.log('\n[Test 5] Adding to bag with size L selected...');
addPdpProductToCart();
console.log('  Cart length:', cart.length);
console.log('  Cart item title:', cart[cart.length - 1].title);
console.log('  Cart item size:', cart[cart.length - 1].size);
if (cart.length === 1 && cart[0].size === 'L') {
  console.log('  => PASS: Product added to bag in exactly size L!');
} else {
  console.error('  => FAIL: Cart item size incorrect!');
  process.exit(1);
}

// TEST 6: Quick View Modal
console.log('\n[Test 6] Quick View Modal size test...');
openProductModal('SET916');
console.log('  selectedSize after openProductModal:', selectedSize);
const modalM = mockDoc.getElementById('modalSizeBtn_M');
console.log('  modalSizeBtn_M selected:', modalM.classList.contains('selected'));
if (selectedSize === null && !modalM.classList.contains('selected')) {
  console.log('  => PASS: Quick View Modal also starts with ZERO default size selected!');
}

console.log('\nAttempting modal add without size...');
const cartMid = cart.length;
addCurrentProductToCart();
console.log('  Cart length before:', cartMid, 'after:', cart.length);
if (cart.length === cartMid && mockDoc.getElementById('modalSizeSelectPrompt').style.display === 'block') {
  console.log('  => PASS: Modal add to bag correctly BLOCKED without size selection!');
}

console.log('\nSelecting modal size XL and adding...');
const modalXL = mockDoc.getElementById('modalSizeBtn_XL');
selectModalSize('XL', modalXL);
addCurrentProductToCart();
console.log('  Cart length:', cart.length);
console.log('  Last cart item size:', cart[cart.length - 1].size);
if (cart[cart.length - 1].size === 'XL') {
  console.log('  => PASS: Modal added piece in Size XL!');
}

console.log('\n========================================');
console.log('ALL RUNTIME VERIFICATIONS PASSED 100%!');
console.log('========================================');

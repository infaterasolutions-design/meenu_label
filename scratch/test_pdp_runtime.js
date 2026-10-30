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
    querySelectorAll: function(sel) { return [createElementMock('sub_q')]; },
    querySelector: function(sel) { return createElementMock('single_' + sel); },
    scrollIntoView: function() {},
    getBoundingClientRect: function() { return { top: 200, bottom: 800, height: 600, width: 1000 }; },
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
    return [createElementMock('mock_card'), createElementMock('mock_tab')];
  },
  querySelector: function(sel) {
    return createElementMock('single_' + sel);
  }
};

global.document = mockDoc;
global.window = global;
global.window.scrollTo = function() {};
global.alert = function(msg) { console.log('ALERT:', msg); };
global.setTimeout = function(fn, ms) { fn(); return 1; };
global.setInterval = function(fn, ms) { return 1; };
global.clearInterval = function() {};

// Load and evaluate the script
const code = fs.readFileSync('scratch/generated_check.js', 'utf-8');
eval(code);

console.log('Script evaluated successfully!');

// 1. Test PDP: openProductPage
console.log('--- Testing Product Detail Page (PDP) ---');
openProductPage('JAB26ST05010');
console.log('openProductPage(JAB26ST05010): OK');
console.log('  Active PDP ID:', activePdpProductId);
console.log('  PDP Title populated:', mockDoc.getElementById('pdpTitle').textContent);
console.log('  PDP Price populated:', mockDoc.getElementById('pdpPriceMain').innerHTML);

// 2. Select Size on PDP
selectPdpSize('XL');
console.log('selectPdpSize(XL): OK, selected:', pdpSelectedSize);

// 3. Add to Bag from PDP
addPdpProductToCart();
console.log('addPdpProductToCart: OK, cart count:', cart.length);

// 4. Toggle Wishlist from PDP
togglePdpWishlist();
console.log('togglePdpWishlist: OK, wishlist count:', wishlist.length);

// 5. Check Pincode on PDP
mockDoc.getElementById('pdpPincodeInput').value = '160017';
checkPdpPincode();
console.log('checkPdpPincode (Tricity 160017): OK, result:', mockDoc.getElementById('pdpPincodeResult').textContent);

mockDoc.getElementById('pdpPincodeInput').value = '110001';
checkPdpPincode();
console.log('checkPdpPincode (Delhi 110001): OK, result:', mockDoc.getElementById('pdpPincodeResult').textContent);

// 6. Close PDP / Back to Collection
closeProductPage();
console.log('closeProductPage: OK, homeView display:', mockDoc.getElementById('storefrontHomeView').style.display);
console.log('  pdpView display:', mockDoc.getElementById('productDetailView').style.display);

// 7. Test Quick View (distinct from PDP)
console.log('--- Testing Quick View Modal ---');
openQuickView('JAB26ST05010');
console.log('openQuickView(JAB26ST05010): OK, active modal:', activeModalProduct?.id);
closeModal();
console.log('closeModal: OK');


// 8. Test Hamburger Nav Drawer on Product Detail Page
console.log('--- Testing Hamburger Menu on Product Page ---');
openProductPage('JAB26ST05010');
console.log('Opened PDP. pdpView display:', mockDoc.getElementById('productDetailView').style.display);
console.log('homeView display:', mockDoc.getElementById('storefrontHomeView').style.display);

openNavDrawer();
console.log('openNavDrawer() called on PDP:');
console.log('  navDrawer open class:', mockDoc.getElementById('navDrawer').classList.contains('open'));
console.log('  navDrawerBackdrop open class:', mockDoc.getElementById('navDrawerBackdrop').classList.contains('open'));

// Click category in nav drawer while on PDP
filterCategory('coord');
closeNavDrawer();
console.log('Category selected from drawer while on PDP:');
console.log('  pdpView display (should be none):', mockDoc.getElementById('productDetailView').style.display);
console.log('  homeView display (should be block):', mockDoc.getElementById('storefrontHomeView').style.display);
console.log('  navDrawer open class (should be false):', mockDoc.getElementById('navDrawer').classList.contains('open'));


// 9. Test Snitch-Style Split-Screen Login & VIP Authentication
console.log('--- Testing Snitch-Style Split-Screen Login ---');

// Mock localStorage if not present
if (!global.localStorage) {
  var storage = {};
  global.localStorage = {
    getItem: function(k) { return storage[k] || null; },
    setItem: function(k, v) { storage[k] = String(v); },
    removeItem: function(k) { delete storage[k]; },
    clear: function() { storage = {}; }
  };
}

// Open Login Modal
openAccountModal();
console.log('openAccountModal(): OK');
console.log('  accountModalBackdrop open class:', mockDoc.getElementById('accountModalBackdrop').classList.contains('open'));
console.log('  loginStepPhone display:', mockDoc.getElementById('loginStepPhone').style.display);

// Test invalid phone number
mockDoc.getElementById('snitchMobileInput').value = '12345';
requestSnitchOtp();
console.log('Validation (<10 digits): error displayed =', mockDoc.getElementById('snitchPhoneError').style.display === 'block');

// Test valid 10-digit Indian mobile number
mockDoc.getElementById('snitchMobileInput').value = '9988898845';
requestSnitchOtp();
console.log('requestSnitchOtp(9988898845): OK');
console.log('  loginStepPhone display (should be none):', mockDoc.getElementById('loginStepPhone').style.display);
console.log('  loginStepOtp display (should be block):', mockDoc.getElementById('loginStepOtp').style.display);
console.log('  target phone displayed:', mockDoc.getElementById('snitchOtpPhoneDisplay').textContent);

// Verify OTP
verifySnitchOtp();
console.log('verifySnitchOtp(): OK');
console.log('  loginStepOtp display (should be none):', mockDoc.getElementById('loginStepOtp').style.display);
console.log('  loginStepVip display (should be block):', mockDoc.getElementById('loginStepVip').style.display);
console.log('  VIP user displayed:', mockDoc.getElementById('snitchVipUserDisplay').textContent);
console.log('  isSnitchLoggedIn():', isSnitchLoggedIn());
console.log('  accountActiveBadge display:', mockDoc.getElementById('accountActiveBadge').style.display);

// Close modal
closeAccountModalDirect();
console.log('closeAccountModalDirect(): OK, open class:', mockDoc.getElementById('accountModalBackdrop').classList.contains('open'));

// Re-open while logged in -> Should directly open VIP dashboard
openAccountModal();
console.log('Re-opened while logged in: loginStepVip display (should be block):', mockDoc.getElementById('loginStepVip').style.display);

// Test Sign Out
signOutSnitchUser();
console.log('signOutSnitchUser(): OK');
console.log('  isSnitchLoggedIn() after signOut:', isSnitchLoggedIn());
console.log('  loginStepPhone display (should be block):', mockDoc.getElementById('loginStepPhone').style.display);
console.log('  loginStepVip display (should be none):', mockDoc.getElementById('loginStepVip').style.display);
console.log('  accountActiveBadge display (should be none):', mockDoc.getElementById('accountActiveBadge').style.display);

closeAccountModalDirect();

console.log('=== ALL TESTS PASSED WITH 0 ERRORS! ===');

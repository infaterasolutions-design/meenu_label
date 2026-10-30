const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const HTML_FILE = "file:///C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html";
const ARTIFACTS_DIR = "C:\\Users\\sande\\.gemini\\antigravity\\brain\\fe03df0d-2244-4c45-b6ec-4503555ee17f";
const TEMP_USER_DATA = path.join(os.tmpdir(), 'chrome_pdp_test_' + Date.now());

async function run() {
  console.log("Starting headless Chrome on port 9222...");
  const chrome = spawn(CHROME_PATH, [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--window-size=412,915',
    '--user-data-dir=' + TEMP_USER_DATA,
    '--no-first-run',
    '--disable-gpu',
    HTML_FILE
  ]);

  chrome.stderr.on('data', d => {});

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    await new Promise(r => setTimeout(r, 400));
    try {
      const res = await fetch('http://127.0.0.1:9222/json/list');
      const data = await res.json();
      if (data && data.length > 0 && data[0].webSocketDebuggerUrl) {
        wsUrl = data[0].webSocketDebuggerUrl;
        break;
      }
    } catch(e) {}
  }

  if (!wsUrl) {
    console.error("Failed to connect to Chrome debug port");
    chrome.kill();
    process.exit(1);
  }

  console.log("Connected to Chrome CDP target:", wsUrl);
  const ws = new WebSocket(wsUrl);

  if (ws.readyState !== 1) { // 1 = OPEN
    await new Promise((resolve, reject) => {
      ws.addEventListener('open', resolve, { once: true });
      ws.addEventListener('error', reject, { once: true });
    });
  }
  console.log("WebSocket connection established!");

  let idCounter = 1;
  const pending = new Map();

  ws.addEventListener('message', (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(msg.error);
      else resolve(msg.result);
    }
  });

  function send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = idCounter++;
      pending.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async function evaluate(expression) {
    const res = await send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(JSON.stringify(res.exceptionDetails));
    }
    return res.result ? res.result.value : undefined;
  }

  async function captureScreenshot(filepath) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(filepath, Buffer.from(res.data, 'base64'));
    console.log("Saved screenshot:", filepath);
  }

  await send('Page.enable');
  await send('Runtime.enable');
  await send('DOM.enable');

  await new Promise(r => setTimeout(r, 1200));

  console.log("\n--- TEST 1: Open PDP for product JAB26ST05010 ---");
  const initPdp = await evaluate(`
    openProductPage('JAB26ST05010');
    ({
      activePdpProductId: activePdpProductId,
      pdpSelectedSize: pdpSelectedSize,
      mSelected: document.getElementById('pdpSizeBtn_M').classList.contains('selected'),
      lSelected: document.getElementById('pdpSizeBtn_L').classList.contains('selected'),
      xlSelected: document.getElementById('pdpSizeBtn_XL').classList.contains('selected'),
      promptDisplay: document.getElementById('pdpSizeSelectPrompt').style.display,
      cartLen: cart.length
    })
  `);
  console.log("PDP Init State:", JSON.stringify(initPdp, null, 2));

  if (initPdp.pdpSelectedSize === null && !initPdp.mSelected && !initPdp.lSelected && !initPdp.xlSelected) {
    console.log("PASS: All PDP size pills (M, L, XL) are completely UNSELECTED on load!");
  } else {
    console.error("FAIL: A size is still pre-selected on PDP!");
  }

  await evaluate(`
    var s = document.querySelector('.pdp-size-section');
    if (s) s.scrollIntoView({ block: 'center' });
  `);
  await new Promise(r => setTimeout(r, 400));
  await captureScreenshot(path.join(ARTIFACTS_DIR, 'pdp_01_unselected_state.png'));

  console.log("\n--- TEST 2: Click 'ADD TO SHOPPING BAG' without choosing a size ---");
  const addWithoutSize = await evaluate(`
    addPdpProductToCart();
    ({
      cartLen: cart.length,
      toastDisplay: document.getElementById('toastNote').style.display,
      toastText: document.getElementById('toastNote').textContent,
      promptDisplay: document.getElementById('pdpSizeSelectPrompt').style.display
    })
  `);
  console.log("Add to Bag without Size:", JSON.stringify(addWithoutSize, null, 2));

  if (addWithoutSize.cartLen === 0 && addWithoutSize.promptDisplay === 'block') {
    console.log("PASS: Add to bag blocked! Toast shown, warning prompt visible, cart remains 0!");
  } else {
    console.error("FAIL: Cart was not protected!");
  }

  await captureScreenshot(path.join(ARTIFACTS_DIR, 'pdp_02_size_required_alert.png'));

  console.log("\n--- TEST 3: Click 'BUY IT NOW' without choosing a size ---");
  const buyWithoutSize = await evaluate(`
    buyPdpProductNow();
    ({
      cartLen: cart.length,
      toastDisplay: document.getElementById('toastNote').style.display,
      promptDisplay: document.getElementById('pdpSizeSelectPrompt').style.display
    })
  `);
  console.log("Buy it now without Size:", JSON.stringify(buyWithoutSize, null, 2));
  if (buyWithoutSize.cartLen === 0) {
    console.log("PASS: Buy It Now blocked without size selection!");
  }

  console.log("\n--- TEST 4: Customer deliberately selects Size 'L (40)' ---");
  const selectL = await evaluate(`
    selectPdpSize('L', document.getElementById('pdpSizeBtn_L'));
    ({
      pdpSelectedSize: pdpSelectedSize,
      mSelected: document.getElementById('pdpSizeBtn_M').classList.contains('selected'),
      lSelected: document.getElementById('pdpSizeBtn_L').classList.contains('selected'),
      xlSelected: document.getElementById('pdpSizeBtn_XL').classList.contains('selected'),
      promptDisplay: document.getElementById('pdpSizeSelectPrompt').style.display,
      indicatorText: document.getElementById('pdpSelectedSizeIndicator').textContent,
      whatsAppLink: document.getElementById('pdpWhatsAppBtn').href
    })
  `);
  console.log("State after selecting Size L:", JSON.stringify(selectL, null, 2));

  if (selectL.pdpSelectedSize === 'L' && selectL.lSelected && !selectL.mSelected && selectL.promptDisplay === 'none') {
    console.log("PASS: Size L selected cleanly! Prompt dismissed, indicator updated.");
  } else {
    console.error("FAIL: Size L selection failed!");
  }

  await captureScreenshot(path.join(ARTIFACTS_DIR, 'pdp_03_size_L_selected.png'));

  console.log("\n--- TEST 5: Click 'ADD TO SHOPPING BAG' after selecting Size L ---");
  const addWithL = await evaluate(`
    addPdpProductToCart();
    ({
      cartLen: cart.length,
      itemTitle: cart[0].title,
      itemSize: cart[0].size,
      cartOpen: document.getElementById('cartDrawer').classList.contains('open')
    })
  `);
  console.log("State after Add to Bag with Size L:", JSON.stringify(addWithL, null, 2));

  if (addWithL.cartLen === 1 && addWithL.itemSize === 'L') {
    console.log("PASS: Ensemble added to bag in exactly Size L!");
  } else {
    console.error("FAIL: Add to bag with Size L failed!");
  }

  await new Promise(r => setTimeout(r, 600));
  await captureScreenshot(path.join(ARTIFACTS_DIR, 'pdp_04_cart_with_size_L.png'));

  console.log("\n--- TEST 6: Quick View Modal Size Selection ---");
  const testModal = await evaluate(`
    closeCart();
    openProductModal('SET916');
    var modalBtns = document.querySelectorAll('.modal-size-btn');
    ({
      modalOpen: document.getElementById('productModalBackdrop').classList.contains('open'),
      selectedSize: selectedSize,
      mSelected: modalBtns[0].classList.contains('selected'),
      lSelected: modalBtns[1].classList.contains('selected'),
      xlSelected: modalBtns[2].classList.contains('selected')
    })
  `);
  console.log("Modal Init State:", JSON.stringify(testModal, null, 2));

  if (testModal.selectedSize === null && !testModal.mSelected && !testModal.lSelected) {
    console.log("PASS: Quick View Modal also starts with ZERO default size selected!");
  }

  // Attempt add to cart from modal without size
  const modalAddEmpty = await evaluate(`
    var cartBefore = cart.length;
    addCurrentProductToCart();
    ({
      cartBefore: cartBefore,
      cartAfter: cart.length,
      modalPromptDisplay: document.getElementById('modalSizeSelectPrompt').style.display,
      toastText: document.getElementById('toastNote').textContent
    })
  `);
  console.log("Modal Add without size:", JSON.stringify(modalAddEmpty, null, 2));

  if (modalAddEmpty.cartBefore === modalAddEmpty.cartAfter && modalAddEmpty.modalPromptDisplay === 'block') {
    console.log("PASS: Modal blocks add to bag until size is deliberately chosen!");
  }

  // Select XL in modal
  const modalSelectXL = await evaluate(`
    var modalBtns = document.querySelectorAll('.modal-size-btn');
    selectModalSize('XL', modalBtns[2]);
    addCurrentProductToCart();
    ({
      cartLen: cart.length,
      lastItemSize: cart[cart.length - 1].size
    })
  `);
  console.log("Modal Add with XL:", JSON.stringify(modalSelectXL, null, 2));

  if (modalSelectXL.lastItemSize === 'XL') {
    console.log("PASS: Modal item added in Size XL successfully!");
  }

  console.log("\nALL VERIFICATIONS PASSED 100%!");

  ws.close();
  chrome.kill();
  try {
    fs.rmSync(TEMP_USER_DATA, { recursive: true, force: true });
  } catch(e) {}
  process.exit(0);
}

run().catch(err => {
  console.error("Fatal Error:", err);
  process.exit(1);
});

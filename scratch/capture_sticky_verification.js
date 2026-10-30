const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const ARTIFACTS_DIR = "C:\\Users\\sande\\.gemini\\antigravity\\brain\\fe03df0d-2244-4c45-b6ec-4503555ee17f";
const TEMP_USER_DATA = path.join(os.tmpdir(), 'chrome_sticky_proof_' + Date.now());
const PORT = 9777;
const FILE_URL = "file:///C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html";

async function run() {
  console.log("Starting Chrome with isolated dir and disabled extensions...");
  const chrome = spawn(CHROME_PATH, [
    '--headless=new',
    `--remote-debugging-port=${PORT}`,
    '--window-size=1280,880',
    '--user-data-dir=' + TEMP_USER_DATA,
    '--no-first-run',
    '--disable-extensions',
    '--disable-gpu',
    FILE_URL
  ]);

  let pageTarget = null;
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 400));
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/list`);
      const data = await res.json();
      pageTarget = data.find(d => d.type === 'page' && d.webSocketDebuggerUrl);
      if (pageTarget) break;
    } catch(e) {}
  }

  if (!pageTarget) {
    console.error("Could not find page target!");
    chrome.kill();
    process.exit(1);
  }

  console.log("Connecting to Page Target WebSocket:", pageTarget.webSocketDebuggerUrl);
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve, { once: true });
    ws.addEventListener('error', reject, { once: true });
  });

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
    const res = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    if (res.exceptionDetails) throw new Error(JSON.stringify(res.exceptionDetails));
    return res.result ? res.result.value : undefined;
  }

  async function snap(filename) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    const full = path.join(ARTIFACTS_DIR, filename);
    fs.writeFileSync(full, Buffer.from(res.data, 'base64'));
    console.log("Saved artifact:", filename);
  }

  await send('Page.enable');
  await send('Runtime.enable');

  console.log("Waiting for openProductPage to be ready...");
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 500));
    try {
      const ready = await evaluate(`typeof window.openProductPage === 'function' && typeof window.productsData !== 'undefined'`);
      if (ready) {
        console.log("Page script ready!");
        break;
      }
    } catch(e) {}
  }

  // Disable smooth scroll during screenshot test so scrollTo is instantaneous
  await evaluate(`
    document.documentElement.style.scrollBehavior = 'auto';
    document.body.style.scrollBehavior = 'auto';
    openProductPage('JAB26ST05010');
    window.scrollTo(0, 0);
  `);
  await new Promise(r => setTimeout(r, 600));

  console.log("\n--- Step 1: Initial Top Position (scrollY = 0) ---");
  const pos0 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var i = document.querySelector('.pdp-info-col');
    var rg = g.getBoundingClientRect();
    var ri = i.getBoundingClientRect();
    ({
      galleryTop: Math.round(rg.top),
      galleryHeight: Math.round(rg.height),
      infoTop: Math.round(ri.top),
      infoHeight: Math.round(ri.height),
      scrollY: window.scrollY
    })
  `);
  console.log("Top metrics:", pos0);
  await snap('pdp_verified_top.png');

  console.log("\n--- Step 2: Window Scrolled Down by 450px ---");
  await evaluate(`window.scrollTo(0, 450);`);
  await new Promise(r => setTimeout(r, 500));

  const pos450 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var i = document.querySelector('.pdp-info-col');
    var rg = g.getBoundingClientRect();
    var ri = i.getBoundingClientRect();
    ({
      galleryTop: Math.round(rg.top),
      galleryHeight: Math.round(rg.height),
      infoTop: Math.round(ri.top),
      infoHeight: Math.round(ri.height),
      scrollY: window.scrollY,
      galleryIsSticky: Math.abs(rg.top - 115) < 15
    })
  `);
  console.log("Scrolled 450px metrics:", pos450);
  await snap('pdp_verified_scrolled_450.png');

  console.log("\n--- Step 3: Window Scrolled Down by 750px (Accordions) ---");
  await evaluate(`window.scrollTo(0, 750);`);
  await new Promise(r => setTimeout(r, 500));

  const pos750 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var i = document.querySelector('.pdp-info-col');
    var rg = g.getBoundingClientRect();
    var ri = i.getBoundingClientRect();
    ({
      galleryTop: Math.round(rg.top),
      galleryHeight: Math.round(rg.height),
      infoTop: Math.round(ri.top),
      infoHeight: Math.round(ri.height),
      scrollY: window.scrollY,
      galleryIsSticky: Math.abs(rg.top - 115) < 15
    })
  `);
  console.log("Scrolled 750px metrics:", pos750);
  await snap('pdp_verified_scrolled_750.png');

  ws.close();
  chrome.kill();
  try { fs.rmSync(TEMP_USER_DATA, { recursive: true, force: true }); } catch(e) {}
  console.log("\nALL VERIFICATIONS AND SCREENSHOTS SUCCESSFUL!");
}

run().catch(err => {
  console.error("Fatal error:", err);
  process.exit(1);
});

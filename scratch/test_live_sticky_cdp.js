const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const ARTIFACTS_DIR = "C:\\Users\\sande\\.gemini\\antigravity\\brain\\fe03df0d-2244-4c45-b6ec-4503555ee17f";
const TEMP_USER_DATA = path.join(os.tmpdir(), 'chrome_sticky_test_' + Date.now());

// Read storefront HTML
let html = fs.readFileSync('C:\\Users\\sande\\Downloads\\Meenu_Label_Desktop_Storefront.html', 'utf-8');

// We will inject the updated CSS to test it live
const testStickyCss = `
<style id="testStickyStyle">
  /* Enable sticky by removing overflow containment from body/html on desktop */
  @media (min-width: 993px) {
    html, body {
      overflow-x: visible !important;
      overflow-y: visible !important;
    }
    .pdp-section {
      overflow: visible !important;
    }
    .pdp-grid {
      display: grid !important;
      grid-template-columns: 1.05fr 1fr !important;
      gap: 48px !important;
      align-items: start !important;
      overflow: visible !important;
    }
    .pdp-gallery-col {
      position: -webkit-sticky !important;
      position: sticky !important;
      top: 95px !important;
      align-self: start !important;
      height: fit-content !important;
    }
    .pdp-main-image-wrap {
      max-height: calc(100vh - 200px) !important;
    }
    .pdp-main-image {
      max-height: calc(100vh - 200px) !important;
      object-fit: cover !important;
    }
    .pdp-info-col {
      max-height: none !important;
      overflow: visible !important;
      padding-right: 0 !important;
    }
  }
</style>
`;

html = html.replace('</head>', testStickyCss + '</head>');
const testHtmlFile = path.join(os.tmpdir(), 'test_sticky_live.html');
fs.writeFileSync(testHtmlFile, html, 'utf-8');

async function run() {
  console.log("Launching headless Chrome for CDP sticky test...");
  const chrome = spawn(CHROME_PATH, [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--window-size=1280,880',
    '--user-data-dir=' + TEMP_USER_DATA,
    '--no-first-run',
    '--disable-gpu',
    'file:///' + testHtmlFile.replace(/\\/g, '/')
  ]);

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
    console.error("Failed to connect to CDP");
    chrome.kill();
    process.exit(1);
  }

  const ws = new WebSocket(wsUrl);
  if (ws.readyState !== 1) {
    await new Promise((resolve, reject) => {
      ws.addEventListener('open', resolve, { once: true });
      ws.addEventListener('error', reject, { once: true });
    });
  }

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

  async function screenshot(filepath) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(filepath, Buffer.from(res.data, 'base64'));
    console.log("Saved screenshot:", filepath);
  }

  await send('Page.enable');
  await send('Runtime.enable');
  await new Promise(r => setTimeout(r, 1200));

  // Open PDP
  await evaluate(`
    openProductPage('JAB26ST05010');
    window.scrollTo(0, 0);
  `);
  await new Promise(r => setTimeout(r, 500));

  console.log("\n--- Checking Initial Position (Scroll Y = 0) ---");
  const pos0 = await evaluate(`
    var gallery = document.querySelector('.pdp-gallery-col');
    var rect0 = gallery.getBoundingClientRect();
    ({
      top: rect0.top,
      bottom: rect0.bottom,
      height: rect0.height,
      scrollY: window.scrollY
    })
  `);
  console.log("Scroll Y=0 Gallery Position:", pos0);
  await screenshot(path.join(ARTIFACTS_DIR, 'live_sticky_y0.png'));

  // Now scroll window down by 450px
  console.log("\n--- Scrolling Window Down by 450px ---");
  await evaluate(`window.scrollTo(0, 450);`);
  await new Promise(r => setTimeout(r, 500));

  const pos450 = await evaluate(`
    var gallery = document.querySelector('.pdp-gallery-col');
    var info = document.querySelector('.pdp-info-col');
    var rectG = gallery.getBoundingClientRect();
    var rectI = info.getBoundingClientRect();
    ({
      galleryTop: rectG.top,
      galleryHeight: rectG.height,
      infoTop: rectI.top,
      infoHeight: rectI.height,
      scrollY: window.scrollY,
      stickyApplied: Math.abs(rectG.top - 95) < 15
    })
  `);
  console.log("Scroll Y=450 Gallery Position:", pos450);

  if (pos450.stickyApplied) {
    console.log("SUCCESS! Left gallery is STICKY at top ~95px while window scrolled down!");
  } else {
    console.log("NOT STICKY YET! galleryTop is:", pos450.galleryTop);
  }

  await screenshot(path.join(ARTIFACTS_DIR, 'live_sticky_y450.png'));

  // Scroll window down by 750px (to accordions)
  console.log("\n--- Scrolling Window Down by 750px (Accordions visible) ---");
  await evaluate(`window.scrollTo(0, 750);`);
  await new Promise(r => setTimeout(r, 500));

  const pos750 = await evaluate(`
    var gallery = document.querySelector('.pdp-gallery-col');
    var rectG = gallery.getBoundingClientRect();
    ({
      galleryTop: rectG.top,
      scrollY: window.scrollY,
      stickyApplied: Math.abs(rectG.top - 95) < 15
    })
  `);
  console.log("Scroll Y=750 Gallery Position:", pos750);
  await screenshot(path.join(ARTIFACTS_DIR, 'live_sticky_y750.png'));

  ws.close();
  chrome.kill();
  try { fs.rmSync(TEMP_USER_DATA, { recursive: true, force: true }); } catch(e) {}
  try { fs.unlinkSync(testHtmlFile); } catch(e) {}
}

run().catch(err => {
  console.error("Fatal:", err);
  process.exit(1);
});

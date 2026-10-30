const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const ARTIFACTS_DIR = "C:\\Users\\sande\\.gemini\\antigravity\\brain\\fe03df0d-2244-4c45-b6ec-4503555ee17f";
const TEMP_USER_DATA = path.join(os.tmpdir(), 'chrome_sticky_proof_' + Date.now());
const PORT = 9339;

// Read the storefront HTML directly!
let html = fs.readFileSync('C:\\Users\\sande\\Downloads\\Meenu_Label_Desktop_Storefront.html', 'utf-8');

// Inject a tiny script that opens PDP right away
const autoOpenPdp = `
<script>
window.addEventListener('DOMContentLoaded', () => {
  if (typeof openProductPage === 'function') {
    openProductPage('JAB26ST05010');
  }
});
</script>
`;
html = html.replace('</body>', autoOpenPdp + '</body>');

const testHtmlFile = path.join(os.tmpdir(), 'test_pdp_sticky_verify.html');
fs.writeFileSync(testHtmlFile, html, 'utf-8');

async function run() {
  console.log("Launching headless Chrome on port " + PORT);
  const chrome = spawn(CHROME_PATH, [
    '--headless=new',
    `--remote-debugging-port=${PORT}`,
    '--window-size=1280,880',
    '--user-data-dir=' + TEMP_USER_DATA,
    '--no-first-run',
    '--disable-gpu',
    'file:///' + testHtmlFile.replace(/\\/g, '/')
  ]);

  let wsUrl = null;
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 300));
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/list`);
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

  async function capture(filename) {
    const res = await send('Page.captureScreenshot', { format: 'png' });
    const fullPath = path.join(ARTIFACTS_DIR, filename);
    fs.writeFileSync(fullPath, Buffer.from(res.data, 'base64'));
    console.log("Saved artifact:", filename);
  }

  await send('Page.enable');
  await send('Runtime.enable');
  
  console.log("Waiting for page and scripts to fully load...");
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 500));
    try {
      const ready = await evaluate(`document.readyState === 'complete' && typeof window.openProductPage === 'function'`);
      if (ready) {
        console.log("Page ready and openProductPage defined!");
        break;
      }
    } catch(e) {}
  }

  // 1. Initial Position (Scroll Y = 0)
  console.log("Capturing Y=0...");
  await evaluate(`
    openProductPage('JAB26ST05010');
    window.scrollTo(0, 0);
  `);
  await new Promise(r => setTimeout(r, 400));
  const pos0 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var rect = g.getBoundingClientRect();
    ({ top: rect.top, height: rect.height, scrollY: window.scrollY })
  `);
  console.log("Y=0 Position:", pos0);
  await capture('verified_sticky_pdp_top.png');

  // 2. Scroll window down to 500px (Size selector and action buttons area)
  console.log("Scrolling to Y=500...");
  await evaluate(`window.scrollTo(0, 500);`);
  await new Promise(r => setTimeout(r, 400));
  const pos500 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var rect = g.getBoundingClientRect();
    ({ top: rect.top, height: rect.height, scrollY: window.scrollY })
  `);
  console.log("Y=500 Position:", pos500);
  await capture('verified_sticky_pdp_scrolled_500.png');

  // 3. Scroll window down to 850px (Accordions area)
  console.log("Scrolling to Y=850...");
  await evaluate(`window.scrollTo(0, 850);`);
  await new Promise(r => setTimeout(r, 400));
  const pos850 = await evaluate(`
    var g = document.querySelector('.pdp-gallery-col');
    var rect = g.getBoundingClientRect();
    ({ top: rect.top, height: rect.height, scrollY: window.scrollY })
  `);
  console.log("Y=850 Position:", pos850);
  await capture('verified_sticky_pdp_scrolled_850.png');

  ws.close();
  chrome.kill();
  try { fs.rmSync(TEMP_USER_DATA, { recursive: true, force: true }); } catch(e) {}
  try { fs.unlinkSync(testHtmlFile); } catch(e) {}
  console.log("Finished successfully!");
}

run().catch(err => {
  console.error("Fatal:", err);
  process.exit(1);
});

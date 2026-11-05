import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

head_inject = """<head><script>
window.__caughtErrors = [];
window.onerror = function(msg, url, line, col, err) {
  window.__caughtErrors.push(msg + " at line " + line + ":" + col);
};
</script>"""

body_inject = """<script>
var d = document.createElement("div");
d.id = "js-error-dump";
d.textContent = "ERRORS: " + JSON.stringify(window.__caughtErrors);
document.body.appendChild(d);
</script></body>"""

test_content = orig.replace('<head>', head_inject, 1)
test_content = test_content.replace('</body>', body_inject, 1)

with open('scratch/temp_js_error_test.html', 'w', encoding='utf-8') as f:
    f.write(test_content)

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd = [chrome_exe, '--headless=new', '--disable-gpu', '--virtual-time-budget=3000', '--dump-dom', 'file:///C:/Users/sande/Documents/antigravity/splendid-nobel/scratch/temp_js_error_test.html']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
for l in res.stdout.split('\n'):
    if 'js-error-dump' in l:
        print(l)

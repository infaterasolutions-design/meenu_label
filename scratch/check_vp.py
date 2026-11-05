import subprocess

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
test_script = """<script>
window.addEventListener('load', function() {
  var d = document.createElement("div");
  d.id = "vp-dump";
  d.textContent = "VIEWPORT: innerW=" + window.innerWidth + ", innerH=" + window.innerHeight + ", htmlClientW=" + document.documentElement.clientWidth + ", bodyClientW=" + document.body.clientWidth;
  document.body.appendChild(d);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('</body>', test_script + '</body>')
with open('scratch/temp_vp_test.html', 'w', encoding='utf-8') as f:
    f.write(text)

cmd = [chrome_exe, '--headless=new', '--disable-gpu', '--window-size=412,915', '--virtual-time-budget=2000', '--dump-dom', 'file:///C:/Users/sande/Documents/antigravity/splendid-nobel/scratch/temp_vp_test.html']
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.split('\n'):
    if 'vp-dump' in l:
        print(l)

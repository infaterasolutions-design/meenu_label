import subprocess, os, json

artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_verify_search'

with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Apply test enhancements to HTML string
# 1. Update .search-close-action css
html = html.replace('.search-close-action {\n      position: absolute;\n      top: 0;\n      right: 0;', 
                    '.search-close-action {\n      position: absolute;\n      top: 0;\n      right: 0;\n      z-index: 280;\n      pointer-events: auto;\n      min-height: 36px;\n      display: inline-flex;\n      align-items: center;')

# 2. Add padding-right to .search-input-box
html = html.replace('.search-input-box {\n      display: flex;',
                    '.search-input-box {\n      display: flex;\n      padding-right: 80px;')

# 3. Update search-close-action button tag
html = html.replace('<button class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>',
                    '<button type="button" class="search-close-action" id="searchCloseBtn" onclick="closeSearchBar(event)" title="Close Search">Close &times;</button>')

# 4. Update JS logic
new_js = """
    function closeSearchBar(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      var bar = document.getElementById('searchOverlayBar');
      if (bar) {
        bar.classList.remove('open');
      }
    }

    /* Search Bar Overlay Logic */
    function toggleSearchBar(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      var bar = document.getElementById('searchOverlayBar');
      if (!bar) return;
      var willOpen = !bar.classList.contains('open');
      bar.classList.toggle('open');
      if (willOpen) {
        setTimeout(function() {
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }, 120);
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
        closeSearchBar();
      }
    });

    document.addEventListener('click', function(e) {
      var bar = document.getElementById('searchOverlayBar');
      if (!bar || !bar.classList.contains('open')) return;
      var isSearchTrigger = e.target.closest('.header-search-btn, .search-close-action, [onclick*="toggleSearchBar"], [onclick*="closeSearchBar"]');
      var isInsideBar = bar.contains(e.target);
      if (!isInsideBar && !isSearchTrigger) {
        closeSearchBar();
      }
    });
"""

html = html.replace("""    /* Search Bar Overlay Logic */
    function toggleSearchBar() {
      var bar = document.getElementById('searchOverlayBar');
      bar.classList.toggle('open');
      if (bar.classList.contains('open')) {
        setTimeout(function() {
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }, 120);
      }
    }""", new_js)

test_html_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\test_search_full.html'
with open(test_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Test HTML written. Now running headless Chrome test...")

test_script = """
<script>
window.addEventListener('load', () => {
    console.log('=== TEST START ===');
    const bar = document.getElementById('searchOverlayBar');
    const closeBtn = document.getElementById('searchCloseBtn');
    
    // 1. Open search
    toggleSearchBar();
    console.log('Opened search bar. Open status:', bar.classList.contains('open'));
    
    // 2. Element at center of close button
    const btnRect = closeBtn.getBoundingClientRect();
    const cx = btnRect.left + btnRect.width / 2;
    const cy = btnRect.top + btnRect.height / 2;
    const hit = document.elementFromPoint(cx, cy);
    console.log('Hit at close button center:', hit ? (hit.tagName + '.' + hit.className + '#' + hit.id) : 'NONE');
    
    // 3. Simulate click on close button
    closeBtn.click();
    console.log('Clicked close button. Open status:', bar.classList.contains('open'));
    
    // 4. Test reopen and escape key
    toggleSearchBar();
    console.log('Reopened search bar. Open status:', bar.classList.contains('open'));
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    console.log('Pressed Escape key. Open status:', bar.classList.contains('open'));
    console.log('=== TEST FINISHED SUCCESSFULLY ===');
});
</script>
"""

with open(test_html_path, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_script + '</body>'))

res = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    '--window-size=1280,800',
    '--virtual-time-budget=3000',
    '--enable-logging=stderr',
    f'file:///{test_html_path}'
], capture_output=True, text=True)

for l in res.stderr.splitlines():
    if 'TEST' in l or 'Hit at' in l or 'status' in l:
        print(l)

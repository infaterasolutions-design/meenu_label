with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace CSS in index.html
with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

snitch_css_start = css_content.find("/* ========================================================\n   EXACT SNITCH-STYLE QUICK SIZE POPUP DRAWER")
snitch_css = css_content[snitch_css_start:]

# Remove any old quick size CSS
old_css_idx = html.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE")
if old_css_idx != -1:
    old_css_end = html.find("</style>", old_css_idx)
    html = html[:old_css_idx] + snitch_css + "\n" + html[old_css_end:]
    print("Replaced quick size CSS in index.html with Snitch drawer CSS")
else:
    # check if snitch css already there
    if "EXACT SNITCH-STYLE QUICK SIZE POPUP DRAWER" not in html:
        style_end = html.find("</style>")
        html = html[:style_end] + "\n" + snitch_css + "\n" + html[style_end:]
        print("Injected Snitch drawer CSS into index.html")

# 2. Replace Modal HTML in index.html
old_modal_start = html.find("<!-- Quick Size Popup Interface Modal")
if old_modal_start != -1:
    old_modal_end = html.find("</div>\n</div>", old_modal_start) + 13
    with open('snippets/quick-size-modal.liquid', 'r', encoding='utf-8') as f:
        snitch_modal_html = f.read()
    html = html[:old_modal_start] + snitch_modal_html + "\n" + html[old_modal_end:]
    print("Replaced modal HTML in index.html with Snitch drawer HTML")
else:
    if "id=\"snitchSizeModalBackdrop\"" not in html:
        body_end = html.find("</body>")
        with open('snippets/quick-size-modal.liquid', 'r', encoding='utf-8') as f:
            snitch_modal_html = f.read()
        html = html[:body_end] + snitch_modal_html + "\n" + html[body_end:]
        print("Injected Snitch drawer HTML into index.html")

# 3. Replace JS in index.html
with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

snitch_js_start = js_content.find("/* ========================================================\n   EXACT SNITCH-STYLE QUICK SIZE DRAWER LOGIC")
snitch_js = js_content[snitch_js_start:]

old_js_start = html.find("/* ========================================================\n   QUICK SIZE POPUP INTERFACE LOGIC")
if old_js_start != -1:
    old_js_end = html.find("</script>", old_js_start)
    html = html[:old_js_start] + snitch_js + "\n" + html[old_js_end:]
    print("Replaced quick size JS in index.html with Snitch drawer JS")
else:
    if "function createSnitchSizeRow" not in html:
        script_end = html.rfind("</script>")
        html = html[:script_end] + "\n" + snitch_js + "\n" + html[script_end:]
        print("Injected Snitch drawer JS into index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")

import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_html = text.find('<div class="announcement-bar">')
snippet = text[pos_html:pos_html+320]
sys.stdout.buffer.write(snippet.encode('utf-8'))

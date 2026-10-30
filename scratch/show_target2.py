import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_pdp = text.find('<div class="pdp-scarcity-banner">')
snippet = text[pos_pdp-150:pos_pdp+250]
sys.stdout.buffer.write(snippet.encode('utf-8'))

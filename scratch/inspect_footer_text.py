import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_footer = text.find('<footer>')
# find after the base64 image
idx_after_img = text.find('class="footer-col"', pos_footer + 100)
snippet = text[idx_after_img:idx_after_img+2500]
sys.stdout.buffer.write(snippet.encode('utf-8'))

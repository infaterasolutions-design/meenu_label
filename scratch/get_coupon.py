import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('function applyCoupon')
snippet = text[idx:idx+1000]
sys.stdout.buffer.write(snippet.encode('utf-8'))

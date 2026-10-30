import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_script = text.find('<script>')
snippet = text[pos_script:pos_script+800]
sys.stdout.buffer.write(snippet.encode('utf-8'))

import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('var btns = document.querySelectorAll(\'.modal-size-btn\');')
print(html[idx:idx+1500])

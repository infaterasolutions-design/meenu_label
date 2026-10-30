import sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('var currentSlide')
if idx != -1:
    print(text[idx:idx+900])
else:
    print("var currentSlide not found")

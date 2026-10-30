import sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function nextSlide')
if idx != -1:
    print(text[idx-100:idx+800])
else:
    print("nextSlide not found")

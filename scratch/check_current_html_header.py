with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<header>')
end = text.find('</header>') + 9
print(text[pos:end])

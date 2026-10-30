with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("document.getElementById('founder').scrollIntoView({behavior:'smooth'});", "document.getElementById('founder').scrollIntoView({{behavior:'smooth'}});")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed braces in scrollIntoView.")

csv_path = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace handles and titles
text = text.replace('jaipur-chanderi-silk-festive-suit', 'the-royal-wine-chanderi-festive-suit')
text = text.replace('Jaipur Chanderi Silk Festive Suit', 'The Royal Wine Chanderi Festive Suit')
text = text.replace('Chanderi Silk & Zari with Organza Dupatta', 'Pure Chanderi Silk in Royal Wine with Antique Gold Zari & Organza Dupatta')

with open(csv_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated CSV successfully!')

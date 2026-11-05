with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("snitchSizeModalBackdrop in index.html:", 'id="snitchSizeModalBackdrop"' in text)
print("CHOOSE YOUR SIZE in index.html:", 'CHOOSE YOUR SIZE' in text)
print("snitchSizeList in index.html:", 'id="snitchSizeList"' in text)
print("openQuickSizePopup in index.html:", 'function openQuickSizePopup' in text)
print("createSnitchSizeRow in index.html:", 'function createSnitchSizeRow' in text)

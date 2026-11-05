with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count('class="snitch-plus-trigger"')
print("snitch-plus-trigger occurrences in index.html:", count)
has_modal = 'id="quickSizeModalBackdrop"' in text
print("Has quickSizeModalBackdrop:", has_modal)
has_js = 'function openQuickSizePopup' in text
print("Has openQuickSizePopup:", has_js)

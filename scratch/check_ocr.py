try:
    import pytesseract
    from PIL import Image
    p = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
    text = pytesseract.image_to_string(Image.open(p))
    print("OCR text found:")
    print(text.strip())
except Exception as e:
    print(f"pytesseract check: {e}")

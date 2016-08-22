#!/usr/bin/env python3.5

try:
    import Image
except ImportError:
    from PIL import Image
 
import pytesseract
filename = '/Users/royce/Desktop/SS.png'
image = Image.open(filename)
string = pytesseract.image_to_string(image)
print(string)

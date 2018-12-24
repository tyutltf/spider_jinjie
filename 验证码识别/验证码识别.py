import pytesseract
from PIL import Image
import tesserocr

im=Image.open('test.jpg')
print(pytesseract.image_to_string(im))
im1=Image.open('image.png')
print(pytesseract.image_to_string(im1))

imag=Image.open('test.jpg')
print(tesserocr.image_to_text(imag))
imag1=Image.open('image.png')
print(tesserocr.image_to_text(imag1))
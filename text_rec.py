from PIL import Image
import pytesseract
import cv2
import numpy as np

img = Image.open(r"C:\Users\snpaj\Desktop\sample_flask\0.jpg").convert('L')
ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)

# Older versions of pytesseract need a pillow image
# Convert back if needed
img = Image.fromarray(img.astype(np.uint8))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(img,lang="tam")  #Specify language to look after!
print(text)
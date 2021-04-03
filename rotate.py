from PIL import Image
import pytesseract
import cv2
import numpy as np
# Opens a image in RGB mode 
im = Image.open(r"C:\Users\snpaj\Desktop\sample_flask\image-temp\ration_card\ration_card_b.jpg")  
img = im.crop((500,62,777,339))

img = img.convert('L')

ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)


img = Image.fromarray(img.astype(np.uint8))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(img,lang="tam")  #Specify language to look after!
print(text)

  

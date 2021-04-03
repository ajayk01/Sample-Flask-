import cv2
import numpy as np
from PIL import Image
import pytesseract
import re



def extract_text_ration(path_front,path_back):
    ration_card={}
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    
    im_f = Image.open(path_front)
    ration_details=[]
    img_f = im_f.crop((242,242,1002,555))
    img_f = img_f.convert('L')
    ret,img_f = cv2.threshold(np.array(img_f), 125, 255, cv2.THRESH_BINARY)
    img_f = Image.fromarray(img_f.astype(np.uint8))
    text_f = pytesseract.image_to_string(img_f,lang="tam")
    s=(text_f.replace("\n","--").replace("\u200c","|").replace("|"," ").split("--"))
    for i in s:
        d=[]
        d.append(i);
        ration_details.append(d)
    ration_details = [ele for ele in ration_details if ele != ['']] 
    ration_card={'Details': ration_details}
    head=(ration_card['Details'][0][0].split(":")[1])
    
    img_f=im_f.crop((4,490,250,600))
    text_f = pytesseract.image_to_string(img_f)
    s=(text_f.replace('\n',' ').split())
    ration_card['Card Number']= s[1]
    ration_card['Card Type'] = s[0];
    
    
    img_f=im_f.crop((5,250,240,492))
    img_data = np.asarray(img_f)
    #img = Image.fromarray(numpydata, 'RGB')
    ration_card['img'] = img_data
    
    
    im_b = Image.open(path_back)
    img_b = im_b.crop((51,71,280,322))
    img_b = img_b.convert('L')
    ret,img_b = cv2.threshold(np.array(img_b), 125, 255, cv2.THRESH_BINARY)
    img_b = Image.fromarray(img_b.astype(np.uint8))
    text_b = pytesseract.image_to_string(img_b,lang="tam")
    s=(text_b.split("\n"))
    pattern = '[0-9,\u200c]'
    s = [re.sub(pattern, '', i) for i in s] 
    s.insert(0,head)
    ration_card['Members']=s;
    
    img_b = im_b.crop((350,80,500,110))
    img_b = img_b.convert('L')
    ret,img_b = cv2.threshold(np.array(img_b), 125, 255, cv2.THRESH_BINARY)
    img_b = Image.fromarray(img_b.astype(np.uint8))
    text_b = pytesseract.image_to_string(img_b,lang="eng")
    ration_card['shop_number']=text_b;
    
    for i in ration_card:
        print(ration_card[i])
    
    



def crop_bg(name,img,loc,w,h,count=0):
    mask = np.zeros(img.shape[:2], np.uint8)
    for pt in zip(*loc[::-1]):
        if mask[pt[1] + h//2, pt[0] + w//2] != 255:
            mask[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = 255
            count += 1
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 3)
            roi = img[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
            roi = cv2.rotate(roi, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)  
            cv2.imwrite(name+str(count+1) + '.jpg', roi)
             

             
def match(img,img_temp): 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h = img_temp.shape[::-1]
    res = cv2.matchTemplate(img_gray,img_temp,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
        
    number = np.sum(res >= threshold)
    print("hello",number)
    if(number==0):
        return img,loc,w,h,0;
    else:
        count = 0
        mask = np.zeros(img.shape[:2], np.uint8)
        for pt in zip(*loc[::-1]):
            if mask[pt[1] + h//2, pt[0] + w//2] != 255:
                mask[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = 255
                count += 1
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 3)
                print("Number of found matches:", count)
                # small = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            
                # cv2.imshow('Matches',small)
                cv2.waitKey(0) & 0xFF== ord('q')
                cv2.destroyAllWindows()
                return img,loc,w,h,count;

        
def main(name):        

# img = cv2.imread(r"C:\Users\snpaj\Desktop\sample_flask\image-temp\ration_card\12-b.jpg");

# img_temp = cv2.imread(r"C:\Users\snpaj\Desktop\sample_flask\image-temp\ration_card\f_"+name+".jpg",0);
# img,loc,w,h,number=match(img,img_temp);
# print(number)
# if(number==1):    
#     crop_bg("ration",img,loc,w,h);   
# else:
#     print("Inside else")
#     img_temp = cv2.rotate(img_temp, cv2.cv2.ROTATE_90_CLOCKWISE) 
#     img,loc,w,h,number=match(img,img_temp);
#     crop_bg("ration",img,loc,w,h);
#     if(number!=1):
#         print("enter the valid image")

f=r'C:\Users\snpaj\Desktop\sample_flask\image-temp\ration_card\f_ration_card.jpg'
b=r'C:\Users\snpaj\Desktop\sample_flask\image-temp\ration_card\ration_card_b.jpg'
extract_text_ration(f,b);



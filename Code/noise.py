import cv2
import os

def median(img, ksize = 3):
    img = cv2.medianBlur(img, ksize)
    return img

os.mkdir('Test_no_noise')

for root, dirs, files in os.walk("./Test"):  
    for filename in files:
        if 'jpg' in filename:
            img = cv2.imread(os.path.join(root, filename))
            img2 = median(img)
            cv2.imwrite(os.path.join(root+'_no_noise', filename), img2)
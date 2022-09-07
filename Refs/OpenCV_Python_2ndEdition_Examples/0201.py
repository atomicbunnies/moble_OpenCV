# 0201.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
imageFile = './data/lena.jpg'
img1  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR

text = 'OpenCV Programming'
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,text, org, font, 1, (255,0,0), 2)
cv2.imshow('img', img1)
##encode_img = np.fromfile(imageFile, np.uint8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)
cv2.imwrite('./data/sample.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 100])

cv2.waitKey()
cv2.destroyAllWindows()


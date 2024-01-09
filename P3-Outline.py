import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_out=cv2.Canny(img,100,100)
cv2.imshow("Image Outline",img_out)
cv2.waitKey(0)

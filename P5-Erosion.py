import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_erosion=cv2.erode(img,kernel,iterations=10)
cv2.imshow("Eroded Image",img_erosion)
cv2.waitKey(0)

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image",img_g)
cv2.waitKey(0)

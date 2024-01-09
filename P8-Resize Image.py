import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_resize=cv2.resize(img,(300,200))
cv2.imshow("Resized Image",img_resize)
cv2.waitKey(0)

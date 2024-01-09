import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_blur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur",img_blur)
cv2.waitKey(0)

import cv2
import numpy as np
img = cv2.imread("D:\Photoshoot\Sample.jpg")
rows,cols,ch = img.shape
p1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
p2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
p = cv2.getPerspectiveTransform(p1,p2)
pt= cv2.warpPerspective(img,p,(cols, rows))
cv2.imshow('Perspective Transformation', pt)
cv2.waitKey(0)
cv2.destroyAllWindows()

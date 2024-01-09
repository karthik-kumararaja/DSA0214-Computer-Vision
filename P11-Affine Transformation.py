import cv2
import numpy as np
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
rows,cols,_=img.shape
p1=np.float32([[50,50],[200,50],[50,200]])
p2=np.float32([[10,100],[200,50],[100,250]])
at=cv2.getAffineTransform(p1,p2)
a=cv2.warpAffine(img,at,(cols,rows))
cv2.imshow("Affine Transformation",a)
cv2.waitKey(0)

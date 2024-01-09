import cv2
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_g,(7,7),0)
canny=cv2.Canny(img_blur,threshold1=10,threshold2=20)
cv2.imshow("Canny Edge Detection",canny)
cv2.waitKey(0)
     

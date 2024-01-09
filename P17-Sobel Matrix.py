import cv2
path="D:\Photoshoot\Sample.jpg"
img=cv2.imread(path)
img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_g,(7,7),0)
sobel=cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
cv2.imshow("Sobel Matrix",sobel)
cv2.waitKey(0)

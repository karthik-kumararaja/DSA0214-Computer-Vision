import cv2
path="D:\Photoshoot\Sample.jpg"
img = cv2.imread(path)
image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated Image", image)
cv2.waitKey(0)

image = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("Rotated Image", image)
cv2.waitKey(0)

import cv2
import numpy as np

img = cv2.imread("res/face.jpg")
print(img.shape) # its return 3 Value first width , seocnd height, third Type of image Like RGB, GRAY

# Here resize function is resize image

# its take 2 parameter first is image object
# second is dimension first width and second height
imgResize = cv2.resize(img,(300,400))

# here you mension first height and second width
# points seperate with : first define x-axis and than y-axis
imgCroped = img[300:600,300:1000]

cv2.imshow("Image", img)
# cv2.imshow("Resize Image", imgResize)
cv2.imshow("Croped Image", imgCroped)
cv2.waitKey(0)
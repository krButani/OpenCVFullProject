import cv2
import numpy as np

# here define matrix object it is used to Dialate function
# numpy ones function create random metrix 5x5. so, first argument is (5,5) metrix size
# and second argument is which type of metrix you need like integer float.
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("res/face.jpg")

# cvtColor is use to convert image color Here is create gray image
# Pass two parameter first is img object second is color Constant it COLOR_BGR2[GRAY, RGB]
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)

# Apply Gaussian Blur using GaussianBlur function
# it's take 3 parameter first image object  second is ksize it alwasy odd and third sigmax
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image", imgBlur)

# Canny function is use to find edge of the image
# it take 2 paramenter first image object second and third is throwsold
imgCanny = cv2.Canny(img,150,200)
cv2.imshow("Canny Image", imgCanny)

# Here dilate function use to sharp image edges
# its take 3 parameter first is image object seoncd is metrix object
# third is how many iterations move around the edges ( it depend of metrix )
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation Image",imgDialation)

# erode function is opsite of dilate function ( display opsite image of dilate function output )
# its take same parameter like dilate
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
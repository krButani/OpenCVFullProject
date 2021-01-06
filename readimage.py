import cv2


# CV2 Method is imread to read image. it require parameter is path of image
# cv2.imread(Path)
img = cv2.imread("res/face.jpg")


# CV2 method is imshow to show image.
# it is required two parameter.

# 1 Name of Output that display on title bar
# 2 Image Object that fetch from imread
cv2.imshow("Output",img)

# CV2 mehtod is waitKey. its take one parameter that has milisecond if you pass 0 mean infinity
cv2.waitKey(0) # if you can't wrote this function image show and immediately close program
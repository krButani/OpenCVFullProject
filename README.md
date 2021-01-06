# Open CV Full Project
To Learn Open CV with easy way

## Table of contents
* [Setup](#setup)
* [Required Library](#required-library)
* [Read Image](#read-image)
* [Read Video](#read-video)
* [Read WebCam](#read-webcam)
* [Require Basic Function](#require-basic-function)

## Setup
* Install Python ( Install below version of latest version )
* Install PyCham 
* Create Project and add require library

#### How to install library
* Goto File > Settings > Project > Python Interpreter
* Press + Icon
* Search name of library 
* Press Install Package button 
	
## Required Library 
* opencv-python
* numpy

## Read Image

The image will appear until you close the program

* File: readimage.py


```
import cv2
img = cv2.imread("res/face.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0) 
```

## Read Video

The video will appear until you close the program or press q

* File: readvideo.py

```
import cv2
cap = cv2.VideoCapture("res/road2.mp4")
while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Video",img) 
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
```

## Read WebCam

* File: readwebcam.py


```
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) # Width
cap.set(4,480) # Height
cap.set(10,80) # increase the brightness level level between 0 to 100
while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Video",img) # show image
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
```

## Require Basic Function

This function is need in OpenCV Developement.

* File: basicfunction.py

```
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
img = cv2.imread("res/face.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image", imgBlur)

imgCanny = cv2.Canny(img,150,200)
cv2.imshow("Canny Image", imgCanny)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation Image",imgDialation)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
```
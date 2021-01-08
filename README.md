# Learn Open CV Using Python
To Learn Open CV with easy way

## Table of contents
* [Setup](#setup)
* [Required Library](#required-library)
* [Read Image](#read-image)
* [Read Video](#read-video)
* [Read WebCam](#read-webcam)
* [Require Basic Function](#require-basic-function)
* [Resize and Crop Image](#resize-and-crop-image)
* [Draw Shape and Text](#draw-shape-and-text)

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

## Resize and Crop Image

* File: imageresizeorcrop.py

```
import cv2
import numpy as np

img = cv2.imread("res/face.jpg")
print(img.shape) # its return 3 Value first width , seocnd height, third Type of image Like RGB, GRAY

imgResize = cv2.resize(img,(300,400))
imgCroped = img[300:600,300:1000]

cv2.imshow("Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Croped Image", imgCroped)
cv2.waitKey(0)
```

## Draw Shape and Text

* File: drawshapeandtext.py

```
import cv2
import numpy as np

imp = np.zeros((512,512,3),np.uint8)
print(imp.shape)

imp[:] = 255,255,255
# imp[200:300,100:300] = 0,255,0

cv2.line(imp,(0,0),(imp.shape[1],imp.shape[0]),(0,0,0),5)
cv2.rectangle(imp,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(imp,(400,200),100,(0,0,255),2)
cv2.putText(imp,"Hello World!",(000,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0))

cv2.imshow("Show Image", imp)
cv2.waitKey(0)
```
# Open CV Full Project
To Learn Open CV with easy way

## Table of contents
* [Setup](#setup)
* [Required Library](#required-library)
* [Read Image](#read-image)
* [Read Video](#read-video)
* [Read WebCam](#read-webcam)

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

```
import cv2
img = cv2.imread("res/face.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0) 
```

## Read Video

The video will appear until you close the program or press q

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

```
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
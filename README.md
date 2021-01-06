# OpenCVFullProject
To Learn Open CV with easy way

## Table of contents
* [Setup](#setup)
* [Required Library](#required-lib)
* [Read Image](#read-img)

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
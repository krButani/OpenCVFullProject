import cv2

# Read Video one by one frame ( Image ) using python

# CV2 method videoCapture is required one parameter.
# It is path of video or webcam id
# if you have connected to one webcam use 0 or more then one you can you 0,1,2...

cap = cv2.VideoCapture(0)

# Web cam preview display with specific size so, use set method of cap
# set has 2 parameter first one is static to do for all like width hase etc and other one is value of it.
cap.set(3,640) # Width
cap.set(4,480) # Height
cap.set(10,80) # increase the brightness level level between 0 to 100
# Using While Loop read Video
while True:
    # return of videoCapture object has on method is called Read That return success and img object
    # success has boolean type if image read than return true else false
    success, img = cap.read()
    if success:
        cv2.imshow("Video",img) # show image
        # here is logic to image show and press q to close program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
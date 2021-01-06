import cv2


# Read Video one by one frame ( Image ) using python

# CV2 method videoCapture is required one parameter. It is path of vide.

cap = cv2.VideoCapture("res/road2.mp4")

# Using While Loop read Video
while True:
    # return of videoCapture object has on method is called Read That return success and img object
    # success has boolean type if image read than return true else false
    success, img = cap.read()
    if success:
        cv2.imshow("Video",img) # show image
        # here is logic to image show and stop waitkey function one image show and stop when you long press
        # any key then all image one by one display or close ( break ) the loop press q
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
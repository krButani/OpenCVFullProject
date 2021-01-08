import cv2
import numpy as np

# here zero means blank
# inside it pass dimension first is height and width
# third argument is color RGB or Gray
imp = np.zeros((512,512,3),np.uint8)
print(imp.shape)

# here assign color as BGR to all cell
imp[:] = 255,255,255
# imp[200:300,100:300] = 0,255,0

# line function to draw line
# Parameter required is following:
# 1. image object
# 2. Starting Point
# 3. Ending Point
# 4. Color Using BGR
# 5. Stroke
cv2.line(imp,(0,0),(imp.shape[1],imp.shape[0]),(0,0,0),5)


# rectangle function to draw line
# Parameter required is following:
# 1. image object
# 2. Starting Point
# 3. Ending Point
# 4. Color Using BGR
# 5. Stroke or Filled cv2.FILLED
cv2.rectangle(imp,(0,0),(250,350),(0,0,255),cv2.FILLED)

# circle function to draw line
# Parameter required is following:
# 1. image object
# 2. Center Point
# 3. Radius
# 4. Color Using BGR
# 5. Stroke
cv2.circle(imp,(400,200),100,(0,0,255),2)


# putText function to draw line
# Parameter required is following:
# 1. image object
# 2. Text
# 3. Origin
# 4. Fonts
# 5. Font Scale
# 5. Font Color
cv2.putText(imp,"Hello World!",(000,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0))

cv2.imshow("Show Image", imp)
cv2.waitKey(0)
import cv2
import numpy as np

img=cv2.imread('corner-detection.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,200,0.01,10) #on gray,number of corners to find,img quality,distance b/w each resp.
corners=np.int0(corners)

for corner in corners:
    x,y =corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

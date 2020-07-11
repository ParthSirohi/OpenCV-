import cv2
import numpy as np

img=cv2.imread('1370_7.jpg',cv2.IMREAD_COLOR)

cv2.line(img , (0,0), (250,250),(0,0,255),15)   # line start , line end , bgr color , line width
cv2.rectangle(img, (15,25) , (200,150), (0,255,0),5)
cv2.circle(img, (100,63), 55, (255,0,0),10)
pts =np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape(-1,1,2)
cv2.polylines(img, [pts],True, (0,255,255),3)

font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'My Photo',(0,140),font,1,(0,0,0),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
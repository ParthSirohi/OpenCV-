import cv2
import numpy as np

img = cv2.imread('1370_7.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
img[55, 55] = [255, 255, 255]
print(px)  # white pixel

roi = img[100:150, 100:150] = [255, 255, 255]  # region of image is now all white

sub_image = img[37:111, 107:194]
img[0:74, 0:87] = sub_image

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

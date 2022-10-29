# İsmail ÖNER 02200201041

import cv2 as cv
import numpy as nm

img = cv.imread('cat.png' , 0)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()

max = 0

[x,y] = nm.shape(img)
for i in range(0,y):
    for z in range(0,x):
        a = img[z,i]
        if max < a:
            max = a

for i in range(0,x):
    for z in range(0,y):
        img[z,i] = max - img[z,i]

cv.imshow('image',img)
cv.waitKey()

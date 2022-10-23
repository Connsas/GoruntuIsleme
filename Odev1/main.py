#İsmail ÖNER 02200201041

import cv2 as cv
import numpy as nm

img = cv.imread('cat.png' , 0)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()

hist = nm.zeros(256)
[x,y] = nm.shape(img)
for i in range(0,y):
    for z in range(0,x):
        a = img[z,i]
        hist[a] = hist[a] + 1

for i in range(0,256):
    print("{0} - {1}".format(i,hist[i]))
    

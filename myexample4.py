import cv2 as cv
import numpy

im= cv.imread('imgandvideo/test.jpeg',-1)
cv.imshow("image",im)

resize1 = cv.resize(im, (300,200),interpolation= cv.INTER_LINEAR)
resize2 = cv.resize(im,(5000,6000),interpolation= cv.INTER_LINEAR)

cv.imshow("Zoom in",resize1)
cv.waitKey()
cv.imshow("Zoom out",resize2)
cv.waitKey()
cv.destroyAllWindows()
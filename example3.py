import cv2 as cv
import numpy as np

img = cv.imread('imgandvideo\harrypotter.jpg')
cv.waitKey(0)

pointA = (600,380)
pointB = (850,380)

imageFilledCircle = img.copy()
circle_center = (650,250)
circle_center2 = (790,250)
radius = 50
# cv.circle(imageFilledCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv.LINE_AA) #içi boş
cv.circle(imageFilledCircle, circle_center2, radius, (255, 0, 0), thickness=-1, lineType=cv.LINE_AA)
cv.circle(imageFilledCircle, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv.LINE_AA)
cv.line(imageFilledCircle, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv.LINE_AA)
cv.line(imageFilledCircle, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv.LINE_AA)
cv.imshow('Image Line', imageFilledCircle)
cv.waitKey(0)
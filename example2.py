import cv2 as cv
import numpy as np

image = cv.imread("imgandvideo\harrypotter.jpg")
height, width = image.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv.getRotationMatrix2D(center=center, angle=45, scale=1)
rotated_image = cv.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
cv.imshow('Original image', image)
cv.imshow('Rotated image', rotated_image)
cv.imwrite("imgandvideo/RotatedImage.jpg", rotated_image)
# cv.imshow("image", im)
print(image.shape) #768, 1024

"""
cropped_image = im[300:500, 768:1024]
cv.imshow("image2", cropped_image)
"""

cv.waitKey(0)
cv.destroyAllWindows()
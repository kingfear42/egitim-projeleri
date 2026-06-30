import cv2

im = cv2.imread('imgandvideo/test.jpeg',0)
cv2.imshow("Resim", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('deneme2.jpeg', im)
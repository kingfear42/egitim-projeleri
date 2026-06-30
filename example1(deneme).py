import cv2 
import numpy as np

font = cv2.AKAZE_DESCRIPTOR_MLDB

org = (50,50)

color = (0, 0, 255) 

im= cv2.imread('imgandvideo/test.jpeg',0)
img = cv2.imread('imgandvideo/test.jpeg',1)
resize1 = cv2.resize(im, (300,200),interpolation= cv2.INTER_LINEAR,)
"""
while(img.isOpened() and im.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = im.read()
  if ret == True:
    frame = cv2.putText(frame, 'Korkmaz Ailesine', org, font,
                       font, color, cv2.LINE_AA)
    cv2.imshow('Frame',frame)
    frame = cv2.putText(frame, 'Hosgeldiniz', org, font,
                       font, color, cv2.LINE_AA)
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(20)

    if key == ord('q'):
      break
  else:
    break
"""
cv2.imshow("Zoom in",resize1)
cv2.imshow("Normal", img)
cv2.waitKey()
cv2.destroyAllWindows()
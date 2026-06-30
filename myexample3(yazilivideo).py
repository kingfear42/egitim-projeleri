import cv2 as cv 
#font
font = cv.AKAZE_DESCRIPTOR_MLDB

#org
org= (50,50)
org1 = (95, 80)

#fontsclae
fontScale = 1

color = (0, 0, 255) 

thickness = 2

vid_capture = cv.VideoCapture(0)

#Create a video capture object, in this case we are reading the video from a file
 
 
while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True:
    frame = cv.putText(frame, 'Korkmaz Ailesine', org, font,
                       fontScale, color, thickness , cv.LINE_AA)
    cv.imshow('Frame',frame)
    frame = cv.putText(frame, 'Hosgeldiniz', org1, font,
                       fontScale, color, thickness , cv.LINE_AA)
    cv.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv.waitKey(20)

    if key == ord('q'):
      break
  else:
    break
 
#Release the video capture object
vid_capture.release()
cv.destroyAllWindows()



"""
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
"""
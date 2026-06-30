"""
import cv2 

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('imgandvideo\karagümrük.mp4')
 
if (vid_capture.isOpened() == False):
  print("Error opening the video file")
# Read fps and frame count
else:
  # Get frame rate information
  # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
  fps = vid_capture.get(5)
  print('Frames per second : ', fps,'FPS')
 
  # Get frame count
  # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
  frame_count = vid_capture.get(7)
  print('Frame count : ', frame_count)
 
while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(20)
     
    if key == ord('q'):
      break
  else:
    break
 
# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()
"""


"""
import cv2

# Video dosyasını aç
vid_capture = cv2.VideoCapture('imgandvideo/karagümrük.mp4')

if (vid_capture.isOpened() == False):
    print("Video dosyası açılamadı.")
else:
    # Ses çıkarmak için bir VideoWriter nesnesi oluşturun
    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

    while (vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        if ret == True:
            # Çerçeveyi göster
            cv2.imshow('Frame', frame)
            
            # Çerçeveyi çıktı dosyasına yaz
            out.write(frame)

            key = cv2.waitKey(20)

            if key == ord('q'):
                break
        else:
            break

    # Video capture ve writer nesnelerini serbest bırak
    vid_capture.release()
    out.release()
    cv2.destroyAllWindows()
"""

import cv2
from moviepy.editor import VideoFileClip

# Video dosyasını aç
vid_capture = cv2.VideoCapture('imgandvideo/karagümrük.mp4')

if (vid_capture.isOpened() == False):
    print("Video dosyası açılamadı.")
else:
    # Ses çıkartmak için video dosyasını yükleyin
    video_clip = VideoFileClip('imgandvideo/karagümrük.mp4')

    while (vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        if ret == True:
            # Çerçeveyi göster
            cv2.imshow('Frame', frame)

            key = cv2.waitKey(20)

            if key == ord('q'):
                break
        else:
            break

    # Video capture nesnesini serbest bırak
    vid_capture.release()
    cv2.destroyAllWindows()

    # Ses çıkartma işlemi
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('output_audio.wav')

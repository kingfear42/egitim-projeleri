import cv2

# Yüz tanıma için CascadeClassifier yükleyin
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Video yakalama nesnesini oluşturun
vid_capture = cv2.VideoCapture(0)

if (vid_capture.isOpened() == False):
    print("Video dosyası açılamadı.")
else:
    # FPS ve çerçeve sayısını okuyun
    fps = vid_capture.get(30)
    print('Saniyede Çerçeve Sayısı: ', fps, 'FPS')

    frame_count = vid_capture.get(3)
    print('Toplam Çerçeve Sayısı: ', frame_count)

while (vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        # Yüz tespiti yapın
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Her tespit edilen yüzün etrafına dikdörtgen çizin
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Kamera', frame)
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
    else:
        break

# Video yakalama nesnesini serbest bırakın
vid_capture.release()
cv2.destroyAllWindows()
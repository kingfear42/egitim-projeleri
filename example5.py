import cv2

# Yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier('28.10.2023\haarcascade_frontalface_default.xml')  # Haar Cascade XML dosyasını kullanabilirsiniz.

# Giriş görüntüsünü yükle
input_image = cv2.imread('imgandvideo\class.jpg')

# Gri tonlamalı görüntüyü oluştur
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Yüzleri algıla
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5, minSize=(30, 30))

# Yüzleri blurlamak için döngü
for (x, y, w, h) in faces:
    # Yüzü belirli bir bölgeye alın
    face_roi = input_image[y:y + h, x:x + w]

    # Yüz bölgesini blurla
    blurred_face = cv2.GaussianBlur(face_roi, (0, 0), sigmaX=30)

    # Blurlanmış yüzü orijinal görüntüye yerleştir
    input_image[y:y + h, x:x + w] = blurred_face

# Sonucu göster veya kaydet
cv2.imshow('Blurred Faces', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output_image.jpg', input_image)
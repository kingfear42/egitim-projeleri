import cv2
import mediapipe as mp

# Mediapipe Pose modülünü yükleyin
mp_pose = mp.solutions.pose

# Pose modülünü başlatın
pose = mp_pose.Pose()

# Kamera başlatın
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Kameradan bir kare alın
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı. Çıkılıyor...")
        break

    # Mediapipe'ı kullanarak pose landmark detection yapın
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Renkli görüntü kullanın

    # Sonuçları çizmek için
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Çıktıyı gösterin
    cv2.imshow('Pose Landmark Detection', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kullanılan kaynakları serbest bırakın
cap.release()
cv2.destroyAllWindows()

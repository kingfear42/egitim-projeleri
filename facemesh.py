import cv2
import mediapipe as mp

def main():
    # Initialize MediaPipe FaceMesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2, min_detection_confidence=0.2, min_tracking_confidence=0.2)

    # Initialize OpenCV
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe FaceMesh
        results = face_mesh.process(rgb_frame)

        # Draw face mesh on the frame
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for landmark in face_landmarks.landmark:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    cv2.circle(frame, (cx, cy), 1, (0, 255, 0), 1)

        # Display the output
        cv2.imshow('Face Mesh', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
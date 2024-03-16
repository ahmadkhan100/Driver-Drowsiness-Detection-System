import cv2
import dlib
from eye_aspect_ratio import eye_aspect_ratio
from facial_landmarks import detect_facial_landmarks

# Initialize dlib's face detector and the facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces in the grayscale frame
    faces = detector(frame, 0)

    # Loop over each face found
    for face in faces:
        landmarks = detect_facial_landmarks(frame, face, predictor)

        # Compute the eye aspect ratio for both eyes
        left_eye_ear = eye_aspect_ratio(landmarks['left_eye'])
        right_eye_ear = eye_aspect_ratio(landmarks['right_eye'])
        ear = (left_eye_ear + right_eye_ear) / 2.0

        # Check if the eye aspect ratio is below the blink threshold
        if ear < EYE_AR_THRESH:
            # Driver might be drowsy, take necessary actions
            cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

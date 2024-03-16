# drowsiness_detector.py
import cv2
from ear_calculator import eye_aspect_ratio
from alert_system import trigger_alert
from facial_landmarks import get_landmarks
from datetime import datetime
import time

# Threshold for EAR below which the eye is considered closed
EAR_THRESHOLD = 0.3
# Number of consecutive frames the eye must be below the threshold to trigger the alert
EYE_CLOSED_FRAMES = 48
# Time to wait before re-checking after an alert has been triggered (in seconds)
ALERT_COOLDOWN = 300

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Variables to keep track of blinking
frame_counter = 0
alert_triggered = False
last_alert_time = datetime.min

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Get the facial landmarks
    landmarks = get_landmarks(frame)

    # Proceed if facial landmarks are detected
    if landmarks:
        # Assume landmarks[36:42] are the coordinates for the right eye,
        # and landmarks[42:48] are for the left eye
        right_eye_ear = eye_aspect_ratio(landmarks[36:42])
        left_eye_ear = eye_aspect_ratio(landmarks[42:48])
        ear = (right_eye_ear + left_eye_ear) / 2.0

        # Check if EAR is below the threshold
        if ear < EAR_THRESHOLD:
            frame_counter += 1

            # If eyes are closed long enough, trigger the alert
            if frame_counter >= EYE_CLOSED_FRAMES and not alert_triggered and (datetime.now() - last_alert_time).total_seconds() > ALERT_COOLDOWN:
                trigger_alert()
                alert_triggered = True
                last_alert_time = datetime.now()
        else:
            frame_counter = 0
            alert_triggered = False

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# The drowsiness_detector.py integrates real-time video capture, facial landmark detection,
# EAR calculation, drowsiness detection logic, and alert system. It is the central part of the
# Driver Drowsiness Detection System.

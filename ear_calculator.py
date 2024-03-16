# ear_calculator.py
import numpy as np

def eye_aspect_ratio(eye_points):
    # Calculate the euclidean distances between the vertical eye landmarks
    # (p2 - p6) and (p3 - p5)
    P2_P6 = np.linalg.norm(eye_points[1] - eye_points[5])
    P3_P5 = np.linalg.norm(eye_points[2] - eye_points[4])

    # Calculate the euclidean distance between the horizontal eye landmarks
    # (p1 - p4)
    P1_P4 = np.linalg.norm(eye_points[0] - eye_points[3])

    # The EAR is then the ratio of the mean of the two vertical distances
    # to the horizontal distance
    ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)

    return ear

# You can now import this function in the main drowsiness detection script to calculate EAR


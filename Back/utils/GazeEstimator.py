import cv2
import numpy as np

class GazeEstimator:
    def __init__(self, predictor):
        self.predictor = predictor

    def estimate_and_draw(self, frame, landmarks):
        # Example: use eyes + eyebrows + mouth for directional hint
        eye_points = [36, 39, 42, 45]  # Eye corners
        brow_points = [21, 22]         # Eyebrow centers
        mouth_points = [48, 54]        # Mouth corners

        all_points = eye_points + brow_points + mouth_points
        coords = [(landmarks.part(p).x, landmarks.part(p).y) for p in all_points]

        for (x, y) in coords:
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        # Simulate direction vector
        eye_center = np.mean([(landmarks.part(p).x, landmarks.part(p).y) for p in [36, 39, 42, 45]], axis=0)
        brow_center = np.mean([(landmarks.part(p).x, landmarks.part(p).y) for p in [21, 22]], axis=0)
        dir_vector = (eye_center[0] - brow_center[0], eye_center[1] - brow_center[1])

        norm = np.linalg.norm(dir_vector)
        if norm != 0:
            dir_vector = (dir_vector[0]/norm, dir_vector[1]/norm)
            end_point = (int(eye_center[0] + dir_vector[0]*100), int(eye_center[1] + dir_vector[1]*100))
            cv2.arrowedLine(frame, (int(eye_center[0]), int(eye_center[1])), end_point, (0, 255, 0), 2)

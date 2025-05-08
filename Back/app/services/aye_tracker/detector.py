import cv2
import mediapipe as mp
import numpy as np
from typing import Tuple, Optional
from core.exceptions import CalibrationError

class EyeDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7)
        
        # Landmarks dos olhos
        self.LEFT_EYE_POINTS = [362, 382, 381, 380, 374, 373, 390, 249, 263]
        self.RIGHT_EYE_POINTS = [33, 7, 163, 144, 145, 153, 154, 155, 133]

    def detect_gaze(self, frame: np.ndarray) -> Optional[Tuple[float, float]]:
        """Detecta a direção do olhar em um frame"""
        try:
            # Pré-processamento
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(frame_rgb)
            
            if not results.multi_face_landmarks:
                return None

            landmarks = results.multi_face_landmarks[0].landmark
            
            # Extrair coordenadas dos olhos
            left_eye = self._get_eye_coords(landmarks, self.LEFT_EYE_POINTS)
            right_eye = self._get_eye_coords(landmarks, self.RIGHT_EYE_POINTS)
            
            # Calcular direção média do olhar
            gaze_x = (left_eye[0] + right_eye[0]) / 2
            gaze_y = (left_eye[1] + right_eye[1]) / 2
            
            return (gaze_x, gaze_y)
            
        except Exception as e:
            raise CalibrationError(f"Falha na detecção do olhar: {str(e)}")

    def _get_eye_coords(self, landmarks, indices) -> Tuple[float, float]:
        """Extrai as coordenadas médias de um olho"""
        points = [(landmarks[i].x, landmarks[i].y) for i in indices]
        return (np.mean([p[0] for p in points]), np.mean([p[1] for p in points]))
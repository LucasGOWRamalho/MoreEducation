# Exemplo hipotético em eye_tracker/mapper.py
class EyeDirectionMapper:
    def __init__(self):
        self.threshold = 0.2  # Ajuste conforme necessidade

    def map_eye_landmarks(self, landmarks) -> str:
        """Converte landmarks em direção ('left', 'right', 'center')"""
        left_ratio = landmarks[36].x / landmarks[39].x
        right_ratio = landmarks[42].x / landmarks[45].x
        if left_ratio < self.threshold:
            return "left"
        elif right_ratio < self.threshold:
            return "right"
        return "center"
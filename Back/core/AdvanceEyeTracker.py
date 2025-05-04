import numpy as np

class AdvanceEyeTracker:
    def extract_features(self, landmarks):
        # Normaliza e retorna uma lista de vetores dos olhos, boca, sobrancelha e nariz
        indices = {
            "left_eye": list(range(36, 42)),
            "right_eye": list(range(42, 48)),
            "nose": list(range(27, 36)),
            "mouth": list(range(48, 68)),
            "left_eyebrow": list(range(17, 22)),
            "right_eyebrow": list(range(22, 27)),
        }

        features = []
        for region in indices.values():
            points = [landmarks[i] for i in region]
            center = np.mean(points, axis=0)
            features.extend(center)  # Adiciona X e Y

        return np.array(features)

import numpy as np

class VectorMath:
    @staticmethod
    def normalize(v):
        norm = np.linalg.norm(v)
        return v / norm if norm != 0 else v

    @staticmethod
    def angle_between(v1, v2):
        v1_u = VectorMath.normalize(v1)
        v2_u = VectorMath.normalize(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


from ..domain.GazePoint import GazePoint

class GazeEstimator:
    def __init__(self, head_pose_estimator):
        self.model = None  # Carregar modelo treinado
        self.head_pose_estimator = head_pose_estimator

    def estimate(self, landmarks, iris_position):
        orientation = self.head_pose_estimator.estimate(landmarks)
        x, y = 960, 540  # Mock para centro da tela
        return GazePoint(x, y, 1.0)

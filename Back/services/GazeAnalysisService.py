class GazeAnalysisService:
    def __init__(self, gaze_model, eye_tracker):
        self.model = gaze_model
        self.eye_tracker = eye_tracker

    def predict(self, landmarks):
        features = self.eye_tracker.extract_features(landmarks)
        return self.model.predict(features)

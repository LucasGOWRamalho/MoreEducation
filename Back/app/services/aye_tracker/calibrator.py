import numpy as np
from sklearn.linear_model import LinearRegression
from core.config import settings
from core.exceptions import CalibrationError

class EyeCalibrator:
    def __init__(self):
        self.screen_points = []
        self.gaze_points = []
        self.model = LinearRegression()
        self.is_calibrated = False

    def add_calibration_point(self, screen_point: tuple, gaze_point: tuple):
        """Adds a calibration point"""
        if len(screen_point) != 2 or len(gaze_point) != 2:
            raise CalibrationError("Points must be (x,y) tuples")
            
        self.screen_points.append(screen_point)
        self.gaze_points.append(gaze_point)

    def calibrate(self) -> bool:
        """Trains the calibration model"""
        min_points = max(4, settings.CALIBRATION_POINTS // 2)
        
        if len(self.screen_points) < min_points:
            raise CalibrationError(
                f"Need at least {min_points} calibration points")
                
        try:
            X = np.array(self.gaze_points)
            y = np.array(self.screen_points)
            self.model.fit(X, y)
            self.is_calibrated = True
            return True
        except Exception as e:
            raise CalibrationError(f"Calibration failed: {str(e)}")

    def predict_screen_position(self, gaze_point: tuple) -> tuple:
        """Predicts screen position from gaze point"""
        if not self.is_calibrated:
            raise CalibrationError("Calibrator is not trained")
            
        try:
            prediction = self.model.predict([gaze_point])[0]
            return (float(prediction[0]), float(prediction[1]))
        except Exception as e:
            raise CalibrationError(f"Prediction failed: {str(e)}")
from data.CalibrationData import CalibrationData
from ui.CalibrationUI import CalibrationUI

class CalibrationManager:
    def __init__(self, screen_width, screen_height):
        self.calibration_data = CalibrationData()
        self.ui = CalibrationUI(screen_width, screen_height)
        self.calibrated = False

    def start_calibration(self, frame, landmarks):
        if not self.calibrated:
            self.ui.draw_points(frame)
            current_point = self.ui.get_current_point()
            if self.ui.is_ready_for_capture():
                self.calibration_data.capture(current_point, landmarks)
                self.ui.advance_point()
            if self.ui.is_finished():
                self.calibrated = True
                return True
        return False

    def get_training_data(self):
        return self.calibration_data.get_data()

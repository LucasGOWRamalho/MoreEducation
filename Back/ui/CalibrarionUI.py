from config.Settings import CALIBRATION_POINTS
import cv2

class CalibrationUI:
    def __init__(self, width, height):
        self.points = [(int(x * width), int(y * height)) for x, y in CALIBRATION_POINTS]
        self.index = 0
        self.ready = False

    def draw_points(self, frame):
        for i, (x, y) in enumerate(self.points):
            color = (0, 0, 255) if i == self.index else (255, 0, 0)
            cv2.circle(frame, (x, y), 10, color, -1)

    def is_ready_for_capture(self):
        return self.ready

    def advance_point(self):
        self.ready = False
        if self.index < len(self.points) - 1:
            self.index += 1

    def get_current_point(self):
        return self.points[self.index]

    def is_finished(self):
        return self.index >= len(self.points) - 1

    def confirm_capture(self):
        self.ready = True


import time
import cv2
from config import settings

class CalibrationService:
    def __init__(self, screen):
        self.screen = screen

    def start_calibration(self):
        points = self.screen.get_calibration_points()
        for point in points:
            self._show_point(point)
            time.sleep(2)  # aguarda fixação visual
            # capturar e salvar dados de landmarks

    def _show_point(self, point):
        img = 255 * np.ones((self.screen.height, self.screen.width, 3), dtype=np.uint8)
        cv2.circle(img, point, 10, (0, 0, 255), -1)
        cv2.imshow("Calibrando", img)
        cv2.waitKey(1000)

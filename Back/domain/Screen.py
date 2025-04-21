from config import settings

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_calibration_points(self):
        return [(int(x * self.width), int(y * self.height)) for x, y in settings.CALIBRATION_POINTS]

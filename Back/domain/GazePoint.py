class GazePoint:
    def __init__(self, x: float, y: float, confidence: float = 1.0):
        self.x = x
        self.y = y
        self.confidence = confidence

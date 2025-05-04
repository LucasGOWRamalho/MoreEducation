class CalibrationData:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def capture(self, screen_point, features):
        self.inputs.append(features)
        self.outputs.append(screen_point)

    def get_data(self):
        return self.inputs, self.outputs

class CalibrationData:
    def __init__(self):
        self.samples = []

    def add_sample(self, facial_points, screen_position):
        self.samples.append({"facial_points": facial_points, "screen_position": screen_position})

    def save_to_file(self, filepath):
        import json
        with open(filepath, "w") as f:
            json.dump(self.samples, f)

    def load_from_file(self, filepath):
        import json
        with open(filepath, "r") as f:
            self.samples = json.load(f)

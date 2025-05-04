from sklearn.linear_model import LinearRegression
import numpy as np

class GazeModel:
    def __init__(self):
        self.model_x = LinearRegression()
        self.model_y = LinearRegression()

    def train(self, X, y):
        self.model_x.fit(X, [p[0] for p in y])
        self.model_y.fit(X, [p[1] for p in y])

    def predict(self, X):
        return [(int(self.model_x.predict([x])[0]), int(self.model_y.predict([x])[0])) for x in X]

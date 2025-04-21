from sklearn.neighbors import KNeighborsRegressor
import joblib

class ModelTrainer:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def train(self):
        model = KNeighborsRegressor(n_neighbors=3)
        model.fit(self.X, self.y)
        joblib.dump(model, "models/ml_model.pkl")

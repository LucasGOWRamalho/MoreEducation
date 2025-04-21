class DatasetCollector:
    def __init__(self):
        self.data = []

    def capture(self, point, landmarks):
        # Salvar mapeamento entre posição da tela e landmarks
        self.data.append((landmarks, point))

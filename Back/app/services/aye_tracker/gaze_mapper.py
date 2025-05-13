# app/services/gaze_mapper.py
class GazeMapper:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.key_grid = [
            ["Q", "W", "E"],
            ["A", "S", "D"],
            ["Z", "X", "C"]
        ]

    def map_to_key(self, x: int, y: int) -> str:
        """Converte coordenadas (x,y) em uma tecla"""
        col = min(int(x / (self.screen_width / 3)), 2)  # 3 colunas
        row = min(int(y / (self.screen_height / 3)), 2)
        return self.key_grid[row][col]
from pydantic import BaseModel

class CalibrationRequest(BaseModel):
    screen_resolution: tuple[int, int]  # (width, height)
    calibration_points: list[tuple[int, int]]  # Pontos na tela
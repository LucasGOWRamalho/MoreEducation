from pydantic import BaseModel

class GazeData(BaseModel):
    x: int  # Coordenada X do olhar
    y: int  # Coordenada Y do olhar
    timestamp: float
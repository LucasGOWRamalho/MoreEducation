from fastapi import APIRouter, WebSocket
from app.models.gaze import GazeData
from app.services.gaze_mapper import map_gaze_to_key

router = APIRouter(prefix="/gaze", tags=["Detecção do Olhar"])

@router.post("/detect")
async def detect_gaze(data: GazeData):
    """Processa direção do olhar e retorna tecla mapeada"""
    return {"key": map_gaze_to_key(data.x, data.y)}

@router.websocket("/track")
async def track_gaze_ws(websocket: WebSocket):
    """WebSocket para rastreamento contínuo"""
    await websocket.accept()
    while True:
        gaze_data = await websocket.receive_json()
        key = map_gaze_to_key(gaze_data["x"], gaze_data["y"])
        await websocket.send_json({"key": key})
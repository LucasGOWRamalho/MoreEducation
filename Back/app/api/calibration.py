from fastapi import APIRouter, WebSocket
from app.models.calibration import CalibrationRequest
from app.services.calibration import calibrate_system

router = APIRouter(prefix="/calibration", tags=["Calibração"])

@router.post("/start")
async def start_calibration(request: CalibrationRequest):
    """Inicia calibração do sistema com pontos de referência"""
    return calibrate_system(request.screen_resolution)

@router.websocket("/ws")
async def websocket_calibration(websocket: WebSocket):
    """WebSocket para calibração em tempo real"""
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        # Processa dados do olhar (ex: coordenadas x, y)
        await websocket.send_json({"status": "calibrated"})
from fastapi import WebSocket, APIRouter

router = APIRouter()

@router.websocket("/eye-tracking")
async def eye_tracking_ws(websocket: WebSocket):
    """WebSocket principal para integração front/back"""
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        # Lógica de processamento do olhar aqui
        await websocket.send_json({"action": "update_screen"})
        
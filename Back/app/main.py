from fastapi import FastAPI, WebSocket
from core.config import settings
from services.eye_tracking import EyeDetector, EyeCalibrator
from services.tts import TTSEngine
import cv2
import numpy as np
import base64
import json

app = FastAPI(title=settings.APP_NAME)

# Inicializa serviços
eye_detector = EyeDetector()
tts_engine = TTSEngine()

@app.websocket("/ws/eye-tracking")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    calibrator = EyeCalibrator()
    
    try:
        while True:
            data = await websocket.receive_text()
            json_data = json.loads(data)
            
            # Processar frame
            img_bytes = base64.b64decode(json_data['image'].split(',')[1])
            nparr = np.frombuffer(img_bytes, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Detectar olhar
            gaze_point = eye_detector.detect_gaze(frame)
            
            if gaze_point:
                response = {
                    'x': gaze_point[0],
                    'y': gaze_point[1],
                    'timestamp': json_data['timestamp']
                }
                await websocket.send_json(response)
                
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        await websocket.close()

@app.post("/calibrate")
async def calibrate(points: dict):
    """Endpoint para calibração"""
    try:
        calibrator = EyeCalibrator()
        # Adicionar pontos de calibração
        for screen_pt, gaze_pt in zip(points['screen_points'], points['gaze_points']):
            calibrator.add_point(tuple(screen_pt), tuple(gaze_pt))
        
        calibrator.calibrate()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/speak")
async def text_to_speech(request: dict):
    """Endpoint para síntese de fala"""
    try:
        tts_engine.speak(request['text'])
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
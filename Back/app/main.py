import sys
from pathlib import Path
from fastapi import FastAPI, WebSocket, HTTPException
sys.path.append(str(Path(__file__).parent.parent))
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import base64
import json
from typing import Optional

# Adjust the sys.path to include the correct parent directory for 'core'
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Adjusted path for 'core'

from .core.config import settings 

# Importações relativas corrigidas
from services.eye_tracking import EyeDetector, EyeCalibrator
from services.tts import TTSEngine

# Inicializa o app FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description="API para controle ocular MoreEducation",
    version="0.1.0"
)

# Configura CORS (importante para o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa serviços
eye_detector = EyeDetector(model=settings.EYE_TRACKING_MODEL)
tts_engine = TTSEngine(engine=settings.TTS_ENGINE, voice=settings.DEFAULT_VOICE)

@app.websocket("/ws/eye-tracking")
async def websocket_eye_tracking(websocket: WebSocket):
    """
    WebSocket para rastreamento ocular em tempo real.
    Espera receber frames codificados em base64.
    """
    await websocket.accept()
    calibrator = EyeCalibrator(settings.CALIBRATION_POINTS)
    
    try:
        while True:
            data = await websocket.receive_text()
            
            try:
                json_data = json.loads(data)
                if 'image' not in json_data:
                    raise ValueError("Campo 'image' não encontrado nos dados")
                
                # Decodifica a imagem
                header, encoded = json_data['image'].split(",", 1)
                img_bytes = base64.b64decode(encoded)
                nparr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                # Processa o frame
                gaze_point = eye_detector.detect_gaze(frame)
                
                if gaze_point:
                    response = {
                        'x': gaze_point[0],
                        'y': gaze_point[1],
                        'timestamp': json_data.get('timestamp'),
                        'status': 'success'
                    }
                else:
                    response = {'status': 'no_face_detected'}
                
                await websocket.send_json(response)
                
            except json.JSONDecodeError:
                await websocket.send_json({'error': 'Dados JSON inválidos'})
            except ValueError as e:
                await websocket.send_json({'error': str(e)})
            except Exception as e:
                await websocket.send_json({'error': f'Erro interno: {str(e)}'})
                
    except WebSocketDisconnect:
        print("Cliente desconectado")
    except Exception as e:
        print(f"Erro crítico: {str(e)}")
    finally:
        await websocket.close()

@app.post("/calibrate")
async def calibrate(points: dict):
    """
    Endpoint para calibração do sistema.
    Requer:
    {
        "screen_points": [[x1, y1], [x2, y2], ...],
        "gaze_points": [[x1, y1], [x2, y2], ...]
    }
    """
    try:
        calibrator = EyeCalibrator(settings.CALIBRATION_POINTS)
        
        if len(points['screen_points']) != len(points['gaze_points']):
            raise HTTPException(400, "Número de pontos inconsistentes")
        
        for screen_pt, gaze_pt in zip(points['screen_points'], points['gaze_points']):
            calibrator.add_calibration_point(
                screen_point=tuple(screen_pt),
                gaze_point=tuple(gaze_pt)
            )
        
        calibration_result = calibrator.calculate_calibration()
        return {
            "status": "success",
            "matrix": calibration_result.tolist() if calibration_result is not None else None
        }
    except Exception as e:
        raise HTTPException(500, f"Erro na calibração: {str(e)}")

@app.post("/speak")
async def text_to_speech(request: dict):
    """
    Endpoint para síntese de fala.
    Requer: {"text": "texto a ser falado"}
    """
    try:
        if 'text' not in request:
            raise HTTPException(400, "Campo 'text' não encontrado")
        
        tts_engine.speak(request['text'])
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(500, f"Erro no TTS: {str(e)}")

@app.get("/health")
async def health_check():
    """Endpoint para verificação do status do serviço"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "environment": settings.ENV
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
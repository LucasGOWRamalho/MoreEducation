import os
from pydantic import BaseSettings, conint
from typing import Literal
from pathlib import Path

class Settings(BaseSettings):
    # Configurações básicas
    APP_NAME: str = "GazeAccess"
    ENV: str = os.getenv("ENV", "development")  # Opcional: pode usar apenas ENV: str = "development"
    
    # Rastreamento ocular
    EYE_TRACKING_MODEL: Literal["mediapipe", "tobii", "pygaze"] = "mediapipe"
    CALIBRATION_POINTS: conint(ge=5, le=15) = 9
    
    # TTS
    TTS_ENGINE: Literal["pyttsx3", "google", "azure"] = "pyttsx3"
    
    # Segurança
    SECRET_KEY: str  # Obrigatório (irá falhar se não estiver no .env)
    DATABASE_URL: str = "sqlite:///./dados.db"  # Valor padrão

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = False
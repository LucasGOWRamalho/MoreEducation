import os
from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "GazeAccess"
    ENV: str = os.getenv("ENV", "development")
    
    # Eye Tracking
    EYE_TRACKING_MODEL: str = "mediapipe"  # ou "tobii", "pygaze"
    CALIBRATION_POINTS: int = 9
    
    # TTS
    TTS_ENGINE: str = "pyttsx3"  # ou "google", "azure"
    DEFAULT_VOICE: str = "brazil"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./gazeapp.db")
    
    class Config:
        env_file = ".env"

settings = Settings()
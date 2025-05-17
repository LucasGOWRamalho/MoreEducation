import os
from pydantic import BaseSettings, conint
from typing import Literal
from pathlib import Path

class Settings(BaseSettings):
    """Main configuration class for GazeAccess application."""
    
    # Basic configurations
    APP_NAME: str = "GazeAccess"
    ENV: str = os.getenv("ENV", "development")  # development/production/staging
    
    # Eye tracking configurations
    EYE_TRACKING_MODEL: Literal["mediapipe", "tobii", "pygaze"] = "mediapipe"
    CALIBRATION_POINTS: conint(ge=5, le=15) = 9  # 5-15 calibration points
    
    # Text-to-Speech configurations
    TTS_ENGINE: Literal["pyttsx3", "google", "azure"] = "pyttsx3"
    DEFAULT_VOICE: str = "default"
    
    # Security configurations (REQUIRED - no defaults)
    SECRET_KEY: str = "048499d07efbd9b5504d80b2ff8a3a284b7d56db2336b7f4a340d718bdff020d"
    DATABASE_URL: str = "sqlite:///./dados.db"  # Default SQLite URL
    
    # API configurations
    API_PREFIX: str = "/api"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = False

# Singleton instance to be imported throughout the application
settings = Settings()
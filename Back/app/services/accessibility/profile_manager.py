import json
import os
from typing import Dict, Any
from pathlib import Path
from core.config import settings
from core.exceptions import ProfileNotFoundError

class AccessibilityManager:
    def __init__(self):
        os.makedirs(settings.USER_PROFILES_DIR, exist_ok=True)

    def save_settings(self, user_id: str, settings: Dict[str, Any]) -> bool:
        """Salva as configurações de acessibilidade"""
        profile_path = self._get_profile_path(user_id)
        try:
            with open(profile_path, 'w') as f:
                json.dump(settings, f)
            return True
        except Exception as e:
            raise ProfileNotFoundError(f"Falha ao salvar: {str(e)}")

    def load_settings(self, user_id: str) -> Dict[str, Any]:
        """Carrega as configurações salvas"""
        profile_path = self._get_profile_path(user_id)
        if not profile_path.exists():
            return self._default_settings()
            
        try:
            with open(profile_path, 'r') as f:
                return json.load(f)
        except Exception:
            return self._default_settings()

    def _get_profile_path(self, user_id: str) -> Path:
        return settings.USER_PROFILES_DIR / f"{user_id}_access.json"

    def _default_settings(self) -> Dict[str, Any]:
        return {
            "dwell_time": 1.5,
            "sensitivity": 0.7,
            "high_contrast": True,
            "audio_feedback": True,
            "font_size": 16
        }
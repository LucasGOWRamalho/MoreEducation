import json
import os
from typing import Dict, Any
from app.core.config import settings 
from app.core.exceptions import ProfileNotFoundError



class VoiceProfileManager:
    def __init__(self):
        os.makedirs(settings.USER_PROFILES_DIR, exist_ok=True)

    def save_profile(self, user_id: str, voice_settings: Dict[str, Any]) -> bool:
        """Salva o perfil de voz do usuário"""
        profile_path = settings.USER_PROFILES_DIR / f"{user_id}_voice.json"
        try:
            with open(profile_path, 'w') as f:
                json.dump(voice_settings, f)
            return True
        except Exception as e:
            raise ProfileNotFoundError(f"Falha ao salvar perfil: {str(e)}")

    def load_profile(self, user_id: str) -> Dict[str, Any]:
        """Carrega o perfil de voz do usuário"""
        profile_path = settings.USER_PROFILES_DIR / f"{user_id}_voice.json"
        if not profile_path.exists():
            return self._default_profile()
            
        try:
            with open(profile_path, 'r') as f:
                return json.load(f)
        except Exception:
            return self._default_profile()

    def _default_profile(self) -> Dict[str, Any]:
        """Retorna um perfil padrão"""
        return {
            "rate": 150,
            "volume": 1.0,
            "voice": 0,
            "language": "pt-br"
        }
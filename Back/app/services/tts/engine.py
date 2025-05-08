import pyttsx3
from typing import Optional
from core.config import settings
from core.exceptions import TTSError
import os

class TTSEngine:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', settings.DEFAULT_VOICE_RATE)
        except Exception as e:
            raise TTSError(f"Falha ao inicializar TTS: {str(e)}")

    def speak(self, text: str, voice_params: Optional[dict] = None):
        """Fala o texto com os parâmetros de voz especificados"""
        try:
            if voice_params:
                self._apply_voice_params(voice_params)
                
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            raise TTSError(f"Falha ao sintetizar fala: {str(e)}")

    def _apply_voice_params(self, params: dict):
        """Aplica configurações de voz"""
        if 'rate' in params:
            self.engine.setProperty('rate', params['rate'])
        if 'volume' in params:
            self.engine.setProperty('volume', params['volume'])
        if 'voice' in params:
            voices = self.engine.getProperty('voices')
            if params['voice'] < len(voices):
                self.engine.setProperty('voice', voices[params['voice']].id)
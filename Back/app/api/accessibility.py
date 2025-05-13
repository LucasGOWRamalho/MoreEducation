from fastapi import APIRouter, HTTPException
from app.models.user import AccessibilitySettings
from app.services.tts import text_to_speech

router = APIRouter(prefix="/accessibility", tags=["Acessibilidade"])

@router.post("/settings")
async def update_settings(settings: AccessibilitySettings):
    """Atualiza configurações de acessibilidade (contraste, tamanho da fonte, etc.)"""
    return {"message": "Configurações atualizadas"}

@router.post("/read-aloud")
async def read_text_aloud(text: str):
    """Usa TTS para ler texto em voz alta"""
    return text_to_speech(text)
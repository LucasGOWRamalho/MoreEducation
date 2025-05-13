from fastapi import APIRouter
from gtts import gTTS
import os

router = APIRouter(prefix="/tts", tags=["Text-to-Speech"])

@router.post("/speak")
async def speak(text: str):
    """Converte texto em áudio e retorna o arquivo"""
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")
    return {"audio_path": "output.mp3"}
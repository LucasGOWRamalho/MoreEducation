import pytesseract
from .preprocessor import ImagePreprocessor
from typing import Optional

class TextReader:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajuste o caminho
        
    def extract_text(self, image) -> Optional[str]:
        """Extrai texto de uma imagem"""
        try:
            processed = ImagePreprocessor.preprocess(image)
            if processed is None:
                return None
                
            # Configurações para português
            config = r'--oem 3 --psm 6 -l por+eng'
            text = pytesseract.image_to_string(processed, config=config)
            return text.strip()
        except Exception as e:
            print(f"Erro na leitura de texto: {e}")
            return None
import cv2
import numpy as np
from typing import Optional

class ImagePreprocessor:
    @staticmethod
    def preprocess(image: np.ndarray) -> Optional[np.ndarray]:
        """Aplica pré-processamento para melhorar o OCR"""
        try:
            # Conversão para escala de cinza
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Redução de ruído
            denoised = cv2.fastNlMeansDenoising(gray, h=30)
            
            # Binarização adaptativa
            processed = cv2.adaptiveThreshold(
                denoised, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY, 11, 2
            )
            return processed
        except Exception as e:
            print(f"Erro no pré-processamento: {e}")
            return None
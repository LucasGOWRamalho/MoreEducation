"""
Configurações globais do sistema
"""
from .Settings import settings  # Importa a instância já configurada

__all__ = [
           'CALIBRATION_POINTS',
           'CALIBRATION_DWELL_TIME',
           'EYE_TRACKING',
           'SCREEN_RESOLUTION',
           'MAX_FPS',
           'GPU_ACCELERATION',
           'VISUAL_FEEDBACK'
           ]
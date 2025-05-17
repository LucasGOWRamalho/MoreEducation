class GazeBaseException(Exception):
    """Base exception for all custom exceptions"""
    
class CalibrationError(GazeBaseException):
    """Errors during eye tracking calibration"""
    
class TTSException(GazeBaseException):
    """Text-to-speech related errors"""
    
class AccessibilityProfileNotFound(GazeBaseException):
    """When user profile is not found"""

class TTSError(Exception):
    """Erro relacionado ao mecanismo de TTS."""
    pass

class InvalidInputError(Exception):
    """Erro para entradas inválidas em acessibilidade/UI."""
    pass

class ProfileNotFoundError(GazeBaseException):
    """When user profile is not found"""
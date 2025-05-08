class GazeBaseException(Exception):
    """Base exception for all custom exceptions"""
    
class CalibrationError(GazeBaseException):
    """Errors during eye tracking calibration"""
    
class TTSException(GazeBaseException):
    """Text-to-speech related errors"""
    
class AccessibilityProfileNotFound(GazeBaseException):
    """When user profile is not found"""
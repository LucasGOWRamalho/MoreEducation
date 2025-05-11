# Back/config/settings.py

class Settings:
    # Configurações de Calibração
    CALIBRATION_POINTS = [
        (0.1, 0.1),
        (0.9, 0.1),
        (0.5, 0.5),
        (0.1, 0.9),
        (0.9, 0.9)
    ] 
    CALIBRATION_DWELL_TIME = 2.0  # Tempo de fixação em cada ponto (segundos)
    
    # Configurações de Rastreamento
    EYE_TRACKING = {
        'min_detection_confidence': 0.7,
        'min_tracking_confidence': 0.7,
        'max_num_faces': 1,
        'refine_landmarks': True
    }
    
    # Configurações de Tela
    SCREEN_RESOLUTION = (1920, 1080)  # Largura, Altura
    
    # Configurações de Performance
    MAX_FPS = 30  # Limite de frames por segundo
    GPU_ACCELERATION = True  # Usar CUDA se disponível
    
    # Configurações de Acessibilidade
    VISUAL_FEEDBACK = {
        'cursor_color': (0, 255, 0),  # Verde
        'cursor_radius': 10,
        'show_calibration_points': True
    }

# Instância única de configurações
settings = Settings()
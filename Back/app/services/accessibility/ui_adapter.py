from typing import Dict, Any
from app.core.exceptions import InvalidInputError

class UIAdapter:
    def __init__(self, accessibility_settings: Dict[str, Any]):
        self.settings = accessibility_settings

    def adapt_ui(self, ui_config: Dict[str, Any]) -> Dict[str, Any]:
        """Adapta a interface com base nas configurações"""
        if not ui_config:
            raise InvalidInputError("Configuração de UI inválida")
            
        adapted = ui_config.copy()
        
        # Aplicar alto contraste
        if self.settings.get('high_contrast', True):
            adapted['colors'] = {
                'background': '#000000',
                'text': '#FFFFFF',
                'buttons': '#FF0000'
            }
        
        # Ajustar tamanho da fonte
        adapted['font_size'] = self.settings.get('font_size', 16)
        
        # Configurar tempo de dwell (fixação)
        adapted['dwell_time'] = self.settings.get('dwell_time', 1.5)
        
        return adapted
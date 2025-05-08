from typing import Dict, Tuple, Optional
from core.exceptions import InvalidInputError

class GazeMapper:
    def __init__(self, ui_elements: Dict[str, Tuple[float, float, float, float]]):
        """
        ui_elements: {
            'btn_ok': (x1, y1, x2, y2),
            'btn_cancel': (x1, y1, x2, y2),
            ...
        }
        """
        self.ui_elements = ui_elements

    def get_element_at_gaze(self, point: Tuple[float, float]) -> Optional[str]:
        """Retorna qual elemento está sendo olhado"""
        if len(point) != 2:
            raise InvalidInputError("Ponto deve ser (x,y)")
            
        x, y = point
        for element_id, (x1, y1, x2, y2) in self.ui_elements.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                return element_id
        return None
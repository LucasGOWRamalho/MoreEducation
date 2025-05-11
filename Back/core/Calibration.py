import time
import cv2
import numpy as np
from typing import List, Tuple
from ..config.__init__ import __all__


class CalibrationService:
    def __init__(self, screen):
        """
        Initialize the calibration service with screen parameters.
        
        Args:
            screen: Object containing screen properties (width, height) and methods
        """
        self.screen = screen
        self.calibration_points = CALIBRATION_POINTS
        self.calibration_data = []

    def start_calibration(self) -> bool:
        """
        Run the full calibration process.
        
        Returns:
            bool: True if calibration succeeded, False otherwise
        """
        try:
            points = self.screen.get_calibration_points() or self.calibration_points
            if not points:
                raise ValueError("No calibration points available")
                
            print("Starting calibration...")
            for idx, point in enumerate(points, 1):
                print(f"Calibrating point {idx}/{len(points)} at {point}")
                self._show_point(point)
                # Here you would typically collect user gaze data
                self.calibration_data.append(point)
                time.sleep(2)
                
            cv2.destroyAllWindows()
            print("Calibration completed successfully")
            return True
            
        except Exception as e:
            print(f"Calibration failed: {str(e)}")
            cv2.destroyAllWindows()
            return False

    def _show_point(self, point: Tuple[int, int]) -> None:
        """
        Display a calibration point on screen.
        
        Args:
            point: (x, y) coordinates of the point to display
        """
        # Create white background
        img = 255 * np.ones((self.screen.height, self.screen.width, 3), dtype=np.uint8)
        
        # Draw calibration point (red circle with black border)
        cv2.circle(img, point, 15, (0, 0, 0), -1)  # Black center
        cv2.circle(img, point, 20, (0, 0, 255), 3)  # Red border
        
        # Add instruction text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "Look at the dot", (50, 50), font, 1, (0, 0, 0), 2)
        
        cv2.imshow("Calibration", img)
        cv2.waitKey(1000)

    def map_to_screen(self, gaze_point: Tuple[float, float]) -> Tuple[int, int]:
        """
        Map normalized gaze coordinates to screen pixels.
        
        Args:
            gaze_point: Normalized gaze coordinates (0-1)
            
        Returns:
            Tuple[int, int]: Screen coordinates in pixels
        """
        if not hasattr(self.screen, 'width') or not hasattr(self.screen, 'height'):
            raise AttributeError("Screen dimensions not available")
            
        return (
            int(gaze_point[0] * self.screen.width),
            int(gaze_point[1] * self.screen.height)
        )

    def get_calibration_data(self) -> List[Tuple[int, int]]:
        """
        Get collected calibration data.
        
        Returns:
            List of calibration points that were displayed
        """
        return self.calibration_data
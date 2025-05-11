import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Optional
from Back.config.__init__ import __all__  # Corrected import path
from Back.core.Calibration import CalibrationService
from Back.core.GazeEstimator import GazeEstimator
from Back.core.HeadPoseEstimator import HeadPoseEstimator
from Back.data.ModelTrainer import ModelTrainer
from Back.domain.Screen import Screen

class EyeTrackingSystem:
    
    def __init__(self):
        # Configurações iniciais
        self.screen = Screen(width=1920, height=1080)
        self.calibration = CalibrationService(self.screen)
        self.model_trainer = ModelTrainer()
        self.head_pose_estimator: Optional[HeadPoseEstimator] = None
        self.gaze_estimator: Optional[GazeEstimator] = None




    def initialize(self):
        """Inicializa todos os componentes do sistema"""
        try:
            print("🔄 Iniciando calibração...")
            self.calibration.start_calibration()
            
            print("🤖 Treinando modelo...")
            self.model_trainer.train()
            
            print("🧠 Inicializando estimadores...")
            self.head_pose_estimator = HeadPoseEstimator()
            self.gaze_estimator = GazeEstimator(self.head_pose_estimator)
            
            return True
        except Exception as e:
            print(f"❌ Falha na inicialização: {str(e)}")
            return False

    def run(self):
        """Loop principal de rastreamento ocular"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("🚨 Não foi possível acessar a webcam!")
            return

        print("👁️ Sistema de rastreamento iniciado. Pressione 'q' para sair.")
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Processamento do frame
                gaze_point = self.process_frame(frame)
                
                if gaze_point:
                    self.handle_gaze(gaze_point)
                
                # Visualização (opcional para debug)
                cv2.imshow('Eye Tracking', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def process_frame(self, frame):
        """Processa um frame da webcam e retorna o ponto de olhar"""
        try:
            # 1. Estimar pose da cabeça
            head_pose = self.head_pose_estimator.estimate(frame)
            
            # 2. Estimar direção do olhar
            gaze_point = self.gaze_estimator.estimate_gaze(frame, head_pose)
            
            # 3. Mapear para coordenadas da tela
            screen_point = self.calibration.map_to_screen(gaze_point)
            
            return screen_point
            
        except Exception as e:
            print(f"⚠️ Erro no processamento: {e}")
            return None

    def handle_gaze(self, point):
        """Lida com o ponto de olhar detectado"""
        x, y = point
        print(f"👀 Olhando para: ({x}, {y})")
        # Aqui você implementaria:
        # - Detecção de elementos da UI
        # - Comandos por piscada
        # - Feedback de acessibilidade

def main():
    system = EyeTrackingSystem()
    
    if not system.initialize():
        sys.exit(1)
        
    try:
        system.run()
    except KeyboardInterrupt:
        print("\n🛑 Sistema encerrado pelo usuário")
    except Exception as e:
        print(f"💥 Erro crítico: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()




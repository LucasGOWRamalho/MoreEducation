from core.Calibration import CalibrationService
from core.GazeEstimator import GazeEstimator
from core.HeadPoseEstimator import HeadPoseEstimator
from Back.data.ModelTrainer import ModelTrainer
from domain.Screen import Screen


def main():
    screen = Screen(width=1920, height=1080)
    calib = CalibrationService(screen)
    calib.start_calibration()

    trainer = ModelTrainer()
    trainer.train()

    head_pose = HeadPoseEstimator()
    gaze_estimator = GazeEstimator(head_pose)
    
    # Aqui entraria a leitura da webcam e estimação em tempo real
    # Ex: while True: captura frame, extrai landmarks e calcula ponto de olhar

if __name__ == "__main__":
    main()

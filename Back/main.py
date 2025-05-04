import cv2
import dlib
import numpy as np
from imutils import face_utils

CALIBRATION_POINTS = [
    (0.1, 0.1), (0.5, 0.1), (0.9, 0.1),
    (0.1, 0.5), (0.5, 0.5), (0.9, 0.5),
    (0.1, 0.9), (0.5, 0.9), (0.9, 0.9)
]

class SimpleEyeTracker:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        self.cap = cv2.VideoCapture(0)
        self.calibrated = False
        self.calibration_data = []

    def midpoint(self, p1, p2):
        return int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)

    def get_eye_region(self, landmarks, points):
        region = [landmarks[i] for i in points]
        return np.array(region, np.int32)

    def get_eye_center(self, eye_region, gray):
        height, width = gray.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [eye_region], True, 255, 2)
        cv2.fillPoly(mask, [eye_region], 255)
        eye = cv2.bitwise_and(gray, gray, mask=mask)

        min_x = np.min(eye_region[:, 0])
        max_x = np.max(eye_region[:, 0])
        min_y = np.min(eye_region[:, 1])
        max_y = np.max(eye_region[:, 1])

        gray_eye = eye[min_y:max_y, min_x:max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours and len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00']) + min_x
                cy = int(M['m01']/M['m00']) + min_y
                return (cx, cy)
        return None

    def map_gaze(self, eye_center):
        x = eye_center[0] / 640
        y = eye_center[1] / 480
        return (int(x * 640), int(y * 480))

    def run(self):
        print("Pressione 'c' para calibrar, 'q' para sair.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                landmarks = self.predictor(gray, face)
                landmarks = face_utils.shape_to_np(landmarks)

                left_eye = self.get_eye_region(landmarks, [36, 37, 38, 39, 40, 41])
                right_eye = self.get_eye_region(landmarks, [42, 43, 44, 45, 46, 47])

                left_center = self.get_eye_center(left_eye, gray)
                right_center = self.get_eye_center(right_eye, gray)

                # Visualização dos olhos
                cv2.polylines(frame, [left_eye], True, (255, 0, 0), 1)
                cv2.polylines(frame, [right_eye], True, (255, 0, 0), 1)
                if left_center:
                    cv2.circle(frame, left_center, 3, (0, 0, 255), -1)
                if right_center:
                    cv2.circle(frame, right_center, 3, (0, 0, 255), -1)

                if left_center and right_center:
                    eye_center = self.midpoint(left_center, right_center)
                    mapped = self.map_gaze(eye_center)
                    cv2.circle(frame, mapped, 10, (0, 255, 0), -1)

            cv2.imshow("Gaze Estimation", frame)
            key = cv2.waitKey(1)

            if key == ord('q'):
                break
            elif key == ord('c'):
                print("Capturando ponto de calibração...")
                if left_center and right_center:
                    eye_center = self.midpoint(left_center, right_center)
                    self.calibration_data.append(eye_center)
                    print(f"Ponto salvo: {eye_center}")

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = SimpleEyeTracker()
    tracker.run()

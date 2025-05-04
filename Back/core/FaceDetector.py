import dlib

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def get_landmarks(self, gray_frame):
        faces = self.detector(gray_frame)
        if faces:
            shape = self.predictor(gray_frame, faces[0])
            return [(p.x, p.y) for p in shape.parts()]
        return None

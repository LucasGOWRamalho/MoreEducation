import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpont(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

while True:
    rec, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces: 
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        
        landmarks = predictor(gray, face)

        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        #x = landmarks.part(36).x
        #y = landmarks.part(36).y
        #vc2.circle(frame, (x, y), 3, (0, 0, 255), 2)
        
        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINKING", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 7, (255, 0, 0))
        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                                   (landmarks.part(37).x, landmarks.part(37).y),
                                   (landmarks.part(38).x, landmarks.part(37).y),
                                   (landmarks.part(38).x, landmarks.part(39).y), 
                                   (landmarks.part(40).x, landmarks.part(41).y),   
                                   (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:




        #Olho direito 
        left_point_ry = (landmarks.part(36).x, landmarks.part(36).y)
        right_point_ry = (landmarks.part(39).x, landmarks.part(39).y)
        
        center_top = midpont(landmarks.part(37), landmarks.part(38))
        center_bottom = midpont(landmarks.part(39), landmarks.part(40))
        
        hor_line = cv2.line(frame, left_point_ry, right_point_ry, (0, 255, 0), 2)
        ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)



        #Olho esquerdo
        left_point_ly = (landmarks.part(42).x, landmarks.part(42).y)
        right_point_ly = (landmarks.part(45).x, landmarks.part(45).y)
       
       
       
        #logs S2
        print(landmarks) 
        print(face)


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    

    cap.release()
    cv2.destroyAllWindows()
import dlib
import cv2
import numpy as np
import face_recognition

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def getFacesFromPic(Frame):  # Well return the faces' locations from a frame
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    faces_dec = {}
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        width = x2 - x1
        height = y2 - y1
        pts1 = np.float32([[x1, y1], [x2, y1], [x1, y2], [x2, y2]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(Frame, matrix, (width, height))
        faces_dec[(x1, y1, x2, y2)] = imgOutput

    return faces_dec


def faceRecognitionGetFacesFromPic(frame):

    face_locations = face_recognition.face_locations(frame)
    unknown_face_encodings = face_recognition.face_encodings(frame, face_locations)

    return unknown_face_encodings

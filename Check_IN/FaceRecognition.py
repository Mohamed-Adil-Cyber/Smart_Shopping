import face_recognition
import numpy as np
# import Database
import pickle


def classify_face(unknown_face_encodings):
    face_names = []

    # faces = Database.import_numpyDatabase()
    fileName = 'D:\Programing\Projects\Python\LastTest1/dataTest'
    with open(fileName, 'rb') as file:
        faces = dict(pickle.load(file))
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    for face_encoding1 in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding1)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding1)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    return face_names

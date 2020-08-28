import cv2
import FaceRecognition as FR
import Faces


def getID():  # It will return the ID of the customer
    currentNumberOfAttempts = 0  # How many times hte program did not know the customer's face
    maxNumberOfAttempts = 5  # How many tries should the program try

    cap = cv2.VideoCapture(0)  # Read frames from Camera to make a video
    clientName = []  # It will collect the output of three attempts of recognizing three pictures of the customer

    while True:  # Infinite loop. It won't stop until it returns the customer's ID or Unknown String
        _, frame = cap.read()
        # cv2.imshow('frame', frame)  #  We will replace it with multi threading program
        # cv2.waitKey(1)  # will make a delay for 1 ms
        facesCV2dec = Faces.getFacesFromPic(frame)
        # Well return the faces' locations from a frame (we use it to reduce the time cause
        # faceRecognitionGetFacesFromPic will take more time)
        imgs = list(facesCV2dec.values())

        for img in imgs:
            faces = Faces.faceRecognitionGetFacesFromPic(img)
            customer_ID = FR.classify_face(faces)

            clientName.append(customer_ID)
        numberOfPics = len(clientName)
        if numberOfPics == 3:
            if clientName[0] == clientName[1] and clientName[1] == clientName[2] and clientName[2] == clientName[0] and \
                    clientName[0]:
                customer_ID = clientName[0][0]
                clientName.clear()

                if customer_ID == 'Unknown':
                    currentNumberOfAttempts += 1
                    if currentNumberOfAttempts == maxNumberOfAttempts:
                        return 'Unknown'
                else:
                    return customer_ID

            else:
                clientName.pop(0)



import pickle
import Database as db
import face_recognition as fr

databaseName = '../dataTest'  # database file location. The same file of Check_IN program


def train(fullName, national_ID, bank_Info, picDirectory):
    """
        looks through the faces folder and encodes all
        the faces

        :return: dict of (ID, image encoded)
        """
    with open(picDirectory, 'rb') as f:  # Reading picture as bytes to uploaded to database
        pic = f.read()
    customer_ID = db.getLastID()
    print('customer_ID _ NewPicTrainer')
    print(customer_ID)

    #  These three functions are to analyse the face and encode it
    with open(databaseName, 'rb') as f:  # Loading Database file which contain encoded faces
        encoded = pickle.load(f)
    face = fr.load_image_file(picDirectory)
    encoding = fr.face_encodings(face)[0]
    encoded[customer_ID] = encoding

    db.createAnAccount(fullName, national_ID, bank_Info, pic, customer_ID)  # Creating an account for the customer

    # (this process will be done only once)

    with open(databaseName, 'wb') as file:  # Re-save database file after adding the new face
        pickle.dump(encoded, file)

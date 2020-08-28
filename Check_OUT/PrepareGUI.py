import cv2
from PIL import Image

print("Start GUI")

nameWidth = 345
nameHeight = 830 + 23

numberWidth = 345
numberHeight = 930 + 35
imagesFileDirectory = "../_Images"


def setImages(name, pic):
    if name == 'Not in the system':
        print('Not in the system')
        return False

    with open(f'{imagesFileDirectory}/ThePicOUT.jpg', 'wb') as f:
        f.write(pic)

    img = cv2.imread(f"{imagesFileDirectory}/DefaultBackground.jpg")
    cv2.putText(img, name, (nameWidth, nameHeight), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255))
    cv2.imwrite(f"{imagesFileDirectory}/backgroundOUT.jpg", img)


def setDefault():
    img = cv2.imread(f"{imagesFileDirectory}/DefaultBackground.jpg")
    cv2.imwrite(f'{imagesFileDirectory}/backgroundOUT.jpg', img)

    img = cv2.imread(f"{imagesFileDirectory}/defaultThePic.jpg")
    cv2.imwrite(f'{imagesFileDirectory}/ThePicOUT.jpg', img)


setDefault()

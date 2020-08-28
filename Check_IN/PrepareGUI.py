import cv2
from PIL import Image
print("Start GUI")

nameWidth = 345
nameHeight = 830 + 23

numberWidth = 345
numberHeight = 930 + 35
imagesFileDirectory = "../_Images"


def setImages(name, pic, cartNumber):
    if name == 'Not in the system':
        print('Not in the system')
        return False

    with open(f'{imagesFileDirectory}/ThePicIN.jpg', 'wb') as f:
        f.write(pic)
    print('cartNumber', cartNumber)

    img = cv2.imread(f"{imagesFileDirectory}/DefaultBackground.jpg")
    cv2.putText(img, name, (nameWidth, nameHeight), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255))
    cv2.putText(img, f'{cartNumber}', (numberWidth, numberHeight), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))
    cv2.imwrite(f"{imagesFileDirectory}/backgroundIN.jpg", img)


def setDefault():

    img = cv2.imread(f"{imagesFileDirectory}/DefaultBackground.jpg")
    cv2.imwrite(f'{imagesFileDirectory}/backgroundIN.jpg', img)

    img = cv2.imread(f"{imagesFileDirectory}/defaultThePic.jpg")
    cv2.imwrite(f'{imagesFileDirectory}/ThePicIN.jpg', img)


setDefault()
